"""Send the rendered HTML report via Gmail SMTP."""

from __future__ import annotations

import logging
import os
import smtplib
from email.message import EmailMessage
from typing import Optional

from .renderer import html_to_text

logger = logging.getLogger(__name__)

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587


class MailerError(RuntimeError):
    pass


def send_report(
    html: str,
    subject: str,
    *,
    to: Optional[str] = None,
    sender: Optional[str] = None,
    password: Optional[str] = None,
) -> None:
    sender = sender or os.environ.get("GMAIL_ADDRESS")
    password = password or os.environ.get("GMAIL_APP_PASSWORD")
    to = to or os.environ.get("MAIL_TO") or sender

    if not sender or not password:
        raise MailerError("GMAIL_ADDRESS and GMAIL_APP_PASSWORD must be set")
    if not to:
        raise MailerError("No recipient configured")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to
    msg.set_content(html_to_text(html))
    msg.add_alternative(html, subtype="html")

    logger.info("Sending mail to %s via Gmail SMTP", to)
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=30) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender, password)
        smtp.send_message(msg)
    logger.info("Mail sent")
