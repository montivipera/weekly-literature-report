# paper-workflow: operating rules for Claude Code

A staged, gated workflow for writing one empirical paper at a time. This file loads every session and is re-read from disk after compaction [B26, B32]; keep it under 200 lines [B28]. It is context, not enforcement: hard rules live in .claude/settings.json and .claude/hooks/guard.sh [B23, G15]. Rules without evidence say (judgement call).

## What this is and how to start a session
First session (once per clone, then once per paper):
- Prerequisites: git; jq; R or Python; pandoc; pdftotext; network access to api.crossref.org, api.openalex.org and doi.org, or the PubMed / Consensus / Scholar Gateway MCP connectors. paper-workflow/ must sit in a git repo (commits, plan tags, `derives-from` hashes).
- Setup, from paper-workflow/: `mkdir -p .claude/agents && cp agents/*.md .claude/agents/` (project subagents load from there [B1]), then `chmod +x .claude/hooks/guard.sh`.
- Check: `ls .claude/agents/` lists eight files, each pinned to a full model ID. Re-copy after any edit to agents/*.md (agents/ is the source, .claude/agents/ the installed copy).
- Never set CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1 and never pass a per-invocation `model` when delegating: both override the agents' pins [B4].
- Launch: `cd paper-workflow && claude`, then `/model claude-opus-5-5`. Main-session effort: leave the default (judgement call); Opus 5.5 defaults to medium [E30].
- New paper: `mkdir -p papers/<slug> && cp STATE.md papers/<slug>/`, then type "start stage 00 for <slug>".
- Run a gate: type "run the stage NN gate"; Claude ticks the checklist and proposes a status, and you approve it (judgement call).
- Propagate: type "propagate inbox", then enter plan mode with Shift+Tab [G23 UNVERIFIED] so the change list waits for your approval.
- After `/clear`: type "continue <slug> at stage NN"; the SessionStart hook re-injects the newest STATE.md [B22].
- Gate commands run from paper-workflow/ (the project root for Claude Code); git object paths use `<tag>:./papers/<slug>/<file>`, diffs use `-- papers/<slug>/...`.

Every session reads papers/<slug>/STATE.md, this file and the current stage file only, and opens other files on demand [G12]. The SessionStart hook prints only the most recently modified STATE.md [B22], so with several papers check the slug. Stages run in order, one file each in stages/, and each ends with a gate; the entry mode decides which run normally.

| ID | stage file | live files (`live_file:` may list several; switch only where the stage file says) |
|---|---|---|
| S00 | 00-intake.md | intake.md (also creates inbox.md, data-access.md, disclosure.md in modes b–e, the STATE.md gate block) |
| S01 | 01-data-inventory.md | data-inventory.md, SHA256SUMS |
| S02 | 02-pre-question-scan.md | search-log.md, scan-notes.md |
| S03 | 03-question-framing.md | questions.md |
| S04 | 04-method-and-plan-freeze.md | method-rationale.md, critique.md (steps 1–3), then analysis-plan.md (steps 4–9); tag `plan-<slug>-v1` |
| S05 | 05-analysis.md | scripts/, results/, analysis-log.md, deviations.md |
| S06 | 06-question-map.md | question-map.md |
| S07 | 07-methods-results.md | methods.md, results.md |
| S08 | 08-literature-extraction.md | doi-ledger.md (R and CL rows) |
| S09 | 09-citation-verification.md | doi-ledger.md (verification cells) |
| S10 | 10-discussion-critique-submission.md | draft/, then critique.md, then disclosure.md |

- STATE.md, inbox.md and data-access.md are always writable. Other folders: agents/ (8 subagents), templates/ (question-map, doi-ledger, section-skeleton, analysis-to-question), docs/rationale.md (why each rule exists).

## The axis rule
- One paper, one axis of findings. Each question in questions.md sits on that axis. A side finding becomes an inbox line, a candidate for another paper (judgement call).
- Every analysis maps to exactly one question. question-map.md has one row per as-run analysis, in run order [F1, F31].
- Null results stay in the map. Analyses that answer no question go to its "not mapped" section and are never deleted [F1, F31].
- Questions are not found by trawling outcomes: data-reader never runs outcome–predictor tests, and candidate RQs are capped and logged [C4, C34].

## Labels and vocabulary
Use these strings exactly.
- Entry modes (set at stage 00; the user confirms, a judgement call): `a-data-only`, `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`.
- Gate statuses, each with an evidence pointer (a file or a commit) and a variant (`normal` or `retro`) in the STATE.md gate table:
  - `PASSED`: the gate was passed, or a dated artefact shows the work predates outcome inspection [F11];
  - `RETRO-AUDIT`: the full checklist was run on existing material, recorded as audited, not prospective [F16]; it is never shortened (judgement call);
  - `NOT-PASSABLE`: the disclosure item is queued (one line in STATE.md, full text in disclosure.md);
  - `OPEN`: still ahead; runs normally.
- S04 (plan freeze) can never pass retrospectively: late registration cannot show that decisions were prespecified [F13, F16].
- Analysis labels: `exploratory` is the default [F5 UNVERIFIED, F6, F26]. `confirmatory` needs a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data) [F10–F12, F35]. In modes b–e, and in a after any outcome-level look recorded in data-access.md, the hold-out or new data must be declared in data-access.md at stage 00/01 before any analysis in this workflow, and the plan tagged before any analysis of it; gates S04 and S05 check that the data-access.md date precedes the first results/ commit. Otherwise `exploratory`. Multiverse and second-analyst checks never upgrade a label (F, Robustness).
- Hypothesis origin on every hypothesis: `origin: literature | data | advisor` [C2].
- Row IDs: `Q<nn>` search strings · `R<nn>` reference rows · `CL<nn>` claim-support rows · `A<nn>` analysis-log rows · `D<nn>` deviations · `I<nn>` inbox items. No `S<nn>`, no `SC<nn>`. Stage IDs are `S04` style; session names are `/rename <slug>-S<NN>`.
- R status: `UNRESOLVED` → `RESOLVED` → `METADATA-OK` (terminal for R), or `RETRACTED` / `NOT-CITABLE`; the retraction check happens before `METADATA-OK` is set. CL status: `UNRESOLVED` → `SUPPORT-CHECKED`, or `NOT-CITABLE`. Flags: `fulltext: yes|no`, `consulted: before-results|after-results`, `risk: high|normal` [C2, D20].
- Markers: `[ledger: CL12, CL15]` (claim-support rows only) and `[log: A03]` for any number taken from an analysis. No other marker forms (`[res:]`, `<!-- src -->`, `[own result]`, `[ledger: R..]`).
- STATE.md: `mode: work | propagate` and `live_file: <path relative to papers/<slug>/>`. A trailing `/` means a directory, and several paths are comma-separated (judgement call).
- Evidence grades in docs/rationale.md: A / B / C, plus `UNVERIFIED` where the research file says so. Never upgrade a grade (judgement call).

## Citation rule
- Drafts cite only CL rows with status `SUPPORT-CHECKED`, as `[ledger: CL12, CL15]`, never a typed-in reference, because a link is not support [D14, D16]. The reference list is generated from the R rows of cited CL rows, each R at least `METADATA-OK`.
- Every CL row is a verbatim quote + page or section from the full text (`fulltext: yes`), tied to an R row with a DOI [D19, D20, A31 UNVERIFIED].
- References come from retrieval (Crossref, OpenAlex, PubMed), never from model memory [D1–D12, A21]. DOI resolution plus a metadata match is the recommended control [D9].
- AI summaries (NotebookLM, chat or agent prose) are `NOT-CITABLE`. They can point to a source but never stand in for it [D19, D21].
- citation-verifier works in its own context and is never the drafter: evidence on model self-verification of references is thin (one n=40 study) [D18]; models fail at self-evaluation [A24]. Human check: every `risk: high` row, plus a sample of ≥10 rows or 10% of the rest [D4, D9].
- Run a retraction check on every cited source at stage 09, in every entry mode, before `METADATA-OK` [F27–F29, F30 UNVERIFIED].

## Model routing
Main session: `claude-opus-5-5`; effort: main session medium; stage 03 sessions high (judgement call). No CLI effort control is documented in research/B or E, so leave the default unless your version offers one. The main session orchestrates, frames questions and updates STATE.md. Switching model mid-session re-reads the history uncached [E6]. The user decides every gate (judgement call).

| task | stages | model (full ID) · `effort:` | agent | evidence |
|---|---|---|---|---|
| inventory raw data and artefacts; no outcome–predictor tests | S00, S01 | claude-sonnet-5-5 · medium | data-reader | judgement call (cost) |
| fill the plan before the tag; run scripts exactly per analysis-plan.md; log every run | S04, S05 | claude-sonnet-5-5 · medium | analyst | [A14] |
| read full texts; write R and CL rows (quote, page/section, fulltext flag) | S02, S08 | claude-sonnet-5-5 · medium | lit-extractor | [E30, D19] |
| resolve DOI and metadata; retraction check; check claim–passage support | S02, S09 | claude-sonnet-5-5 · low | citation-verifier | [D9, D10, D12, D18] |
| re-open one source passage on request; return quote and location | S08, S10 | claude-sonnet-5-5 · medium | source-rechecker | [A25] |
| propose and justify models (Zuur & Ieno 2016, Bolker 2009, Harrison 2018) | S04 | claude-opus-5-5 · high | methods-advisor | [A5, A20, C37] |
| write section text to the skeleton | S07, S10 | claude-opus-5-5 · medium | drafter | [A8, A28] |
| fresh-context adversarial review: method critique (S04), draft critique (S10) | S04, S10 | claude-opus-5-5 · high | critic | [A24, A25, A17] |
| prose polish or methods critique only after Opus 5.5 fails an acceptance check; new session; check retention terms first | S10 | claude-fable-5-1 · default | none (user switches) | [A5; A19 C UNVERIFIED]; switching model re-reads history uncached [E6] |

- Pin full model IDs in agent frontmatter; aliases move [B3, B37]. Effort is the `effort:` frontmatter key [B2, E32], one level per agent file (judgement call); the body repeats "Work at <level> effort". Budgets are body rules.
- The orchestrator never passes `model` when it calls an agent, because a per-invocation model outranks frontmatter [B4].
- Haiku is not used [A4, A33, E4].
- Sonnet readers extract to schema and never summarise prose [D19]. Opus agents never read raw sources or data, and read only a grep-extracted slice of doi-ledger.md (the CL rows named in the skeleton or the question map), never the whole ledger (judgement call).
- Subagents draw on the same usage limits and start with a cold 5-minute cache. Delegate only when the output would otherwise bloat the main context [G18, G19].

## One live file, inbox, answers, propagate
- Why: every edit is another request that re-sends the whole context [G6], so one idea that touches six files costs at least six of them (inference).
- Live files: STATE.md `live_file:` names what this session may edit. It may list several paths; switch only where the stage file says, never to get past a deny (judgement call). STATE.md, inbox.md and data-access.md are always writable. guard.sh enforces this in every permission mode [G22]; this text alone would not [B23, G15].
- guard.sh is a strong speed bump against accidental cascades, not a lock: Claude can edit STATE.md, so the user reviews `git diff papers/<slug>/STATE.md` at every gate (judgement call). guard.sh prints a stderr notice whenever an edit changes `live_file:` or `mode:`.
- Inbox rule: an idea, correction or question that would change any file other than the live file becomes one row appended to papers/<slug>/inbox.md, and Claude stops there. Format (header defined in stages/00): `I<nn> | date | text | target file | status`, where status is `OPEN` or `CLOSED -> <file>@<commit>`. Never edit or delete a row; close an item by appending a row with the same ID and status `CLOSED -> <file>@<commit>` (inference from [G13]; append-only records [G27, C UNVERIFIED]).
- Answer without editing: answer in chat any question about content, methods, definitions or status, any "what if", and any request for suggested wording. Use files in context or read on demand. If the answer implies a change outside the live file, append one inbox row and stop. Edit the live file only when the user asks for an edit (inference; [G25 UNVERIFIED]).
- Propagate trigger: the user's phrase "propagate inbox", or a gate's propagate step; never automatic (judgement call; [G13]). Then: set `mode: propagate` → read the OPEN items → propose a change list in plan mode [G23 UNVERIFIED] → user approves → edit upstream first → add downstream files to `stale:` → close the items with pointers → set `mode: work` → commit. Full steps: each stage file's Propagate step.
- Update order, upstream → downstream only: intake.md → data/ (raw, read-only), sources/ (full-text PDFs, read-only) → data-inventory.md, SHA256SUMS → search-log.md, scan-notes.md → questions.md → method-rationale.md → analysis-plan.md (frozen) → scripts/, results/A<nn>.md, analysis-log.md, deviations.md → question-map.md → methods.md, results.md → doi-ledger.md → draft/*, critique.md, disclosure.md. STATE.md, inbox.md and data-access.md sit outside the chain.
- Every derived file starts with `derives-from: <file>@<short-commit>` (the stage file's wording wins). An upstream change never edits downstream files; it lists them in `stale:` (inference; one authoritative file per fact [G26, C UNVERIFIED]).
- After tag `plan-<slug>-v1`, any change to the plan is only ever a row in deviations.md (`D<nn> | date | plan-id | what changed | why | effect on label | user OK`) [F23]. guard.sh denies the edit even in propagate mode.
- Analysis scripts write only to results/, because deny rules do not see R or Python subprocess writes [G21].
- Write per-paper files only with Edit or Write, never through Bash redirects, so guard.sh sees every write (judgement call).
- Never edit .claude/settings.json or guard.sh (`Edit(/.claude/**)` asks first); propose any change to the user (judgement call).

## Session pattern
1. One stage per session, starting from CLAUDE.md, the stage file and STATE.md only [G12, G13].
2. At the end of each stage or work burst: write STATE.md → `git commit` → `/rename <slug>-S<NN>` → `/clear`. `/clear` costs nothing and the old session stays resumable [G9, G17]; the SessionStart hook re-injects STATE.md [B22].
3. Use `/compact Focus on <task>` only mid-stage, in S05 or S08, when the stage does not fit one session. Run it at a natural break while the cache is warm; compaction is lossy and is itself a full-history request [G9, G12, G16, B31].
4. Work in bursts inside the 1-hour cache window [G7]. After a longer break, do not resume a session over 100k tokens; start fresh from STATE.md [G7, G10].
5. Keep the main session thin: agents write files and return a message of 10 lines or fewer (path, counts, flags) [B6, G14, G18].
6. Watch `/usage` for long-context and cache-miss flags [G11]. After two failed corrections on one issue, `/clear` and restart with a better prompt [G25 UNVERIFIED].

## Compact Instructions
When compacting, keep these and drop tool output, file bodies and draft text [B31]:
- the slug and the current stage (stages/NN file);
- the current gate's status and evidence pointer;
- `mode:` and `live_file:`;
- the open inbox IDs and their count;
- the last decision and the next step.
After compaction, re-read papers/<slug>/STATE.md (the SessionStart hook re-prints the newest one [B22, B32]) and the stage file before acting.

## Data and policy caveats
- Fable retention terms: before uploading unpublished data to any session, re-read the current data-retention and training-use terms for the model and plan in use, and your data agreement [A19 C UNVERIFIED]. If they do not allow it, keep the raw data out of sessions (judgement call).
- NotebookLM: check its terms before uploading PDFs or data. Its output is `NOT-CITABLE` [D19, D21].
- At stage 10, re-read the target publisher's AI-use disclosure policy, because policies change. The main session writes disclosure.md and the Methods AI-use statement follows it (judgement call).
- Raw data in papers/<slug>/data/ is read-only (deny rule). Scripts never write there [G20, G21]. Before any script runs (stage 01 setup; stage 05 RETRO-AUDIT): `chmod -R a-w papers/<slug>/data` and commit data/ (judgement call).
- SHA256SUMS sits beside data/, never inside it; gate 01 runs `sha256sum -c SHA256SUMS` from papers/<slug>/.
- data-access.md (append-only, created at stage 00 in every mode) logs every look: `date | who | what was seen/run | outcome-level? yes|no` [F11].

## Enforcement reference
.claude/settings.json (exact content):
```json
{
  "permissions": {
    "deny": ["Edit(/papers/*/data/**)"],
    "ask": ["Edit(/papers/*/analysis-plan.md)", "Edit(/CLAUDE.md)", "Edit(/stages/**)", "Edit(/agents/**)", "Edit(/templates/**)", "Edit(/.claude/**)"]
  },
  "hooks": {
    "PreToolUse": [{"matcher": "Edit|Write", "hooks": [{"type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/guard.sh"}]}],
    "SessionStart": [{"matcher": "startup|resume|clear|compact", "hooks": [{"type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && ls -t papers/*/STATE.md 2>/dev/null | head -1 | xargs -r cat"}]}],
    "Stop": [{"hooks": [{"type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && if [ -n \"$(git status --porcelain papers/ 2>/dev/null)\" ]; then echo '{\"systemMessage\": \"Reminder: papers/ has uncommitted changes. Update STATE.md (gate status, live_file, stale, open inbox count) and commit before /clear.\"}'; fi; exit 0"}]}]
  }
}
```
- Deny beats ask, which beats allow. `Edit(...)` rules cover every built-in edit tool and `sed`/`tee`/`>`, but not subprocess writes [G20, G21]. A hook "allow" is silence, so these rules still apply.
- guard.sh (PreToolUse, every permission mode [G22]) reads `tool_input.file_path` with jq (none → allow), then: (1) path not under papers/<slug>/ → allow; `.`/`..` segments → deny;
  (2) inbox.md or data-access.md → allow; STATE.md → allow, with a stderr notice "guard: live_file/mode changed in STATE.md" when the edit changes `live_file:` or `mode:`;
  (3) analysis-plan.md while `git tag -l "plan-<slug>-*"` is non-empty → deny, in any mode; (4) no STATE.md → allow, with a stderr warning;
  (5) `mode: propagate` → allow; (6) the path equals `live_file:`, or lies under it when it ends in `/` (comma list allowed) → allow;
  (7) anything else → deny: "not the live file … append the idea to inbox.md instead". If jq is missing, exit 2 (blocks every edit).
- Deny = `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"…"}}` on stdout, exit 0 [B20, G22].
- SessionStart (`startup|resume|clear|compact` [B22]) prints the newest papers/*/STATE.md. Stop emits `{"systemMessage": "<reminder>"}` on stdout (exit 0) when papers/ has uncommitted changes; it never blocks [B20, B21].
