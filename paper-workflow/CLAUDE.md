# paper-workflow: operating rules for Claude Code

A staged, gated workflow for writing one empirical paper at a time. This file loads every session and is re-read from disk after compaction [B26, B32]; keep it under 200 lines [B28]. It is context, not enforcement: hard rules live in .claude/settings.json and .claude/hooks/guard.sh [B23, G15]. Rules without evidence say (judgement call).

## What this is and how to start a session
- Start: `cd paper-workflow && claude`, then say "start stage NN for <slug>". Read papers/<slug>/STATE.md, this file and that stage file only; open other files on demand [G12]. The SessionStart hook prints only the most recently modified STATE.md [B22], so with several papers check the slug.
- New paper: create papers/<slug>/, copy STATE.md into it, then say "start stage 00 for <slug>" (judgement call).
- Setup checklist (once per clone):
  - [ ] copy agents/*.md to .claude/agents/ (project subagents load from there [B1]);
  - [ ] .claude/settings.json present (permissions and hooks [B19]);
  - [ ] .claude/hooks/guard.sh executable (`chmod +x`); `jq` and `git` installed;
  - [ ] paper-workflow/ sits in a git repo (commits, plan tags, `derives-from` hashes);
  - [ ] CLAUDE_CODE_SUBAGENT_MODEL_FORCE is not set [B4].
- Stages: one file each in stages/, run in order, and each ends with a gate. Entry mode decides which run normally.

| # | stage file | main outputs (live files; the stage file is authoritative) |
|---|---|---|
| 00 | 00-intake.md | intake.md, inbox.md, entry mode and gate block in STATE.md |
| 01 | 01-data-inventory.md | data-inventory.md |
| 02 | 02-pre-question-scan.md | search-log.md, scan-notes.md |
| 03 | 03-question-framing.md | questions.md |
| 04 | 04-method-and-plan-freeze.md | method-rationale.md, analysis-plan.md, then tag `plan-<slug>-v1` |
| 05 | 05-analysis.md | scripts/, results/*.md, analysis-log.md, deviations.md |
| 06 | 06-question-map.md | question-map.md |
| 07 | 07-methods-results.md | methods.md, results.md |
| 08 | 08-literature-extraction.md | doi-ledger.md (reference and claim rows) |
| 09 | 09-citation-verification.md | doi-ledger.md (status columns) |
| 10 | 10-discussion-critique-submission.md | draft/intro.md, draft/discussion.md, draft/abstract.md, critique.md, disclosure.md |

- Other folders: agents/ (8 subagents), templates/ (question-map, doi-ledger, section-skeleton, analysis-to-question), docs/rationale.md (why each rule exists).

## The axis rule
- One paper, one axis of findings. Each question in questions.md sits on that axis. A side finding becomes an inbox line, a candidate for another paper (judgement call).
- Every analysis maps to exactly one question. question-map.md has one row per as-run analysis, in run order [F1, F31].
- Null results stay in the map. Analyses that answer no question go to its "not mapped" section and are never deleted [F1, F31].
- Questions are not found by trawling outcomes: data-reader never runs outcome–predictor tests, and candidate RQs are capped and logged [C4, C34].

## Labels and vocabulary
Use these strings exactly.
- Entry modes (set at stage 00; the user confirms, a judgement call): `a-data-only`, `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`.
- Gate statuses, each with an evidence pointer (a file or a commit):
  - `PASSED`: the gate was passed, or a dated artefact shows the work predates outcome inspection [F11];
  - `RETRO-AUDIT`: the full checklist was run as an audit of existing material and is never shortened [F16];
  - `NOT-PASSABLE`: the disclosure item is queued in STATE.md;
  - `OPEN`: still ahead; runs normally.
- S04 (plan freeze) can never pass retrospectively: late registration cannot show that decisions were prespecified [F13, F16].
- Analysis labels: `exploratory` is the default [F5 UNVERIFIED, F6, F26]. `confirmatory` needs a `plan-id` from a plan tagged before any outcome model ran, or new or never-explored held-out data [F10–F12, F35]. Multiverse and second-analyst checks never upgrade a label (F, Robustness).
- Hypothesis origin on every hypothesis: `origin: literature | data | advisor` [C2, C7, C25].
- Ledger row status: `UNRESOLVED`, `RESOLVED`, `METADATA-OK`, `SUPPORT-CHECKED`, `NOT-CITABLE`, `RETRACTED`. Flags: `fulltext: yes|no` and `consulted: before-results|after-results` [C2, D20].
- STATE.md: `mode: work | propagate` and `live_file: <path relative to papers/<slug>/>`. A trailing `/` means a directory, and several paths are comma-separated (judgement call).
- Evidence grades in docs/rationale.md: A / B / C, plus `UNVERIFIED` where the research file says so. Never upgrade a grade (judgement call).

## Citation rule
- Cite only ledger rows with status `SUPPORT-CHECKED`. Draft text cites row IDs (`[ledger: R12]`), never a typed-in reference, because a link is not support [D14, D16].
- Every citation is DOI + verbatim quote + page/section, taken from the full text (`fulltext: yes`) [D19, D20, A31].
- References come from retrieval (Crossref, OpenAlex, PubMed), never from model memory [D1–D12, A21]. DOI resolution plus a metadata match is the proven control [D9].
- AI summaries (NotebookLM, chat or agent prose) are `NOT-CITABLE`. They can point to a source but never stand in for it [D19, D21].
- citation-verifier works in its own context and is never the drafter, because self-checks are weak [D18]. High-risk references (regional, post-2020) also get a human check [D4, D9].
- Run a retraction check on every cited source at stage 09, in every entry mode [F27–F29, F30 UNVERIFIED].

## Model routing
Main session: `claude-opus-5-5`, effort medium, for the whole session. It orchestrates, frames questions and updates STATE.md. Switching model mid-session re-reads the history uncached [E6, A5]. The user decides every gate (judgement call).

| task | model (full ID) · effort | agent | evidence |
|---|---|---|---|
| inventory raw data and artefacts; no outcome–predictor tests | claude-sonnet-5-5 · medium | data-reader | judgement call (cost) |
| write and run scripts exactly per analysis-plan.md; log every run | claude-sonnet-5-5 · medium | analyst | [A14] |
| read full texts; write ledger rows (quote, page/section, fulltext flag) | claude-sonnet-5-5 · medium | lit-extractor | [E30, D19] |
| resolve DOI and metadata; check claim–passage support | claude-sonnet-5-5 · low | citation-verifier | [D9, D10, D12, D18] |
| re-open one source passage on request; return quote and location | claude-sonnet-5-5 · medium | source-rechecker | [A25] |
| propose and justify models (Zuur & Ieno 2016, Bolker 2009, Harrison 2018) | claude-opus-5-5 · high | methods-advisor | [A5, A20, C37] |
| write section text to the skeleton | claude-opus-5-5 · medium (high for Discussion) | drafter | [A8, A28] |
| fresh-context adversarial review; check every citation maps to a verified row | claude-opus-5-5 · high | critic | [A24, A25, A17] |

- Pin full model IDs in agent frontmatter; aliases move [B3, B37]. Effort and budget are body rules in each agent file.
- The orchestrator never passes `model` when it calls an agent, because a per-invocation model outranks frontmatter [B4].
- Never set `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`: it forces every subagent onto one model [B4].
- Haiku is not used [A4, A33, E4].
- Sonnet readers extract to schema and never summarise prose [D19]. Opus agents never read raw sources or data (judgement call).
- Subagents draw on the same usage limits and start with a cold 5-minute cache. Delegate only when the output would otherwise bloat the main context [G18, G19].

## One live file, inbox, answers, propagate
- Why: every edit is another request that re-sends the whole context [G6], so one idea that touches six files costs at least six of them (inference).
- One live file: STATE.md `live_file:` names what this session may edit. STATE.md and inbox.md are always writable. guard.sh enforces this in every permission mode [G22]; this text alone would not [B23, G15].
- Change `live_file:` only where a stage file says to (stage start or gate pass), never to get past a deny (judgement call).
- Inbox rule: an idea, correction or question that would change any file other than the live file becomes one line appended to papers/<slug>/inbox.md, and Claude stops there. Format: `I<NN> | <YYYY-MM-DD> | target: <file> | <text> | OPEN`. Never edit or delete a line. To close an item, append `I<NN> | <YYYY-MM-DD> | CLOSED -> <file>@<commit>` (inference from [G13]; append-only records [G27, C UNVERIFIED]).
- Answer without editing: answer in chat any question about content, methods, definitions or status, any "what if", and any request for suggested wording. Use files in context or read on demand. If the answer implies a change outside the live file, append one inbox line and stop. Edit the live file only when the user asks for an edit (inference; [G25 UNVERIFIED]).
- Propagate trigger: the user's phrase "propagate inbox", or a gate's propagate step; never automatic (judgement call; [G13]). Then: set `mode: propagate` → read the OPEN items → propose a change list in plan mode [G23 UNVERIFIED] → user approves → edit upstream first → add downstream files to `stale:` → close the items with pointers → set `mode: work` → commit. Full steps: each stage file's Propagate step.
- Update order, upstream → downstream only: intake.md → data/ (raw, read-only) → data-inventory.md → search-log.md, scan-notes.md → questions.md → method-rationale.md → analysis-plan.md (frozen) → scripts/, results/*.md, analysis-log.md, deviations.md → question-map.md → methods.md, results.md → doi-ledger.md → draft/*, critique.md, disclosure.md. STATE.md and inbox.md sit outside the chain.
- Every derived file starts with `derives-from: <file>@<short-commit>`. An upstream change never edits downstream files; it lists them in `stale:` (inference; one authoritative file per fact [G26, C UNVERIFIED]).
- After tag `plan-<slug>-v1`, any change to the plan is only ever a row in deviations.md [F23]. guard.sh denies the edit even in propagate mode.
- Analysis scripts write only to results/, because deny rules do not see R or Python subprocess writes [G21].
- Write per-paper files only with Edit or Write, never through Bash redirects, so guard.sh sees every write (judgement call).
- Never edit .claude/settings.json or guard.sh; propose any change to the user (judgement call).

## Session pattern
1. One stage per session, starting from CLAUDE.md, the stage file and STATE.md only [G12, G13].
2. At the end of each stage or work burst: write STATE.md → `git commit` → `/rename <slug>-SNN` → `/clear`. `/clear` costs nothing and the old session stays resumable [G9, G17].
3. Use `/compact Focus on <task>` only mid-stage, in 05 or 08, when the stage does not fit one session. Run it at a natural break while the cache is warm; compaction is lossy and is itself a full-history request [G9, G12, G16, B31].
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
- Fable retention terms: before uploading unpublished data to any session, re-read the current data-retention and training-use terms for the model and plan in use, and your data agreement. If they do not allow it, keep the raw data out of sessions (judgement call; not verified in research).
- NotebookLM: check its terms before uploading PDFs or data. Its output is `NOT-CITABLE` [D19, D21].
- At stage 10, re-read the target publisher's AI-use disclosure policy, because policies change. disclosure.md and the Methods AI-use statement follow it (judgement call).
- Raw data in papers/<slug>/data/ is read-only (deny rule). Scripts never write there [G20, G21].

## Enforcement reference
.claude/settings.json (exact content):
```json
{
  "permissions": {
    "deny": ["Edit(/papers/*/data/**)"],
    "ask": ["Edit(/papers/*/analysis-plan.md)", "Edit(/CLAUDE.md)", "Edit(/stages/**)", "Edit(/agents/**)", "Edit(/templates/**)"]
  },
  "hooks": {
    "PreToolUse": [{"matcher": "Edit|Write", "hooks": [{"type": "command", "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/guard.sh"}]}],
    "SessionStart": [{"matcher": "compact|resume|startup", "hooks": [{"type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && ls -t papers/*/STATE.md 2>/dev/null | head -1 | xargs -r cat"}]}],
    "Stop": [{"hooks": [{"type": "command", "command": "cd \"$CLAUDE_PROJECT_DIR\" && if [ -n \"$(git status --porcelain papers/ 2>/dev/null)\" ]; then echo 'Reminder: papers/ has uncommitted changes. Update STATE.md (gate status, live_file, stale, open inbox count) and commit before /clear.'; fi; exit 0"}]}]
  }
}
```
- Deny beats ask, which beats allow. `Edit(...)` rules cover every built-in edit tool and `sed`/`tee`/`>`, but not subprocess writes [G20, G21]. A hook "allow" is silence, so these rules still apply.
- guard.sh (PreToolUse, every permission mode [G22]) reads `tool_input.file_path` with jq, then: (1) path not under papers/<slug>/ → allow; `.`/`..` segments → deny; (2) STATE.md or inbox.md → allow;
  (3) analysis-plan.md while `git tag -l "plan-<slug>-*"` is non-empty → deny, in any mode; (4) no STATE.md → allow, with a stderr warning;
  (5) `mode: propagate` → allow; (6) the path equals `live_file:`, or lies under it when it ends in `/` (comma list allowed) → allow;
  (7) anything else → deny: "not the live file … append the idea to inbox.md instead". If jq is missing, exit 2 (blocks every edit).
- Deny = `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"…"}}` on stdout, exit 0 [B20, G22].
- SessionStart prints the newest papers/*/STATE.md [B22]. Stop prints a reminder to update STATE.md and commit when papers/ has changes; it never blocks [B20, B21].
