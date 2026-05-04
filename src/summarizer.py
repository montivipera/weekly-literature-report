"""Gemini-powered structured summarizer.

For each article we send a prompt that returns strict JSON with the four
sections used by the report. The summary is bounded by a fallback structure
that we use when the model returns invalid JSON twice in a row, so a single
problematic article never breaks the run."""

from __future__ import annotations

import json
import logging
import os
import re
import time
from dataclasses import dataclass, field
from typing import List, Optional

from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from .fetchers.base import Article

logger = logging.getLogger(__name__)


SYSTEM_PROMPT = """You are a careful scientific summarizer. You read a scientific
article (full text when available, otherwise the abstract) and produce a strict
JSON object describing the article in BOTH English and Turkish. You never invent
facts. If a section is not supported by the source text, return an empty list
for that section in both languages.

Return JSON only, with no markdown fences and no extra prose. The schema is:

{
  "article_type": one of ["research_article", "review", "meta_analysis", "preprint", "other"],
  "domain":      one of ["molecular", "ecology", "hydrology", "remote_sensing", "synthesis", "policy"],
  "en": {
    "aim":         array of 1-3 short bullet strings (the goal/objective of the study),
    "gap":         array of 0-2 bullet strings (the gap or motivation; empty if not stated),
    "methods":     array of 2-4 bullet strings (study area / organism / sample size / analytic approach),
    "conclusions": array of 2-5 bullet strings drawn from the Discussion section
                   (what the authors interpret and recommend, NOT raw measurements)
  },
  "tr": {
    "aim":         same content as en.aim, translated into natural, fluent academic Turkish,
    "gap":         same content as en.gap, in Turkish,
    "methods":     same content as en.methods, in Turkish,
    "conclusions": same content as en.conclusions, in Turkish
  }
}

DOMAIN classification — pick the SINGLE best fit:
- "molecular":      genetics, eDNA, microbiome, metagenomics, omics, microbial ecology,
                    sequencing-based studies, molecular biomarkers
- "ecology":        species, populations, communities, biodiversity, behaviour, ecology
                    of macro-organisms (plants, animals, invertebrates), trophic interactions
- "hydrology":      water quality, hydrology, biogeochemistry, carbon/nitrogen cycling,
                    sediment, nutrients, soil chemistry, gas fluxes
- "remote_sensing": satellite imagery, GIS, drones, spatial modelling, simulation,
                    machine-learning prediction, mapping
- "synthesis":      literature review, systematic review, meta-analysis, evidence synthesis
- "policy":         conservation policy, restoration management, governance, economics,
                    citizen science, stakeholder studies, indigenous knowledge

If a study spans two domains, pick the one most central to its METHODS and FINDINGS.
For preprints with thin abstracts, use journal name and keywords as additional signal.

Rules:
- Conclusions must reflect what the authors INTERPRET and RECOMMEND in the
  Discussion section, not the raw findings reported in Results. If only an
  abstract is provided, use the closing interpretive statements there.
- Each bullet must be a complete, self-contained sentence under 30 words.
- The Turkish translation must be a real translation (same meaning, same number
  of bullets), not a paraphrase or different content. Use natural academic
  Turkish — translate scientific terms idiomatically (e.g. "biodiversity" →
  "biyoçeşitlilik", "wetland" → "sulak alan", "remote sensing" → "uzaktan
  algılama"). Keep proper nouns (place names, taxa, instruments) in their
  original form.
- Do not output any text outside the JSON object.
- Do not use markdown. Do not wrap the JSON in code fences.
- If the source text is empty or unintelligible, return all eight arrays
  (en.* and tr.*) empty, "article_type": "other", and pick the closest
  "domain" you can infer (default "ecology").
"""


@dataclass
class Summary:
    article_type: str = "other"
    domain: str = "ecology"
    # English bullets (default for backward compatibility)
    aim: List[str] = field(default_factory=list)
    gap: List[str] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)
    conclusions: List[str] = field(default_factory=list)
    # Turkish bullets
    aim_tr: List[str] = field(default_factory=list)
    gap_tr: List[str] = field(default_factory=list)
    methods_tr: List[str] = field(default_factory=list)
    conclusions_tr: List[str] = field(default_factory=list)
    error: Optional[str] = None

    def for_lang(self, lang: str) -> dict:
        """Return the four bullet sections for the requested language."""
        if lang == "tr":
            return {
                "aim": self.aim_tr,
                "gap": self.gap_tr,
                "methods": self.methods_tr,
                "conclusions": self.conclusions_tr,
            }
        return {
            "aim": self.aim,
            "gap": self.gap,
            "methods": self.methods,
            "conclusions": self.conclusions,
        }


def _extract_json(text: str) -> dict:
    """Pull the first JSON object out of a string, even if wrapped in noise."""
    text = (text or "").strip()
    # Strip code fences if the model added them despite instructions
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    # Try direct parse first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Fall back to finding the first {...} chunk
    m = re.search(r"\{[\s\S]*\}", text)
    if not m:
        raise ValueError("No JSON object found in model output")
    return json.loads(m.group(0))


def _normalize_summary(data: dict) -> Summary:
    valid_types = {"research_article", "review", "meta_analysis", "preprint", "other"}
    at = (data.get("article_type") or "other").strip()
    if at not in valid_types:
        at = "other"

    valid_domains = {"molecular", "ecology", "hydrology", "remote_sensing", "synthesis", "policy"}
    dom = (data.get("domain") or "ecology").strip().lower()
    if dom not in valid_domains:
        dom = "ecology"

    def _list_from(d: dict, key: str) -> List[str]:
        v = (d or {}).get(key) or []
        if isinstance(v, str):
            v = [v]
        return [str(x).strip() for x in v if str(x).strip()]

    # Bilingual nested layout (preferred). Fall back to flat keys for
    # backwards compatibility with older prompt outputs.
    en_block = data.get("en") if isinstance(data.get("en"), dict) else None
    tr_block = data.get("tr") if isinstance(data.get("tr"), dict) else None
    en_source = en_block if en_block is not None else data
    tr_source = tr_block if tr_block is not None else {}

    return Summary(
        article_type=at,
        domain=dom,
        aim=_list_from(en_source, "aim"),
        gap=_list_from(en_source, "gap"),
        methods=_list_from(en_source, "methods"),
        conclusions=_list_from(en_source, "conclusions"),
        aim_tr=_list_from(tr_source, "aim"),
        gap_tr=_list_from(tr_source, "gap"),
        methods_tr=_list_from(tr_source, "methods"),
        conclusions_tr=_list_from(tr_source, "conclusions"),
    )


class GeminiSummarizer:
    """Wraps `google-generativeai` with retries, JSON parsing, and rate limiting."""

    def __init__(
        self,
        model_name: Optional[str] = None,
        api_key: Optional[str] = None,
        request_delay_seconds: float = 1.5,
    ):
        self.model_name = model_name or os.environ.get("GEMINI_MODEL", "gemini-2.0-flash")
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.request_delay_seconds = request_delay_seconds
        self._model = None
        if self.api_key:
            try:
                import google.generativeai as genai

                genai.configure(api_key=self.api_key)
                self._model = genai.GenerativeModel(self.model_name)
            except Exception as exc:
                logger.error("Failed to initialize Gemini: %s", exc)
                self._model = None
        else:
            logger.warning("GEMINI_API_KEY not set — summaries will be placeholders")

    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=20),
        retry=retry_if_exception_type(Exception),
    )
    def _call(self, prompt: str) -> str:
        if self._model is None:
            raise RuntimeError("Gemini model not configured")
        resp = self._model.generate_content(prompt)
        # Log token usage where available
        try:
            usage = getattr(resp, "usage_metadata", None)
            if usage:
                logger.info(
                    "Gemini tokens — prompt=%s, candidates=%s, total=%s",
                    getattr(usage, "prompt_token_count", "?"),
                    getattr(usage, "candidates_token_count", "?"),
                    getattr(usage, "total_token_count", "?"),
                )
        except Exception:
            pass
        return getattr(resp, "text", "") or ""

    def summarize(self, article: Article, full_text: str) -> Summary:
        if self._model is None:
            return Summary(error="GEMINI_API_KEY missing")

        # Cap the source text — Gemini Flash has a generous context but we stay
        # well under the free-tier limits to keep costs/latency low.
        source = (full_text or article.abstract or "").strip()[:30_000]
        if not source:
            return Summary(error="No source text")

        header = (
            f"Title: {article.title}\n"
            f"Journal: {article.journal or 'n/a'}\n"
            f"Source: {article.source}\n"
            f"Year: {article.year or 'n/a'}\n"
        )
        prompt = f"{SYSTEM_PROMPT}\n\nARTICLE METADATA:\n{header}\n\nARTICLE TEXT:\n{source}"

        last_error: Optional[str] = None
        for attempt in (1, 2):
            try:
                raw = self._call(prompt)
                data = _extract_json(raw)
                summary = _normalize_summary(data)
                if self.request_delay_seconds:
                    time.sleep(self.request_delay_seconds)
                return summary
            except Exception as exc:
                last_error = str(exc)
                logger.warning(
                    "Summarize attempt %d failed for %s: %s",
                    attempt,
                    article.stable_id(),
                    exc,
                )
                time.sleep(2)

        return Summary(error=f"Gemini failed: {last_error}")
