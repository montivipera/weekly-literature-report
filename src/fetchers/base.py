"""Shared fetcher interface and the Article dataclass."""

from __future__ import annotations

import logging
import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

logger = logging.getLogger(__name__)


@dataclass
class Article:
    """Normalized representation of a single article from any source."""

    doi: Optional[str] = None
    title: str = ""
    authors: List[str] = field(default_factory=list)
    journal: Optional[str] = None
    year: Optional[int] = None
    published_date: Optional[datetime] = None
    indexed_date: Optional[datetime] = None
    abstract: str = ""
    source: str = ""
    url: Optional[str] = None
    article_type_hint: Optional[str] = None
    full_text_url: Optional[str] = None
    pmid: Optional[str] = None
    pmcid: Optional[str] = None
    arxiv_id: Optional[str] = None

    def normalized_doi(self) -> Optional[str]:
        if not self.doi:
            return None
        d = self.doi.strip().lower()
        d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
        d = d.strip()
        return d or None

    def normalized_title(self) -> str:
        t = (self.title or "").lower()
        t = re.sub(r"[^a-z0-9\s]", " ", t)
        t = re.sub(r"\s+", " ", t).strip()
        return t

    def stable_id(self) -> str:
        """A best-effort stable identifier for logging and merge tracking."""
        return (
            self.normalized_doi()
            or (self.pmid and f"pmid:{self.pmid}")
            or (self.arxiv_id and f"arxiv:{self.arxiv_id}")
            or (self.url or self.normalized_title())
        )


class BaseFetcher(ABC):
    """All source fetchers share this interface."""

    name: str = "base"

    @abstractmethod
    def fetch(
        self,
        query: str,
        since: datetime,
        until: datetime,
        limit: Optional[int] = None,
    ) -> List[Article]:
        """Return a list of Article objects for the given query and date window."""
        raise NotImplementedError
