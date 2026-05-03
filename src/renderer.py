"""HTML renderer using Jinja2."""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

from jinja2 import Environment, FileSystemLoader, select_autoescape

from .fetchers.base import Article
from .summarizer import Summary

logger = logging.getLogger(__name__)


TEMPLATE_DIR = Path(__file__).resolve().parent.parent / "templates"


@dataclass
class RenderItem:
    """One article + its summary, in the form the template expects."""

    article: Article
    summary: Summary


@dataclass
class RenderCategory:
    name: str
    items: List[RenderItem] = field(default_factory=list)


def _format_authors(authors: List[str]) -> str:
    if not authors:
        return ""
    if len(authors) <= 3:
        return ", ".join(authors)
    return f"{authors[0]}, {authors[1]} et al. ({len(authors)} authors)"


def _make_env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATE_DIR)),
        autoescape=select_autoescape(["html", "j2"]),
        trim_blocks=False,
        lstrip_blocks=False,
    )
    return env


def _isoweek(d: datetime) -> int:
    return d.isocalendar()[1]


def render(
    categories: List[RenderCategory],
    since: datetime,
    until: datetime,
    sources_used: List[str],
    subject: Optional[str] = None,
    template_name: str = "report.html.j2",
) -> str:
    env = _make_env()
    template = env.get_template(template_name)

    cat_payload = []
    total = 0
    for cat in categories:
        items = []
        for it in cat.items:
            # Attach a display string for authors via a tiny shim object
            it.article.authors_display = _format_authors(it.article.authors)  # type: ignore[attr-defined]
            items.append({"article": it.article, "summary": it.summary})
        cat_payload.append(
            {"name": cat.name, "count": len(items), "articles": items}
        )
        total += len(items)

    iso_week = _isoweek(until)
    subject = subject or (
        f"[Lit Report] Week {iso_week} · "
        f"{since.strftime('%Y-%m-%d')} – {until.strftime('%Y-%m-%d')} · {total} articles"
    )

    return template.render(
        subject=subject,
        iso_week=iso_week,
        since_str=since.strftime("%Y-%m-%d"),
        until_str=until.strftime("%Y-%m-%d"),
        total_count=total,
        category_count=len(cat_payload),
        sources_used=sources_used,
        categories=cat_payload,
        generated_at=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    )


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
