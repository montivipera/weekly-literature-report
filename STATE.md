# STATE.md — job state for "paper-workflow" design task

Re-read this file first after any /compact.

## Layout (decided 2026-10-04)
- `STATE.md` (this file): job state. Updated at the end of every phase.
- `research/<stream>.md`: Phase 1 outputs (A–E), max 150 lines each, English.
- `analysis/synthesis.md`: Phase 2 output (Opus), English.
- `paper-workflow/`: Phase 3 deliverable (after user approval). Its own `STATE.md` is a *template* for future papers, not this job's state.
- Final Turkish HTML report: Phase 5, published as an artifact.

## Model routing for this job
Sonnet 5.5 = research streams; Opus 5.5 = synthesis, structure drafting, fresh audit; Fable 5.1 = decisions at Checkpoint 1 and 2 only; Haiku 4.5 = formatting / consistency checks.
Higher models read only md outputs, never raw sources.

## Phase status
- [x] Phase 1 — Research (5 parallel Sonnet streams) — DONE 2026-10-04. Files: research/A..E (77–111 lines each). Haiku check: all ≤150 lines, sections present; 5 grade cells normalised (A UNVERIFIED = official source read via secondary copy; C UNVERIFIED = open question).
- [x] Phase 2 — Synthesis (Opus, analysis/synthesis.md, 255 lines, 191 claims: 148 A / 21 B / 21 C) + Checkpoint 1 (Fable decisions D3–D14 below) — DONE 2026-10-04. STOPPED for user approval.
- [ ] Phase 3 — Build `paper-workflow/` (after approval)
- [ ] Phase 4 — Fresh Opus audit, fixes, Checkpoint 2 (Fable)
- [ ] Phase 5 — Turkish HTML report (≥5 inline SVGs)

## Decisions so far
- D1: research/ and analysis/ live at repo root beside paper-workflow/ so Phase 4 can audit the structure against the evidence files.
- D2: Evidence grades: A = official docs / peer-reviewed; B = systematic independent test; C = anecdote / blog.

### Checkpoint 1 decisions (Fable, 2026-10-04) — spot-checked rows A4, A5, A19, B3, B4, B20–B23, B26, B32, C7, C29, D16, D36, E4
- D3: Adopt the 10-stage list in synthesis §4 (1 data inventory, 2 pre-question scan NEW, 3 question framing, 4 method justification + plan freeze NEW, 5 analysis, 6 question map, 7 M&R draft, 8 layered literature extraction, 9 citation verification NEW, 10 Intro/Discussion + critique + submission audit). Advisors enter at 4, 6, 10.
- D4: Plan registration = internal git-tagged analysis-plan.md is mandatory before any outcome model runs; public OSF secondary-data preregistration is recommended whenever the paper will call a result "confirmatory"; Registered Reports are not on the default path (ecology availability UNVERIFIED, C15–C17).
- D5: Existing field data earns "confirmatory" only through a plan frozen before outcome inspection plus a prior-exposure statement (C7, C24, C25). Default label for every same-data analysis is "exploratory". Held-out splits only with advisor/statistician sign-off (spatial/temporal dependence makes naive splits misleading; judgement call).
- D6: NotebookLM stays as an orientation layer for the global/regional/national/local review; its outputs are tagged "not citable". Citable evidence comes only from full-text extraction into ledger rows by Sonnet (D19, D24, D25, D36).
- D7: Haiku 4.5 is NOT pinned anywhere in the deliverable (agents/). Mechanical checks run as shell one-liners in hooks or as Sonnet 5.5 at low effort. CHANGE vs the user's brief (which routed formatting to Haiku): reason = official retirement notice "not sooner than 2026-10-15" (A4, grade A), 200K window, 4,096-token cache minimum (E4), no academic evaluation (A33). For THIS job Haiku is still used for format checks as the user instructed.
- D8: "Higher models read only md" is strict, plus one Sonnet source-rechecker subagent that Opus may call on disputed rows (A25, D21).
- D9: Fable 5.1 = escalation only (methods critique or final polish after Opus 5.5 fails an acceptance check), with the data-retention caveat (A19, C/UNVERIFIED; consistent with the Anthropic-maintained claude-api skill text) recorded in CLAUDE.md.
- D10: Advisor surface = DOCX/PDF exported from the md files; canonical text stays in git; Claude Docs optional (Editor role, no version history, B35–B36).
- D11: Enforcement = two hard PreToolUse hooks (deny edits to analysis-plan.md once tagged; deny writes to draft sections until the ledger status file reads VERIFIED) + SessionStart(matcher compact) hook re-injecting STATE.md + CLAUDE.md rules for the rest (B20–B23, B32). Hook JSON is documented inside CLAUDE.md for pasting into .claude/settings.json (settings file is outside the mandated structure). No Workflow tool dependency; fan-out via subagents in stages 8–9.
- D12: agents/ = 8 definitions. Sonnet 5.5: data-reader, analyst, lit-extractor, citation-verifier, source-rechecker. Opus 5.5: methods-advisor, drafter, critic. Each pins a full model ID, effort, maxTurns, tools and a token budget. Orchestrator must never pass a per-invocation model; never set CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1 (B4).
- D13: Stage 9 DOI resolution is a documented procedure (Crossref/OpenAlex lookup via Bash inside the citation-verifier agent), not a separate script file, to respect the file structure.
- D14: Sessions must start with cwd = paper-workflow/ (or the repo-root CLAUDE.md must @-import paper-workflow/CLAUDE.md); otherwise the workflow CLAUDE.md is nested and summarised away at compaction (B26, B32).
- Held positions changed by evidence (stated explicitly): labels alone insufficient (C7–C8); literature timing is not the harm, undisclosed post hoc sourcing is (C2); DOI ledger becomes search log + resolution + claim-support (D1, D4, D16); Haiku dropped from deliverable (A4); step 1 changes from "what can we produce" to "describe the dataset, no association tests" (C4, C34).

## Open questions
- OQ1: Egress proxy denies CONNECT (403) to publisher/COPE/ICMJE/COS/arxiv hosts (e.g. www.elsevier.com, www.springer.com, publicationethics.org). Policy wording in research/D rests on search snippets, marked UNVERIFIED. Tell user at Checkpoint 1; fix is the environment's Network access setting.

## Next step
WAITING FOR USER APPROVAL of the Checkpoint 1 summary (Turkish, in chat). On approval → Phase 3: Opus drafts paper-workflow/ per D3–D14 (CLAUDE.md <200 lines, no file >500 lines, every stage ends with a pass/fail gate), Haiku/Sonnet-low format check, then Phase 4 fresh-Opus audit against research/*.md, then Checkpoint 2, then Phase 5 Turkish HTML report.
