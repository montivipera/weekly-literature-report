"""PubMed fetcher using NCBI E-utilities."""

from __future__ import annotations

import logging
import os
import time
from datetime import datetime
from typing import List, Optional
from xml.etree import ElementTree as ET

import requests
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from ..query_translator import parse_query, to_pubmed
from .base import Article, BaseFetcher

logger = logging.getLogger(__name__)

ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


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
        raise requests.RequestException(f"PubMed {r.status_code}")
    r.raise_for_status()
    return r


def _date_field(article: ET.Element, tag_path: str) -> Optional[datetime]:
    el = article.find(tag_path)
    if el is None:
        return None
    y = el.findtext("Year")
    m = el.findtext("Month") or "1"
    d = el.findtext("Day") or "1"
    if not y:
        return None
    months = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
        "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
    }
    try:
        month = int(m) if m.isdigit() else months.get(m[:3], 1)
        return datetime(int(y), month, int(d))
    except (ValueError, TypeError):
        return None


def _parse_pubmed_article(art_el: ET.Element) -> Optional[Article]:
    try:
        medline = art_el.find("MedlineCitation")
        if medline is None:
            return None
        article_el = medline.find("Article")
        if article_el is None:
            return None

        pmid = medline.findtext("PMID") or None
        title = (article_el.findtext("ArticleTitle") or "").strip()

        # Abstract — concatenate AbstractText nodes (some have labels)
        abstract_parts: List[str] = []
        ab = article_el.find("Abstract")
        if ab is not None:
            for at in ab.findall("AbstractText"):
                label = at.get("Label")
                text = "".join(at.itertext()).strip()
                if label:
                    abstract_parts.append(f"{label}: {text}")
                else:
                    abstract_parts.append(text)
        abstract = "\n".join(p for p in abstract_parts if p)

        # Authors
        authors: List[str] = []
        author_list = article_el.find("AuthorList")
        if author_list is not None:
            for a in author_list.findall("Author"):
                last = a.findtext("LastName") or ""
                fore = a.findtext("ForeName") or a.findtext("Initials") or ""
                name = f"{fore} {last}".strip()
                if name:
                    authors.append(name)
                else:
                    coll = a.findtext("CollectiveName")
                    if coll:
                        authors.append(coll)

        # Journal
        journal = None
        journal_el = article_el.find("Journal")
        if journal_el is not None:
            journal = journal_el.findtext("Title") or journal_el.findtext("ISOAbbreviation")

        # DOI / PMC
        doi = None
        pmcid = None
        for elist in (
            article_el.findall("ELocationID"),
            (medline.find("PubmedData/ArticleIdList") or ET.Element("x")).findall("ArticleId"),
        ):
            for el in elist:
                t = el.get("EIdType") or el.get("IdType")
                val = (el.text or "").strip()
                if not val:
                    continue
                if t == "doi":
                    doi = val
                elif t == "pmc":
                    pmcid = val if val.lower().startswith("pmc") else f"PMC{val}"

        # Dates: published (DP / ArticleDate) and indexed (PubmedPubDate[PubStatus=entrez])
        published_date = (
            _date_field(article_el, "ArticleDate")
            or _date_field(article_el, "Journal/JournalIssue/PubDate")
        )
        indexed_date = None
        pubmed_data = art_el.find("PubmedData/History")
        if pubmed_data is not None:
            for d in pubmed_data.findall("PubMedPubDate"):
                if d.get("PubStatus") in ("entrez", "pubmed"):
                    indexed_date = _date_field(art_el, f"PubmedData/History/PubMedPubDate[@PubStatus='{d.get('PubStatus')}']")
                    if indexed_date:
                        break

        # Article type hint
        type_hint = "research_article"
        ptl = article_el.find("PublicationTypeList")
        if ptl is not None:
            types_lower = [(pt.text or "").lower() for pt in ptl.findall("PublicationType")]
            if any("meta-analysis" in t for t in types_lower):
                type_hint = "meta_analysis"
            elif any(("review" in t) for t in types_lower):
                type_hint = "review"

        url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else None
        full_text_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/" if pmcid else None

        year = published_date.year if published_date else None

        return Article(
            doi=doi,
            title=title,
            authors=authors,
            journal=journal,
            year=year,
            published_date=published_date,
            indexed_date=indexed_date,
            abstract=abstract,
            source="pubmed",
            url=url,
            article_type_hint=type_hint,
            full_text_url=full_text_url,
            pmid=pmid,
            pmcid=pmcid,
        )
    except Exception as exc:  # pragma: no cover - defensive
        logger.warning("Failed to parse PubMed article: %s", exc)
        return None


class PubMedFetcher(BaseFetcher):
    name = "pubmed"

    def fetch(
        self,
        query: str,
        since: datetime,
        until: datetime,
        limit: Optional[int] = None,
    ) -> List[Article]:
        try:
            ast = parse_query(query)
            term = to_pubmed(ast)
        except Exception as exc:
            logger.error("Query translation failed for PubMed: %s", exc)
            return []

        # Combine with EDAT / PDAT date range. NCBI date format is YYYY/MM/DD.
        date_filter = (
            f"({since.strftime('%Y/%m/%d')}:{until.strftime('%Y/%m/%d')}[edat]) "
            f"OR ({since.strftime('%Y/%m/%d')}:{until.strftime('%Y/%m/%d')}[pdat])"
        )
        full_term = f"({term}) AND ({date_filter})"

        retmax = limit if limit else 200
        params = {
            "db": "pubmed",
            "term": full_term,
            "retmax": str(retmax),
            "retmode": "json",
            "sort": "pub+date",
        }
        try:
            r = _http_get(ESEARCH, params)
            data = r.json()
            ids = data.get("esearchresult", {}).get("idlist", [])
        except Exception as exc:
            logger.warning("PubMed esearch failed: %s", exc)
            return []

        if not ids:
            return []

        time.sleep(0.34)  # ~3 req/sec without API key
        try:
            r = _http_get(
                EFETCH,
                {"db": "pubmed", "id": ",".join(ids), "retmode": "xml"},
                timeout=60,
            )
        except Exception as exc:
            logger.warning("PubMed efetch failed: %s", exc)
            return []

        articles: List[Article] = []
        try:
            root = ET.fromstring(r.content)
        except ET.ParseError as exc:
            logger.warning("PubMed XML parse error: %s", exc)
            return []

        for art_el in root.findall("PubmedArticle"):
            article = _parse_pubmed_article(art_el)
            if article and article.title:
                articles.append(article)

        logger.info("PubMed: %d articles", len(articles))
        return articles
