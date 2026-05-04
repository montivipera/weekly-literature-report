"""Render the report as a PDF using WeasyPrint.

The HTML supplied here should already be the print-native template
(``report_pdf.html.j2``) — page size, margins, fonts and breaks live in that
template's ``<style>`` block, so this module is just a thin WeasyPrint wrapper.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


def html_to_pdf(html: str, output_path: Path) -> Optional[Path]:
    """Render the given HTML to a PDF file at ``output_path``.

    Returns the path on success, ``None`` if WeasyPrint is unavailable or
    rendering fails — callers should treat the PDF as best-effort and fall
    back to HTML-only delivery.
    """
    try:
        # Imported lazily so the rest of the system runs even if WeasyPrint's
        # native deps aren't installed locally.
        from weasyprint import HTML  # type: ignore
    except ImportError as exc:
        logger.error("WeasyPrint not installed: %s", exc)
        return None

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        HTML(string=html, base_url=".").write_pdf(target=str(output_path))
        logger.info("Wrote PDF: %s (%d bytes)", output_path, output_path.stat().st_size)
        return output_path
    except Exception as exc:
        logger.exception("PDF generation failed: %s", exc)
        return None
