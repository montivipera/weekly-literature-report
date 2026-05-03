"""bioRxiv / medRxiv fetcher.

The bioRxiv API does not support search; it only exposes details by date
interval. We fetch the interval and filter client-side using the Boolean AST.
"""

from __future__ import annotations

import logging
import os
import time
from datetime import datetime
from typing import List, Optional

import requests
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ..query_translator import filter_articles, parse_query
from .base import Article, BaseFetcher

logger = logging.getLogger(__name__)

BASE = "https://api.biorxiv.org/details"


def _ua() -> str:
    email = os.environ.get("UNPAYWALL_EMAIL", "anonymous@example.com")
    return f"weekly-literature-report/1.0 (mailto:{email})"


@retry(
    reraise=True,
    stop=stop_after_attempt(4),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    retry=retry_if_exception_type((requests.RequestException,)),
)
def _http_get(url: str, timeout: int = 30) -> requests.Response:
    r = requests.get(url, headers={"User-Agent": _ua()}, timeout=timeout)
    if r.status_code in (429, 500, 502, 503, 504):
        raise requests.RequestException(f"bioRxiv {r.status_code}")
    r.raise_for_status()
    return r


def _parse_record(rec: dict, server: str) -> Optional[Article]:
    try:
        doi = rec.get("doi")
        title = (rec.get("title") or "").strip()
        abstract = (rec.get("abstract") or "").strip()
        authors_raw = rec.get("authors") or ""
        authors = [a.strip() for a in authors_raw.split(";") if a.strip()]
        date_str = rec.get("date") or ""
        try:
            published_date = datetime.strptime(date_str, "%Y-%m-%d") if date_str else None
        except ValueError:
            published_date = None
        year = published_date.year if published_date else None
        url = f"https://www.{server}.org/content/{doi}v{rec.get('version', '1')}" if doi else None
        full_text_url = (
            f"https://www.{server}.org/content/{doi}v{rec.get('version', '1')}.full.pdf"
            if doi
            else None
        )
        journal = rec.get("category") or None

        return Article(
            doi=doi,
            title=title,
            authors=authors,
            journal=journal,
            year=year,
            published_date=published_date,
            indexed_date=published_date,
            abstract=abstract,
            source=server,
            url=url,
            article_type_hint="preprint",
            full_text_url=full_text_url,
        )
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning("Failed to parse bioRxiv record: %s", exc)
        return None


def _fetch_interval(server: str, since: datetime, until: datetime) -> List[dict]:
    """Page through `details/{server}/{from}/{to}/{cursor}` until exhausted."""
    interval = f"{since.strftime('%Y-%m-%d')}/{until.strftime('%Y-%m-%d')}"
    cursor = 0
    out: List[dict] = []
    while True:
        url = f"{BASE}/{server}/{interval}/{cursor}"
        try:
            r = _http_get(url, timeout=60)
            payload = r.json()
        except Exception as exc:
            logger.warning("%s page %s failed: %s", server, cursor, exc)
            break
        collection = payload.get("collection") or []
        out.extend(collection)
        msgs = payload.get("messages") or []
        total = 0
        if msgs:
            total = int(msgs[0].get("total", 0) or 0)
        if not collection:
            break
        cursor += len(collection)
        if total and cursor >= total:
            break
        time.sleep(0.5)
        if cursor > 5000:
            logger.warning("%s: stopping pagination at 5000 records", server)
            break
    return out


class BioRxivFetcher(BaseFetcher):
    name = "biorxiv"

    def __init__(self, include_medrxiv: bool = True):
        self.include_medrxiv = include_medrxiv

    def fetch(
        self,
        query: str,
        since: datetime,
        until: datetime,
        limit: Optional[int] = None,
    ) -> List[Article]:
        try:
            ast = parse_query(query)
        except Exception as exc:
            logger.error("Query translation failed for bioRxiv: %s", exc)
            return []

        servers = ["biorxiv"] + (["medrxiv"] if self.include_medrxiv else [])
        articles: List[Article] = []
        for server in servers:
            records = _fetch_interval(server, since, until)
            for rec in records:
                a = _parse_record(rec, server)
                if a and a.title:
                    articles.append(a)

        try:
            articles = filter_articles(ast, articles)
        except Exception as exc:  # pragma: no cover - defensive
            logger.warning("bioRxiv post-filter failed: %s", exc)

        if limit:
            articles = articles[:limit]
        logger.info("bioRxiv: %d articles", len(articles))
        return articles
