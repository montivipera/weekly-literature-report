"""Tests for the Boolean query parser and serializers."""

from __future__ import annotations

import pytest

from src.query_translator import (
    And,
    Not,
    Or,
    Term,
    filter_articles,
    matches,
    parse_query,
    to_arxiv,
    to_bibliographic,
    to_pubmed,
)


# ---------------------------------------------------------------------------
# Tokenization / parsing
# ---------------------------------------------------------------------------


def test_parse_single_term():
    ast = parse_query("vegetation")
    assert isinstance(ast, Term)
    assert ast.text == "vegetation"
    assert ast.quoted is False


def test_parse_phrase():
    ast = parse_query('"plant community"')
    assert isinstance(ast, Term)
    assert ast.text == "plant community"
    assert ast.quoted is True


def test_parse_and_or_not():
    ast = parse_query("(a OR b) AND NOT c")
    assert isinstance(ast, And)
    assert isinstance(ast.children[0], Or)
    assert isinstance(ast.children[1], Not)


def test_parse_implicit_and():
    ast = parse_query("foo bar")
    assert isinstance(ast, And)
    assert [c.text for c in ast.children] == ["foo", "bar"]


def test_parse_lowercase_operators():
    ast = parse_query("a and b or c")
    assert isinstance(ast, Or)


def test_parse_unbalanced_parens_raises():
    with pytest.raises(ValueError):
        parse_query("(a OR b")


# ---------------------------------------------------------------------------
# Serializers
# ---------------------------------------------------------------------------


def test_pubmed_serialization():
    ast = parse_query('vegetation AND "remote sensing"')
    out = to_pubmed(ast)
    assert "[Title/Abstract]" in out
    assert "AND" in out
    assert '"remote sensing"' in out


def test_pubmed_not_serialization():
    ast = parse_query('a NOT b')
    out = to_pubmed(ast)
    assert "NOT" in out


def test_arxiv_serialization():
    ast = parse_query('"machine learning" AND vision')
    out = to_arxiv(ast)
    assert "all:" in out
    assert "AND" in out
    assert '"machine learning"' in out


def test_arxiv_andnot():
    ast = parse_query('a NOT b')
    out = to_arxiv(ast)
    assert "ANDNOT" in out


def test_bibliographic_drops_not():
    ast = parse_query('foo AND bar NOT baz')
    out = to_bibliographic(ast)
    assert "foo" in out
    assert "bar" in out
    assert "baz" not in out


# ---------------------------------------------------------------------------
# Client-side evaluation
# ---------------------------------------------------------------------------


def test_matches_simple_term():
    ast = parse_query("vegetation")
    assert matches(ast, "Vegetation cover changes over time")
    assert not matches(ast, "Soil microbiome paper")


def test_matches_word_boundaries():
    ast = parse_query("cat")
    assert matches(ast, "The cat sat down")
    assert not matches(ast, "scattering of light")


def test_matches_phrase():
    ast = parse_query('"plant community"')
    assert matches(ast, "We measured plant community structure")
    assert not matches(ast, "We measured plant species community level")


def test_matches_and_or_not():
    ast = parse_query("(restoration OR monitoring) AND vegetation NOT review")
    assert matches(ast, "Vegetation monitoring of grasslands")
    assert not matches(ast, "Vegetation review of restoration techniques")
    assert not matches(ast, "Soil monitoring techniques")


def test_filter_articles():
    class A:
        def __init__(self, title, abstract=""):
            self.title = title
            self.abstract = abstract

    arts = [
        A("Vegetation monitoring of meadows"),
        A("Soil microbiome diversity"),
        A("Plant community restoration", abstract="A vegetation study"),
    ]
    ast = parse_query("vegetation")
    filtered = filter_articles(ast, arts)
    assert len(filtered) == 2
