"""Semantic Scholar Graph API fetcher."""

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

S2_SEARCH = "https://api.semanticscholar.org/graph/v1/paper/search"

FIELDS = ",".join([
    "paperId",
    "externalIds",
    "title",
    "abstract",
    "authors",
    "venue",
    "journal",
    "year",
    "publicationDate",
    "publicationTypes",
    "url",
    "openAccessPdf",
])


def _ua() -> str:
    email = os.environ.get("UNPAYWALL_EMAIL", "anonymous@example.com")
    return f"weekly-literature-report/1.0 (mailto:{email})"


@retry(
    reraise=True,
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=2, max=20),
    retry=retry_if_exception_type((requests.RequestException,)),
)
def _http_get(url: str, params: dict, timeout: int = 45) -> requests.Response:
    headers = {"User-Agent": _ua()}
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    if api_key:
        headers["x-api-key"] = api_key
    r = requests.get(url, params=params, headers=headers, timeout=timeout)
    if r.status_code in (429, 500, 502, 503, 504):
        raise requests.RequestException(f"S2 {r.status_code}")
    r.raise_for_status()
    return r


def _parse_paper(p: dict) -> Optional[Article]:
    try:
        ext = p.get("externalIds") or {}
        doi = ext.get("DOI")
        title = (p.get("title") or "").strip()
        abstract = (p.get("abstract") or "").strip()
        authors = [a.get("name", "").strip() for a in (p.get("authors") or []) if a.get("name")]
        journal = (p.get("journal") or {}).get("name") or p.get("venue")
        year = p.get("year")
        pub_str = p.get("publicationDate")
        published_date = None
        if pub_str:
            try:
                published_date = datetime.strptime(pub_str, "%Y-%m-%d")
            except ValueError:
                pass
        url = p.get("url") or (f"https://doi.org/{doi}" if doi else None)

        types = [t.lower() for t in (p.get("publicationTypes") or [])]
        type_hint = "research_article"
        if any("review" in t for t in types):
            type_hint = "review"
        if any("meta" in t for t in types):
            type_hint = "meta_analysis"

        oa = p.get("openAccessPdf") or {}
        full_text_url = oa.get("url")

        return Article(
            doi=doi,
            title=title,
            authors=authors,
            journal=journal,
            year=year,
            published_date=published_date,
            indexed_date=published_date,
            abstract=abstract,
            source="semantic_scholar",
            url=url,
            article_type_hint=type_hint,
            full_text_url=full_text_url,
        )
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning("Failed to parse Semantic Scholar paper: %s", exc)
        return None


class SemanticScholarFetcher(BaseFetcher):
    name = "semantic_scholar"

    def fetch(
        self,
        query: str,
        since: datetime,
        until: datetime,
        limit: Optional[int] = None,
    ) -> List[Article]:
        try:
            ast = parse_query(query)
            q = to_bibliographic(ast)
        except Exception as exc:
            logger.error("Query translation failed for Semantic Scholar: %s", exc)
            return []

        params = {
            "query": q,
            "limit": str(min(limit or 100, 100)),
            "fields": FIELDS,
            "publicationDateOrYear": (
                f"{since.strftime('%Y-%m-%d')}:{until.strftime('%Y-%m-%d')}"
            ),
        }
        try:
            r = _http_get(S2_SEARCH, params)
            data = r.json()
        except Exception as exc:
            logger.warning("Semantic Scholar unreachable: %s", exc)
            return []

        articles: List[Article] = []
        for p in data.get("data") or []:
            a = _parse_paper(p)
            if not a or not a.title:
                continue
            articles.append(a)

        try:
            articles = filter_articles(ast, articles)
        except Exception as exc:  # pragma: no cover - defensive
            logger.warning("Semantic Scholar post-filter failed: %s", exc)

        time.sleep(1.0)
        logger.info("Semantic Scholar: %d articles", len(articles))
        return articles
