# Stage 02 — Pre-question scan
Goal: a short, logged literature scan (≥2 databases, 10–20 key papers with resolved DOIs) that places the data in context before any question or plan is fixed.

## Entry modes
- `a-data-only`: all steps run in full as a prospective scan, and the gate status is `PASSED`. Because the data were designed and collected before the scan, queue the "post-design" disclosure item (stage 00 rule): "literature scan postdates data design and collection; it informed questions and plan, not design or sample size". `after-results` rows are not allowed in this mode.
- RETRO-AUDIT in `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`: rebuild search-log.md from dated artefacts (proposal, reference-manager export dates, early drafts); the date cell of each rebuilt Q row reads `<date> reconstructed: <artefact>`. A row gets `consulted: before-results` only if a dated artefact predates the first outcome result; all others get `after-results`. Each hypothesis whose only literature support is `after-results` is flagged as HARKing form (b) [C2] in one inbox.md item targeting questions.md.
- NOT-PASSABLE: when no dated artefact shows any literature consulted before results. Queue the disclosure item "literature search postdates the results; hypotheses drawn from it are post hoc".

## Inputs · Live file(s) · Outputs
- **Inputs:** data-inventory.md (taxa, habitat, variables, region), the user's keywords, intake.md; templates/doi-ledger.md for the column definitions.
- **Live files:** `search-log.md, scan-notes.md` (both live for the whole stage).
- **Outputs** (columns = templates/doi-ledger.md tables (a) and (b), copied verbatim; stage 08 copies these rows into doi-ledger.md with IDs unchanged):
  - `search-log.md`: header `derives-from: data-inventory.md@<short-commit>`; rows `Q<nn> | date | database | string | filters | hits | rows kept | consulted (before-results|after-results)`. `string` is exact, as approved; `rows kept` lists the R IDs taken from that run.
  - `scan-notes.md`: header `derives-from: search-log.md@<short-commit>`; reference rows `R<nn> | DOI | source (first author, year, venue) | layer (scan|global|regional|national|local) | resolver | resolve date | metadata match (yes|no) | retraction check (clear|RETRACTED|not-run) | fulltext (yes|no) | sources path | risk (high|normal) | consulted | status`, all with `layer: scan`; then `## Key`: `R<nn> | concept block | relevance (one extracted line, not a summary)` for the 10–20 key rows. R status ladder: UNRESOLVED → RESOLVED → METADATA-OK (stage 09, after the retraction check), or RETRACTED / NOT-CITABLE. A `fulltext: no` row is orientation only and is not citable until stage 08 extracts it from the full text, because abstracts tend to overstate results [D20].

## Model and agent
- `agents/lit-extractor.md` (claude-sonnet-5-5, effort medium; scan budget ≤100k source tokens, a judgement call well under the 300k stream cap): runs approved strings with retrieval tools only (database APIs, WebSearch/WebFetch, bibliographic MCP tools such as PubMed, Consensus, Scholar Gateway), never from memory [A21, D5].
- `agents/citation-verifier.md` (claude-sonnet-5-5, effort low; one row per check; writes verification cells only): resolves each DOI via Crossref, OpenAlex or PubMed and fills `resolver`, `resolve date`, `metadata match` and `status`. When the network blocks those resolvers it uses a bibliographic MCP tool, recorded as `mcp:<tool>`. The retraction check stays `not-run` until stage 09.
- Main session (Opus 5.5, effort medium): drafts the strings with the user and reads scan-notes.md only. It adds no reference, DOI or author from memory.

## Procedure
1. Set `live_file: search-log.md, scan-notes.md`; the user names the concept blocks (taxon, habitat, response, driver, region) using data-inventory.md.
2. Main session drafts one Boolean string per database (litsearchr optional [C43]), and the user approves the exact strings before any search runs.
3. lit-extractor runs each approved string in ≥2 databases (Google Scholar never the principal one [C44]) and screens the hits; for each kept candidate it writes one R row (DOI copied from the tool result, `status: UNRESOLVED`, `consulted: before-results`, `fulltext: no` unless the full text was read), then appends the run's Q row with date, hits and the R IDs kept.
4. lit-extractor fills `## Key` with 10–20 rows spread across the concept blocks (judgement call).
5. citation-verifier resolves every DOI and sets `RESOLVED` with resolver, resolve date and metadata match, or leaves `UNRESOLVED` with the reason [D9].
6. An `UNRESOLVED` key row is swapped for a `RESOLVED` one; `UNRESOLVED` rows stay in the file and are never cited.
7. The user reviews the key list; main session reads scan-notes.md only and adds nothing from memory.
8. `a-data-only`: queue the "post-design" item and set S02 to `PASSED` at the gate.
9. Commit search-log.md and scan-notes.md and write the hash to STATE.md as `scan_commit:`; this commit must precede the plan tag `plan-<slug>-v1` (checked again at stage 04).
10. Run the gate and set `live_file: questions.md` for stage 03.

## Gate (pass/fail)
Run gate commands from paper-workflow/ (the project root for Claude Code).
- [ ] search-log.md: every Q row has string, database, date, hits, rows kept and consulted, and at least 2 distinct databases appear.
- [ ] search-log.md rows were only ever appended: `git log -p -- papers/<slug>/search-log.md` shows no changed or deleted row.
- [ ] Every R row in scan-notes.md is listed in the `rows kept` cell of a Q row (no reference without a logged search); IDs are `Q<nn>` and `R<nn>` only.
- [ ] `## Key` has 10–20 rows, all `RESOLVED` with resolver, resolve date and `metadata match: yes`.
- [ ] Every R row has `fulltext` and `consulted`. `a-data-only`: every Q and R row is `before-results`, and any `after-results` row fails the gate. Modes b–e: `after-results` appears only on reconstructed rows.
- [ ] `a-data-only`: S02 is `PASSED` and the "post-design" item is queued.
- [ ] `scan_commit:` is in STATE.md; if `plan-<slug>-v1` already exists, `git merge-base --is-ancestor <scan_commit> plan-<slug>-v1` succeeds.
- [ ] Both files start with their derives-from header.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is search-log.md or scan-notes.md. Write the change list in plan mode and wait for user approval. Set `mode: propagate`; new searches are appended as new Q rows and new references as new R rows (logged rows are never edited, only their verification cells and status). Mark questions.md and every later file `stale:` in STATE.md, close each item by appending its row with status `CLOSED -> <file>@<commit>`, then set `mode: work`. In `a-data-only`, literature needed after the first outcome result goes to stage 08 (doi-ledger.md, `after-results`), never into scan-notes.md; in modes b–e a search run after the plan tag or after the first outcome result is logged `after-results`.

## Evidence
- [C2] A: hypotheses from a post hoc literature search reported as a priori are a named HARKing form.
- [C43] A: reproducible search strings (litsearchr) reduce bias towards familiar studies.
- [C44] A: only about half of 28 search systems suit evidence synthesis; Google Scholar is unsuitable as the principal one.
- [C45] A: share search syntax and use version control.
- [A21] B: closed-book reference generation had no model above 0.475 existence rate; [D5] A: 28.3% of references fabricated with retrieval disabled.
- [D9] A: invalid-DOI rates checked against Crossref exceed 80% for lower-income-country topics and rise for 2020s papers.
- [D20] B: main-result claims are stronger in abstracts than in discussions.
