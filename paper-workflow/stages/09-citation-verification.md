# Stage 09 — Citation verification
Goal: before any draft/*.md is written, prove that every to-be-cited source exists, matches its metadata, is not retracted, and supports its claim in the full text.

## Entry modes
- Runs in full at every entry mode, because no check depends on when results were seen [F27–F29].
  - `c-half-draft`: covers every citation already in the draft, re-extracted in stage 08.
  - `d-finished-manuscript`: covers every in-text claim.
  - `e-under-revision`: new or changed citations go through all four steps, and every cited row gets a fresh retraction check [F29].
- `RETRO-AUDIT` variant: none. An existing reference list is checked, never trusted, so the status is `OPEN` until the gate passes and then `PASSED`, in every mode.
- `NOT-PASSABLE`: never. A row that cannot reach `SUPPORT-CHECKED` is dropped or replaced (back to stage 08), so no disclosure item is queued here. The references-checked declaration [D17] is written into disclosure.md at stage 10.

## Inputs / Live file / Outputs
- **Inputs:**
  - STATE.md;
  - doi-ledger.md: tables (a)–(c), the to-be-cited list, the provenance list;
  - methods.md and results.md, for their `[ledger: Rn]` placeholders;
  - full texts at the paths given in the ledger;
  - in modes c–e, the existing reference list.
- **To-be-cited rows:** the claim-support rows that are named in the stage 08 to-be-cited list, in methods.md or results.md, or in the existing draft (modes c–e), together with their reference rows. A row that nobody names keeps its status and can never be cited.
- **Live file:** `live_file: doi-ledger.md`. Only these fields are written: status, resolver, resolve date, metadata-match, retraction check, verifier and date.
- **Output:** doi-ledger.md with every to-be-cited row verified. A gate line sits at the top: `to-be-cited: N | SUPPORT-CHECKED: N | other: 0 | checked <date>`.
- **Status ladder:**
  - a reference row goes `UNRESOLVED` → `RESOLVED` (the DOI resolves) → `METADATA-OK` (title, authors, year and journal match, and the retraction check is clear);
  - a claim-support row then becomes `SUPPORT-CHECKED` when the quote is found word for word in the full text at its page/section and supports the claim as worded;
  - the side exits are `RETRACTED` and `NOT-CITABLE`;
  - a claim row with `fulltext: no` cannot reach `SUPPORT-CHECKED` [D20].

## Model and agent
- **agents/citation-verifier.md:** Sonnet 5.5 (`claude-sonnet-5-5`) at effort low.
  - It checks one ledger row per check and writes status fields only.
  - It runs in a fresh context and is never the drafter or the extractor of the row it checks, because evidence that a model can verify its own references is weak [D18].
- **Deterministic first:** steps 1 and 3 are curl/jq or MCP lookups, not model judgement. The model only compares and records.
- **Main session (Opus 5.5):**
  - builds the to-be-cited list;
  - corrects row metadata from resolver output;
  - runs the count.
  It never sets a status. The drafter is never used in this stage.
- **Budget:** low. One audit costs about $0.04 per paper [D12] B. Claim checks re-read only the cited passage.

## Procedure
1. Read STATE.md, stop unless stage 08 is `PASSED` or `RETRO-AUDIT`, and write the to-be-cited count into the ledger gate line.
2. Step 1 (resolve, deterministic): for each reference row the verifier queries `curl -s https://api.crossref.org/works/<DOI>`, then `https://api.openalex.org/works/doi:<DOI>`, then PubMed (E-utilities or a PubMed MCP tool), and records resolver and date (`RESOLVED`) [D9, D10].
3. If the environment's proxy blocks a resolver, the verifier uses a bibliographic MCP tool and records its name as resolver, and a row nothing resolves stays `UNRESOLVED` until the user checks it in a browser, recorded as `resolver: user`.
4. Step 2 (metadata): the verifier compares title, authors, year and journal from the resolver with the row and sets `METADATA-OK`, or flags the mismatch for the main session to correct and the verifier to re-check [D1, D4].
5. A DOI that resolves to a different work makes the row `NOT-CITABLE` until stage 08 supplies the right source.
6. Step 3 (retraction): the verifier checks OpenAlex `is_retracted`, Crossref update relations and PubMed's "Retracted Publication" type (field names are a judgement call, not from research), records result and date, and sets `RETRACTED` on a hit [F29, F30 UNVERIFIED].
7. Step 4 (support, verifier ≠ drafter): a separate verifier call opens the full text at the recorded page/section, confirms the verbatim quote is there word for word and supports the claim as worded, and sets `SUPPORT-CHECKED` or returns the row to stage 08 via inbox.md [D14, D16, D18].
8. The user spot-checks claim rows in priority order (post-2020, then `risk: high` regional/national/local, then niche topics), at least 10 rows or 10% of rows, whichever is more (judgement call), recording `verifier: user` and the date [D4, D9].
9. The main session recounts and sets `live_file: draft/` in STATE.md only if every gate item passes; otherwise it keeps `live_file: doi-ledger.md` and lists the failing row IDs.
10. Commit, run `/rename stage-09`, then `/clear`.

## Gate (pass/fail) — HARD: no draft/*.md may be written until every item passes
- [ ] The to-be-cited count N in the ledger gate line matches the IDs named in the to-be-cited list, methods.md and results.md (grep count), plus the draft citations in modes c–e.
- [ ] Every to-be-cited reference row has a resolver and resolve date, and its status is `METADATA-OK`.
- [ ] Every to-be-cited reference row has a dated retraction check. None is `RETRACTED`, unless the sentence citing it states the retraction and gives the notice DOI.
- [ ] 100% of to-be-cited claim-support rows are `SUPPORT-CHECKED`, each with a verifier (not the drafter or extractor) and a date. None of them has `fulltext: no`.
- [ ] No `NOT-CITABLE` row (AI or NotebookLM summary, wrong-work DOI) is in the to-be-cited set.
- [ ] The user spot-check sample is done and recorded, priority rows first.
- [ ] No draft/ file changed since the stage 08 gate commit: `git diff <stage-08 commit> -- draft/` is empty.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count. `live_file: draft/` is set only on pass. The guard hook then admits draft/ for stage 10 and nothing else.

## Propagate step
This runs at this gate, or when the user types "propagate inbox".
1. Read the OPEN inbox.md items that target doi-ledger.md or upstream files.
2. Set `mode: propagate` and list the changes in plan mode.
3. Get user approval.
4. Edit upstream first. A wrong quote goes back to a stage 08 re-extraction, and a wrong methods claim is fixed in methods.md.
5. Any changed row returns to `UNRESOLVED` and goes through all four steps again.
6. Mark draft/ as `stale:` where it exists.
7. Close each item with a commit pointer, then set `mode: work`.

## Evidence
- [D9] A: invalid-DOI rates, checked against Crossref, exceed 80% for lower-income-country topics and rise for 2020s publications.
- [D4] A: 19.9% of citations were fabricated and 45.4% of real ones had errors, mostly invalid DOIs. Low-visibility topics were worse.
- [D1] A: 43% (GPT-3.5) and 24% (GPT-4) of real citations had substantive errors, so existence alone is not enough.
- [D10] B: 69,557 citations checked via Crossref, OpenAlex and Semantic Scholar; 11.4–56.8% were hallucinated.
- [D14] A: even a PubMed-API agent was only 96.8% consistent between citation metadata and the in-text claim.
- [D16] B: deep-research agents had working links but only 39–77% factual support.
- [D18] A: self-verification of references was tested with n=40, a single model and author grading, which is weak; hence verifier ≠ drafter.
- [F29] A: 220 of 478 retracted papers were still cited, and 89% of the citing authors were unaware.
