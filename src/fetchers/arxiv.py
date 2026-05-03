"""arXiv fetcher using the Atom API."""

from __future__ import annotations

import logging
import os
import time
from datetime import datetime, timezone
from typing import List, Optional

import feedparser
import requests
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ..query_translator import filter_articles, parse_query, to_arxiv
from .base import Article, BaseFetcher

logger = logging.getLogger(__name__)

ARXIV_API = "http://export.arxiv.org/api/query"


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
        raise requests.RequestException(f"arXiv {r.status_code}")
    r.raise_for_status()
    return r


def _parse_entry(entry) -> Optional[Article]:
    try:
        title = (entry.get("title") or "").replace("\n", " ").strip()
        summary = (entry.get("summary") or "").replace("\n", " ").strip()
        authors = [a.get("name", "").strip() for a in entry.get("authors", []) if a.get("name")]
        # arXiv entry id like http://arxiv.org/abs/2401.12345v1
        eid = entry.get("id", "")
        arxiv_id = eid.rsplit("/", 1)[-1] if eid else None

        # DOI may be present as arxiv_doi or in links
        doi = entry.get("arxiv_doi") or None
        if not doi:
            for link in entry.get("links", []):
                if link.get("title") == "doi":
                    href = link.get("href", "")
                    if "doi.org/" in href:
                        doi = href.split("doi.org/", 1)[1]
                        break

        # Published date
        published_str = entry.get("published") or entry.get("updated")
        published_date = None
        if published_str:
            try:
                published_date = datetime.strptime(
                    published_str, "%Y-%m-%dT%H:%M:%SZ"
                ).replace(tzinfo=timezone.utc)
            except ValueError:
                pass

        url = entry.get("link") or eid
        # PDF link
        pdf_url = None
        for link in entry.get("links", []):
            if link.get("type") == "application/pdf":
                pdf_url = link.get("href")
                break

        year = published_date.year if published_date else None

        # Primary category as journal-ish label
        primary = entry.get("arxiv_primary_category", {})
        journal = primary.get("term") if isinstance(primary, dict) else None

        return Article(
            doi=doi,
            title=title,
            authors=authors,
            journal=journal,
            year=year,
            published_date=published_date.replace(tzinfo=None) if published_date else None,
            indexed_date=published_date.replace(tzinfo=None) if published_date else None,
            abstract=summary,
            source="arxiv",
            url=url,
            article_type_hint="preprint",
            full_text_url=pdf_url,
            arxiv_id=arxiv_id,
        )
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning("Failed to parse arXiv entry: %s", exc)
        return None


class ArxivFetcher(BaseFetcher):
    name = "arxiv"

    def fetch(
        self,
        query: str,
        since: datetime,
        until: datetime,
        limit: Optional[int] = None,
    ) -> List[Article]:
        try:
            ast = parse_query(query)
            search_query = to_arxiv(ast)
        except Exception as exc:
            logger.error("Query translation failed for arXiv: %s", exc)
            return []

        params = {
            "search_query": search_query,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
            "max_results": str(min(limit or 100, 200)),
        }
        try:
            r = _http_get(ARXIV_API, params, timeout=30)
        except Exception as exc:
            logger.warning("arXiv unreachable: %s", exc)
            return []

        feed = feedparser.parse(r.content)
        articles: List[Article] = []
        for entry in feed.entries:
            article = _parse_entry(entry)
            if not article or not article.title:
                continue
            if article.published_date is None:
                continue
            if since <= article.published_date <= until:
                articles.append(article)

        # arXiv's Boolean is decent but quoting is finicky — re-filter client-side
        try:
            articles = filter_articles(ast, articles)
        except Exception as exc:  # pragma: no cover - defensive
            logger.warning("arXiv post-filter failed: %s", exc)

        time.sleep(3.0)  # be polite — arXiv asks for >=3s between batched requests
        logger.info("arXiv: %d articles", len(articles))
        return articles
