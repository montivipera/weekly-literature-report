"""Tests for the deduplicator."""

from __future__ import annotations

from src.deduplicator import deduplicate
from src.fetchers.base import Article


def _mk(source, doi=None, title="Some Title", abstract=""):
    return Article(source=source, doi=doi, title=title, abstract=abstract)


def test_doi_dedup_prefers_priority_source():
    a = _mk("crossref", doi="10.1234/x")
    b = _mk("pubmed", doi="10.1234/x")
    out = deduplicate([a, b])
    assert len(out) == 1
    assert out[0].source == "pubmed"


def test_doi_normalization():
    a = _mk("pubmed", doi="https://doi.org/10.1234/X")
    b = _mk("crossref", doi="10.1234/x")
    out = deduplicate([a, b])
    assert len(out) == 1


def test_title_fallback_dedup():
    a = _mk("crossref", title="Foo Bar Baz!")
    b = _mk("pubmed", title="foo bar baz")
    out = deduplicate([a, b])
    assert len(out) == 1
    assert out[0].source == "pubmed"


def test_merge_fills_missing_fields():
    a = _mk("pubmed", doi="10.1/x", abstract="")
    b = _mk("crossref", doi="10.1/x", abstract="An abstract from Crossref")
    out = deduplicate([a, b])
    assert len(out) == 1
    # Pubmed wins, but inherits abstract from Crossref
    assert out[0].source == "pubmed"
    assert out[0].abstract == "An abstract from Crossref"


def test_no_duplicates_passes_through():
    a = _mk("pubmed", doi="10.1/a")
    b = _mk("crossref", doi="10.1/b")
    out = deduplicate([a, b])
    assert len(out) == 2


def test_priority_swap_replaces_in_order():
    a = _mk("arxiv", doi="10.1/x")
    b = _mk("pubmed", doi="10.1/x")
    out = deduplicate([a, b])
    assert len(out) == 1
    assert out[0].source == "pubmed"
