# Stage 08 — Layered literature extraction
Goal: turn the global, regional, national and local literature into verifiable ledger rows (DOI, verbatim quote, page/section, full-text flag), never into prose summaries.

## Entry modes
- Runs normally in every mode after stage 07. Rows are always `consulted: after-results`, except stage 02 rows carried over. Gate status: `PASSED`.
- `c-half-draft`: additionally imports every citation already in the draft and re-extracts it from the full text [F27, F28].
- `d-finished-manuscript`: runs for every source never read in full. `e-under-revision`: runs for new or changed citations and for references the reviewers suggest.
- `RETRO-AUDIT` variant, used when the ledger is reconstructed from an existing reference list (modes c–e). Instead of a fresh extraction, each existing citation is audited:
  - it is imported as a row;
  - its quote is re-extracted from the full text;
  - `consulted:` is set from dated artefacts, defaulting to `after-results` [F11].
- `NOT-PASSABLE`: never for the gate as a whole. Rows without a full text stay `fulltext: no` and cannot be cited for claims.
- If the Introduction's hypotheses rest on literature consulted after results, queue this disclosure item in STATE.md: "Introduction literature was searched after results were known; hypotheses are not presented as derived from it" [C2 form b].

## Inputs / Live file / Outputs
- **Inputs:**
  - STATE.md, search-log.md, scan-notes.md (stage 02 rows), question-map.md;
  - methods.md and results.md, for their `[ledger: Rn]` placeholders;
  - inbox.md items targeting doi-ledger.md;
  - full texts at the paths the user lists;
  - optional NotebookLM notes, for orientation only.
- **Live file:** `live_file: doi-ledger.md`.
- **Output:** doi-ledger.md, header `derives-from: question-map.md@<short-commit>`, built from templates/doi-ledger.md:
  - **(a) search-and-consultation log**, one row per layer search: string | databases (≥2) | date | hits | `consulted: before-results|after-results`;
  - **(b) reference rows:** ID | DOI or other ID | layer | resolver | resolve date | metadata-match | retraction check | `fulltext: yes|no` | status (`UNRESOLVED` at entry) | `risk: high` for the regional, national and local layers;
  - **(c) claim-support rows:** claim ID | ref ID | verbatim quote | page/section | verifier | date | status;
  - the **AI-summary provenance list**: every NotebookLM or other AI summary, each marked `NOT-CITABLE`;
  - **layer syntheses:** a section of at most 15 lines per layer. Every sentence ends in ledger row IDs. Build-spec §2 gives syntheses no separate file, so they live here.

## Model and agent
- **agents/lit-extractor.md:** Sonnet 5.5 (`claude-sonnet-5-5`) at effort medium. One stream per layer. Budget per stream: ≤300k source tokens and ≤150 ledger rows per run.
  - It extracts to schema and never summarises prose.
- **Main session (Opus 5.5, `claude-opus-5-5`, effort medium):**
  - agrees the search strings with the user;
  - reads only ledger rows;
  - writes the layer syntheses;
  - never opens full texts.
- **agents/source-rechecker.md:** Sonnet 5.5, ≤20k tokens per call. It re-opens one passage when a row looks wrong.
- **Session control:**
  - between layer streams: update STATE.md, commit, then `/clear`;
  - `/compact Focus on stage 08` is allowed mid-stage, only if one layer cannot finish within a session. This is the only stage besides 05 where it is allowed.

## Procedure
1. Read STATE.md and question-map.md, agree one search string per layer with the user, and log each search in ledger table (a) (string, ≥2 databases, date, hits) before any reading [C43, C44, C45].
2. Carry the stage 02 rows from scan-notes.md into the ledger unchanged, keeping `consulted: before-results`.
3. Collect a full text for every candidate source, entering any source without one as `fulltext: no`.
4. Use NotebookLM, if at all, only to decide what to read, upload published sources only (never unpublished data, results or drafts), and list each NotebookLM output in the provenance list as `NOT-CITABLE`.
5. Run one lit-extractor stream per layer, in the order global, regional, national, local, writing reference rows and claim-support rows (verbatim quote, page/section, `fulltext:`, `consulted: after-results`, `UNRESOLVED`).
6. After each stream, write the layer's row counts and source tokens into STATE.md, commit, and `/clear` before starting the next stream.
7. Mark every reference row from the regional, national and local layers `risk: high`, so that stage 09 checks them first [D4, D9].
8. Write each layer synthesis from ledger rows only, with every sentence ending in row IDs and never citing another synthesis or a NotebookLM output [D21].
9. List in the syntheses' header which claim rows are meant to be cited, since stage 09 verifies exactly that set.
10. Run the gate, write STATE.md, commit, run `/rename stage-08`, then `/clear`.

## Gate (pass/fail)
- [ ] Table (a) has, for each of the four layers, at least one search with string, ≥2 databases, date, hits and the consulted field.
- [ ] Every reference row has a DOI or other ID, its layer, a `fulltext:` flag and a status.
- [ ] Every claim-support row has a ref ID, a verbatim quote in quotation marks, a page or section, and the consulted field.
- [ ] There is no prose summary outside the layer syntheses, and every synthesis sentence ends in ledger IDs. Checked by grep: 0 synthesis lines without `[R`.
- [ ] The AI-summary provenance list is complete, and no `NOT-CITABLE` item is cited in any synthesis.
- [ ] Every regional, national and local reference row carries `risk: high`.
- [ ] Stream budgets are recorded in STATE.md: ≤300k source tokens per layer stream and ≤150 rows per run.
- [ ] Modes c–e: every citation in the existing text has a ledger row. Checked by count match.
- [ ] The to-be-cited list is present.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count. Next: `live_file: doi-ledger.md` for stage 09.

## Propagate step
This runs at this gate, or when the user types "propagate inbox".
1. Read the OPEN inbox.md items that target doi-ledger.md or upstream files.
2. Set `mode: propagate` and list the changes in plan mode.
3. Get user approval.
4. Edit upstream first. A methods claim is fixed in methods.md, and a new question goes to questions.md as `origin: literature`, post hoc.
5. A changed or added ledger row returns to `UNRESOLVED`.
6. Mark draft/ as `stale:` where it exists.
7. Close each item with a commit pointer, then set `mode: work`.

## Evidence
- [D19] A: LLM summaries overgeneralise 4.85 times as often as human summaries, even when told to be accurate.
- [D21] B: recursive merging of summaries can amplify hallucination; re-injecting source citations mitigates it.
- [D20] B: main-result claims are stronger in abstracts than in discussions, so reading only abstracts risks overconfidence. Hence the `fulltext:` flag.
- [D24] B: NotebookLM hallucinated less than general chatbots (13% vs 40%), but its errors were unsupported characterisations of sources.
- [D25] A: NotebookLM's risk-of-bias scoring agreed poorly with manual scoring (ICC 0.08–0.27).
- [D36] UNVERIFIED: no source shows that NotebookLM citations carry page numbers, or that page-numbered quotes cut fabrication.
- [D4] A: fabrication was 28–29% for low-visibility topics, against 6% for a well-known one.
- [D9] A: invalid-DOI rates exceed 80% for lower-income-country topics and rise for 2020s publications.
