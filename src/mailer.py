"""Send the rendered report via Gmail SMTP."""

from __future__ import annotations

import logging
import mimetypes
import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from typing import List, Optional, Sequence, Union

from .renderer import html_to_text

logger = logging.getLogger(__name__)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


class MailerError(RuntimeError):
    pass


def send_report(
    *,
    subject: str,
    summary_html: str,
    pdf_paths: Optional[Sequence[Path]] = None,
    pdf_path: Optional[Path] = None,  # legacy, single attachment
    fallback_html: Optional[str] = None,
    to: Optional[str] = None,
    sender: Optional[str] = None,
    password: Optional[str] = None,
) -> None:
    """Send a report email.

    Args:
        subject: Subject line.
        summary_html: Compact HTML summary used as the email body.
        pdf_paths: Sequence of PDF files to attach. Each existing file is
            attached. If empty/None, no PDFs are attached.
        pdf_path: Legacy single-PDF parameter, kept for backwards compatibility.
        fallback_html: If no PDFs end up attached, this full HTML report is
            used as the body instead of the summary so no information is lost.
        to: Recipient. Defaults to ``MAIL_TO`` env var or the sender address.
        sender: Sender Gmail address. Defaults to ``GMAIL_ADDRESS``.
        password: Gmail app password. Defaults to ``GMAIL_APP_PASSWORD``.
    """
    sender = sender or os.environ.get("GMAIL_ADDRESS")
    password = password or os.environ.get("GMAIL_APP_PASSWORD")
    to = to or os.environ.get("MAIL_TO") or sender

    if not sender or not password:
        raise MailerError("GMAIL_ADDRESS and GMAIL_APP_PASSWORD must be set")
    if not to:
        raise MailerError("No recipient configured")

    # Normalize attachment list. ``pdf_path`` (legacy) is appended for
    # backwards compatibility with older callers.
    paths: List[Path] = []
    if pdf_paths:
        paths.extend(pdf_paths)
    if pdf_path is not None:
        paths.append(pdf_path)
    existing = [p for p in paths if p is not None and p.exists()]

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to

    body_html = summary_html if existing else (fallback_html or summary_html)
    msg.set_content(html_to_text(body_html))
    msg.add_alternative(body_html, subtype="html")

    for p in existing:
        try:
            data = p.read_bytes()
            ctype, _ = mimetypes.guess_type(str(p))
            maintype, subtype = (ctype or "application/pdf").split("/", 1)
            msg.add_attachment(
                data,
                maintype=maintype,
                subtype=subtype,
                filename=p.name,
            )
            logger.info("Attached PDF: %s (%d bytes)", p.name, len(data))
        except Exception as exc:
            logger.warning("Failed to attach %s: %s", p, exc)

    logger.info("Sending mail to %s via Gmail SMTP", to)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, password)
        smtp.send_message(msg)
    logger.info("Mail sent")
