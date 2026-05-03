"""Tests for HTML rendering."""

from __future__ import annotations

from datetime import datetime

from src.fetchers.base import Article
from src.renderer import RenderCategory, RenderItem, html_to_text, render
from src.summarizer import Summary


def _article(title, source="pubmed", doi="10.1/x", year=2026, journal="Nature"):
    return Article(
        title=title,
        authors=["Alice Author", "Bob Researcher"],
        journal=journal,
        year=year,
        source=source,
        doi=doi,
        abstract="Some abstract.",
    )


def _summary(article_type="research_article"):
    return Summary(
        article_type=article_type,
        aim=["Investigate X."],
        gap=["No prior work on Y."],
        methods=["Field sampling.", "Random forest classifier."],
        conclusions=["X is associated with Y.", "Recommends further study."],
    )


def test_renders_two_categories_with_articles():
    cats = [
        RenderCategory(
            name="Vegetation monitoring",
            items=[
                RenderItem(article=_article("Forest canopy dynamics"), summary=_summary()),
                RenderItem(
                    article=_article(
                        "Grassland restoration trial",
                        source="biorxiv",
                        doi="10.1/y",
                    ),
                    summary=_summary(article_type="preprint"),
                ),
            ],
        ),
        RenderCategory(
            name="Soil microbiome",
            items=[
                RenderItem(
                    article=_article("Microbiome meta-analysis"),
                    summary=_summary(article_type="meta_analysis"),
                ),
            ],
        ),
    ]
    html = render(
        categories=cats,
        since=datetime(2026, 4, 25),
        until=datetime(2026, 5, 2),
        sources_used=["pubmed", "biorxiv"],
    )

    assert "Weekly literature report" in html
    assert "Vegetation monitoring" in html
    assert "Soil microbiome" in html
    assert "Forest canopy dynamics" in html
    assert "Grassland restoration trial" in html
    assert "Microbiome meta-analysis" in html
    assert "Aim" in html
    assert "Gap" in html
    assert "Methods" in html
    assert "Conclusions" in html
    assert "10.1/x" in html
    assert "pill-research_article" in html
    assert "pill-preprint" in html
    assert "pill-meta_analysis" in html


def test_renders_empty_state():
    html = render(
        categories=[],
        since=datetime(2026, 4, 25),
        until=datetime(2026, 5, 2),
        sources_used=["pubmed"],
    )
    assert "No enabled categories" in html


def test_renders_category_with_no_articles():
    cats = [RenderCategory(name="Empty cat", items=[])]
    html = render(
        categories=cats,
        since=datetime(2026, 4, 25),
        until=datetime(2026, 5, 2),
        sources_used=["pubmed"],
    )
    assert "No new articles" in html


def test_html_to_text_strips_tags():
    html = "<p>Hello <b>world</b></p><ul><li>One</li><li>Two</li></ul>"
    text = html_to_text(html)
    assert "Hello" in text
    assert "world" in text
    assert "<" not in text


def test_render_falls_back_when_summary_empty():
    cats = [
        RenderCategory(
            name="x",
            items=[
                RenderItem(
                    article=_article("t"),
                    summary=Summary(article_type="other"),  # no bullets
                ),
            ],
        ),
    ]
    html = render(
        categories=cats,
        since=datetime(2026, 4, 25),
        until=datetime(2026, 5, 2),
        sources_used=["pubmed"],
    )
    assert "Not stated." in html
