# E - Token economy of a multi-stage Claude workflow (cheap readers, strong synthesisers)

Scope: prompt caching (API + Claude Code), context size vs quality, markdown hand-offs, compaction, list prices, effort/task budgets, cost per completed task. Researched 2026-10-04, English only.
Method: 12 searches, 12 fetch attempts; 2 fetches blocked by the egress proxy (arxiv.org, research.trychroma.com), so those facts come from search summaries. Official pages were read 2026-10-04 and are undated; prices are API list prices, standard speed.
Grades: A official docs / peer-reviewed (incl. Anthropic engineering guidance); B systematic independent test; C anecdote, blog or vendor-internal numbers. UNVERIFIED = not read at the primary source.

## Claims

| # | Claim | Source URL or DOI | Source date | Grade |
|---|---|---|---|---|
| 1 | Cache reads bill at 0.1x base input; 0.05x on Opus 5.5 ($0.20/MTok); 0.025x on Fable 5.1 ($0.25/MTok); a hit also refreshes the entry | https://platform.claude.com/docs/en/about-claude/pricing | page, read 2026-10-04 | A |
| 2 | Cache writes cost 1.25x (5-min TTL) or 2x (1-hour TTL) base input; 5-min pays back after one read, 1-hour after two | https://platform.claude.com/docs/en/about-claude/pricing | page, read 2026-10-04 | A |
| 3 | Default TTL is 5 min, refreshed at no cost on each hit (timed from request start); 1-hour TTL via `ttl: "1h"` | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | page, read 2026-10-04 | A |
| 4 | Minimum cacheable prefix: 512 tokens on Fable 5.1 / Opus 5.5 / Sonnet 5.5; 4,096 on Haiku 4.5; shorter prompts are silently not cached | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | page, read 2026-10-04 | A |
| 5 | Cache is an exact-prefix match in order tools, system, messages; a change at one level invalidates it and every later level; max 4 breakpoints, 20-block lookback | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | page, read 2026-10-04 | A |
| 6 | Each model has its own cache: switching model (also opusplan toggles, model-pinned skills, automatic fallback) re-reads the whole history uncached | https://code.claude.com/docs/en/prompt-caching | page, read 2026-10-04 | A |
| 7 | Changing top-level effort invalidates the cache on most models; Opus 5.5 / Sonnet 5.5 / Fable 5.1 keep it via per-message effort (beta `mid-conversation-output-config-2026-07-01`) | https://platform.claude.com/docs/en/build-with-claude/effort ; https://code.claude.com/docs/en/prompt-caching | page, read 2026-10-04 | A |
| 8 | Claude Code caches automatically (system prompt/tools first, then CLAUDE.md/memory, then conversation); main conversation gets 1h TTL only on a subscription within plan usage, else 5 min; subagents, workflows, compaction default to 5 min (settable) | https://code.claude.com/docs/en/prompt-caching | page, read 2026-10-04 | A |
| 9 | A subagent's first request does not read the parent's cache (a fork does); the Claude Code cache is effectively scoped to one machine and directory | https://code.claude.com/docs/en/prompt-caching | page, read 2026-10-04 | A |
| 10 | `/compact` reads the warm prefix cheaply, but after the cache expires the summarisation request reprocesses the full history uncached | https://code.claude.com/docs/en/prompt-caching | page, read 2026-10-04 | A |
| 11 | List prices (in/out per MTok): Fable 5.1 $10/$50, Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 4.5 $1/$5; Batch is 50% off and stacks with caching; 1M context has no surcharge on 4.6+ models | https://platform.claude.com/docs/en/about-claude/pricing | page, read 2026-10-04 | A |
| 12 | The 4.7+ tokenizer yields about 30% more tokens for the same text than Sonnet 4.6 and earlier (incl. Haiku 4.5), so token counts are not comparable across tiers | https://platform.claude.com/docs/en/about-claude/pricing | page, read 2026-10-04 | A |
| 13 | Claude Code averages about $13 per developer per active day ($150-250/month; under $30/day for 90%); subagents and agent teams draw their own tokens (teams about 7x a standard session in plan mode) | https://code.claude.com/docs/en/costs | page, read 2026-10-04 | A |
| 14 | "Lost in the middle": accuracy is highest when relevant text is at the start or end of the context and drops sharply in the middle, even for long-context models | doi:10.1162/tacl_a_00638 (https://aclanthology.org/2024.tacl-1.9/) | TACL 2024 (arXiv 2307.03172, Jul 2023) | A |
| 15 | RULER: near-perfect needle-in-haystack scores but large drops as length grows; of models claiming 32K+ only about half stay satisfactory at 32K | https://arxiv.org/abs/2404.06654 | COLM 2024 | A |
| 16 | NoLiMa: with little lexical overlap GPT-4o falls from 99.3% to 69.7% at 32K; 11 models drop below 50% of their short-context baseline at 32K | https://proceedings.mlr.press/v267/modarressi25a.html | ICML 2025 | A |
| 17 | Chroma "Context Rot": 18 LLMs (incl. Claude 4, GPT-4.1, Gemini 2.5) degrade non-uniformly as input grows even on trivial tasks. Vendor tech report, not peer-reviewed; page blocked, UNVERIFIED (search summary) | https://research.trychroma.com/context-rot | 2025-07-14 | B |
| 18 | LOCA-bench: with task semantics fixed, agent success falls sharply as environment context grows; context editing and tool-use strategies substantially recover it | https://arxiv.org/abs/2602.07962 | 2026-02-08 | B |
| 19 | 2026 blog roundups of MRCR v2 8-needle at 512K-1M are mutually inconsistent (Opus 4.6 76% at 1M vs Opus 4.7 32.2%); no Claude 5-series figures found. UNVERIFIED | https://yage.ai/share/long-context-benchmark-en-20260315.html ; https://llmtest.io/blog/best-llms-1m-context-2026 | 2026 | C |
| 20 | Anthropic: recall accuracy decreases as context tokens increase (attention budget, n^2 pairwise relations); aim for the smallest set of high-signal tokens | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 2025-09-29 | A |
| 21 | Claude Code docs: context "fills up fast, and performance degrades as it fills" (snippet only); API compaction docs: compaction keeps active context small because quality degrades as a conversation grows | https://code.claude.com/docs/en/best-practices ; https://platform.claude.com/docs/en/build-with-claude/compaction | page, read 2026-10-04 | A |
| 22 | Subagents run in their own context window and return only a summary; docs warn that many subagents returning detailed results still consume parent context and each spends its own tokens | https://code.claude.com/docs/en/sub-agents | page, read 2026-10-04 | A |
| 23 | Subagents may use tens of thousands of tokens and return a 1,000-2,000-token distilled summary; Claude Code's own demo: 6,100 tokens read in the subagent, 420 returned | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; https://code.claude.com/docs/en/context-window | 2025-09-29; page 2026-10-04 | A |
| 24 | Multi-agent research (Opus 4 lead, Sonnet 4 subagents) beat single-agent Opus 4 by 90.2% on Anthropic's internal eval; agents use about 4x and multi-agent about 15x chat tokens; token usage explains 80% of variance in a browsing eval | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | C |
| 25 | Same post: subagent outputs can bypass the coordinator (external store) to avoid information loss and copy overhead; lead saves its plan to Memory because context over 200k is truncated; store essential info externally before moving on | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | A |
| 26 | MAST (1,642 traces, 14 failure modes): failures stem largely from specification and inter-agent misalignment (incl. information withholding), not only model limits; venue not verified | https://arxiv.org/abs/2503.13657 | 2025 (v3 Oct 2025) | B |
| 27 | Claude Code compaction: structured summary replaces history; system prompt, root CLAUDE.md, auto memory and plan-mode plan reload from disk; at most 5 recent files re-read (over 5,000 tokens: path only); skill bodies capped 5,000 each / 25,000 total; hook-added context, nested and path-scoped rules are summarised away | https://code.claude.com/docs/en/context-window | page, read 2026-10-04 | A |
| 28 | Official advice: early detailed instructions may be lost, so put persistent rules in CLAUDE.md; use `/compact <focus>`, "Compact instructions" in CLAUDE.md, `/autocompact N`; default auto-compact about 967K tokens on 1M-window models (how-claude-code-works and model-config seen as search snippets only) | https://code.claude.com/docs/en/how-claude-code-works ; https://code.claude.com/docs/en/costs | page, read 2026-10-04 | A |
| 29 | API compaction (beta): server-side summary; modes on demand (`compact-2026-09-04`), at token threshold (`compact-2026-01-12`, default trigger 150K per bundled claude-api skill, UNVERIFIED), own summariser; docs say write your own prompt when the default summary drops something a later turn needs | https://platform.claude.com/docs/en/build-with-claude/compaction | page, read 2026-10-04 | A |
| 30 | Effort (GA, `output_config.effort`): low/medium/high/xhigh/max; default high except Opus 5.5 medium; applies to all output tokens incl. thinking and tool calls; lower effort = fewer, terser tool calls; `low` suits subagents; a behavioural signal, not a hard budget; thinking cannot be disabled on Opus 5.5 / Sonnet 5.5 / Fable and is billed as output | https://platform.claude.com/docs/en/build-with-claude/effort ; https://code.claude.com/docs/en/costs | page, read 2026-10-04 | A |
| 31 | Task budgets are an advisory token ceiling for a whole agentic loop (effort page); beta `task-budgets-2026-03-13`, minimum 20,000, Opus 5.5 / Sonnet 5.5, Fable 5.1 "confirm at launch" come from the bundled claude-api skill only, UNVERIFIED | https://platform.claude.com/docs/en/build-with-claude/effort | page, read 2026-10-04 | A |
| 32 | Claude Code cost controls: subagent `model` and `effort` frontmatter, `--max-budget-usd`, workspace spend limits, `/usage` prompt-cache line (v2.1.251+) | https://code.claude.com/docs/en/costs ; https://code.claude.com/docs/en/sub-agents | page, read 2026-10-04 | A |
| 33 | Lowest-token-price model cost 2.3x more per successful task than the best after retries (720 browser-agent runs, 4 LLMs; worst wasted 22.9% of inference). Vendor blog, models not identified, no Claude-tier data, UNVERIFIED (search summary) | https://fireworks.ai/blog/agent-execution-tax | undated | C |
| 34 | Cost-controlled evaluation: simple baselines matched complex agents' accuracy at up to 50x lower cost, so accuracy-only or price-per-token comparisons mislead | https://arxiv.org/abs/2407.01502 | 2024 | B |
| 35 | "Judge cost per completed task, not per request"; try the strongest model at lower effort before a multi-model cascade (caches are model-scoped, claim 6). Text from the bundled claude-api skill, no public page read, UNVERIFIED | bundled claude-api skill (no URL) | cached 2026-09-25 | C |

## Price table

| Model | Input $/MTok | Output $/MTok | Cache read $/MTok | Cache write $/MTok (5m / 1h) | Source |
|---|---|---|---|---|---|
| Fable 5.1 | 10 | 50 | 0.25 | 12.50 / 20 | https://platform.claude.com/docs/en/about-claude/pricing |
| Opus 5.5 | 4 | 20 | 0.20 | 5 / 8 | same |
| Sonnet 5.5 | 2 | 10 | 0.20 | 2.50 / 4 | same |
| Haiku 4.5 | 1 | 5 | 0.10 | 1.25 / 2 | same |

Batch (50% off, not for interactive loops): Fable 5.1 $5/$25, Opus 5.5 $2/$10, Sonnet 5.5 $1/$5, Haiku 4.5 $0.50/$2.50. Min cacheable prefix 512 / 512 / 512 / 4,096 tokens (claim 4). Context: 1M on 4.6+ models; Haiku 4.5 is 200K per the bundled skill table, not page-verified. Claude Code on a subscription meters plan usage, not dollars.

## Worked cost estimate

Assumptions: (A1) a stream reads about 300k source tokens (4.7+ tokenizer count) and writes a 150-line markdown file, assumed about 5k tokens. (A2) List price, standard speed, 5-min cache writes, turns under 5 min apart. (A3) Design X: one request with all sources, no cache, output 10-40k (5k file + 5-35k thinking). (A4) Design Y: 30 tool-call turns, context grows 5k to 305k, each token cache-written once, prior context read every turn (about 4.5M cache-read tokens), output 20-80k. (A5) Output volumes are one shared guess for all models; real volumes differ (default effort is medium on Opus 5.5, high on Sonnet 5.5 / Fable 5.1), so measure `usage` on a pilot.

| Model | X: one-shot, no cache | Y: agentic loop, cached | Y if caching silently fails (4.8M tokens at full input price) |
|---|---|---|---|
| Sonnet 5.5 | $0.71-$1.01 | $1.86-$2.46 (writes 0.76 + reads 0.90 + output 0.20-0.80) | $9.80-$10.40 |
| Opus 5.5 | $1.42-$2.02 | $2.83-$4.03 (writes 1.53 + reads 0.90 + output 0.40-1.60) | $19.60-$20.80 |
| Fable 5.1 | $3.55-$5.05 | $5.94-$8.94 (writes 3.81 + reads 1.13 + output 1.00-4.00) | $49.00-$52.00 |
| Haiku 4.5 (derived) | not possible (300k exceeds 200K window) | $0.58-$0.88 (two chunks of about 115K old-tokenizer tokens, plus a merge step) | not computed |

- Caching cuts the loop bill about 5-7x (Sonnet 10.1 to 2.2, Opus 20.2 to 3.4, Fable 50.5 to 7.4 at midpoints). Plan on about $2-$4 per stream for Sonnet/Opus and $6-$9 for Fable if cached; roughly 5-7x more if the cache fails (claims 5, 6, 7).
- Cached, Sonnet vs Opus differ by only about 1.5-1.6x, not 2x: cache-read price is identical ($0.20) and reads dominate.
- A strong model reading the 5k-token hand-off file costs about $0.02 (Opus 5.5) or $0.05 (Fable 5.1) uncached, about $0.001 per cached re-read, against $2.83-$8.94 for reading the raw sources.
- Sonnet reader + Opus reading the file is about $1.9-$2.5 per stream: about a third below Opus doing the read itself, 68-72% below Fable.
- Break-even (derived): Sonnet stays cheaper per accepted file only if first-pass acceptance is at least about 0.61-0.66 of Opus's, assuming a failed stream is fully re-run; reviewer rework lowers that threshold.
- Sensitivity: 60 turns roughly doubles read cost; 1-hour writes cost 1.6x the 5-min write (+$0.46 Sonnet, +$0.92 Opus), worth it only with idle gaps over 5 min.

## Context-size vs quality: what the evidence says

- Position matters (claim 14, peer-reviewed): relevant text in the middle is used worst. Inference: put the task question and the key hand-off files at the start or end of the strong model's prompt.
- Length matters on 2024-25 models (claims 15, 16, peer-reviewed): degradation is visible by 32K and steepest when the answer is not a literal match, which is typical of synthesis questions.
- Independent tests agree on direction (claims 17, 18, grade B): 18 models incl. Claude 4 degrade even on simple tasks (Chroma); LOCA-bench (2026) shows agent success falling as context grows, and context management recovering part of it.
- Anthropic treats it as a design constraint (claims 20, 21): "smallest possible set of high-signal tokens"; compaction exists partly because quality degrades as context grows.
- Magnitude for current models is unknown: 2026 MRCR numbers are blog-sourced and conflict (claim 19); no Opus 5.5 / Sonnet 5.5 / Fable 5.1 data found. Treat this as direction, not a threshold; a 1M window at standard price (claim 11) is capacity, not a quality guarantee.
- Cost points the same way: Claude Code re-sends the whole conversation on every request, so long sessions keep costing even at cached rates (https://code.claude.com/docs/en/costs, claim 13).

## Hand-off and compaction rules that follow from the evidence

- Hand off distilled files, not transcripts: Anthropic's pattern is tens of thousands of tokens read, 1,000-2,000 returned (claim 23); a 150-line file is about 5k tokens, so the strong model's read cost is negligible (estimate above).
- Pass file paths, let downstream agents read just-in-time; direct file hand-offs avoid copy overhead and information loss in the coordinator (claim 25).
- Persist state outside the conversation before it grows: the multi-agent post stores plans in memory because context over 200k is truncated (claim 25); structured note-taking is the documented pattern (claim 20).
- Do not rely on conversation history surviving compaction: only CLAUDE.md, memory, plan file, 5 recent files (inline only if 5,000 tokens or less) and capped skill bodies come back; hook context, nested rules and early instructions are summarised (claims 27, 28). Put durable rules in root CLAUDE.md and state in files.
- Compact manually at task boundaries with a focus (`/compact <focus>`, "Compact instructions"), or `/clear` between streams, rather than letting auto-compact fire mid-task (claims 10, 28).
- Give hand-off files a fixed schema (source ID, verbatim number or quote, confidence, explicit "not found"). Inference from claims 26 and 29: default summaries can drop details later turns need, and information withholding is a documented multi-agent failure mode.
- Keep subagent returns short: many detailed returns still fill the parent's context (claim 22).
- Keep each reader's prefix, model and effort fixed for the whole stream; subagent caches start cold and default to 5-min TTL (claims 6-9).

## Gaps

- No measurement found of information loss when sources are compressed to markdown for a downstream model; only design guidance (claim 25) and a failure taxonomy (claim 26).
- No independent long-context results for Opus 5.5, Sonnet 5.5, Fable 5.1 or Haiku 4.5; peer-reviewed papers used older models (claims 14-16); 2026 numbers are blog-sourced.
- Primary text unavailable for Chroma and for the arXiv papers (egress blocked); Liu, RULER, NoLiMa confirmed through ACL Anthology / PMLR / search abstracts, not full text.
- Fetch cap reached: how-claude-code-works, model-config, best-practices and task-budgets pages were seen only as search snippets; compaction thresholds and task-budget details need a direct read.
- No Anthropic first-party data on retry or acceptance rates by tier; cost-per-task evidence is vendor-only (claim 33) or non-Claude (claim 34). No numeric token savings per effort level found.
- Output token volume (thinking, notes) is the largest uncertainty in the estimate; pilot runs with `usage` logging are needed.

## Implications for the workflow

- The saving comes from the strong model never ingesting raw sources: reading a 5k-token file costs cents, reading 300k tokens costs $3-$9 per stream. The Sonnet-vs-Opus choice for the reader moves cost only about 1.5x when cached.
- Run each reader as one continuous session on one model and effort, stable prefix, turns under 5 min apart; check `cache_read_input_tokens` or the `/usage` cache line, since a silent miss multiplies cost about 5-7x.
- Treat the hand-off as the quality risk: use a schema with verbatim quotes and "not found", keep sources reachable so the strong model can re-open a specific one, and spot-check a sample against sources.
- Cap working context per stream (split source sets, `/clear` between streams, state in files, manual `/compact`); the exact safe size for the 5-series models is untested, so test it.
- Decide reader tier on cost per accepted file, not price per token: pilot Sonnet 5.5 vs Haiku 4.5 (and effort low/medium for readers) on a sample, log retries and rework, and use about 0.6-0.65 first-pass acceptance vs Opus as the break-even.
