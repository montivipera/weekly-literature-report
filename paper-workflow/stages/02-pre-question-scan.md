# Stage 02 — Pre-question scan
Goal: a short, logged literature scan (≥2 databases, 10–20 key papers with resolved DOIs) that places the data in context before any question or plan is fixed.

## Entry modes
- `a-data-only`: all steps run in full, but the gate status is `RETRO-AUDIT` noted `post-design` (mode table, stage 00): the data were designed and collected before the scan, so it can inform the questions and the plan, not the design or sample size.
- RETRO-AUDIT in `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`: rebuild search-log.md from dated artefacts (proposal, reference-manager export dates, early drafts) and mark those rows `reconstructed`. A row gets `consulted: before-results` only if a dated artefact predates the first outcome result; all others get `consulted: after-results`. Each hypothesis whose only literature support is `after-results` is flagged as HARKing form (b) [C2] in one inbox.md item targeting questions.md.
- NOT-PASSABLE: when no dated artefact shows any literature consulted before results. Queue the disclosure item "literature search postdates the results; hypotheses drawn from it are post hoc".

## Inputs · Live file(s) · Outputs
- **Inputs:** data-inventory.md (taxa, habitat, variables, region), the user's keywords, intake.md.
- **Live files:** `search-log.md` (steps 1–3), then `scan-notes.md` (steps 4–9). The main session switches `live_file:` in STATE.md between them; only one is live at a time.
- **Outputs:**
  - `search-log.md`: header `derives-from: data-inventory.md@<short-commit>`; rows `ID (Qnn) | date | database | string (exact, as approved) | filters | hits | rows kept`.
  - `scan-notes.md`: header `derives-from: search-log.md@<short-commit>`; ledger rows `ID (SCnn) | DOI | resolver | resolve date | authors, year, title (from resolver) | source (Qnn) | status UNRESOLVED or RESOLVED | fulltext: yes|no | consulted: before-results | key: yes|no | relevance (one extracted line, not a summary)`. Stage 08 imports these rows into doi-ledger.md with IDs unchanged. A `fulltext: no` row is orientation only and is not citable until stage 08 extracts it from the full text, because abstracts tend to overstate results [D20].

## Model and agent
- `agents/lit-extractor.md` (claude-sonnet-5-5, effort medium; scan budget ≤100k source tokens, a judgement call well under the 300k stream cap): runs approved strings with retrieval tools only (database APIs, WebSearch/WebFetch, bibliographic MCP tools such as PubMed, Consensus, Scholar Gateway), never from memory [A21, D5].
- `agents/citation-verifier.md` (claude-sonnet-5-5, effort low; one row per check; writes status only): resolves each DOI via Crossref, OpenAlex or PubMed. When the network blocks those resolvers it uses a bibliographic MCP tool, and the `resolver` field records which (`crossref`, `openalex`, `pubmed`, `mcp:<tool>`).
- Main session (Opus 5.5, effort medium): drafts the strings with the user and reads scan-notes.md only. It adds no reference, DOI or author from memory.

## Procedure
1. Set `live_file: search-log.md`; the user names the concept blocks (taxon, habitat, response, driver, region) using data-inventory.md.
2. Main session drafts one Boolean string per database (litsearchr optional [C43]), and the user approves the exact strings before any search runs.
3. lit-extractor runs each approved string in ≥2 databases (Google Scholar never the principal one [C44]) and appends one search-log.md row per run with date and hit count.
4. Main session sets `live_file: scan-notes.md`, and lit-extractor writes one row per screened candidate, copying the DOI from the tool result, with status `UNRESOLVED`, `consulted: before-results`, and `fulltext: no` unless the full text was read.
5. lit-extractor marks 10–20 rows `key: yes` (judgement call), spread across the concept blocks.
6. citation-verifier resolves every DOI and sets `RESOLVED` with resolver, date and resolver metadata, or leaves `UNRESOLVED` with the reason [D9].
7. An `UNRESOLVED` key row is swapped for a `RESOLVED` one; `UNRESOLVED` rows stay in the file and are never cited.
8. The user reviews the key list; main session reads scan-notes.md only and adds nothing from memory.
9. Commit search-log.md and scan-notes.md and write the hash to STATE.md as `scan_commit:`; this commit must precede the plan tag `plan-<slug>-v1` (checked again at stage 04).
10. Run the gate and set `live_file: questions.md` for stage 03.

## Gate (pass/fail)
- [ ] search-log.md: every row has string, database, date and hits, and at least 2 distinct databases appear.
- [ ] search-log.md rows were only ever appended: `git log -p -- search-log.md` shows no changed or deleted row.
- [ ] scan-notes.md: every row's `source` names a Qnn that exists in search-log.md (no reference without a logged search).
- [ ] 10–20 rows have `key: yes`, and all of them are `RESOLVED` with resolver and resolve date.
- [ ] Every row has `fulltext: yes|no` and `consulted: before-results` (`after-results` allowed only in RETRO-AUDIT).
- [ ] `scan_commit:` is in STATE.md; if `plan-<slug>-v1` already exists, `git merge-base --is-ancestor <scan_commit> plan-<slug>-v1` succeeds.
- [ ] Both files start with their derives-from header.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is search-log.md or scan-notes.md. Write the change list in plan mode and wait for user approval. Set `mode: propagate`; new searches are appended as new Qnn rows and new references as new SCnn rows (logged rows are never edited, only their status). Mark questions.md and every later file `stale:` in STATE.md, close each item by appending a CLOSED row with its pointer, then set `mode: work`. A search run after the plan tag or after the first outcome result is logged with `consulted: after-results`.

## Evidence
- [C2] A: hypotheses from a post hoc literature search reported as a priori are a named HARKing form.
- [C43] A: reproducible search strings (litsearchr) reduce bias towards familiar studies.
- [C44] A: only about half of 28 search systems suit evidence synthesis; Google Scholar is unsuitable as the principal one.
- [C45] A: share search syntax and use version control.
- [A21] B: closed-book reference generation had no model above 0.475 existence rate; [D5] A: 28.3% of references fabricated with retrieval disabled.
- [D9] A: invalid-DOI rates checked against Crossref exceed 80% for lower-income-country topics and rise for 2020s papers.
- [D20] B: main-result claims are stronger in abstracts than in discussions.
