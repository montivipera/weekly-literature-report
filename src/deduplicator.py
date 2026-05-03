"""Deduplicate articles by DOI then normalized title.

Source order is configurable; the first occurrence of an article from a higher-
priority source wins. Useful fields from the loser are merged in (e.g. an
abstract or full-text URL the winner is missing)."""

from __future__ import annotations

import logging
from typing import Iterable, List, Sequence

from .fetchers.base import Article

logger = logging.getLogger(__name__)


DEFAULT_PRIORITY = ("pubmed", "crossref", "biorxiv", "medrxiv", "arxiv", "semantic_scholar")


def _priority_key(article: Article, priority: Sequence[str]) -> int:
    src = (article.source or "").lower()
    try:
        return priority.index(src)
    except ValueError:
        return len(priority)


def _merge_fill(winner: Article, loser: Article) -> Article:
    """Fill in missing-but-useful fields on the winner from the loser."""
    if not winner.abstract and loser.abstract:
        winner.abstract = loser.abstract
    if not winner.full_text_url and loser.full_text_url:
        winner.full_text_url = loser.full_text_url
    if not winner.doi and loser.doi:
        winner.doi = loser.doi
    if not winner.pmid and loser.pmid:
        winner.pmid = loser.pmid
    if not winner.pmcid and loser.pmcid:
        winner.pmcid = loser.pmcid
    if not winner.arxiv_id and loser.arxiv_id:
        winner.arxiv_id = loser.arxiv_id
    if not winner.journal and loser.journal:
        winner.journal = loser.journal
    if not winner.year and loser.year:
        winner.year = loser.year
    if not winner.published_date and loser.published_date:
        winner.published_date = loser.published_date
    if not winner.authors and loser.authors:
        winner.authors = list(loser.authors)
    if not winner.url and loser.url:
        winner.url = loser.url
    return winner


def deduplicate(
    articles: Iterable[Article],
    priority: Sequence[str] = DEFAULT_PRIORITY,
) -> List[Article]:
    """Return a deduplicated list, preferring earlier sources in `priority`."""
    by_doi: dict[str, Article] = {}
    by_title: dict[str, Article] = {}
    out_order: list[Article] = []

    for art in articles:
        doi_key = art.normalized_doi()
        title_key = art.normalized_title() if not doi_key else None

        existing = None
        if doi_key and doi_key in by_doi:
            existing = by_doi[doi_key]
        elif title_key and title_key in by_title:
            existing = by_title[title_key]

        if existing is None:
            if doi_key:
                by_doi[doi_key] = art
            if title_key:
                by_title[title_key] = art
            out_order.append(art)
            continue

        # Decide winner
        if _priority_key(art, priority) < _priority_key(existing, priority):
            # Replace existing in mapping and in out_order
            _merge_fill(art, existing)
            idx = out_order.index(existing)
            out_order[idx] = art
            if doi_key:
                by_doi[doi_key] = art
            if title_key:
                by_title[title_key] = art
            # If existing was indexed under a title that art also has, sync
            ex_title = existing.normalized_title()
            if ex_title and ex_title in by_title and by_title[ex_title] is existing:
                by_title[ex_title] = art
        else:
            _merge_fill(existing, art)

    logger.info(
        "Deduplicated %d -> %d articles",
        sum(1 for _ in articles) if isinstance(articles, list) else len(out_order),
        len(out_order),
    )
    return out_order
