# Phase 4 fix directives (Fable decisions after the independent audit, 2026-10-04)

Source: scratchpad phase4-audit.md (0 BLOCKER / 16 MAJOR / 32 MINOR; 76 refs checked, 13 bad). Every MAJOR and MINOR is to be fixed unless listed under "Declined". Where this file and build-spec.md differ, this file wins. Fixers: A = CLAUDE.md, STATE.md template, .claude/*, docs/rationale.md; B = stages 00–05 + agents data-reader, analyst, methods-advisor, critic; C = stages 06–10 + agents lit-extractor, citation-verifier, drafter, source-rechecker + templates/*. Caps unchanged (CLAUDE.md <200, STATE ≤60, stage ≤120, agent ≤80, template ≤120, rationale ≤400).

## 1. Canonical identifiers, schemas and markers (all fixers copy these verbatim)
- Row IDs: `Q<nn>` search strings · `R<nn>` reference rows · `CL<nn>` claim-support rows · `A<nn>` analysis-log rows · `D<nn>` deviations · `I<nn>` inbox items. No `S<nn>`, no `SC<nn>`. Stage 02 writes R rows straight into scan-notes.md with the ledger (b) columns; stage 08 copies them into doi-ledger.md with IDs unchanged.
- Citation marker in drafts and skeleton: `[ledger: CL12, CL15]` (claim-support rows only). Result pointer for any number taken from an analysis: `[log: A03]`. No other marker forms (`[res:]`, `<!-- src -->`, `[own result]`, `[ledger: R..]`).
- Ledger table (a) search log: `Q<nn> | date | database | string | filters | hits | rows kept | consulted (before-results|after-results)`.
- Ledger table (b) reference rows: `R<nn> | DOI | source (first author, year, venue) | layer (scan|global|regional|national|local) | resolver | resolve date | metadata match (yes|no) | retraction check (clear|RETRACTED|not-run) | fulltext (yes|no) | sources path | risk (high|normal) | consulted | status`. R status ladder: UNRESOLVED → RESOLVED → METADATA-OK (terminal for R), or RETRACTED / NOT-CITABLE. Retraction check happens BEFORE METADATA-OK is set.
- Ledger table (c) claim-support rows: `CL<nn> | R<nn> | claim (as worded in the draft) | verbatim quote | page or section | verifier | date | status`. CL status: UNRESOLVED → SUPPORT-CHECKED, or NOT-CITABLE. Drafts cite only CL rows with status SUPPORT-CHECKED; the reference list is generated from the R rows of cited CL rows, each R at least METADATA-OK.
- Analysis log (analysis-log.md): the nine columns in stages/05 are canonical; result files are `results/A<nn>.md`. Deviations: `D<nn> | date | plan-id | what changed | why | effect on label | user OK`.
- Inbox (inbox.md): `I<nn> | date | text | target file | status` where status is `OPEN` or `CLOSED -> <file>@<commit>`. Defined once in stages/00 and quoted identically in CLAUDE.md.
- derives-from headers: the stage file's wording wins; agents and templates copy it.
- Per-paper files ADDED: `data-access.md` (append-only, always writable, created at stage 00 in every mode; rows: date | who | what was seen/run | outcome-level? yes|no), `SHA256SUMS` (written at stage 01 beside data/, never inside it; gate 01 runs `sha256sum -c SHA256SUMS` from papers/<slug>/). `disclosure.md` is created at stage 00 in modes b–e (it holds the full disclosure-queue text; STATE.md keeps only one line per queued item: ID + 6 words).
- Live lists (comma form is allowed; "switch only where the stage file says"): S00 `intake.md`; S01 `data-inventory.md, SHA256SUMS`; S02 `search-log.md, scan-notes.md`; S03 `questions.md`; S04 `method-rationale.md, critique.md` (steps 1–3), then `analysis-plan.md` (steps 4–9); S05 `scripts/, results/, analysis-log.md, deviations.md`; S06 `question-map.md`; S07 `methods.md, results.md`; S08 `doi-ledger.md`; S09 `doi-ledger.md`; S10 `draft/` then `critique.md` then `disclosure.md`. STATE.md, inbox.md and data-access.md are always writable (guard allowlist).
- Effort as frontmatter (`effort:`): data-reader medium · analyst medium · lit-extractor medium · citation-verifier low · source-rechecker medium · methods-advisor high · drafter medium · critic high. The "high for Discussion" idea is dropped (one effort per agent file; judgement call). Keep the body line "Work at <level> effort" too.
- Session names: `/rename <slug>-S<NN>` everywhere. Stage IDs always `S04` style, never `S4`.
- Gate commands: every stage states "run gate commands from paper-workflow/ (the project root for Claude Code)"; git object paths use `<tag>:./papers/<slug>/<file>`; diffs use `-- papers/<slug>/...`.

## 2. Decisions on the MAJOR findings
- M1 data-reader schema: copy the six-section stage 01 schema verbatim into data-reader.md; data-reader writes SHA256SUMS and the first data-access.md rows; intake.md is created by data-reader with Write if absent, using the stage 00 columns.
- M2 results/ writes: add `results/` to the S05 live list; the analyst may write results/A<nn>.md with Write; scripts may also write there. Stage 05 text updated accordingly.
- M3 analyst and analysis-plan.md: analyst NEVER list becomes "never edit analysis-plan.md once a `plan-<slug>-*` tag exists; before the tag, stage 04 step 4 asks you to fill it from the template".
- M4 analysis-log columns: stage 05's nine columns are canonical; analyst.md and templates/analysis-to-question.md copy them; IDs `A<nn>`.
- M5 ledger fields: templates/doi-ledger.md adopts §1 columns; lit-extractor, stages 02 and 08 cite the template and use the same columns.
- M6 R vs CL status: as §1 (cite CL rows; R terminal at METADATA-OK). Fix CLAUDE.md §4, section-skeleton, drafter, stage 09/10 gates, critic grep.
- M7 result marker: `[log: A<nn>]` everywhere.
- M8 critic at stage 04: live list `method-rationale.md, critique.md`; main session commits method-rationale.md BEFORE the critic runs; critic writes/appends `## Stage 04` to critique.md; stage 10 appends `## Stage 10`. Remove stage 07 from the critic's description and from CLAUDE.md routing.
- M9 effort frontmatter: as §1.
- M10 SessionStart matcher: `startup|resume|clear|compact` in settings.json and the CLAUDE.md copy (keep them byte-identical).
- M11 self-unlock: (a) add `Edit(/.claude/**)` to permissions.ask; (b) guard.sh: when the edited file is STATE.md and the new content changes `live_file:` or `mode:`, print a one-line stderr notice "guard: live_file/mode changed in STATE.md" (allow, do not block); (c) CLAUDE.md §6 wording: "guard.sh is a strong speed bump against accidental cascades, not a lock: Claude can edit STATE.md, so the user reviews `git diff papers/<slug>/STATE.md` at every gate (judgement call)". Rationale D15 says the same.
- M12 b–e confirmatory: in modes b–e (and in a after any outcome-level look recorded in data-access.md), `confirmatory` requires ALL of: a hold-out or new dataset declared in data-access.md at stage 00/01 before any analysis in this workflow; a plan tagged before any analysis of that hold-out; gate items in S04 and S05 that check the data-access.md date precedes the first results/ commit. Otherwise `exploratory`. Phrase everywhere as: "a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data)".
- M13 mode-e re-entry: stage 00 gets an "existing paper" branch: keep STATE.md (update fields only), keep inbox.md and data-access.md, append intake rows, tag `submitted-<slug>-v<n>` as the baseline, gate on the intake header and the baseline tag, not on an empty inbox.
- M14 gate command paths: as §1.
- M15 First session block: CLAUDE.md §1 gets a ≤14-line "First session" block: prerequisites (git; R or Python; pandoc; pdftotext; network to api.crossref.org, api.openalex.org, doi.org, or the PubMed/Consensus/Scholar MCP connectors); exact setup commands (`mkdir -p .claude/agents && cp agents/*.md .claude/agents/`, `chmod +x .claude/hooks/guard.sh`); launch (`cd paper-workflow && claude`, then `/model claude-opus-5-5`; effort for the main session: cite the documented control if research/B or E names one, else write "leave the default (judgement call)"); the phrase to start a paper ("start stage 00 for <slug>"); the phrase to run a gate ("run the stage NN gate"); plan mode for propagate (Shift+Tab, marked [G23 UNVERIFIED]); what to type after /clear ("continue <slug> at stage NN"; the SessionStart hook re-injects STATE.md).
- M16 D18 wording: "evidence on model self-verification of references is thin (one n=40 study) [D18]; models fail at self-evaluation [A24]". Apply in CLAUDE.md and citation-verifier.md.

## 3. Decisions on MINOR findings (apply all unless noted)
- Inbox format unified (§1). Live-file wording (§1). S04 spelling. /rename form. Mode table (stage 00) and rationale aligned to stage files: mode d → S08 and S10 RETRO-AUDIT; "post-design" note applies to mode a only.
- Stage 02 in mode a: full prospective run → status `PASSED` plus a queued "post-design" disclosure item; gate 02 rejects `after-results` rows in mode a.
- Stage 03 "≥15 candidates" is mode-a only; RETRO-AUDIT checks that every existing question is dated.
- Data-access log → data-access.md (§1). STATE.md gate table gains a `variant (normal|retro)` column. Disclosure queue in STATE.md = one line per item (ID + ≤6 words), full text in disclosure.md.
- Ledger "fill at stage 07" → "fill at stage 10 (disclosure.md)". Human-check rule everywhere: "every `risk: high` row, plus a sample of ≥10 rows or 10% of the rest".
- Prior exposure is read from STATE.md's prior-exposure statement (stage 07, skeleton).
- methods-advisor returns the ≤10-line message only. Install notes move from critic.md to CLAUDE.md §1; critic.md loses them.
- Stage 04 step numbering ("step 4 writes the robustness rule"). CLAUDE.md effort note: "main session medium; stage 03 sessions high (judgement call)".
- Stop hook: emit `{"systemMessage": "<reminder>"}` on stdout (exit 0) instead of plain echo; CLAUDE.md copy stays byte-identical to settings.json. Mark the field as "hooks reference; not in research/B" in rationale.
- Opus agents read a grep-extracted slice of doi-ledger.md (the CL rows named in the skeleton or the question map), never the whole ledger; analyst gets an input cap of ≤120k tokens.
- Runtime files (stages, rationale) must not cite build-spec, D22 or the repo-root STATE.md; inline the needed text or drop the pointer.
- Confirmatory phrasing (M12 wording) in CLAUDE.md §3, analyst.md, question-map template.
- Stage 05 RETRO-AUDIT and stage 01 setup: `chmod -R a-w papers/<slug>/data` and a commit of data/ before any script runs.
- Drafter budget ≤60k (align stage 07); drafter does not write disclosure.md (main session does).
- citation-verifier OUTPUT covers scan-notes.md (stage 02) and doi-ledger.md (stage 09); it writes verification cells only; retraction check before METADATA-OK.
- Gate greps use `\[ledger: CL` and `\[log: A`.
- CLAUDE.md routing table gains a Fable 5.1 row: "prose polish or methods critique only after Opus 5.5 fails an acceptance check; new session; check retention terms first [A5; A19 C UNVERIFIED]; switching model re-reads history uncached [E6]".
- Bad refs: replace A5→E6 for "uncached re-read"; drop C25/C7 for origin tags (cite C2 instead); B20→B23 for "CLAUDE.md not enforced"; drop F23 for "checklist never shortened" (judgement call); mark A31, F4, F5 as UNVERIFIED wherever cited; D9 reworded "the recommended control"; A5 not cited for "open-ended".

## 4. Declined (with reason)
- A second drafter file for "high effort Discussion": no (one effort per agent; file structure fixed).
- `Edit(/papers/*/STATE.md)` in `ask`: no; it would prompt on every burst. M11 (a)–(c) instead.
- A separate disclosure-queue.md: no; disclosure.md already exists for that text.

## 5. Each fixer, when done
Re-run the caps; keep CLAUDE.md §10 JSON byte-identical to .claude/settings.json (fixer A owns both); report the files touched with line counts and any directive you could not apply.
