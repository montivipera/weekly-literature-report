"""Upload the weekly PDF to a Google Drive folder.

Uses a service-account credential supplied via the ``GDRIVE_CREDENTIALS_JSON``
environment variable (the entire JSON key, not a path) and a target folder ID
in ``GDRIVE_FOLDER_ID``. The folder must be shared with the service account's
email — the service account does not see the user's regular Drive folders by
default.

This module is deliberately defensive: if either env var is missing or the
upload fails, it logs a warning and returns ``None``, so a failure here never
blocks the email send.
"""

from __future__ import annotations

import io
import json
import logging
import os
from pathlib import Path
from typing import Optional

logger = logging.getLogger(__name__)


SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def upload_to_drive(pdf_path: Path) -> Optional[str]:
    """Upload ``pdf_path`` into the configured Drive folder.

    Returns a public web-view URL on success, or ``None`` if Drive is not
    configured / the upload failed. The system continues normally either way.
    """
    creds_json = os.environ.get("GDRIVE_CREDENTIALS_JSON", "").strip()
    folder_id = os.environ.get("GDRIVE_FOLDER_ID", "").strip()

    if not creds_json or not folder_id:
        logger.info("Drive upload skipped: GDRIVE_CREDENTIALS_JSON or GDRIVE_FOLDER_ID not set")
        return None
    if not pdf_path.exists():
        logger.info("Drive upload skipped: PDF not found at %s", pdf_path)
        return None

    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaIoBaseUpload
    except ImportError as exc:
        logger.warning("Google API libraries not available: %s", exc)
        return None

    try:
        info = json.loads(creds_json)
    except json.JSONDecodeError as exc:
        logger.error("GDRIVE_CREDENTIALS_JSON is not valid JSON: %s", exc)
        return None

    try:
        creds = service_account.Credentials.from_service_account_info(
            info, scopes=SCOPES
        )
        service = build("drive", "v3", credentials=creds, cache_discovery=False)

        # If a file with the same name already exists in the folder, replace it.
        existing = (
            service.files()
            .list(
                q=(
                    f"'{folder_id}' in parents and name = '{_escape(pdf_path.name)}' "
                    "and trashed = false"
                ),
                fields="files(id, name)",
                pageSize=1,
                supportsAllDrives=True,
                includeItemsFromAllDrives=True,
            )
            .execute()
        )

        with pdf_path.open("rb") as fp:
            data = fp.read()
        media = MediaIoBaseUpload(io.BytesIO(data), mimetype="application/pdf", resumable=False)

        existing_files = existing.get("files", [])
        if existing_files:
            file_id = existing_files[0]["id"]
            file = (
                service.files()
                .update(
                    fileId=file_id,
                    media_body=media,
                    fields="id,webViewLink",
                    supportsAllDrives=True,
                )
                .execute()
            )
            logger.info("Replaced existing Drive file: %s", file.get("webViewLink"))
        else:
            metadata = {"name": pdf_path.name, "parents": [folder_id]}
            file = (
                service.files()
                .create(
                    body=metadata,
                    media_body=media,
                    fields="id,webViewLink",
                    supportsAllDrives=True,
                )
                .execute()
            )
            logger.info("Uploaded to Drive: %s", file.get("webViewLink"))

        return file.get("webViewLink")
    except Exception as exc:
        logger.exception("Drive upload failed: %s", exc)
        return None


def _escape(name: str) -> str:
    """Escape single quotes for the Drive query language."""
    return name.replace("'", "\\'")
