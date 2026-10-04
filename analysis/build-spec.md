# Build spec for paper-workflow/ (Phase 3) — Fable decisions, 2026-10-04

Authoritative for every writer. Where this spec and analysis/synthesis.md differ, this spec wins. Evidence refs use [Letter#] = research/<Letter>-*.md row. English only. No model names in commit messages.

## 1. Directory layout (exact)
```
paper-workflow/
  CLAUDE.md                     # <200 lines
  STATE.md                      # TEMPLATE for a paper's STATE.md, ≤60 lines
  .claude/settings.json         # approved exception: permissions + hooks
  .claude/hooks/guard.sh        # approved exception: PreToolUse guard (live file, frozen plan)
  stages/00-intake.md … stages/10-discussion-critique-submission.md   # 11 files, ≤120 lines each
  agents/<name>.md              # 8 files, ≤80 lines each (see §4)
  templates/question-map.md, doi-ledger.md, section-skeleton.md, analysis-to-question.md   # ≤120 lines each
  docs/rationale.md             # ≤400 lines
  papers/<slug>/                # one folder per paper (created at Stage 0, not by Phase 3)
```
Stage file names: 00-intake, 01-data-inventory, 02-pre-question-scan, 03-question-framing, 04-method-and-plan-freeze, 05-analysis, 06-question-map, 07-methods-results, 08-literature-extraction, 09-citation-verification, 10-discussion-critique-submission.

## 2. Per-paper files (papers/<slug>/), dependency order = update order (upstream → downstream only)
STATE.md (copied from template; the only file every burst overwrites; ≤60 lines) · inbox.md (append-only) · intake.md → data/ (raw, read-only) → data-inventory.md → search-log.md, scan-notes.md → questions.md → method-rationale.md → analysis-plan.md (frozen by git tag `plan-<slug>-v1`) → scripts/, results/*.md, analysis-log.md, deviations.md → question-map.md → methods.md, results.md → doi-ledger.md → draft/intro.md, draft/discussion.md, draft/abstract.md, critique.md, disclosure.md.
Every derived file starts with a header line: `derives-from: <file>@<short-commit>`. An upstream change never edits downstream files; it sets `stale:` entries in STATE.md. A change to the frozen plan is only ever a row in deviations.md.

## 3. Vocabulary (use exactly these strings)
- Entry modes: `a-data-only`, `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`.
- Gate statuses: `PASSED`, `RETRO-AUDIT`, `NOT-PASSABLE`, `OPEN`. Each with an evidence pointer (file or commit).
- Analysis labels: `confirmatory` (only with a `plan-id` from a plan tagged before any outcome model ran, or new/never-explored held-out data), `exploratory` (default).
- Hypothesis origin tags: `origin: literature | data | advisor`.
- Ledger row status: `UNRESOLVED`, `RESOLVED`, `METADATA-OK`, `SUPPORT-CHECKED`, `NOT-CITABLE`, `RETRACTED`. Full-text flag: `fulltext: yes|no`. Consultation: `consulted: before-results|after-results`.
- STATE.md modes: `mode: work | propagate`. Live file: `live_file: <path relative to papers/<slug>/>`.
- Evidence grades in rationale: A / B / C, plus `UNVERIFIED` where the research file says so. Never upgrade.

## 4. Agents (agents/<name>.md) — frontmatter fields only as documented in research/B (name, description, model, tools, disallowedTools, maxTurns, permissionMode); anything else goes in the body as a rule
| name | model (full ID) | effort (body rule) | role | tools | maxTurns | budget (body rule) |
|---|---|---|---|---|---|---|
| data-reader | claude-sonnet-5-5 | medium | inventory raw data and artefacts; never run outcome–predictor tests | Read, Grep, Glob, Bash | 25 | ≤100k input tokens; output ≤150 lines |
| analyst | claude-sonnet-5-5 | medium | write/run scripts exactly per analysis-plan.md; log every run | Read, Write, Edit, Bash, Grep, Glob | 60 | one analysis per turn; results/*.md ≤100 lines each |
| lit-extractor | claude-sonnet-5-5 | medium | read full texts, write ledger rows with verbatim quote, page/section, fulltext flag | Read, Bash, WebFetch, WebSearch, Grep, Glob + bibliographic MCP tools if present | 40 | ≤300k source tokens per stream; ≤150 ledger rows per run |
| citation-verifier | claude-sonnet-5-5 | low | resolve DOI/metadata (Crossref/OpenAlex/PubMed), check claim–passage support; never the drafter | Read, Bash, WebFetch, Grep + bibliographic MCP tools | 40 | one ledger row per check; writes status only |
| source-rechecker | claude-sonnet-5-5 | medium | re-open a single source passage on request from Opus; returns quote + location | Read, Bash, WebFetch, Grep | 10 | ≤20k tokens per call |
| methods-advisor | claude-opus-5-5 | high | propose and justify candidate models against named protocols (Zuur & Ieno 2016, Bolker 2009, Harrison 2018); list assumptions, selection rule, sensitivity checks | Read, Grep, Glob | 20 | reads md only (≤50k tokens); output ≤150 lines |
| drafter | claude-opus-5-5 | medium (high for Discussion) | write section text to the skeleton; cite only ledger rows with status SUPPORT-CHECKED | Read, Write, Edit, Grep, Glob | 30 | reads md only; one section per run |
| critic | claude-opus-5-5 | high | fresh-context adversarial review; must find errors; checks every citation maps to a verified row | Read, Grep, Glob | 20 | reads md only; output ≤120 lines |
Rules for every agent body: state inputs (paths), output file + schema, budget, "never do" list, and the return message (≤10 lines: path, counts, flags). Sonnet readers never summarise prose; they extract to schema. Opus agents never read raw sources or data. Haiku is not used (A4, A33, E4).

## 5. Stage file schema (every stages/*.md, in this order, ≤120 lines)
1. `# Stage NN — <name>` + one-line goal.
2. **Entry modes**: which modes run this stage normally; the RETRO-AUDIT variant (what is audited instead of produced); when it is NOT-PASSABLE and the disclosure item to queue.
3. **Inputs** (paths) · **Live file(s)** (what Claude may edit in this stage) · **Outputs** (paths + one-line schema each).
4. **Model and agent**: which agents/ file, effort, budget; what the main session (Opus 5.5) does itself.
5. **Procedure**: ≤10 numbered steps, each one sentence.
6. **Gate (pass/fail)**: a checklist; every item mechanically or visibly checkable; last item always "STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count".
7. **Propagate step**: read OPEN inbox items targeting this stage's files → plan-mode change list → user approval → edit upstream first → mark downstream `stale` → close items with pointer.
8. **Advisor touchpoint** (stages 04, 06, 10 only): what is exported (DOCX/PDF from md), what they are asked.
9. **Evidence**: 3–8 refs [X#] with grade.

## 6. CLAUDE.md sections (in order, <200 lines total)
1. What this is / how to start a session (cwd = paper-workflow/, `claude`, say "start stage NN for <slug>"); setup checklist (copy agents/*.md → .claude/agents/, settings.json present, hook executable).
2. The axis rule (one axis of findings; every analysis maps to one question; nulls and unmapped rows kept).
3. Labels and vocabulary (§3 above).
4. Citation rule (cite only SUPPORT-CHECKED ledger rows; AI/NotebookLM summaries NOT-CITABLE; retrieval never memory; every citation = DOI + verbatim quote + page/section).
5. Model routing table (task → model/effort → agent) + pinning rules (full IDs; orchestrator never passes `model`; never set CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1; Haiku not used).
6. One-live-file rule, inbox rule, answer-without-editing rule, propagate trigger phrase "propagate inbox".
7. Session pattern (one stage per session; write STATE.md → commit → `/rename` → `/clear`; `/compact Focus on <task>` only mid-stage in 05/08; bursts inside the 1-hour cache window; after a long break start fresh from STATE.md).
8. Compact Instructions (what to keep if compaction ever runs: current stage, gate status, live_file, open inbox IDs, last decision).
9. Data and policy caveats (Fable retention terms before uploading unpublished data; NotebookLM terms; publisher AI disclosure re-read at stage 10).
10. Enforcement reference: the exact content of .claude/settings.json and the guard.sh behaviour, in ≤25 lines.

## 7. .claude/settings.json and guard.sh (approved exception)
- permissions.deny: `Edit(/papers/*/data/**)` (raw data read-only). permissions.ask: `Edit(/papers/*/analysis-plan.md)`, `Edit(/CLAUDE.md)`, `Edit(/stages/**)`, `Edit(/agents/**)`, `Edit(/templates/**)`.
- hooks.PreToolUse matcher `Edit|Write` → command `"$CLAUDE_PROJECT_DIR"/.claude/hooks/guard.sh`. guard.sh reads tool_input.file_path via jq; only acts on paths under papers/<slug>/; always allows STATE.md and inbox.md; denies analysis-plan.md when a tag `plan-<slug>-*` exists (exit 2 with reason); if STATE.md has `mode: propagate` allows everything else; otherwise allows only paths matching `live_file:` (file or directory prefix); denies others with reason "not the live file; append to inbox.md". Use the JSON `hookSpecificOutput.permissionDecision` form or exit 2 (B20, G22).
- hooks.SessionStart matcher `compact|resume|startup` → `ls -t papers/*/STATE.md 2>/dev/null | head -1 | xargs -r cat`.
- hooks.Stop (type command): print a reminder to update STATE.md if `git status --porcelain papers/` is non-empty (never block; reminder only).

## 8. templates/
- question-map.md: the advisor package: question | hypothesis + origin | analysis (plan-id or exploratory) | result incl. null | deviation ref | figure/table | status. Plus "not mapped" section and a 5-line cover note for advisors.
- doi-ledger.md: three linked tables: (a) search-and-consultation log (string, databases, date, hits, consulted before/after results); (b) reference rows (ID, DOI, resolver, resolve date, metadata-match, retraction check, fulltext flag, status); (c) claim-support rows (claim ID, ref ID, verbatim quote, page/section, verifier, date, status). Plus the AI-summary provenance list (NOT-CITABLE) and disclosure fields.
- section-skeleton.md: per section (Abstract, Introduction, Methods, Results, Discussion, Disclosure statement, Data/code availability) the bullet slots, each with `[ledger: R12, R15]` placeholders; the Methods block lists the mandatory items (dataset pre-existed, prior exposure, plan date or "no plan", deviations, candidate model set + selection rule, n/effect/uncertainty, data & code availability, AI-use statement); the Disclosure statement block covers modes b–e ("not preregistered", all-analyses-reported, post hoc subsection).
- analysis-to-question.md: the mechanical table for stage 06: analysis-log row ID → question ID → label → plan-id → result → reported where → notes; completeness rule: one row per analysis-log row.

## 9. docs/rationale.md
One entry per decision D3–D20 and per gate: decision · why · evidence refs with grade · what would change the decision. Include an "evidence quality" summary (what is A-grade and independent vs vendor-only vs UNVERIFIED/snippet) and the list of environment limits met during research (proxy-blocked hosts).

## 10. Caps and checks
CLAUDE.md <200 lines; STATE.md template ≤60; stage ≤120; agent ≤80; template ≤120; rationale ≤400; no file >500. Every stage ends with a gate. Every rule in CLAUDE.md that rests on evidence names a ref; rules without evidence say "judgement call".
