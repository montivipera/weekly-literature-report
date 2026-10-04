# Stage 08 — Layered literature extraction
Goal: turn the global, regional, national and local literature into verifiable ledger rows (DOI, verbatim quote, page/section, full-text flag), never into prose summaries.

## Entry modes
- Runs normally in every mode after stage 07. New Q and R rows are always `consulted: after-results`; stage 02 rows keep their value. Gate status: `PASSED`.
- `c-half-draft`: additionally imports every citation already in the draft and re-extracts it from the full text [F27, F28].
- `d-finished-manuscript`: runs for every source never read in full. `e-under-revision`: runs for new or changed citations and for references the reviewers suggest.
- `RETRO-AUDIT` variant, used when the ledger is reconstructed from an existing reference list (modes c–e). Instead of a fresh extraction, each existing citation is audited:
  - it is imported as an R row, with a CL row for each claim it supports in the text;
  - its quote is re-extracted from the full text;
  - `consulted:` is set from dated artefacts, defaulting to `after-results` [F11].
- `NOT-PASSABLE`: never for the gate as a whole. R rows without a full text stay `fulltext: no`, and their CL rows can never reach `SUPPORT-CHECKED`.
- If the Introduction's hypotheses rest on literature consulted after results, queue this disclosure item (one STATE.md line, ID + ≤6 words; full text goes to inbox.md as an item with target file `disclosure.md` and is written into disclosure.md at stage 10): "Introduction literature was searched after results were known; hypotheses are not presented as derived from it" [C2 form b].

## Inputs / Live file / Outputs
- **Inputs:**
  - STATE.md, search-log.md (stage 02 Q rows), scan-notes.md (stage 02 R rows), question-map.md;
  - methods.md and results.md, for their `[GAP: cite — …]` markers;
  - inbox.md items targeting doi-ledger.md;
  - full texts in papers/<slug>/sources/ (read-only) or at the URLs the user lists;
  - optional NotebookLM notes, for orientation only.
- **Live file:** `live_file: doi-ledger.md`.
- **Output:** doi-ledger.md, header `derives-from: question-map.md@<short-commit>`, built from templates/doi-ledger.md with its columns exactly:
  - **(a) search log:** `Q<nn> | date | database | string | filters | hits | rows kept | consulted (before-results|after-results)`;
  - **(b) reference rows:** `R<nn> | DOI | source (first author, year, venue) | layer (scan|global|regional|national|local) | resolver | resolve date | metadata match (yes|no) | retraction check (clear|RETRACTED|not-run) | fulltext (yes|no) | sources path | risk (high|normal) | consulted | status`, status `UNRESOLVED` at entry;
  - **(c) claim-support rows:** `CL<nn> | R<nn> | claim (as worded in the draft) | verbatim quote | page or section | verifier | date | status`, status `UNRESOLVED` at entry;
  - the **AI-summary provenance list**: every NotebookLM or other AI summary, each `NOT-CITABLE`;
  - **layer syntheses:** at most 15 lines per layer, each sentence ending in `[ledger: <CL-ids>]`;
  - the **to-be-cited list:** the CL rows meant to be cited, one for every `[GAP: cite — …]` in methods.md and results.md included.

## Model and agent
- **agents/lit-extractor.md:** Sonnet 5.5 (`claude-sonnet-5-5`), `effort: medium` in its frontmatter. One stream per layer. Budget per stream: ≤300k source tokens and ≤150 ledger rows per run.
  - It extracts to the template's columns and never summarises prose.
- **Main session (Opus 5.5, `claude-opus-5-5`, effort medium):**
  - agrees the search strings with the user;
  - reads only ledger rows;
  - writes the layer syntheses and the to-be-cited list;
  - never opens full texts.
- **agents/source-rechecker.md:** Sonnet 5.5, ≤20k tokens per call. It re-opens one passage when a row looks wrong.
- **Session control:**
  - between layer streams: update STATE.md, commit, then `/clear`;
  - `/compact Focus on stage 08` is allowed mid-stage, only if one layer cannot finish within a session. This is the only stage besides 05 where it is allowed.

## Procedure
1. Read STATE.md and question-map.md, and agree one search string per layer with the user.
2. Copy the stage 02 Q rows from search-log.md into table (a) and the stage 02 R rows from scan-notes.md into table (b), IDs and cells unchanged; new IDs continue from the highest Q, R and CL numbers.
3. The user puts each candidate's full text in papers/<slug>/sources/ (read-only for Claude), or lit-extractor reads it from PubMed full text or an open-access URL; a source with neither is `fulltext: no`.
4. Use NotebookLM, if at all, only to decide what to read, upload published sources only (never unpublished data, results or drafts), and list each NotebookLM output in the provenance list as `NOT-CITABLE`.
5. Run one lit-extractor stream per layer, in the order global, regional, national, local. It runs each string in ≥2 databases and logs Q rows before any reading [C43, C44, C45], then writes R rows (layer, `risk: high` for regional, national and local [D4, D9], `consulted: after-results`, `UNRESOLVED`) and CL rows (verbatim quote, page/section, `UNRESOLVED`).
6. After each stream, write the layer's row counts and source tokens into STATE.md, commit, and `/clear` before starting the next stream.
7. For each `[GAP: cite — …]` in methods.md and results.md, make sure a CL row words that claim; its inbox.md line closes at stage 10, when the GAP is replaced by `[ledger: CL<nn>]`.
8. Write each layer synthesis from CL rows only, every sentence ending in `[ledger: <CL-ids>]` and never citing another synthesis or a NotebookLM output [D21].
9. Write the to-be-cited list (CL-ID, R-ID, draft section, human check), since stage 09 verifies exactly that set.
10. Run the gate, write STATE.md, commit, run `/rename <slug>-S08`, then `/clear`.

## Gate (pass/fail)
Run gate commands from paper-workflow/ (the project root for Claude Code).
- [ ] For each of the four layers, the Q rows whose "rows kept" name that layer's R rows cover ≥2 databases, each with string, date, hits and consulted.
- [ ] Every R row has a DOI or other ID, its layer, fulltext, sources path, risk, consulted and status; every R row is named under "rows kept" of a Q row.
- [ ] Every CL row has an R-ID, a verbatim quote in quotation marks, and a page or section.
- [ ] There is no prose summary outside the layer syntheses: `sed -n '/^## Layer syntheses/,/^## To-be-cited/p' papers/<slug>/doi-ledger.md | grep '^- ' | grep -vc '\[ledger: CL'` prints 0.
- [ ] The AI-summary provenance list is complete, and no `NOT-CITABLE` item is cited in any synthesis.
- [ ] `awk -F'|' '$2 ~ /^ R[0-9]/ && $5 ~ /regional|national|local/ && $12 !~ /high/' papers/<slug>/doi-ledger.md` prints nothing.
- [ ] Stream budgets are recorded in STATE.md: ≤300k source tokens per layer stream and ≤150 rows per run.
- [ ] Modes c–e: every citation in the existing text has an R row and a CL row. Checked by count match.
- [ ] The to-be-cited list is present and has a CL row for every `[GAP: cite — …]` in methods.md and results.md (count match).
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count. Next: `live_file: doi-ledger.md` for stage 09.

## Propagate step
This runs at this gate, or when the user types "propagate inbox".
1. Read the OPEN inbox.md items that target doi-ledger.md or upstream files.
2. Set `mode: propagate` and list the changes in plan mode.
3. Get user approval.
4. Edit upstream first. A methods claim is fixed in methods.md, and a new question goes to questions.md as `origin: literature`, post hoc.
5. A changed or added ledger row returns to `UNRESOLVED`.
6. Mark draft/ as `stale:` where it exists.
7. Close each item as `CLOSED -> <file>@<commit>`, then set `mode: work`.

## Evidence
- [D19] A: LLM summaries overgeneralise 4.85 times as often as human summaries, even when told to be accurate.
- [D21] B: recursive merging of summaries can amplify hallucination; re-injecting source citations mitigates it.
- [D20] B: main-result claims are stronger in abstracts than in discussions, so reading only abstracts risks overconfidence. Hence the `fulltext:` flag.
- [D24] B: NotebookLM hallucinated less than general chatbots (13% vs 40%), but its errors were unsupported characterisations of sources.
- [D25] A: NotebookLM's risk-of-bias scoring agreed poorly with manual scoring (ICC 0.08–0.27).
- [D36] UNVERIFIED: no source shows that NotebookLM citations carry page numbers, or that page-numbered quotes cut fabrication.
- [D4] A: fabrication was 28–29% for low-visibility topics, against 6% for a well-known one.
- [D9] A: invalid-DOI rates exceed 80% for lower-income-country topics and rise for 2020s publications.
