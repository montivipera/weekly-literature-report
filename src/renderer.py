"""HTML renderer using Jinja2."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .fetchers.base import Article
from .query_translator import _tokenize
from .summarizer import Summary

logger = logging.getLogger(__name__)


TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"


# ---------------------------------------------------------------------------
# Domain registry
# ---------------------------------------------------------------------------

DOMAINS: List[Dict[str, str]] = [
    {"id": "molecular",      "name": "Molecular & Microbial",       "icon": "🧬"},
    {"id": "ecology",        "name": "Ecology & Biodiversity",      "icon": "🌿"},
    {"id": "hydrology",      "name": "Hydrology & Biogeochemistry", "icon": "💧"},
    {"id": "remote_sensing", "name": "Remote Sensing & Modeling",   "icon": "🛰️"},
    {"id": "synthesis",      "name": "Synthesis",                   "icon": "📚"},
    {"id": "policy",         "name": "Policy & Management",         "icon": "📋"},
]
DOMAIN_BY_ID = {d["id"]: d for d in DOMAINS}


@dataclass
class RenderItem:
    """One article + its summary, in the form the template expects."""

    article: Article
    summary: Summary


@dataclass
class RenderCategory:
    name: str
    query: str = ""
    items: List[RenderItem] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _format_authors(authors: List[str]) -> str:
    if not authors:
        return ""
    if len(authors) <= 3:
        return ", ".join(authors)
    return f"{authors[0]}, {authors[1]} et al. · {len(authors)} authors"


def _isoweek(d: datetime) -> int:
    return d.isocalendar()[1]


def _make_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=False,
        lstrip_blocks=False,
    )


def _tokenize_query(query: str) -> List[Dict[str, str]]:
    """Convert a Boolean query into render-ready token dicts.

    Each dict has: ``kind`` (term, op, lparen, rparen) and ``text``,
    plus ``primary``/``phrase`` flags for terms. The first non-NOT term is
    flagged ``primary`` so the template can highlight it as the anchor term.
    """
    if not query or not query.strip():
        return []
    try:
        tokens = _tokenize(query)
    except Exception as exc:
        logger.warning("Could not tokenize query for display: %s", exc)
        return [{"kind": "term", "text": query, "primary": True, "phrase": False}]

    out: List[Dict[str, str]] = []
    primary_assigned = False
    for t in tokens:
        if t.kind == "TERM":
            is_primary = not primary_assigned
            primary_assigned = True
            out.append(
                {
                    "kind": "term",
                    "text": t.value,
                    "primary": is_primary,
                    "phrase": t.quoted,
                }
            )
        elif t.kind in ("AND", "OR", "NOT"):
            out.append({"kind": "op", "text": t.kind, "primary": False, "phrase": False})
        elif t.kind == "LPAREN":
            out.append({"kind": "lparen", "text": "(", "primary": False, "phrase": False})
        elif t.kind == "RPAREN":
            out.append({"kind": "rparen", "text": ")", "primary": False, "phrase": False})
    return out


def _group_by_domain(items: List[RenderItem]) -> List[Dict]:
    """Group items by their summary's domain, preserving DOMAINS order."""
    buckets: Dict[str, List[Dict]] = {d["id"]: [] for d in DOMAINS}
    for item in items:
        dom = (item.summary.domain or "ecology").lower()
        if dom not in buckets:
            dom = "ecology"
        buckets[dom].append(
            {"article": item.article, "summary": item.summary}
        )

    groups = []
    for d in DOMAINS:
        bucket = buckets[d["id"]]
        if not bucket:
            continue
        # Mark the first card of the largest domain as featured for visual rhythm
        for idx, entry in enumerate(bucket):
            entry["featured"] = (idx == 0 and len(bucket) >= 3)
            entry["wide"] = (idx == 0 and len(bucket) == 2)
        groups.append(
            {
                "id": d["id"],
                "name": d["name"],
                "icon": d["icon"],
                "count": len(bucket),
                "articles": bucket,
            }
        )
    return groups


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def _build_context(
    categories: List[RenderCategory],
    since: datetime,
    until: datetime,
    sources_used: List[str],
    subject: Optional[str] = None,
    pdf_filename: str = "weekly-report.pdf",
    drive_link: Optional[str] = None,
) -> dict:
    cat_payload = []
    total = 0
    domain_counts: Dict[str, int] = {d["id"]: 0 for d in DOMAINS}

    for cat in categories:
        for it in cat.items:
            it.article.authors_display = _format_authors(it.article.authors)  # type: ignore[attr-defined]

        groups = _group_by_domain(cat.items)
        for g in groups:
            domain_counts[g["id"]] += g["count"]

        cat_payload.append(
            {
                "name": cat.name,
                "count": len(cat.items),
                "query_tokens": _tokenize_query(cat.query),
                "groups": groups,
            }
        )
        total += len(cat.items)

    active_domains = []
    for d in DOMAINS:
        c = domain_counts[d["id"]]
        if c > 0:
            active_domains.append(
                {"id": d["id"], "name": d["name"], "icon": d["icon"], "count": c}
            )

    iso_week = _isoweek(until)
    subject = subject or (
        f"[Lit Report] Week {iso_week} · "
        f"{since.strftime('%Y-%m-%d')} – {until.strftime('%Y-%m-%d')} · {total} articles"
    )

    return {
        "subject": subject,
        "iso_week": iso_week,
        "since_str": since.strftime("%d %b").lstrip("0"),
        "until_str": until.strftime("%d %b").lstrip("0"),
        "since_full": since.strftime("%Y-%m-%d"),
        "until_full": until.strftime("%Y-%m-%d"),
        "total_count": total,
        "category_count": len(cat_payload),
        "domain_count": len(active_domains),
        "sources_used": sources_used,
        "sources_count": len(sources_used),
        "categories": cat_payload,
        "active_domains": active_domains,
        "pdf_filename": pdf_filename,
        "drive_link": drive_link,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


def render(
    categories: List[RenderCategory],
    since: datetime,
    until: datetime,
    sources_used: List[str],
    subject: Optional[str] = None,
    template_name: str = "report.html.j2",
    pdf_filename: str = "weekly-report.pdf",
    drive_link: Optional[str] = None,
) -> str:
    """Render the full HTML report (web/email view).

    Pass ``template_name="report_pdf.html.j2"`` for the print-optimized
    journal-style PDF layout instead.
    """
    env = _make_env()
    template = env.get_template(template_name)
    ctx = _build_context(
        categories, since, until, sources_used, subject, pdf_filename, drive_link
    )
    return template.render(**ctx)


def render_email_summary(
    categories: List[RenderCategory],
    since: datetime,
    until: datetime,
    sources_used: List[str],
    subject: Optional[str] = None,
    template_name: str = "email_summary.html.j2",
    pdf_filename: str = "weekly-report.pdf",
    drive_link: Optional[str] = None,
) -> str:
    """Render the short email body that accompanies the PDF attachment."""
    env = _make_env()
    template = env.get_template(template_name)
    ctx = _build_context(
        categories, since, until, sources_used, subject, pdf_filename, drive_link
    )
    return template.render(**ctx)


def html_to_text(html: str) -> str:
    """Minimal plain-text fallback by stripping tags."""
    text = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<script[^>]*>.*?</script>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</li>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
