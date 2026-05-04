"""Render the report as a PDF using WeasyPrint.

The PDF uses a print-optimized variant of the HTML template — the regular
template's hover effects and viewport-relative sizing don't translate well to
print, and we want explicit page breaks between domain sections.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def _print_css() -> str:
    """Page-level CSS overrides applied on top of the HTML report's styles."""
    return """
    @page {
        size: A4;
        margin: 14mm 14mm 16mm 14mm;
        @bottom-center {
            content: "Weekly Literature Report  ·  page " counter(page) " of " counter(pages);
            font-family: Georgia, serif;
            font-size: 9pt;
            color: #9a9890;
            font-style: italic;
        }
    }

    /* Override viewport-based sizing that doesn't translate to print. */
    html, body {
        background: #ffffff !important;
        background-image: none !important;
    }
    .layout {
        min-height: auto !important;
        padding: 0 !important;
        max-width: none !important;
        margin: 0 !important;
        gap: 12px !important;
    }

    /* Print-friendly typography sizing (px → reasonable on A4). */
    .hero-left h1 { font-size: 26pt; line-height: 1.15; }
    .stat strong { font-size: 18pt; }
    .stat span { font-size: 8pt; }
    .category-header h2 { font-size: 16pt; }
    .domain-header h3 { font-size: 13pt; }
    .card-title { font-size: 11pt; }
    .card.featured .card-title { font-size: 14pt; }
    .card.wide .card-title { font-size: 12pt; }
    .card-authors { font-size: 9pt; }
    .section ul { font-size: 9.5pt; }
    .section .label { font-size: 7.5pt; }
    .pill, .pill-domain, .pill-type { font-size: 7.5pt; }
    .meta { font-size: 8.5pt; }
    .doi { font-size: 8pt; }
    .qtoken { font-size: 9pt; }
    .qop { font-size: 8pt; }

    /* Cards must not split across pages. */
    .card {
        page-break-inside: avoid;
        break-inside: avoid;
        box-shadow: none !important;
    }
    .domain-header { page-break-after: avoid; break-after: avoid; }

    /* Each domain section starts fresh on a page when there isn't enough room. */
    .domain { page-break-inside: auto; }

    /* Drop interactive bits — they're meaningless in print. */
    .domain-pill { pointer-events: none; }
    a { color: #0f4c5c !important; text-decoration: none; }

    /* Grid: WeasyPrint supports CSS Grid — keep 4 columns on A4 in landscape,
       but A4 portrait doesn't have room for 4. Force 2-column for portrait
       which matches our @page size. */
    .grid {
        grid-template-columns: repeat(2, 1fr) !important;
        grid-auto-rows: auto !important;
    }
    .grid .card.featured { grid-column: span 2 !important; grid-row: span 1 !important; }
    .grid .card.wide { grid-column: span 2 !important; }

    /* Hide cosmetic gradients that confuse some PDF readers. */
    .card.featured { background: #ffffff !important; }
    """


def html_to_pdf(html: str, output_path: Path) -> Optional[Path]:
    """Render the given HTML report to a PDF file.

    Returns the path on success, ``None`` if WeasyPrint is unavailable or
    rendering fails — callers should treat the PDF as best-effort and fall
    back to HTML-only delivery.
    """
    try:
        # Imported lazily so the rest of the system runs even if WeasyPrint's
        # native deps aren't installed locally.
        from weasyprint import CSS, HTML  # type: ignore
    except ImportError as exc:
        logger.error("WeasyPrint not installed: %s", exc)
        return None

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        HTML(string=html, base_url=".").write_pdf(
            target=str(output_path),
            stylesheets=[CSS(string=_print_css())],
        )
        logger.info("Wrote PDF: %s (%d bytes)", output_path, output_path.stat().st_size)
        return output_path
    except Exception as exc:
        logger.exception("PDF generation failed: %s", exc)
        return None
