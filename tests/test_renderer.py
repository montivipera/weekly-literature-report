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


def _summary(article_type="research_article", domain="ecology"):
    return Summary(
        article_type=article_type,
        domain=domain,
        aim=["Investigate X."],
        gap=["No prior work on Y."],
        methods=["Field sampling.", "Random forest classifier."],
        conclusions=["X is associated with Y.", "Recommends further study."],
    )


def test_renders_two_categories_with_articles():
    cats = [
        RenderCategory(
            name="Vegetation monitoring",
            query='vegetation AND monitoring',
            items=[
                RenderItem(
                    article=_article("Forest canopy dynamics"),
                    summary=_summary(domain="ecology"),
                ),
                RenderItem(
                    article=_article(
                        "Grassland restoration trial",
                        source="biorxiv",
                        doi="10.1/y",
                    ),
                    summary=_summary(article_type="preprint", domain="hydrology"),
                ),
            ],
        ),
        RenderCategory(
            name="Soil microbiome",
            query='"soil microbiome"',
            items=[
                RenderItem(
                    article=_article("Microbiome meta-analysis"),
                    summary=_summary(article_type="meta_analysis", domain="molecular"),
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

    assert "weekly literature report" in html.lower()
    assert "Vegetation monitoring" in html
    assert "Soil microbiome" in html
    assert "Forest canopy dynamics" in html
    assert "Grassland restoration trial" in html
    assert "Microbiome meta-analysis" in html
    # Domain section names
    assert "Ecology &amp; Biodiversity" in html or "Ecology & Biodiversity" in html
    assert "Hydrology" in html
    assert "Molecular" in html
    # Pills / sections
    assert "Key findings" in html
    assert "10.1/x" in html
    # Article-type rendering (with underscores replaced)
    assert "research article" in html.lower()
    assert "preprint" in html.lower()
    assert "meta-analysis" in html.lower() or "meta analysis" in html.lower()


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
    """When summary is empty for a featured card, the placeholder should appear."""
    # Three articles in same domain forces the first one into 'featured' mode
    cats = [
        RenderCategory(
            name="x",
            query="foo",
            items=[
                RenderItem(
                    article=_article("Featured title"),
                    summary=Summary(article_type="other", domain="ecology"),
                ),
                RenderItem(
                    article=_article("Compact 1", doi="10.1/a"),
                    summary=Summary(article_type="other", domain="ecology"),
                ),
                RenderItem(
                    article=_article("Compact 2", doi="10.1/b"),
                    summary=Summary(article_type="other", domain="ecology"),
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
    # Featured card with empty summary shows the placeholder
    assert "Not stated." in html
    assert "Featured title" in html


def test_render_groups_by_domain():
    """Articles must end up under their domain, not duplicated."""
    cats = [
        RenderCategory(
            name="cat",
            query="x",
            items=[
                RenderItem(article=_article("A1", doi="10.1/a"), summary=_summary(domain="molecular")),
                RenderItem(article=_article("A2", doi="10.1/b"), summary=_summary(domain="molecular")),
                RenderItem(article=_article("E1", doi="10.1/c"), summary=_summary(domain="ecology")),
            ],
        ),
    ]
    html = render(
        categories=cats,
        since=datetime(2026, 4, 25),
        until=datetime(2026, 5, 2),
        sources_used=["pubmed"],
    )
    # Both molecular articles appear, ecology section also exists
    assert "A1" in html
    assert "A2" in html
    assert "E1" in html
    # Domain filter pills
    assert "Molecular" in html
    assert "Ecology" in html


def test_render_query_tokenization():
    """The query bar should render Boolean tokens as pills."""
    cats = [
        RenderCategory(
            name="cat",
            query='"wetland" AND (restoration OR biodiversity)',
            items=[
                RenderItem(
                    article=_article("title"),
                    summary=_summary(),
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
    assert "Search query" in html
    assert "wetland" in html
    assert "restoration" in html
    assert "biodiversity" in html
    assert "qtoken" in html
    assert "qop" in html
