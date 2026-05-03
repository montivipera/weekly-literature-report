"""Open-access full-text retrieval.

For each article we try, in order:
  1. PMC (NCBI E-utilities) when a PMC ID is known.
  2. Unpaywall for an open-access PDF, then extract text.
  3. bioRxiv full-text URL when known.
  4. Fall back to the abstract.

We strip references and figure captions when possible to keep token usage low.
"""

from __future__ import annotations

import io
import logging
import os
import re
from typing import Optional
from xml.etree import ElementTree as ET

import requests
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from .fetchers.base import Article

logger = logging.getLogger(__name__)


PMC_EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
UNPAYWALL = "https://api.unpaywall.org/v2/{doi}"

MAX_FULLTEXT_CHARS = 60_000


def _ua() -> str:
    email = os.environ.get("UNPAYWALL_EMAIL", "anonymous@example.com")
    return f"weekly-literature-report/1.0 (mailto:{email})"


@retry(
    reraise=True,
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    retry=retry_if_exception_type((requests.RequestException,)),
)
def _http_get(url: str, params=None, timeout: int = 45, stream: bool = False):
    r = requests.get(url, params=params, headers={"User-Agent": _ua()}, timeout=timeout, stream=stream)
    if r.status_code in (429, 500, 502, 503, 504):
        raise requests.RequestException(f"HTTP {r.status_code}")
    r.raise_for_status()
    return r


# ---------------------------------------------------------------------------
# Cleaning helpers
# ---------------------------------------------------------------------------


_REF_PATTERNS = [
    re.compile(r"\n\s*References\b.*", re.IGNORECASE | re.DOTALL),
    re.compile(r"\n\s*Bibliography\b.*", re.IGNORECASE | re.DOTALL),
    re.compile(r"\n\s*Literature Cited\b.*", re.IGNORECASE | re.DOTALL),
]

_FIGURE_PATTERN = re.compile(
    r"^\s*(Figure|Fig\.|Table)\s+\d+[.:].*?(?:\n\s*\n|\Z)",
    re.MULTILINE | re.DOTALL,
)


def _strip_references(text: str) -> str:
    for pat in _REF_PATTERNS:
        text = pat.sub("\n", text)
    text = _FIGURE_PATTERN.sub("\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def _truncate(text: str, n: int = MAX_FULLTEXT_CHARS) -> str:
    if len(text) <= n:
        return text
    return text[:n] + "\n\n[...truncated]"


# ---------------------------------------------------------------------------
# PMC
# ---------------------------------------------------------------------------


def _fetch_pmc(pmcid: str) -> Optional[str]:
    pid = pmcid.upper().replace("PMC", "")
    try:
        r = _http_get(
            PMC_EFETCH,
            {"db": "pmc", "id": pid, "rettype": "xml"},
            timeout=60,
        )
    except Exception as exc:
        logger.info("PMC fetch failed for %s: %s", pmcid, exc)
        return None
    try:
        root = ET.fromstring(r.content)
    except ET.ParseError as exc:
        logger.info("PMC XML parse failed for %s: %s", pmcid, exc)
        return None

    # Strip <ref-list> and <fig>/<table-wrap>
    for tag in ("ref-list", "fig", "table-wrap", "back"):
        for el in root.iter():
            for child in list(el):
                if child.tag.endswith(tag):
                    el.remove(child)

    parts = []
    for body in root.iter("body"):
        text = "".join(body.itertext())
        parts.append(text)
    if not parts:
        # Fall back to abstract section
        for absel in root.iter("abstract"):
            parts.append("".join(absel.itertext()))
    text = "\n".join(p for p in parts if p)
    text = re.sub(r"\s+", " ", text).strip()
    return text or None


# ---------------------------------------------------------------------------
# Unpaywall
# ---------------------------------------------------------------------------


def _unpaywall_pdf_url(doi: str) -> Optional[str]:
    email = os.environ.get("UNPAYWALL_EMAIL")
    if not email:
        return None
    try:
        r = _http_get(UNPAYWALL.format(doi=doi), {"email": email}, timeout=30)
        data = r.json()
    except Exception as exc:
        logger.info("Unpaywall lookup failed for %s: %s", doi, exc)
        return None
    best = data.get("best_oa_location") or {}
    return best.get("url_for_pdf") or best.get("url")


def _extract_pdf_text(content: bytes) -> Optional[str]:
    try:
        from pypdf import PdfReader
    except ImportError:  # pragma: no cover
        logger.warning("pypdf not installed")
        return None
    try:
        reader = PdfReader(io.BytesIO(content))
        pages = [p.extract_text() or "" for p in reader.pages]
        text = "\n".join(pages)
        return text
    except Exception as exc:
        logger.info("PDF extract failed: %s", exc)
        return None


def _fetch_oa_pdf(doi: Optional[str], known_pdf_url: Optional[str] = None) -> Optional[str]:
    pdf_url = known_pdf_url
    if not pdf_url and doi:
        pdf_url = _unpaywall_pdf_url(doi)
    if not pdf_url:
        return None
    try:
        r = _http_get(pdf_url, timeout=60, stream=False)
    except Exception as exc:
        logger.info("PDF GET failed for %s: %s", pdf_url, exc)
        return None
    if "pdf" not in (r.headers.get("Content-Type") or "").lower() and not pdf_url.lower().endswith(".pdf"):
        # Sometimes a landing page is returned — try anyway, but bail if it's HTML
        if b"<html" in r.content[:1000].lower():
            return None
    return _extract_pdf_text(r.content)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def get_full_text(article: Article) -> str:
    """Return the best available open-access text for ``article``.

    Falls back to the abstract if nothing else is reachable. Always returns a
    non-empty string when an abstract exists.
    """
    text: Optional[str] = None

    if article.pmcid:
        text = _fetch_pmc(article.pmcid)
        if text:
            logger.debug("Full text from PMC for %s", article.stable_id())
    if not text and article.doi:
        text = _fetch_oa_pdf(article.doi, known_pdf_url=article.full_text_url)
        if text:
            logger.debug("Full text from Unpaywall PDF for %s", article.stable_id())
    if not text and article.full_text_url and article.source in ("biorxiv", "medrxiv"):
        try:
            r = _http_get(article.full_text_url, timeout=60)
            text = _extract_pdf_text(r.content)
        except Exception as exc:
            logger.info("bioRxiv PDF fetch failed: %s", exc)

    if text:
        text = _strip_references(text)
        return _truncate(text)

    return article.abstract or ""
