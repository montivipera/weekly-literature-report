# G. Context cost, state-in-files, and update-cascade control (Claude Code, Pro/Max, as of 2026-10-04)

Scope: (1) how plan limits meter context; (2) official guidance on state-in-files and session handoff; (3) mechanisms that stop multi-file update cascades; (4) doc-engineering patterns; (5) subagent isolation as a cost tool.
Method: 12 fetches + 9 searches, 2026-10-04. Docs pages carry no date (they cite versions up to ~v2.1.283); "UNVERIFIED" = claim taken from a search snippet, page not read.
Grades: A = first-party Anthropic docs/support/engineering post (vendor-authored, not peer-reviewed); B = systematic independent; C = blog/anecdote.

## Claims
| # | Claim | Source URL | Source date | Grade |
|---|-------|-----------|-------------|-------|
| 1 | Pro and Max limits are shared across claude.ai and Claude Code; warnings show remaining capacity; `/status` checks it. The article gives no mechanics (no 5-hour/weekly detail, no counting rules). | support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan | 2026-08-19 | A |
| 2 | Teams/Enterprise Claude Code usage draws from a per-seat allowance on "a rolling five-hour window and a weekly window", shared with chat and Cowork. | code.claude.com/docs/en/costs | undated | A |
| 3 | Pro/Max/Team/seat-Enterprise have a 5-hour rolling session limit plus weekly limits (fixed per-account reset); Max 5x/20x = 5x/20x Pro per-session allowance. | support.claude.com/en/articles/11049741-what-is-the-max-plan | undated | A UNVERIFIED |
| 4 | Usage depends on message length, attachment size, conversation length, tool use, model, effort level; it is not counted in messages. | support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work | undated | A UNVERIFIED |
| 5 | 2026-05-06: Claude Code five-hour limits doubled for Pro/Max/Team/seat-Enterprise; peak-hours reduction removed for Pro/Max. | anthropic.com/news/higher-limits-spacex | 2026-05-06 | A UNVERIFIED |
| 6 | "Token costs scale with context size." Claude Code sends the full conversation with every request; each tool round is another request. With caching the history is re-read "at the cached token rate", so "a one-line question in a session that has been open all day still draws usage for the whole conversation". | code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session | undated | A |
| 7 | First message after a break longer than the cache lifetime misses the cache and reprocesses full context; lifetime is 1 hour on a subscription (5 min once drawing usage credits). | code.claude.com/docs/en/prompt-caching#cache-lifetime | undated | A |
| 8 | Cached portions "count less against your limits than new content" (stated for chat/project content; no Claude Code-specific weight given). | support.claude.com/en/articles/9797557-usage-limit-best-practices | undated | A UNVERIFIED |
| 9 | `/clear` "costs nothing"; `/compact` "reads the conversation it summarizes", so compacting a large context is itself a large request: a fraction of context cost if cache is warm, full reprocess if cold. | code.claude.com/docs/en/costs ; /prompt-caching#compacting-the-conversation | undated | A |
| 10 | Pro/Max: resuming a session idle >~1 h and >100k tokens opens a dialog: "Resume from summary" (runs /compact), "Resume full session as-is", or "Don't ask me again". | code.claude.com/docs/en/sessions#resume-from-a-summary | undated | A |
| 11 | `/usage` on a plan shows attribution to skills/subagents/plugins/MCP servers and flags behaviours >=10% of usage (long context, cache misses). | code.claude.com/docs/en/costs#plan-usage-breakdown | undated | A |
| 12 | Context rot: recall falls as tokens rise; remedies are compaction, structured note-taking (NOTES.md / to-do persisted outside context), sub-agents returning "1,000-2,000" token summaries; aggressive compaction risks losing "subtle but critical context". | anthropic.com/engineering/effective-context-engineering-for-ai-agents | 2025-09-29 | A |
| 13 | "Compaction isn't sufficient" for long-running work. Handoff = progress file + JSON feature list + git commits; "one feature at a time... critical"; agents may edit the feature list only by changing a `passes` field because models overwrite JSON less than Markdown. | anthropic.com/engineering/effective-harnesses-for-long-running-agents | 2025-11-26 | A |
| 14 | Lead agent saves its plan to memory (context >200k is truncated); subagents write outputs to external artifacts and pass "lightweight references" back; agents ~4x, multi-agent ~15x chat tokens; poor fit when agents share context or have many dependencies. | anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | A |
| 15 | Each session starts with a fresh context; CLAUDE.md and auto memory are "context, not enforced configuration" (use a PreToolUse hook to enforce); target <200 lines/file; root CLAUDE.md survives /compact (re-read from disk), conversation-only instructions do not. | code.claude.com/docs/en/memory | undated | A |
| 16 | After compaction: root CLAUDE.md, unscoped rules, auto memory, and the plan-mode plan are re-injected from disk; `paths:` rules and nested CLAUDE.md are summarised away until a matching file is read again; up to 5 recent files re-read (>5,000 tokens become path-only); SessionStart `compact` hooks re-run. | code.claude.com/docs/en/context-window#what-survives-compaction | undated | A |
| 17 | `claude --continue` reopens the latest conversation in cwd; `--resume <name>` resumes by name; `/clear` saves the old conversation (resume with `/resume`); resume restores full history, model, and (terminal) permission mode. | code.claude.com/docs/en/sessions | undated | A |
| 18 | A subagent runs in its own context; verbose output stays there and "only the summary returns"; but "it also sends its own requests, which count toward the same usage limits". | code.claude.com/docs/en/sub-agents ; /costs#delegate-verbose-operations-to-subagents | undated | A |
| 19 | A subagent builds its own cache (cannot read the parent's), gets a 5-min TTL even on a subscription; the parent's cache is untouched. Agent teams use ~7x tokens of a standard session (plan mode). | code.claude.com/docs/en/prompt-caching#subagents-and-the-cache ; /costs | undated | A |
| 20 | Rule order is deny > ask > allow, first match wins; an allow cannot carve an exception from a deny. `Edit(path)` rules cover all built-in edit tools; a path rule written for `Write` is accepted but never consulted. | code.claude.com/docs/en/permissions#manage-permissions ; #read-and-edit | undated | A |
| 21 | Read/Edit deny rules also cover recognised Bash file commands (`cat`, `sed`, `tee`, `>` redirects) but not arbitrary subprocesses (a Python script); OS-level enforcement needs the sandbox. | code.claude.com/docs/en/permissions#read-and-edit | undated | A |
| 22 | PreToolUse hooks run before the permission-mode check; exit 2 (stderr to Claude) or JSON `permissionDecision:"deny"` blocks the call even in `bypassPermissions`. | code.claude.com/docs/en/hooks-guide | undated | A |
| 23 | Plan mode: Claude "explores the codebase and proposes an approach for your approval" before editing (costs page recommends it for complex tasks). Entry via Shift+Tab, `/plan`, `--permission-mode plan` (snippet). | code.claude.com/docs/en/costs ; /permission-modes | undated | A UNVERIFIED |
| 24 | `.claude/rules/*.md` with `paths:` frontmatter load only when Claude uses Read/Write/Edit on a matching file; unscoped rules load at launch. This scopes instructions, not write access. | code.claude.com/docs/en/memory#path-specific-rules | undated | A |
| 25 | Run `/clear` between unrelated tasks; after >2 corrections on one issue, `/clear` and restart with a better prompt; "kitchen sink session" is an anti-pattern. | code.claude.com/docs/en/best-practices | undated | A UNVERIFIED |
| 26 | Single source of truth: one authoritative location per fact; other docs link or derive; "two files both claim to be source of truth" is a failure mode. | docsie.io/blog/glossary/single-source-of-truth ; quanos.com (vendor glossaries) | undated | C UNVERIFIED |
| 27 | Append-only records: ADRs are never edited, only superseded by a new record (Nygard practice). | adr.github.io / realpython.com glossary (practitioner) | undated | C UNVERIFIED |

## Usage-limit arithmetic
- Per-turn cost tracks total context, not the size of your question: every request re-sends the whole history and each tool call adds another request (#6). Cumulative cost over a session therefore grows faster than linearly in turns (inference from #6).
- Caching makes re-reads cheaper but not free: re-reads are billed "at the cached token rate" and still draw plan usage (#6, #8). The 1-hour subscription cache expires after idle gaps, and the next turn reprocesses everything (#7). Exact Pro/Max token weights (cached vs uncached vs output) are NOT published; official docs are silent.
- `/clear` is free and drops all conversation tokens, but also drops the cache; CLAUDE.md, auto memory and unscoped rules reload from disk (#9, #16). A cleared session is resumable, so clearing loses nothing on disk (#17).
- `/compact` (and auto-compaction) is a request that reads the full history: cheap if the cache is warm, most expensive after idle (#9, #10). It is lossy by design (#12); only root CLAUDE.md, plan-mode plan, auto memory, <=5 recent files survive intact (#16). Official docs do not state that compaction saves plan usage versus `/clear`; they say compact at "natural breaks".
- Subagents move bulk reading out of the main context but their requests still count against the same limits (#18); each has a cold cache (#19). Saving is real only when their output volume would otherwise bloat the main context; teams cost ~7x (#19).
- Thinking tokens bill as output and effort/model choice change burn (costs page); `/usage` flags "long context" and "cache misses" when each is >=10% of recent usage (#11).

## Mechanisms to stop update cascades
| Mechanism | Exact config or command | What it prevents | Grade |
|-----------|------------------------|------------------|-------|
| Edit deny rule (path) | `.claude/settings.json`: `{"permissions":{"deny":["Edit(/plan.md)","Edit(/ledger/**)"]}}` (syntax pattern: `Edit(/src/**/*.ts)`; `/` anchors at project root, `//` absolute, `~/` home) | Any built-in tool edit of those paths, plus `sed`/`tee`/`>` writes; not Python/Node subprocess writes | A (path example assembled from documented syntax) |
| Edit ask rule | `{"permissions":{"ask":["Edit(/drafts/**)"]}}` | Silent edits: forces a prompt even if a broader allow rule matches | A |
| Allowlist by default prompting | `{"permissions":{"allow":["Edit(/STATE.md)","Edit(/INBOX.md)"]}}` in default (Manual) mode; docs table says file modification "asks" | Everything not allow-listed prompts (breaks in acceptEdits/bypass modes) | inference from A |
| PreToolUse hook (deny) | settings: `{"hooks":{"PreToolUse":[{"matcher":"Edit\|Write","hooks":[{"type":"command","command":"\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-files.sh"}]}]}}`; script: `FILE_PATH=$(echo "$INPUT" \| jq -r '.tool_input.file_path // empty')` ... `echo "Blocked: ..." >&2; exit 2` | Writes to protected paths in every permission mode; Claude gets the reason | A |
| Hook JSON form | stdout `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"..."}}` (fields at top level are silently ignored) | Same as above, with structured reason | A |
| Hook allowlist (invert docs example) | Same registration; script exits 2 unless `$FILE_PATH` matches STATE.md / INBOX.md | Any write outside an allowlist, incl. new files | inference (docs example is a denylist) |
| Plan mode | `claude --permission-mode plan`, Shift+Tab, or `/plan` | Edits until the plan is approved; plan survives compaction (#16) | A (flags UNVERIFIED) |
| Read-only subagent | frontmatter: `tools: Read, Grep, Glob` / `disallowedTools: Write, Edit` / `permissionMode: plan` / `model: haiku` | Research or mapping subagents writing anywhere; keeps bulk reads out of main context | A |
| `paths:` rule files | `---\npaths:\n  - "drafts/**/*.md"\n---` in `.claude/rules/x.md` | Loads stage instructions only when matching files are touched; does NOT block edits | A |
| OS sandbox | `/en/sandboxing` (enable sandbox) | Subprocess writes that deny rules cannot see | A UNVERIFIED |

## Recommended session pattern
- One stage per session; `/rename <stage>` then `/clear` between stages; return with `/resume <name>` or `claude --continue` - official (costs, sessions).
- Make STATE.md the only file updated on every turn; keep it short; link other files by path and read them on demand, not inline - engineering post (#12 just-in-time retrieval, #13 handoff); "STATE.md" naming is inference.
- Put bootstrap instructions in root CLAUDE.md (<200 lines, survives compaction); put stage-specific procedures in skills or `paths:` rules (loaded on demand, but lost after compaction until re-triggered) - official (#15, #16, costs).
- Route every stray idea/question to an append-only INBOX.md; propagate to plan, question map, ledger, log, drafts only at a gate, in a dedicated "propagate" session - inference (supported by #13 "one feature at a time" and #27, C).
- Enforce the gate with ask/deny Edit rules on gate-updated files, and a hook if an allowlist is needed, because CLAUDE.md instructions are not enforced - official (#15, #20, #22); file-to-rule mapping is inference.
- Use plan mode for any multi-file change; approve a short change list before any edit - official (costs, #23).
- Delegate heavy reading (PDF/literature scans, log review) to read-only subagents on a smaller model; have them write findings to a file and return only the path plus a short summary - official (#18) + engineering post (#14 lightweight references).
- Compact only at natural breaks with `/compact Focus on <X>` or a SessionStart `compact` hook that re-injects STATE.md; avoid resuming a >100k-token session after >1 h; start fresh from files instead - official (costs, #10, hooks-guide).

## Gaps
- No official numeric weights for how cached, uncached and output tokens count toward Pro/Max five-hour or weekly limits; the support articles that might state them (11647753, 14552983, 9797557, 11049741) were seen only as snippets. The one support article read (11145838) has no mechanics.
- No official statement that compaction saves or costs plan usage relative to `/clear` beyond the qualitative claims in #9; no published tokens-per-limit figure for Pro vs Max.
- Whether subagent/teammate tokens weigh the same as main-thread tokens is not stated; docs say only "same usage limits".
- No standards-body or peer-reviewed source found for linked-document-set patterns (SSOT, derived files, append-only logs, dependency direction); only vendor and practitioner blogs (C). Treat the file-dependency design as engineering judgement.
- No built-in "edit only these files" setting exists; allowlisting needs prompts or a hook (script logic is inference).
- Anthropic engineering-post quotes (#12-#14) and the sub-agents page (#18) were returned via a summarising fetch; wording not re-checked against raw text. The ~15x figure (#14) is vendor-measured on research workloads, not a plan-limit measurement.
- Not read in full: best-practices and permission-modes pages (snippets only), sandboxing page, the harness post's full text.

## Implications for the workflow structure
- Split files by write cadence: STATE.md (hot, tiny) and INBOX.md (append-only) versus gate-updated files (plan, question map, ledger, analysis log, drafts) protected by ask/deny Edit rules; the propagate session lifts the gate (e.g. a separate settings.local.json) - inference on #20/#22.
- Declare dependency direction and keep it acyclic: ledger and analysis log as sources, then question map, plan, drafts as derived; each derived file notes what it derives from and when - inference (C support, #26).
- Make each stage end with a STATE.md update and a commit, and each next stage begin from STATE.md alone in a fresh session; this is the "state in files, one task per session" pattern in #12, #13, #25 and avoids both compaction loss and long-context burn.
- Keep status fields in structured form (JSON/YAML for ledger status) with a narrow permitted edit surface, as the harness post does with `passes` - engineering post (#13).
- Move propagation procedures out of CLAUDE.md into an on-demand skill or slash command so the always-loaded context stays under ~200 lines - official (costs "Move instructions from CLAUDE.md to skills").
