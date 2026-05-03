# Weekly Literature Report

Automated weekly pipeline that scans scientific literature across PubMed, arXiv,
bioRxiv, Crossref, and Semantic Scholar; summarizes new articles with Gemini;
renders an HTML report; and emails it via Gmail SMTP. Runs on GitHub Actions
every Monday at 06:00 Europe/Istanbul.

## What it does

For each category you define in `config.yaml`, the system:

1. Fetches articles published or indexed in the last 7 days from each enabled
   source.
2. Deduplicates by DOI (then normalized title), preferring the highest-priority
   source.
3. Retrieves open-access full text when available (PMC, Unpaywall PDFs,
   bioRxiv full text), falling back to the abstract.
4. Asks Gemini for a structured JSON summary: **Aim**, **Gap**, **Methods**,
   **Conclusions** (drawn from the Discussion section, not from raw findings).
5. Detects the article type (research article, review, meta-analysis,
   preprint).
6. Renders a single self-contained HTML email with one section per category and
   one card per article.
7. Sends the email via Gmail SMTP with a plain-text fallback.

## Architecture

```
config.yaml
   |
   v
+---------+    +-----------+    +-----------+    +-----------+
| Loader  | -> | Fetchers  | -> | Dedup     | -> | Full-text |
+---------+    | (Pub/arXi |    +-----------+    +-----------+
               |  /bioR/CR/|                            |
               |  S2)      |                            v
               +-----------+                    +-----------+
                                                | Summariz. |
                                                | (Gemini)  |
                                                +-----------+
                                                       |
                                                       v
                                                +-----------+
                                                | Renderer  |
                                                | (Jinja2)  |
                                                +-----------+
                                                       |
                                                       v
                                                +-----------+
                                                | Mailer    |
                                                | (SMTP)    |
                                                +-----------+
```

## Setup

1. **Fork or clone this repository.**

2. **Create a Gmail app password** so the workflow can send mail through your
   account. Follow Google's instructions:
   <https://support.google.com/accounts/answer/185833>. You'll need 2-Step
   Verification enabled.

3. **Create a Gemini API key** in Google AI Studio:
   <https://aistudio.google.com/app/apikey>. The free tier is sufficient for
   weekly runs.

4. **Add GitHub repository secrets** (Settings → Secrets and variables →
   Actions → New repository secret):

   | Secret              | Value                                                  |
   |---------------------|--------------------------------------------------------|
   | `GEMINI_API_KEY`    | Your Gemini API key                                    |
   | `GMAIL_ADDRESS`     | The Gmail address that will send the report            |
   | `GMAIL_APP_PASSWORD`| The 16-character app password from step 2              |
   | `MAIL_TO`           | Where to send the report (defaults to GMAIL_ADDRESS)   |
   | `UNPAYWALL_EMAIL`   | An email used in API User-Agents (your own is fine)    |

   Optional: `SEMANTIC_SCHOLAR_API_KEY` if you have one (raises rate limits).

5. **Edit `config.yaml`** with your categories and Boolean queries (see
   examples below).

6. **Push** to GitHub. The workflow runs automatically every Monday at 03:00
   UTC (06:00 Europe/Istanbul). You can also run it manually from the Actions
   tab using the **workflow_dispatch** trigger; tick the *dry_run* checkbox to
   render without sending.

## Local testing

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Render only — no email sent. Output goes to out/report.html.
python -m src.main --dry-run --save-html

# Run the test suite (no network calls).
pytest -q
```

Set environment variables in a `.env` (see `.env.example`) and export them
before running locally — `--dry-run` only requires `GEMINI_API_KEY` if you
actually have categories enabled; otherwise the run finishes immediately with
"No enabled categories".

## Schedule and time zones

GitHub Actions cron runs in UTC. `0 3 * * 1` is Monday at 03:00 UTC, which is
06:00 in Europe/Istanbul (UTC+3, no DST). Adjust the cron expression if your
target time changes.

## Boolean query syntax

Queries support `AND`, `OR`, `NOT`, parentheses, and quoted phrases. Operators
are case-insensitive when parsed; uppercase is preferred for readability.

```yaml
categories:
  - name: "Vegetation monitoring"
    query: '(vegetation OR "plant community") AND (restoration OR monitoring)'
    enabled: true

  - name: "Soil microbiome"
    query: '"soil microbiome" AND (diversity OR function) NOT review'
    enabled: true

  - name: "Climate sensing"
    query: '"remote sensing" AND climate AND (drought OR heatwave)'
    enabled: true
```

Notes:

- PubMed and arXiv support full Boolean and field-tagged search natively.
- Crossref and Semantic Scholar do not support full Boolean — the query is sent
  as a relevance-ranked free-text search and re-filtered client-side using your
  Boolean expression.
- bioRxiv has no search API; the system fetches all preprints in the date
  window and filters them client-side.

## Troubleshooting

- **No articles in the report.** Confirm `enabled: true` on at least one
  category and that your Boolean query isn't too restrictive. Check the
  workflow logs for per-source counts.
- **Gemini quota errors.** The summarizer respects retries with exponential
  backoff. If you regularly hit free-tier limits, lower the number of
  categories or reduce `per_category_limit` in `config.yaml`.
- **Rate limits from sources.** Each fetcher backs off automatically. Persistent
  429s usually mean the User-Agent email isn't set; make sure
  `UNPAYWALL_EMAIL` is configured.
- **Gmail "Authentication failed".** Use a 16-character **App Password**, not
  your normal Google password. App passwords require 2-Step Verification.
- **Empty conclusions.** Conclusions come from the Discussion section. If only
  an abstract is available, the summarizer extracts interpretive language from
  the abstract; some preprints with structured-but-thin abstracts may yield
  fewer bullets.

## License

MIT.
