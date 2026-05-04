"""Weekly literature report — main entry point.

Pipeline:
  1. Load config.yaml.
  2. Compute since/until from lookback_days in the configured timezone.
  3. For each enabled category × source: fetch, deduplicate.
  4. Retrieve full text per article.
  5. Summarize each article via Gemini.
  6. Render HTML.
  7. Send email (or save to disk in --dry-run / --save-html mode).
"""

from __future__ import annotations

import argparse
import logging
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

import yaml

try:  # Python 3.9+
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    from backports.zoneinfo import ZoneInfo  # type: ignore

from .deduplicator import deduplicate
from .fetchers.arxiv import ArxivFetcher
from .fetchers.base import Article, BaseFetcher
from .fetchers.biorxiv import BioRxivFetcher
from .fetchers.crossref import CrossrefFetcher
from .fetchers.pubmed import PubMedFetcher
from .fetchers.semantic_scholar import SemanticScholarFetcher
from .full_text import get_full_text
from .mailer import send_report
from .pdf_generator import html_to_pdf
from .renderer import RenderCategory, RenderItem, render, render_email_summary
from .summarizer import GeminiSummarizer, Summary

logger = logging.getLogger("weekly_report")


FETCHERS: Dict[str, type[BaseFetcher]] = {
    "pubmed": PubMedFetcher,
    "arxiv": ArxivFetcher,
    "biorxiv": BioRxivFetcher,
    "crossref": CrossrefFetcher,
    "semantic_scholar": SemanticScholarFetcher,
}


def _setup_logging() -> None:
    level = os.environ.get("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=getattr(logging, level, logging.INFO),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def _load_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f) or {}
    cfg.setdefault("settings", {})
    cfg.setdefault("categories", [])
    return cfg


def _date_window(settings: dict) -> tuple[datetime, datetime]:
    tz_name = settings.get("timezone") or "UTC"
    tz = ZoneInfo(tz_name)
    now_local = datetime.now(tz)
    until = now_local
    since = until - timedelta(days=int(settings.get("lookback_days", 7)))
    # Strip tz so downstream comparisons (against naive parsed dates) are simple
    return since.replace(tzinfo=None), until.replace(tzinfo=None)


def _build_fetchers(source_names: List[str]) -> Dict[str, BaseFetcher]:
    out: Dict[str, BaseFetcher] = {}
    for name in source_names:
        cls = FETCHERS.get(name)
        if not cls:
            logger.warning("Unknown source %r — skipping", name)
            continue
        out[name] = cls()
    return out


def _fetch_category(
    category_name: str,
    query: str,
    fetchers: Dict[str, BaseFetcher],
    since: datetime,
    until: datetime,
    limit: Optional[int],
    priority: List[str],
) -> List[Article]:
    all_articles: List[Article] = []
    for src_name, fetcher in fetchers.items():
        try:
            results = fetcher.fetch(query, since, until, limit)
        except Exception as exc:
            logger.exception("Fetcher %s crashed: %s", src_name, exc)
            results = []
        logger.info("[%s] %s -> %d", category_name, src_name, len(results))
        all_articles.extend(results)

    deduped = deduplicate(all_articles, priority=priority)
    if limit:
        deduped = deduped[:limit]
    return deduped


def run(
    config_path: str,
    dry_run: bool,
    save_html: bool,
) -> int:
    cfg = _load_config(config_path)
    settings = cfg.get("settings") or {}
    categories_cfg = cfg.get("categories") or []

    since, until = _date_window(settings)
    logger.info("Window: %s -> %s", since.isoformat(), until.isoformat())

    enabled_cats = [c for c in categories_cfg if c.get("enabled", True)]
    if not enabled_cats:
        logger.info("No enabled categories. Nothing to do.")
        if save_html or dry_run:
            html = render(
                categories=[],
                since=since,
                until=until,
                sources_used=settings.get("sources") or [],
            )
            _maybe_write_html(html, save_html or dry_run)
        return 0

    sources = settings.get("sources") or list(FETCHERS.keys())
    fetchers = _build_fetchers(sources)
    if not fetchers:
        logger.error("No valid sources configured")
        return 1

    priority = settings.get("dedup_priority") or list(FETCHERS.keys())
    limit = settings.get("per_category_limit")

    summarizer = GeminiSummarizer()

    render_categories: List[RenderCategory] = []
    failures: Dict[str, int] = {}
    for cat in enabled_cats:
        name = cat.get("name") or "(unnamed)"
        query = cat.get("query") or ""
        if not query.strip():
            logger.warning("Category %r has empty query — skipping", name)
            continue

        logger.info("=== Category: %s ===", name)
        articles = _fetch_category(
            name, query, fetchers, since, until, limit, priority
        )
        logger.info("[%s] After dedup: %d articles", name, len(articles))

        items: List[RenderItem] = []
        cat_failures = 0
        for art in articles:
            try:
                full = get_full_text(art)
            except Exception as exc:
                logger.warning("Full-text retrieval failed for %s: %s", art.stable_id(), exc)
                full = art.abstract or ""

            try:
                summary = summarizer.summarize(art, full)
            except Exception as exc:
                logger.warning("Summarization crashed for %s: %s", art.stable_id(), exc)
                summary = Summary(error=str(exc))

            if summary.error:
                cat_failures += 1
                summary.article_type = summary.article_type or art.article_type_hint or "other"
            else:
                # If model didn't choose a type, fall back to source hint
                if summary.article_type == "other" and art.article_type_hint:
                    summary.article_type = art.article_type_hint

            items.append(RenderItem(article=art, summary=summary))

        failures[name] = cat_failures
        render_categories.append(RenderCategory(name=name, query=query, items=items))

    iso_week = until.isocalendar()[1]
    pdf_filename = f"weekly-report-{until.strftime('%Y')}-W{iso_week:02d}.pdf"

    html = render(
        categories=render_categories,
        since=since,
        until=until,
        sources_used=list(fetchers.keys()),
        pdf_filename=pdf_filename,
    )
    _maybe_write_html(html, save_html or dry_run)

    # Generate PDF (best-effort — falls back to HTML body if WeasyPrint fails)
    pdf_path: Optional[Path] = None
    out_dir = Path("out")
    pdf_target = out_dir / pdf_filename
    try:
        pdf_path = html_to_pdf(html, pdf_target)
    except Exception as exc:
        logger.warning("PDF generation raised, will send HTML only: %s", exc)
        pdf_path = None

    total = sum(len(c.items) for c in render_categories)
    subject = (
        f"[Lit Report] Week {iso_week} · "
        f"{since.strftime('%Y-%m-%d')} – {until.strftime('%Y-%m-%d')} · {total} articles"
    )

    summary_html = render_email_summary(
        categories=render_categories,
        since=since,
        until=until,
        sources_used=list(fetchers.keys()),
        subject=subject,
        pdf_filename=pdf_filename,
    )

    if not dry_run:
        try:
            send_report(
                subject=subject,
                summary_html=summary_html,
                pdf_path=pdf_path,
                fallback_html=html,
            )
        except Exception as exc:
            logger.exception("Failed to send mail: %s", exc)
            return 2
    else:
        logger.info("Dry-run: skipping email send")

    # Final summary
    logger.info("---- Summary ----")
    for cat in render_categories:
        logger.info(
            "  %s: %d articles, %d summary failures",
            cat.name,
            len(cat.items),
            failures.get(cat.name, 0),
        )
    logger.info("Total articles: %d", total)
    return 0


def _maybe_write_html(html: str, do_write: bool) -> None:
    if not do_write:
        return
    out_dir = Path("out")
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "report.html"
    out_path.write_text(html, encoding="utf-8")
    logger.info("Wrote %s", out_path)


def parse_args(argv: Optional[List[str]] = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Weekly literature report")
    p.add_argument("--config", default="config.yaml", help="Path to config.yaml")
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Render only; do not send email. Implies --save-html.",
    )
    p.add_argument(
        "--save-html",
        action="store_true",
        help="Also write the rendered HTML to out/report.html.",
    )
    return p.parse_args(argv)


def main(argv: Optional[List[str]] = None) -> int:
    _setup_logging()
    args = parse_args(argv)
    return run(
        config_path=args.config,
        dry_run=args.dry_run,
        save_html=args.save_html,
    )


if __name__ == "__main__":
    sys.exit(main())
