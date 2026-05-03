"""Crossref REST API fetcher.

Crossref does not support full Boolean syntax. We pass the bibliographic terms
ANDed via ``query.bibliographic`` and re-apply the Boolean AST client-side.
"""

from __future__ import annotations

import logging
import os
import time
from datetime import datetime
from typing import List, Optional

import requests
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ..query_translator import filter_articles, parse_query, to_bibliographic
from .base import Article, BaseFetcher

logger = logging.getLogger(__name__)

CROSSREF = "https://api.crossref.org/works"


def _ua() -> str:
    email = os.environ.get("UNPAYWALL_EMAIL", "anonymous@example.com")
    return f"weekly-literature-report/1.0 (mailto:{email})"


@retry(
    reraise=True,
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((requests.RequestException,)),
)
def _http_get(url: str, params: dict, timeout: int = 30) -> requests.Response:
    r = requests.get(url, params=params, headers={"User-Agent": _ua()}, timeout=timeout)
    if r.status_code in (429, 500, 502, 503, 504):
        raise requests.RequestException(f"Crossref {r.status_code}")
    r.raise_for_status()
    return r


def _date_from_parts(parts) -> Optional[datetime]:
    try:
        if not parts:
            return None
        bits = parts[0] if isinstance(parts, list) else parts
        if not bits:
            return None
        y = bits[0]
        m = bits[1] if len(bits) > 1 else 1
        d = bits[2] if len(bits) > 2 else 1
        return datetime(int(y), int(m), int(d))
    except Exception:
        return None


def _parse_item(item: dict) -> Optional[Article]:
    try:
        doi = item.get("DOI")
        title_list = item.get("title") or []
        title = (title_list[0] if title_list else "").strip()
        abstract = (item.get("abstract") or "").strip()
        # Crossref abstracts often come wrapped in <jats:p> tags — strip them
        if abstract:
            import re as _re
            abstract = _re.sub(r"<[^>]+>", " ", abstract)
            abstract = _re.sub(r"\s+", " ", abstract).strip()

        authors = []
        for a in item.get("author") or []:
            given = a.get("given") or ""
            family = a.get("family") or ""
            name = f"{given} {family}".strip()
            if name:
                authors.append(name)

        journal = None
        ct = item.get("container-title")
        if ct:
            journal = ct[0] if isinstance(ct, list) else ct

        published_date = (
            _date_from_parts(item.get("issued", {}).get("date-parts"))
            or _date_from_parts(item.get("published-print", {}).get("date-parts"))
            or _date_from_parts(item.get("published-online", {}).get("date-parts"))
        )
        indexed_date = None
        idx = item.get("indexed", {})
        idx_parts = idx.get("date-parts") if isinstance(idx, dict) else None
        indexed_date = _date_from_parts(idx_parts)

        year = published_date.year if published_date else None

        type_str = (item.get("type") or "").lower()
        type_hint = "research_article"
        if "review" in type_str:
            type_hint = "review"
        elif "posted-content" in type_str or "preprint" in type_str:
            type_hint = "preprint"

        url = item.get("URL") or (f"https://doi.org/{doi}" if doi else None)

        return Article(
            doi=doi,
            title=title,
            authors=authors,
            journal=journal,
            year=year,
            published_date=published_date,
            indexed_date=indexed_date,
            abstract=abstract,
            source="crossref",
            url=url,
            article_type_hint=type_hint,
        )
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning("Failed to parse Crossref item: %s", exc)
        return None


class CrossrefFetcher(BaseFetcher):
    name = "crossref"

    def fetch(
        self,
        query: str,
        since: datetime,
        until: datetime,
        limit: Optional[int] = None,
    ) -> List[Article]:
        try:
            ast = parse_query(query)
            biblio = to_bibliographic(ast)
        except Exception as exc:
            logger.error("Query translation failed for Crossref: %s", exc)
            return []

        rows = min(limit or 100, 1000)
        params = {
            "query.bibliographic": biblio,
            "filter": (
                f"from-pub-date:{since.strftime('%Y-%m-%d')},"
                f"until-pub-date:{until.strftime('%Y-%m-%d')},"
                f"from-index-date:{since.strftime('%Y-%m-%d')}"
            ),
            "rows": str(rows),
            "sort": "issued",
            "order": "desc",
        }
        try:
            r = _http_get(CROSSREF, params, timeout=45)
            data = r.json()
        except Exception as exc:
            logger.warning("Crossref unreachable: %s", exc)
            return []

        items = data.get("message", {}).get("items", [])
        articles: List[Article] = []
        for it in items:
            a = _parse_item(it)
            if not a or not a.title:
                continue
            # Keep things in the date window even though the filter should already
            ref_date = a.published_date or a.indexed_date
            if ref_date and (ref_date < since or ref_date > until):
                continue
            articles.append(a)

        try:
            articles = filter_articles(ast, articles)
        except Exception as exc:  # pragma: no cover - defensive
            logger.warning("Crossref post-filter failed: %s", exc)

        time.sleep(0.5)
        logger.info("Crossref: %d articles", len(articles))
        return articles
