# Rationale: why paper-workflow/ is built this way

Written 2026-10-04 (Phase 3 of the design job) and updated the same day after the Phase 4 audit (see the last section). This file has one entry per design decision D3–D20 and one per stage gate 00–10. Each entry gives the decision, why it was made, the evidence, and what would change it.

- **Reference format.** `[X#, grade]` means row # of `research/X-*.md`, with the grade that file gives. Grades are never upgraded.
- **Grades.**
  - **A**: official or peer-reviewed source.
  - **A-vendor**: graded A in the research file, but the source is Anthropic's own documentation or an Anthropic engineering post, so it is first-party and neither independent nor peer-reviewed.
  - **B**: a systematic independent test or a preprint audit.
  - **C**: an anecdote, a blog, or a snippet.
  - **UNVERIFIED**: the research file says the primary page or detail was not read.
- **Other labels.** "Judgement call" means there is no evidence. "Inference" means the point is derived from evidence but not stated by it.
- **Decision IDs.** D3–D20 are the design job's decisions; each is stated in full in its entry below. They are not research rows. A research row from file D always carries a grade, for example [D16, B].
- **As built.** Where the implementation differs from the decision as first taken, the entry says so under "As built".

## Decisions

### D3 · Stages 00–10; advisors at 04, 06 and 10
- **Decision:** the stages are:
  - 00 intake;
  - 01 data inventory;
  - 02 pre-question scan;
  - 03 question framing;
  - 04 method justification and plan freeze;
  - 05 analysis;
  - 06 question map;
  - 07 Methods and Results;
  - 08 layered literature extraction;
  - 09 citation verification;
  - 10 Introduction and Discussion, critique and submission audit.

  Advisors see the plan (04), the question map (06) and the full draft (10).
- **Why:** the user's sequence is kept, and three stages are added where the evidence shows a gap: the scan, the plan freeze and the citation gate. Step 1 becomes descriptive. Stage 04 is the only advisor review that can be outcome-independent.
- **Evidence:**
  - [C2, A]: hypotheses taken from a post hoc literature search are a form of HARKing.
  - [C7, A]: only pre-specified analyses can be confirmatory.
  - [C31, A]: outcome-independent decisions reduce bias.
  - [C33, A]: the regression protocol starts from design and questions.
  - [D16, B]: valid links do not mean factual support.
  - [D17, A]: a journal now requires authors to declare that their references support their claims.
- **Would change if:** over the first real papers a stage never catches anything, so it can be merged; or a target journal imposes another order, such as a Registered Report Stage 1 before data access.

### D4 · Plan registration route
- **Decision:**
  - A structured analysis-plan.md, git-tagged `plan-<slug>-v1` before any outcome model runs, is mandatory.
  - Public OSF secondary-data preregistration is recommended whenever the paper will call a result `confirmatory`.
  - Registered Reports are not on the default path.
- **Why:** a preregistration is by definition a public archive. The git tag is an internal timestamp that readers can trust only through the repository. The outcome evidence for preregistration is mixed and comes from psychology, and ecology editors keep it optional, so public registration is recommended rather than forced.
- **Evidence:**
  - Registration and plans: [C14, A]; [C23, A] (templates for existing data); [C24, A] (prior knowledge weakens such plans); [C25, A] (access logging); [C29, A] (no robust anti-HARKing effect); [C30, A] (structured plans work better); [C12, A] (optional in ecology).
  - Registered Reports in ecology: [C15, C UNVERIFIED]; [C16, B UNVERIFIED]; [C17, C UNVERIFIED]; [F32, A, snippet-level].
- **Would change if:** the target journal requires public registration, or accepts Registered Reports on existing data (DCN does, outside ecology: [F33, A]); or ecology-specific outcome evidence appears (C, Gaps).

### D5 · How existing field data earns `confirmatory` (mode `a-data-only`)
- **Decision:** `exploratory` is the default. An analysis is `confirmatory` only with a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data), plus a prior-exposure statement. Every look at the data is a row in data-access.md, created at stage 00. After any outcome-level look recorded there, mode a follows the D16 rule. Held-out splits need advisor or statistician sign-off.
- **Why:** a label cannot make a same-data test confirmatory; prior exposure and access history decide credibility. Spatial and temporal dependence make naive splits misleading (judgement call).
- **Evidence:** [C7, A]; [C8, A] (hindsight bias); [C24, A]; [C25, A]; [C26, A UNVERIFIED detail] (ECAW held-out subset); [F10, A] (disclose prior knowledge; use hold-outs).
- **Would change if:** for modes b–e it already has been, by D16. A validated spatial hold-out protocol for wetland survey data would let the split route run without sign-off.

### D6 · NotebookLM is for orientation only
- **Decision:** NotebookLM and every other AI summary stay an orientation layer for the four literature layers. Each output is listed in the ledger's AI-summary provenance list as `NOT-CITABLE`. Citable evidence comes only from lit-extractor (Sonnet 5.5) extracting full texts into ledger rows.
- **Why:** LLM summaries overgeneralise, and chained summaries can amplify errors. NotebookLM agreed poorly with manual appraisal, and no source shows its citations carry page numbers.
- **Evidence:** [D19, A] (4.85x overgeneralisation); [D21, B] (recursive merging); [D24, B] (13% vs 40% hallucination, errors mostly interpretive); [D25, A] (ICC 0.08–0.27); [D33, A] (inline passage citations); [D36, UNVERIFIED] (no page-number evidence); [D20, B] (abstracts overstate).
- **Would change if:** NotebookLM extraction is shown to agree with manual extraction on ecology papers with page-accurate citations, and its data terms are confirmed acceptable for unpublished work.

### D7 · Haiku 4.5 is not used in the deliverable
- **Decision:** no agent pins Haiku. Mechanical checks run as shell one-liners in hooks and gates, or on Sonnet 5.5 at low effort. For the design job itself, Haiku did the format checks the user asked for.
- **Why:** Haiku has a retirement notice, a small window, a high cache minimum, an old tokenizer and no academic evaluation. The lowest price per token is not the lowest cost per accepted output.
- **Evidence:** [A4, A-vendor] (retirement "not sooner than 2026-10-15", 200K window); [E4, A-vendor] (4,096-token cache minimum); [E12, A-vendor] (token counts not comparable); [A33, C UNVERIFIED] (no academic evaluation); [E34, B] and [E33, C UNVERIFIED] (cost per success).
- **Would change if:** a small successor model without a retirement notice is evaluated on extraction tasks, or a mechanical task appears that the shell cannot do.

### D8 · Higher models read only md, plus a source re-checker
- **Decision:** the Opus agents and the main session read only md hand-offs. For a disputed row, Opus calls source-rechecker (Sonnet 5.5, ≤20k tokens per call), which re-opens one passage and returns the quote and its location.
- **Why:** reading raw sources drives the cost, but hand-offs can lose details, and supplied records get accepted uncritically. Re-opening a single passage restores grounding cheaply.
- **Evidence:** [A25, B] (supplied records accepted; Opus 5, not 5.5); [D21, B] (re-injecting source context mitigates errors); [E23, A-vendor] (1–2k-token subagent summaries); [E25, A-vendor] (outputs stored outside the coordinator); [E26, B] (information withheld between agents). The E worked estimate puts reading a 5k md file at about $0.02 and 300k raw tokens at about $3–9.
- **Would change if:** the first real papers show how often hand-offs drop decisive details (E, Gaps). Frequent loss would mean letting Opus open single passages directly; rare loss would mean fewer re-check calls.

### D9 · Fable 5.1 is for escalation only
- **Decision:** Fable 5.1 runs only after Opus 5.5 at higher effort fails an acceptance check (a methods critique or the final polish), and only once its data-retention terms have been checked for unpublished data.
- **As built:** a routing-table row in CLAUDE.md. The user starts a new session for it, because switching model mid-session re-reads the history uncached [E6, A-vendor].
- **Why:** Anthropic's own selection rule starts with Opus 5.5, and the parity claims are vendor-reported. Fable costs 2.5x Opus per token and uses many tokens, its prose advantage is anecdotal, and its 30-day retention is unconfirmed.
- **Evidence:** [A5, A-vendor]; [A11, A-vendor] ("Fable 5.1 level on most tasks"); [E11, A-vendor] (prices); [A26, B] (token use); [A28, C] (prose edge); [A19, C UNVERIFIED] (retention).
- **Would change if:** independent academic evaluations show Fable clearly ahead on methods critique or synthesis. If its retention terms prove incompatible with unpublished data, Fable is never used.

### D10 · Advisor surface
- **Decision:** at stages 04, 06 and 10, advisors receive DOCX or PDF files exported from the md files. The canonical text stays in git, and Claude Docs is optional.
- **Why:** advisors need a familiar surface. Git keeps the dates that the plan-freeze and provenance claims depend on, while Docs has no version history and offers only Viewer and Editor roles.
- **Evidence:** [B35, A-vendor] (export; beta); [B36, A-vendor] (no version history; Viewer/Editor); [B38, C UNVERIFIED] (comment-only access); [C31, A]; [C37, A] (multiple analysts).
- **Would change if:** Docs gains version history and a comment-only role.

### D11 · Enforcement: hooks for hard rules, CLAUDE.md for the rest
- **Decision:** hard rules are enforced by hooks, not by text in CLAUDE.md. Nothing depends on the Workflow tool; fan-out in stages 08–09 uses subagents.
- **As built:** `.claude/settings.json` and `.claude/hooks/guard.sh` are the approved exception to the fixed file structure; CLAUDE.md §10 shows the same JSON byte for byte and describes guard.sh.
  - guard.sh denies edits to analysis-plan.md once a `plan-<slug>-*` tag exists, and enforces the live-file rule (D15). It is a strong speed bump against accidental cascades, not a lock (D15).
  - `ask` rules cover the plan, CLAUDE.md, stages/, agents/, templates/ and `.claude/**`, so Claude cannot quietly change its own guard.
  - The SessionStart hook (matcher `startup|resume|clear|compact` [B22, A-vendor]) re-injects the newest STATE.md, including after the `/clear` that ends every stage.
  - The Stop hook only reminds; it never blocks. It prints `{"systemMessage": "<reminder>"}` on stdout with exit 0, because plain stdout from a Stop hook is likely not shown outside verbose mode. The `systemMessage` field comes from the hooks reference; it is not in research/B, so check it in a test session.
  - The citation gate is enforced indirectly by guard.sh: `draft/` becomes the live file only when the stage 09 gate passes, so draft writes are denied before verification; the stage 09 and 10 checklists and the drafter and critic rules cover claim-level support.
- **Why:** CLAUDE.md is context, not configuration. PreToolUse hooks block in every permission mode. Blocking Stop hooks are overridden after 8 consecutive blocks and do not fire on interrupts, so keeping Stop as a reminder is a judgement call. Workflows take no input mid-run.
- **Evidence:** [B23, A-vendor]; [B20, A-vendor]; [G22, A-vendor]; [B21, A-vendor]; [B22, A-vendor]; [B16, A-vendor]; [B39, C UNVERIFIED] (workflow model key).
- **Would change if:** guard.sh misfires in practice, in which case the `ask` rules are the fallback; or Claude Code ships a native file allowlist or a reliable blocking gate for drafts.

### D12 · Eight pinned agents
- **Decision:** there are eight agents:
  - on claude-sonnet-5-5: data-reader, analyst, lit-extractor, citation-verifier and source-rechecker;
  - on claude-opus-5-5: methods-advisor, drafter and critic.

  Frontmatter pins the full model ID, `effort:`, the tools and maxTurns; the body repeats the effort and states the budget, inputs, the output schema and a "never do" list. Effort: data-reader medium · analyst medium · lit-extractor medium · citation-verifier low · source-rechecker medium · methods-advisor high · drafter medium · critic high. The orchestrator never passes `model`, and nobody sets CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1.
- **As built:** the earlier "high effort for the Discussion" for the drafter is dropped: one effort per agent file, and a second drafter file would break the fixed structure (judgement call).
- **Why:** a per-invocation model outranks frontmatter, and FORCE=1 puts every agent on one model, which defeats routing. Switching models re-reads the history uncached. A separate critic exists because models fail at self-evaluation.
- **Evidence:** [B2, A-vendor] (`effort` is a frontmatter key); [E32, A-vendor] (subagent `model` and `effort` frontmatter as cost controls); [B3, A-vendor]; [B4, A-vendor]; [B37, A-vendor]; [E6, A-vendor]; [E30, A-vendor] (`low` effort suits subagents; Sonnet 5.5 defaults to high); [A8, A-vendor] (lowering effort cuts cost more reliably than prompt instructions); [A5, A-vendor]; [A24, A].
- **Would change if:** usage data from the first real papers show Opus readers cost less per accepted output (cached Sonnet and Opus readers differ only about 1.5x; E worked estimate); or a test session shows the `effort:` key is ignored, in which case the body line is the only lever left.

### D13 · DOI resolution is a procedure inside citation-verifier
- **Decision:** the Crossref, OpenAlex and PubMed lookups run through Bash or bibliographic MCP tools inside the citation-verifier agent, documented in its body. There is no separate script file.
- **Why:** this keeps the fixed file structure, and deterministic lookups are the recommended control and are cheap. The retraction check runs before a reference row is set to `METADATA-OK`.
- **Evidence:** [D9, A] (Crossref check); [D10, B] (Crossref, OpenAlex and Semantic Scholar); [D12, B] (about $0.04 per paper); [D14, A] (a PubMed-API agent is still only 96.8% metadata-consistent).
- **Would change if:** the same lookup code is retyped paper after paper, in which case a versioned script is better; or the API hosts stay blocked (see Environment limits), leaving MCP tools as the only resolver.

### D14 · Sessions start in paper-workflow/
- **Decision:** cwd is paper-workflow/, or else the repo-root CLAUDE.md @-imports paper-workflow/CLAUDE.md.
- **Why:** CLAUDE.md files at and above cwd load at launch and survive compaction. A nested CLAUDE.md loads only on demand and is summarised away at compaction.
- **Evidence:** [B26, A-vendor]; [B27, A-vendor]; [B32, A-vendor]; [G16, A-vendor]; [B28, A-vendor] (keep it under 200 lines).
- **Would change if:** Claude Code starts re-injecting nested CLAUDE.md files after compaction.

### D15 · One live file per session
- **Decision:** a static `deny` rule protects raw data, and `ask` rules cover the plan, CLAUDE.md, stages/, agents/ and templates/. A PreToolUse guard allows writes only to STATE.md, inbox.md and the `live_file:` path. `mode: propagate` lifts the allowlist but never the plan freeze.
- **As built:** guard.sh is a script file, not the inline command D15 named. Agents write per-paper files only with Write or Edit, never with Bash redirects, so the guard sees every write. `live_file:` may list several paths; the main session switches it only where the stage file says. data-access.md joins STATE.md and inbox.md on the always-writable list. `ask` also covers `.claude/**`.
- **Why:** each edit is a full-context request, so a six-file cascade costs six requests. CLAUDE.md cannot enforce anything. `Edit(path)` rules cover every built-in edit tool, deny beats allow, and hooks block in every mode.
- **Evidence:** [G6, A-vendor]; [G15, A-vendor]; [G20, A-vendor]; [G21, A-vendor] (R and Python writes escape deny rules); [G22, A-vendor]. G, Gaps: there is no built-in "edit only these files" setting, so the allowlist logic is inference.
- **Residual risk:** guard.sh is a strong speed bump against accidental cascades, not a lock: it reads `live_file:` and `mode:` from STATE.md, which Claude can edit, and it does not see Bash writes. Mitigations: guard.sh prints the stderr notice "guard: live_file/mode changed in STATE.md" (allow, not block) on any such edit, and the user reviews `git diff papers/<slug>/STATE.md` at every gate (judgement call). An `ask` rule on every STATE.md was declined because it would prompt on every burst. Subprocess writes are not caught, so scripts write only to results/.
- **Would change if:** Claude Code adds a native write allowlist, or practice shows Claude editing `live_file:` to pass the guard.

### D16 · `confirmatory` in retrospective entries
- **Decision:** `confirmatory` needs a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data). In modes b–e, and in mode a after any outcome-level look recorded in data-access.md, that requires ALL of: the hold-out or new dataset declared in data-access.md at stage 00/01 before any analysis in this workflow; a plan tagged before any analysis of that hold-out; and gate items in S04 and S05 that check the data-access.md date precedes the first results/ commit. Otherwise the label is `exploratory`. It is never earned through a plan registered after analysis. This supersedes D5 for those modes.
- **Why:** retrospective registration cannot show that decisions were prespecified, and late registration is common and rarely disclosed.
- **Evidence:** [F16, A]; [F13, A]; [F10, A]; [F11, A] (a data checkout log); [F12, A]; [F35, A]. F, Gaps: no source accepts registration after analysis as equivalent. The ALL-of rule closes a gap the Phase 4 audit found: the access log was opened only in mode a, so nothing checked the hold-out in b–e.
- **Would change if:** an ecology journal or an integrity body accepts a post-analysis registration with an access log as equivalent. None was found.

### D17 · Inbox propagation
- **Decision:** an idea that touches a file other than the live file becomes one row in inbox.md, which is append-only: `I<nn> | date | text | target file | status`, where status is `OPEN` or `CLOSED -> <file>@<commit>`; an item is closed by appending a row with the same ID. Propagation runs only at gates or when the user types "propagate inbox": the stage file's plan-mode change list, then user approval. It is never automatic, and there is no /propagate command file.
- **Why:** one change at a time keeps long work stable, and plan mode puts approval before edits. A command file would break the fixed structure.
- **Evidence:** [G13, A-vendor] ("one feature at a time"); [G23, A-vendor UNVERIFIED] (plan mode); [G27, C UNVERIFIED] (append-only records); [G6, A-vendor] (each edit round is a full request).
- **Would change if:** OPEN items routinely pile up across stages, in which case propagate at every burst end; or a command file is allowed into the structure.

### D18 · Stage 00 intake and gate statuses
- **Decision:** every paper starts at stage 00.
  - data-reader inventories the artefacts, Opus classifies the entry mode (`a-data-only` … `e-under-revision`), and the user confirms it.
  - Each gate gets `PASSED`, `RETRO-AUDIT`, `NOT-PASSABLE` or `OPEN`, with an evidence pointer.
  - Gate 04 is never `PASSED` retrospectively, and RETRO-AUDIT checklists are never shortened (judgement call).
  - The STATE.md gate table records a `variant` column (`normal` or `retro`).
  - The disclosure queue in STATE.md is one line per item (ID + ≤6 words); the full text is in disclosure.md, created at stage 00 in modes b–e. The disclosure block lives in templates/section-skeleton.md.
  - Mode e re-enters stage 00 through an "existing paper" branch: STATE.md, inbox.md and data-access.md are kept, intake rows are appended, and the tag `submitted-<slug>-v<n>` is the baseline.
- **Mode table (aligned with the stage files):**
  - `a-data-only`: all stages normal; S02 `PASSED` with a queued "post-design" disclosure item (the data predate the scan); S04 `NOT-PASSABLE` for design and sample size, and fully after an outcome-level look.
  - `b-analysis-done`: RETRO-AUDIT S02, S03, S05, S06; NOT-PASSABLE S04; normal S01, S07–S10.
  - `c-half-draft`: as b, plus RETRO-AUDIT S08 (existing citations re-extracted) and S10 (existing Introduction and Discussion).
  - `d-finished-manuscript`: RETRO-AUDIT S01–S03, S05–S08 and S10; NOT-PASSABLE S04 unless a dated prior plan exists; S09 in full.
  - `e-under-revision`: RETRO-AUDIT everything before first submission against the baseline tag; normal S05 for requested analyses, S09 for new or changed citations with a fresh retraction check, S10 critique.
  - S00 and S09 have no RETRO-AUDIT variant.
- **Why:** papers arrive in any state, and claiming that early gates were passed would be exactly the misrepresentation the HARKing literature describes.
- **Evidence:** [F16, A]; [F13, A]; [F2, A]; [F1, A] (transparent post hoc subsection); [F4, A UNVERIFIED] (disclosure statement). No source covers "never shortened"; it is a judgement call.
- **Would change if:** the first mode-d paper has an artefact with no stage to map to (the planned pilot was cancelled, so the mapping is untested). The mapping itself has no source; F built it (F, Entry scenarios).

### D19 · /clear at stage boundaries
- **Decision:**
  - Run one stage per session.
  - At the end of a stage, write STATE.md (overwritten, ≤60 lines), commit, `/rename <slug>-S<NN>`, then `/clear`; the SessionStart hook re-injects STATE.md after `/clear` [B22, A-vendor].
  - Use `/compact Focus on <task>` only mid-stage, in 05 or 08.
  - Work in bursts inside the 1-hour cache window, and after a long break start fresh from STATE.md.
- **Why:** state lives in files, so `/clear` loses nothing and costs nothing. `/compact` is a full-history request and is lossy, and the first turn after the cache expires reprocesses everything.
- **Evidence:** [G9, A-vendor]; [G12, A-vendor]; [G16, A-vendor]; [G17, A-vendor]; [G7, A-vendor]; [G10, A-vendor]; [E10, A-vendor]. Plan-limit weights are unknown: [G3, A-vendor UNVERIFIED]; [G8, A-vendor UNVERIFIED].
- **Would change if:** Anthropic publishes usage weights showing that compaction is cheaper than a fresh session, or the cache lifetime changes.

### D20 · Dependency direction and answers without edits
- **Decision:**
  - Per-paper files update upstream → downstream only, in the order CLAUDE.md §6 lists (intake.md → data-inventory.md → scan → questions → method and plan → analysis → question map → Methods and Results → ledger → draft), and each derived file starts with `derives-from: <file>@<short-commit>`. STATE.md, inbox.md and data-access.md sit outside the chain.
  - An upstream change sets `stale:` entries in STATE.md instead of editing downstream files.
  - A change to the frozen plan is only ever a deviations.md row.
  - Claude answers content questions in chat without editing, and logs any implied change as one inbox line.
- **Why:** this stops one idea from rewriting many files at full-context cost, and keeps provenance checkable in git.
- **Evidence:** [G6, A-vendor]; [F23, A]; [G26, C UNVERIFIED] (single source of truth); [G25, A-vendor UNVERIFIED]. G, Gaps: no standards-body source covers the pattern, so it is engineering judgement.
- **Would change if:** stale flags are ignored in practice, in which case the gate should fail while any `stale:` entry is open.

## Stage gates
Every gate ends with the same item: "STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count" [G12, A-vendor], [G13, A-vendor].

### Gate 00 · Intake
- **Gate:** every artefact is mapped to a stage output or marked out of scope, and the user has confirmed the entry mode. Gates 01–10 each have a status, variant and evidence pointer, and every `NOT-PASSABLE` gate has a disclosure item queued. data-access.md exists (every mode); disclosure.md exists in modes b–e. On mode-e re-entry the gate checks the intake header and the baseline tag, not an empty inbox.
- **Why:** an honest record of what existed before the workflow is what every later label and disclosure rests on.
- **Evidence:** [F16, A]; [F13, A]; [F11, A] (data checkout log); [F4, A UNVERIFIED].
- **Would change if:** dated artefacts are too sparse to classify the paper. Then the stricter mode applies and is disclosed (judgement call).

### Gate 01 · Data inventory
- **Gate:** every variable, n, nesting and dependence, missingness and outliers is listed; a prior-exposure statement is written in STATE.md; SHA256SUMS sits beside data/ and `sha256sum -c SHA256SUMS` passes from papers/<slug>/; data/ is read-only and committed; data-access.md has its first rows; and no outcome–predictor test appears.
- **Why:** an initial analysis that looks at associations biases later inference, and searching many relationships inflates effects.
- **Evidence:** [C34, A]; [C4, A]; [C32, A]; [C33, A]; [C24, A]; [C5, A].
- **Would change if:** the data are new and nobody has seen the outcomes. Then a plan can be frozen before any look at outcomes, which is a stronger route.

### Gate 02 · Pre-question scan
- **Gate:** the strings, at least 2 databases, the date and the hit counts are logged; every listed DOI resolves on entry; abstract-only rows are marked `fulltext: no`; and the scan is dated before the plan tag. In mode a the scan runs prospectively: `PASSED`, plus a queued "post-design" disclosure item, and `after-results` rows are rejected. In modes b–e this gate is `RETRO-AUDIT`, rebuilt from dated artefacts.
- **Why:** presenting literature-sourced hypotheses found after the results as a priori is a named form of HARKing, and reproducible strings reduce bias toward familiar studies. No standard requires the scan itself (inference; C, Gaps).
- **Evidence:** [C2, A]; [C43, A]; [C44, A]; [C45, A]; [D9, A]; [D20, B].
- **Would change if:** evidence shows the scan anchors questions more than it informs them. It cannot be blind, because the data were seen first [C8, A].

### Gate 03 · Question framing
- **Gate:** every candidate is logged (≥15 candidates in mode a only; in RETRO-AUDIT every existing question is dated); each chosen question has an origin tag, a one-line theoretical rationale and the user's selection mark; and the number chosen is within the cap (judgement call).
- **Why:** LLM ideas lack diversity, and models rank their own ideas poorly. Labels do not repair a weak link between theory and hypothesis.
- **Evidence:** [A24, A]; [C13, A]; [C2, A]; [C4, A].
- **Would change if:** Opus 5.x is shown to rank research questions as well as experts. No such test exists (A, Gaps).

### Gate 04 · Method and plan freeze
- **Gate:** method-rationale.md ties each model choice to a named protocol and is committed before the critic runs; the critic's findings are under `## Stage 04` in critique.md; advisor sign-off is recorded; analysis-plan.md is tagged before any outcome model runs; and any `confirmatory` hold-out was declared in data-access.md before the tag. The gate is never `PASSED` retrospectively: in modes b–e it is `NOT-PASSABLE`, with a disclosure item.
- **Why:** only pre-specified analyses can be confirmatory, and agents are weak at scientific judgement. This is the advisors' only outcome-independent review.
- **Evidence:** [C7, A]; [C25, A]; [C30, A]; [C29, A] (against: mixed outcome evidence); [A20, B] (tested on Opus 4.7); [C36, A]; [F16, A]; [G22, A-vendor] (the hook blocks edits after the tag).
- **Would change if:** the target journal requires public registration (add OSF, per D4), or ecology evidence shows that plan freezes make no difference.

### Gate 05 · Analysis
- **Gate:** every analysis-log row (`A<nn>`, the nine stage 05 columns) is labelled and has its results/A<nn>.md; nulls, failed fits and abandoned models are logged; every deviation has a reasoned deviations.md row; scripts write only to results/; and for any `confirmatory` row the data-access.md declaration predates the first results/ commit.
- **Why:** omitting non-significant results is common in ecology, and deviations are fine only when reported. Deny rules miss R and Python writes.
- **Evidence:** [C5, A] (64% omitted non-significant results); [C27, A]; [C37, A]; [A15, A-vendor] (early stops in long runs); [G21, A-vendor].
- **Would change if:** a second analyst re-runs the plan; then their log is added alongside. Many-analyst spread: [F21, A].

### Gate 06 · Question map
- **Gate:** the analysis-to-question table (Part A of question-map.md) has exactly one row per analysis-log row (count check); nulls and unmapped analyses are kept; questions with no analysis are listed; orphan claims are flagged; and the advisor package is exported.
- **Why:** a single narrative axis can silently drop unsupported hypotheses, and unexpected findings tend to be played down.
- **Evidence:** [C2, A] (form c: silently dropped hypotheses); [C12, A]; [C47, C]; [F1, A]; [F31, A]; [C31, A] (advisors at 06 have already seen results).
- **Would change if:** advisors ask for a different package format (judgement call). The completeness rule is not relaxed.

### Gate 07 · Methods and Results
- **Gate:** the text gives the plan date or "no plan", prior exposure, deviations, the model set and selection rule, and n, effect and uncertainty for every mapped analysis. Data and code availability is stated, the AI-use statement is placed, prior exposure is taken from the STATE.md statement, and every number carries `[log: A<nn>]`, which points to results/A<nn>.md.
- **Why:** ecology papers often omit these items, and they are required whatever the entry mode.
- **Evidence:** [C19, A]; [C23, A]; [C27, A]; [C36, A]; [C39, A]; [D28, A] and [D31, A] (both via search extracts); [F23, A].
- **Would change if:** the target journal's checklist adds items. They are added; none of these is removed.

### Gate 08 · Literature extraction
- **Gate:** every R row has a DOI or ID, a layer, a `risk:` flag and the `fulltext:` and `consulted:` fields; every CL row has a verbatim quote and a page or section with full-text extraction behind it (columns as in templates/doi-ledger.md). AI outputs appear only in the provenance list, as `NOT-CITABLE`. The layer syntheses, which live inside doi-ledger.md, cite row IDs only.
- **Why:** summaries overgeneralise and drift when chained, and regional and post-2020 topics have the highest fabrication rates.
- **Evidence:** [D19, A]; [D21, B]; [D25, A]; [D20, B]; [D4, A]; [D9, A]; [D36, UNVERIFIED].
- **Would change if:** a direct test shows page-numbered quotes add nothing (none exists; D, Gaps). The quotes would still be kept for verification.

### Gate 09 · Citation verification
- **Gate:** every R row to be cited reaches `METADATA-OK` (resolved, metadata match, retraction check clean before `METADATA-OK`), which is terminal for R rows; every CL row to be cited reaches `SUPPORT-CHECKED` (the claim has a supporting verbatim passage). The verifier is never the drafter, and a human checks every `risk: high` row, plus a sample of ≥10 rows or 10% of the rest.
- **Why:** real references often carry wrong fields, links do not imply support, evidence on model self-verification of references is thin (one n=40 study) [D18, A], models fail at self-evaluation [A24, A], and retracted papers keep being cited.
- **Evidence:** [D1, A]; [D4, A]; [D16, B]; [D14, A]; [D18, A]; [D17, A]; [F27, A] (16.9% of quotations wrong); [F29, A] (retracted papers still cited).
- **Would change if:** a measured citation error rate near zero for Claude 5.x with retrieval appears; then sampled checks could replace 100% checks. No such measurement exists (A, Gaps).

### Gate 10 · Discussion, critique, submission
- **Gate:** every `[ledger: CL..]` marker names a `SUPPORT-CHECKED` CL row, every number carries `[log: A..]`, and the fresh-context critic's items under `## Stage 10` in critique.md are resolved or logged. The post hoc subsection is present where required, the disclosure matches the target journal's live policy (re-read at this stage), and the advisors have reviewed the draft.
- **Why:** models fail at self-evaluation and accept supplied notes, and our policy evidence is snippet-level only.
- **Evidence:** [A24, A]; [A25, B]; [A17, A-vendor]; [F1, A]; [F4, A UNVERIFIED]; [D27, A], [D28, A], [D30, A] and [D31, A] (via search extracts); [D29, A UNVERIFIED]; [D32, A UNVERIFIED].
- **Would change if:** the live policy differs from the snippets, in which case the live page wins; or Opus fails acceptance, in which case Fable escalation follows (D9).

## Positions the evidence changed
- Labels alone are not enough, because a same-data test stays exploratory [C7, A], [C8, A].
- The timing of the literature review is not the harm; undisclosed post hoc sourcing is [C2, A].
- The DOI ledger becomes a search log plus resolution plus claim support [D1, A], [D4, A], [D16, B].
- Haiku is dropped from the deliverable [A4, A-vendor].
- Step 1 becomes "describe the dataset; no association tests" [C4, A], [C34, A].
- `/clear` plus STATE.md replaces `/compact` at stage boundaries [G9, A-vendor], [G17, A-vendor].
- D5's frozen-plan route is unavailable once outcomes have been seen [F16, A].

## Evidence quality
- **Independent peer-reviewed A (strongest, but read as abstracts or snippets).** Every fetch in C, D and F was blocked, so these rows rest on abstracts, index records or snippets.
  - Methodology: C1–C14, C18–C20, C22–C25, C27–C39 and C42–C46. This covers HARKing forms, labels, secondary-data preregistration, reporting standards, model protocols and search methods. Some journal years were recalled (C, Gaps).
  - Entry modes: F1–F2, F6–F8, F10–F13, F15–F19, F21–F23, F26–F29, F31–F33 and F35–F37. This covers retrospective registration, transparent post hoc reporting, multiverse analysis, many-analysts studies, quotation errors and citation of retracted papers.
  - Citation and summary studies: D1–D9, D13, D14, D17–D19 and D25. They are mostly from medicine or computer science and use older or non-Claude models; the Claude data are free-tier or n = 10 per arm (D, Gaps).
  - Long context (E14–E16) and LLM ideation (A23, A24): older models.
- **Vendor-documentation A (A-vendor).** These rows are authoritative for product mechanics (hooks, permissions, caching, compaction, prices) but not independent:
  - B1–B37; the 19 G rows graded plain A;
  - A1–A11 and A15–A18;
  - E1–E13, E20–E23, E25 and E27–E32.

  The benchmarks in A8, A10 and A11 are vendor-reported, and B's pages were summarised by a small model, so exact numbers need re-checking.
- **Grade B.** A20–A22, A25, A26 and A30 (older models, snippet-level); D10–D12, D15, D16 and D20–D24 (preprints; arXiv blocked); E17, E18, E26 and E34; F20; and C16 (UNVERIFIED).
- **C, UNVERIFIED or snippet-level (check before relying on them):**
  - Publisher and integrity policies: D26–D28, D30 and D31 are A via search extracts; D29 and D32 are A UNVERIFIED.
  - NotebookLM: inline passage citations [D33, A, date UNVERIFIED]; page numbers [D36, UNVERIFIED]; limits [D34, C UNVERIFIED]; the rename [D35, A UNVERIFIED]. Data and training terms were not captured.
  - Fable 5.1 retention terms: [A19, C UNVERIFIED], from the bundled claude-api skill only.
  - Registered Reports in ecology: [C15, C UNVERIFIED]; [C16, B UNVERIFIED]; [C17, C UNVERIFIED]; [F32, A] (snippet); [F34, A UNVERIFIED].
  - Haiku 4.5 academic performance: [A33, C UNVERIFIED].
  - Other:
    - plan-limit mechanics: G3–G5 and G8, all A UNVERIFIED; plan mode: G23, A UNVERIFIED; G25, A UNVERIFIED;
    - B38–B40, C UNVERIFIED; task budgets: E31, with the detail UNVERIFIED;
    - E19, E24, E33 and E35, all C;
    - A12–A14, A27–A29, A31 and A32, all C;
    - G26 and G27, C UNVERIFIED;
    - C18, C21, C26, C40 and C41, A with UNVERIFIED detail; C47, C.

## Environment limits during research
- The research environment's egress proxy refused connections to www.elsevier.com, www.springer.com, publicationethics.org, arxiv.org, cos.io, icmje.org, api.crossref.org, api.openalex.org and doi.org. The research files also report blocks on www-cdn.anthropic.com (A), research.trychroma.com (E), and the PMC, BMJ, OSF, PCI, Wiley, T&F, BES, BMC and Google help pages (C, D, F).
- As a result, publisher policies, COPE, ICMJE and COS guidance, arXiv preprints and the Fable 5.1 system card are known only from snippets or abstracts. No DOI in research/ was resolved live; DOIs were copied from index records, and a few were recalled (C, Gaps; F5).
- For use: stage 09 needs api.crossref.org, api.openalex.org and doi.org to be reachable, or a bibliographic MCP tool such as PubMed. The fix is the environment's Network access setting; this was still open when the workflow was built.

## Sources
Research files (claim rows, grades as given):
- research/A-model-capabilities.md: 33 claims (17 A, 6 B, 10 C).
- research/B-claude-code-features.md: 40 (37 A, 3 C UNVERIFIED).
- research/C-methodology-standards.md: 47 (43 A, 5 of them with UNVERIFIED detail; 1 B UNVERIFIED; 3 C, 2 of them UNVERIFIED).
- research/D-ai-academic-writing.md: 36 (24 A, 3 of them UNVERIFIED; 10 B; 1 C UNVERIFIED; 1 ungraded UNVERIFIED).
- research/E-token-economy.md: 35 (27 A, 4 B, 4 C).
- research/F-entry-points.md: 37 (36 A, 9 of them UNVERIFIED; 1 B).
- research/G-context-cascade.md: 27 (25 A, 6 of them UNVERIFIED; 2 C UNVERIFIED).

The 255 rows were synthesised and decided during the design job; this file carries the decisions that ship.

Most load-bearing primary sources (copied from the research tables):
1. Kerr, Pers Soc Psychol Rev, 10.1207/s15327957pspr0203_4 (1998). HARKing defined [C1, F2].
2. Rubin, Rev Gen Psychol, 10.1037/gpr0000128 (2017). Three forms of HARKing [C2].
3. Murphy & Aguinis, J Bus Psychol, 10.1007/s10869-017-9524-7 (2019). Question trolling [C4].
4. Fraser et al., PLOS ONE, 10.1371/journal.pone.0200303 (2018). QRP survey of ecologists [C5, F31].
5. Wagenmakers et al., Perspect Psychol Sci, 10.1177/1745691612463078 (2012). The confirmatory label [C7].
6. Nosek et al., PNAS, 10.1073/pnas.1708274114 (2018). Prediction vs postdiction [C8, F7].
7. Shaw et al., Ecol Evol, 10.1002/ece3.2291 (2016). Editors keep preregistration optional [C12].
8. Baldwin et al., Eur J Epidemiol, 10.1007/s10654-021-00839-0 (2022+). Prior knowledge of the data [C24, F12].
9. Scott et al. (Scott & Kline in F11), AMPPS, 10.1177/2515245918815849 (2019). Data checkout log [C25, F11].
10. Lakens, Collabra Psychol, 10.1525/collabra.117094 (2024). Reporting deviations [C27, F23].
11. van den Akker et al., Behav Res Methods, 10.3758/s13428-023-02277-0 (2023). Matched preregistration study [C29].
12. Zuur & Ieno, Methods Ecol Evol, 10.1111/2041-210x.12577 (2016). The 10-step protocol [C33].
13. Heinze et al., BMC Med Res Methodol, 10.1186/s12874-024-02294-3 (2024). Initial data analysis [C34].
14. Harrison et al., PeerJ, 10.7717/peerj.4794 (2018). Mixed-model best practice [C36].
15. Parker, Nakagawa & Gurevitch, Ecol Lett, 10.1111/ele.12610 (2016). Reporting gaps in ecology [C19].
16. Hollenbeck & Wright, J Manage, doi:10.1177/0149206316679487 (2017). Transparent post hoc reporting [F1].
17. Borges, Syst Rev, doi:10.1186/s13643-026-03278-8 (2026). Retrospective registration [F16].
18. Walters & Wilder, Sci Rep, doi:10.1038/s41598-023-41032-5 (2023). Fabricated citations [D1].
19. Linardon et al., JMIR Ment Health, doi:10.2196/80371 (2025). Error rates by topic visibility [D4].
20. Kim et al., Publications, doi:10.3390/publications13040049 (2025). Invalid DOIs on regional topics [D9].
21. Onweller et al., arXiv, doi:10.48550/arxiv.2605.06635 (2026, B). Links do not imply support [D16].
22. Peters et al., R Soc Open Sci, doi:10.1098/rsos.241776 (2025). Summaries overgeneralise [D19].
23. Brown et al., Addiction editorial, doi:10.1111/add.70379 (2026). Reference declaration [D17].
24. Anthropic docs: code.claude.com/docs/en/hooks, /hooks-guide, /memory, /permissions, /context-window and /costs. Enforcement, compaction and usage [B20–B23, B32, G6, G9, G15–G22].
25. Anthropic docs: platform.claude.com/docs/en/models/overview and /about-claude/pricing. Model selection, retirement and prices [A4, A5, E11].

## Phase 4 audit
An independent audit on 2026-10-04 read every file in paper-workflow/ against the research rows and ran guard.sh on 13 simulated inputs. It found 0 BLOCKER, 16 MAJOR and 32 MINOR items, and 13 bad references among the 76 it checked. Every MAJOR and MINOR item was fixed in the same pass. Three alternative fixes were declined: a second drafter file, an `ask` rule on every STATE.md, and a separate disclosure-queue.md.
- The bad references were fixed as follows:
  - D18 inverted (now: evidence on self-verification is thin, n=40);
  - A5 → E6 for the uncached re-read;
  - C25 and C7 → C2 for origin tags;
  - B20 → B23 for "CLAUDE.md is not enforced";
  - F23 dropped from "never shortened" (judgement call);
  - D9 → "the recommended control";
  - A31, F4 and F5 now carry UNVERIFIED wherever they are cited.
- The 16 MAJOR findings, and how each was fixed:
  1. The data-reader schema differed from stage 01. The agent now copies the six-section schema and writes SHA256SUMS and the first data-access.md rows.
  2. The analyst wrote results/, but results/ was not live. results/ is now in the S05 live list.
  3. The analyst could never edit analysis-plan.md, yet stage 04 asks it to fill the plan. It is now barred only once a `plan-<slug>-*` tag exists.
  4. The analysis-log columns disagreed across files. Stage 05's nine columns and `A<nn>` IDs are now canonical.
  5. Ledger fields that the gates check were missing. There is now one schema in templates/doi-ledger.md: Q, R and CL rows with layer, risk and consulted.
  6. Drafts cited R rows, which never reach `SUPPORT-CHECKED`. Drafts now cite CL rows, and R rows stop at `METADATA-OK`.
  7. The result pointer was spelled four ways. It is now `[log: A<nn>]` everywhere.
  8. The critic at stage 04 could not write its output, or could overwrite the rationale. method-rationale.md is now committed first, and the critic appends `## Stage 04` to critique.md. Stage 07 no longer routes to the critic.
  9. Effort was set only in prose. Each agent's frontmatter now has an `effort:` key.
  10. The SessionStart matcher missed `clear`. It is now `startup|resume|clear|compact`.
  11. Claude could lift the guard by editing STATE.md. Changes: an `Edit(/.claude/**)` ask rule; a stderr notice when an edit changes live_file or mode; the guard is described as "speed bump, not a lock"; the user reviews the STATE.md diff at every gate.
  12. Nothing checked the `confirmatory` hold-out in modes b–e. The ALL-of rule now applies, with a data-access.md declaration and gate items at S04 and S05.
  13. Mode-e re-entry overwrote STATE.md and inbox.md. Stage 00 now has an "existing paper" branch, with a `submitted-<slug>-v<n>` baseline tag.
  14. The gate commands assumed different working directories. They now run from paper-workflow/ with `<tag>:./papers/<slug>/` paths, and checksums go in a SHA256SUMS file.
  15. A first-time user could not start from CLAUDE.md alone. CLAUDE.md §1 now has a "First session" block of 14 lines or fewer.
  16. D18 was cited as "self-checks are weak". It is reworded in CLAUDE.md and citation-verifier.md.
- New per-paper files from the audit:
  - data-access.md: append-only and always writable; created at stage 00 in every mode.
  - SHA256SUMS: beside data/, written at stage 01.
  - disclosure.md: created at stage 00 in modes b–e; it holds the full disclosure-queue text.
