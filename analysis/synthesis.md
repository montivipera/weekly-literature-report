# Synthesis: evidence-based redesign of the data-first paper workflow (Phase 2, 2026-10-04)

## 1. Scope and evidence base
- Sources are only the five Phase 1 files: A (models, 33 rows), B (Claude Code features, 40), C (methodology, 47), D (AI-assisted writing, 36), E (token economy, 35). That is 191 claims: 148 A, 21 B, 21 C and 1 ungraded UNVERIFIED [D36]. Grades are taken as given and none is upgraded. Citations are [file letter + row]; "(X, Gaps)" or "(X, worked estimate)" points to a section of a file.
- Many A rows come from search snippets or summarised fetches, not full primary pages. This covers every journal and guideline claim in C, every publisher policy and NotebookLM fact in D, the Fable 5.1 system card, known only from snippets (A), and B's undated docs, which a small model summarised.
- Main gaps: (1) no independent academic-task test of Fable 5.1, Opus 5.5 or Sonnet 5.5, so every 5.x number is vendor-reported; (2) no measured Claude 5.x citation-fabrication rate (A, Gaps); (3) no ecology-specific evidence that preregistration changes outcomes, because all outcome evidence is from psychology [C28–C30]; (4) no study of summary-of-summary drift or of page-numbered quotes as a control [D36]; (5) no measure of what is lost in md hand-offs (E, Gaps); (6) no academic evaluation of Haiku 4.5 [A33].

## 2. Step-by-step recommendations
Blocks follow the proposed order. NEW blocks sit where they belong in that order, and every current step keeps its place.

### Step 1: Provide data, ask "what can we produce from this?"
- **Current:** the user hands over the dataset and Claude proposes what it could yield.
- **For (keep):** data-first exploration is legitimate and necessary, and applied ecology needs both modes [C9, C10, C11]. Zuur & Ieno's protocol also starts with data organisation, sampling layout and dependence [C33].
- **Against:** an open "what can we produce" invites question trolling. Simulations show that searching many relationships for notable results gives substantial upward bias [C4]. Initial data analysis that looks at outcome–predictor associations biases later inference [C34]. In a survey, 51% of ecologists said they had presented an unexpected finding as hypothesised [C5]; the true frequency is probably lower [C6].
- **Verdict:** keep data first, but change the first question to "describe what this dataset is". That means variables, sampling design, n, nesting and dependence, missingness and outliers [C32, C33], with no outcome–predictor tests. Add a prior-exposure statement: what the user has already seen or analysed in these data [C23–C25].
- **Model:** a Sonnet 5.5 subagent at medium effort reads the raw data and returns data-inventory.md. Under the constraint, Opus and Fable never read the raw files.
- **Risk → Control:** question trolling and early peeking. The inventory gate rejects any association test, and the prior-exposure statement goes into STATE.md.
- **Token cost:** low. This is one reader pass over tabular files, usually far smaller than a 300k-token literature stream (E, worked estimate). The data size is a judgement call.

### NEW 1b: Pre-question literature scan (logged)
- **Current:** none. Literature enters only after the results (step 6).
- **For:** presenting hypotheses from a post hoc literature search as a priori is a named HARKing form [C2]. Reproducible search strings reduce bias towards familiar studies and take under 2 h to build with litsearchr [C43].
- **Against:** no standard requires a pre-question scan in data-first work (C, Gaps). The analyst has already seen the data, so the scan cannot be blind [C8]. A scan is only as good as its databases and strings, and Google Scholar is unsuitable as the main system [C44].
- **Verdict:** add the scan, keep it short, and log it: strings, at least 2 databases, date, hit counts, and about 10–20 key papers with DOIs resolved on entry [C42, C43, C45]. The 10–20 figure is a judgement call. The scan feeds question framing and the plan freeze, and its timestamp must come before the freeze.
- **Model:** a Sonnet 5.5 subagent at medium effort retrieves papers with database tools, never from memory [A21, D5, D13], and writes scan-notes.md in the ledger schema. Opus 5.5 reads only that file.
- **Risk → Control:** fabricated references are caught by resolving every DOI on entry [D9, D10]. The evidence suggests abstracts overstate results [D20], so rows marked "abstract only" cannot be cited until full-text extraction in step 6.
- **Token cost:** medium. One reader stream costs about $2–4 cached on Sonnet per 300k source tokens (E, worked estimate), and a short scan should stay well under that.

### Step 2: Questions the data allows → research questions in context
- **Current:** questions are framed from what the data can support.
- **For (keep):** stating relevant questions against the data is step one of the Zuur & Ieno protocol [C33]. The user's sense of ecological relevance is the scarce input.
- **Against:** LLM-generated ideas are rated more novel but less feasible than expert ideas, lack diversity, and the model ranks its own ideas poorly [A24]. Splitting exploratory from confirmatory work does not repair a weak link from theory to hypothesis [C13].
- **Verdict:** keep the step. Claude proposes many candidate questions from data-inventory.md and scan-notes.md, and the user ranks them. Each chosen question gets an origin tag (literature, data or advisor) and a one-line theoretical rationale [C2, C13]. All candidates are logged.
- **Model:** Opus 5.5 at high effort. This is open-ended judgement, and Opus 5.5 is Anthropic's suggested starting model [A5]. The model never ranks its own output [A24].
- **Risk → Control:** fishing across many questions [C4] is limited by a cap on chosen questions plus a log of every candidate in questions.md. The cap is a judgement call.
- **Token cost:** low. Opus reads hand-off files of about 5k tokens, roughly $0.02 per read (E, worked estimate). Most of the cost is high-effort thinking, billed as output at $20/MTok [E30, E11].

### NEW 2b: Method justification for a non-statistician
- **Current:** none. Methods "emerge" in step 3.
- **For:** named, accessible protocols exist: the Zuur & Ieno 10 steps [C33], Zuur et al. data exploration [C32], Bolker and Harrison for GLMMs [C35, C36], and Santon's low-code R template [C38]. Multimodel inference is hard without formal training [C36]. The evidence suggests agents are weak on scientific judgement and miss subtle details (AARRI-Bench, Opus 4.7) [A20].
- **Against:** no retrieved source explicitly says "consult a statistician" (C, Method choice). A model-written justification reads as authoritative. The evidence also suggests models accept supplied records uncritically [A25].
- **Verdict:** add method-rationale.md. For each research question it lists the candidate models and why (structure, dependence, response distribution), the assumptions to check, the candidate set and selection rule, and the sensitivity checks [C36, C37]. Every choice is tied to a cited protocol. An advisor or statistician reviews it before the freeze; this is a recommendation, not a retrieved requirement [C37].
- **Model:** Opus 5.5 at high effort writes the draft. A separate critic subagent (Opus 5.5 high, fresh context) attacks it. Fable 5.1 is used only if Opus fails the acceptance check [A5].
- **Risk → Control:** a plausible but wrong method is caught by advisor sign-off at the gate. Multiverse or second-analyst sensitivity checks are listed in the plan [C37].
- **Token cost:** low–medium. Inputs are md only, plus two high-effort Opus passes. Fable escalation costs 2.5x Opus per token [E11].

### NEW 2c: Time-stamped analysis plan (plan freeze) before outcome inspection
- **Current:** none. Hypotheses are formed and tested on the same data in one move.
- **For:** only analyses specified before seeing the data count as confirmatory [C7], and postdiction must be kept apart from prediction [C8]. Templates exist for preregistering analyses of existing data [C23]. Logging data access makes confirmatory secondary analysis credible [C25]. Structured plans limit researcher degrees of freedom better than unstructured ones [C30].
- **Against:** the analyst's prior knowledge weakens plans for existing data [C24]. Matched psychology studies found no robust evidence that preregistration prevents p-hacking or HARKing [C29]. Ecology editors keep preregistration optional [C12], and there is no ecology outcome evidence (C, Gaps).
- **Verdict:** add the freeze. analysis-plan.md is a structured plan covering hypotheses with origin tags, variables, exclusions, models, decision rules, deviation policy and the prior-exposure statement. It is committed and git-tagged before any outcome model runs. Public OSF registration is optional (Decision 1). Later deviations are reported and justified [C27].
- **Model:** Sonnet 5.5 at low effort fills the template from questions.md and method-rationale.md, and the user commits it (judgement call, no direct evidence).
- **Risk → Control:** silent edits after results are blocked by a PreToolUse hook that denies edits to the frozen plan, because CLAUDE.md is not enforced [B20, B23]. The git tag is the timestamp, and deviations go to deviations.md.
- **Token cost:** low. Filling a template from md files.

### Step 3: Hypotheses tested; Methods & Results emerge
- **Current:** hypotheses are tested on the data and the methods and results emerge from that.
- **For (keep):** running the analyses in Claude Code. Exploration after the freeze is legitimate if it is labelled [C9, C10].
- **Against:** this is where HARKing happens. Same-data tests have no evidential weight as confirmation [C7]. When hypotheses "emerge", post hoc ones are reported as a priori [C1, C2]. In the survey, 64% of ecologists had left out non-significant results [C5].
- **Verdict:** split the step. 3a confirmatory runs exactly the frozen plan. 3b exploratory runs further analyses, each labelled. Every analysis goes into analysis-log.md, including nulls and abandoned models. Report sensitivity to preprocessing choices [C37] and give n, effect and uncertainty so the study can be reused [C19, C39].
- **Model:** Sonnet 5.5 at medium effort writes and runs the R scripts. Its coding strength is vendor or secondary data on coding tasks only (grade C) [A14]. Opus 5.5 at medium effort reviews the log and deviations as md.
- **Risk → Control:** undisclosed exploration is caught at the gate: every log row is labelled confirmatory (with a plan ID) or exploratory. Early stops in long runs [A15] are handled by a checklist, a completion criterion and a cap of 2–3 automatic continuations.
- **Token cost:** medium. An agentic loop with code runs costs about $2–4 per cached stream on Sonnet or Opus, and 5–7x more if caching silently fails (E, worked estimate) [E5].

### Step 4: Findings on a single axis; analysis-to-question map for advisors
- **Current:** findings are placed on one axis, each analysis is mapped to the question it answers, and the package goes to the advisors.
- **For (keep):** this is the user's strongest practice. Ecology editors say separating pre-planned from post hoc analyses greatly helps readers [C12], and complete reporting of analyses is a core standard [C19, C37].
- **Against:** a single narrative axis can quietly drop unsupported hypotheses, which is HARKing form (c) [C2]. The evidence suggests unexpected findings tend to be played down [C47]. Advisors also see results before they see any plan, so their review is not outcome-independent [C31].
- **Verdict:** keep the axis and the package. Add columns for plan ID or exploratory label, the result (nulls included), a deviation reference, and "not mapped" rows. Advisors see the plan earlier, at stage 4.
- **Model:** Opus 5.5 at medium effort, on md only. This is synthesis and judgement [A5].
- **Risk → Control:** dropped nulls are caught at the gate: the question map must have one row for every analysis-log row.
- **Token cost:** low. The step reads md only.

### Step 5: Methods & Results written on that axis
- **Current:** Methods and Results are drafted along the axis.
- **For (keep):** writing Methods and Results before Introduction and Discussion keeps the text tied to what was actually done.
- **Against:** ecology papers often leave out sample sizes, effect directions and uncertainty [C19]. Publishers require AI-use disclosure, often in Methods [D28, D30, D31].
- **Verdict:** keep the step. Methods must state:
  - that the dataset pre-existed and what the analyst had already seen;
  - the plan-freeze date and any deviations;
  - the candidate model set and the selection criterion [C23, C27, C36];
  - data and code availability [C18, C20].
  The AI-use statement is drafted now, in the place the target journal requires [D27–D32].
- **Model:** Opus 5.5 at medium effort, set explicitly because medium is also its default [A2, A5, A8].
- **Risk → Control:** numbers drifting from the outputs. Every number in Results must trace to a script output file (judgement call).
- **Token cost:** low–medium. Inputs are md, and output tokens at $20/MTok dominate [E11].

### Step 6: Layered literature review (global / regional / national / local) via NotebookLM into md
- **Current:** after the results, a NotebookLM skill summarises each layer into md files that Claude then builds on.
- **For (keep):** the four layers have no evidence against them (judgement call). NotebookLM answers carry inline citations to passages in the uploaded sources [D33]. The evidence suggests it hallucinates less than general chatbots, 13% vs 40% [D24].
- **Against:**
  - LLM summaries overgeneralise (4.85x more often than human summaries) even when asked to be accurate [D19].
  - The evidence suggests recursive summary merging amplifies hallucination [D21].
  - NotebookLM agreed poorly with manual structured appraisal [D25], and the evidence suggests abstracts overstate results [D20].
  - Regional, niche and post-2020 topics, which are exactly the national and local layers, show the highest fabrication and invalid-DOI rates [D4, D9].
- **Verdict:** keep the layers and the post-results timing for Introduction and Discussion. Change the unit from prose summary to extraction: each paper becomes ledger rows with claim, verbatim quote, page or section, full-text yes/no, DOI, and "consulted after results" (D, Implications). NotebookLM output becomes orientation only and is marked not citable (Decision 3).
- **Model:** Sonnet 5.5 subagents at medium effort read the full texts, one stream per layer, each under about 300k tokens. Opus 5.5 reads only the ledger and the layer syntheses built from ledger rows.
- **Risk → Control:** summary-of-summary drift is controlled by a rule that a summary may cite only ledger row IDs, never another summary. Abstract-only reading is controlled by the full-text flag.
- **Token cost:** high. This is the only step that reads many raw sources: about $2–4 per cached Sonnet stream across four layers, and 5–7x more on a cache miss (E, worked estimate).

### NEW 6b: Citation-verification gate before drafting
- **Current:** none.
- **For:**
  - Existence checks against Crossref or OpenAlex are the proven control [D9]; B-grade audits point the same way [D10, D12].
  - Real references still carry metadata errors in 24–45% of cases [D1, D4].
  - The evidence suggests deep-research agents produce working links but only 39–77% factual support [D16]; even a PubMed-API agent reached only 96.8% claim–metadata consistency [D14].
  - The journal Addiction now requires authors to declare that references exist, are accurate and support the claims [D17].
- **Against:** no direct test shows that page-numbered quotes reduce fabrication [D36]. Evidence that a model can verify its own references is weak [D18], and the evidence suggests retrieval-grounded tools still err [D15].
- **Verdict:** add a hard gate. Every ledger reference must resolve (DOI, resolver, date) and match its metadata. Every claim it supports needs a checked verbatim passage. Human checks go first to post-2020, regional and niche references [D4, D9].
- **Model:** deterministic lookups by script or API, plus Sonnet 5.5 at medium effort for claim–passage matching in a context separate from the drafter. The user spot-checks. No Haiku (Decision 4).
- **Risk → Control:** fabricated or wrong-field references are stopped because a Stop-hook gate blocks drafting until every ledger row is verified [B21].
- **Token cost:** low–medium. The evidence suggests an automated reference audit costs about $0.04 per paper [D12]. Claim checks re-read only the cited passages.

### Step 7: Per-section skeleton → text
- **Current:** a skeleton for each section, then text written to it.
- **For (keep):** written checklists and completion criteria are the documented mitigation for early stops and shortcuts in long tasks [A15, A16].
- **Against:** models fail at self-evaluation [A24], and the evidence suggests they accept supplied notes uncritically [A25]. Fable's prose advantage is anecdotal [A28]. Fable's reported 30-day data retention is unverified but matters for unpublished work [A19].
- **Verdict:** keep the step, with three additions:
  - each skeleton bullet carries ledger row IDs, and the draft may cite only verified rows;
  - an adversarial critique pass, in a fresh context and required to find errors, runs before the advisors see the draft;
  - a submission audit re-reads the live publisher policy and completes the disclosure [D27–D32].
- **Model:** Opus 5.5 at medium effort for Introduction and Discussion, raised to high for Discussion synthesis. The critic is Opus 5.5 high in a new subagent. Fable 5.1 does polish only if Opus fails acceptance, and only after its retention terms are checked [A5, A19].
- **Risk → Control:** uncited or unverified claims are caught at the gate: every citation in the draft must map to a verified ledger row.
- **Token cost:** medium. Several Opus drafting and revision rounds. Fable polish costs 2.5x Opus per token [E11].

## 3. Verdict on the three proposed fixes
### Fix 1: Exploratory/confirmatory labels
- **For:** the labelling norm is established [C7], ecology editors say the split helps readers [C12], legitimate exploration sits on a continuum with confirmation [C9, C10], and the core harm of HARKing is non-disclosure [C2, C3].
- **Against:** a label cannot make a same-data test confirmatory [C7, C8]. Labels assigned after seeing results are exposed to hindsight bias [C8]. Preregistration outcome evidence is mixed and comes only from psychology [C29, C30]. Labels do not repair weak theory [C13].
- **Verdict: adopt, but it is necessary, not sufficient.** To work it must include:
  - the default "exploratory" for every same-data analysis;
  - "confirmatory" only with a plan ID from a frozen, time-stamped plan, or with held-out or new data [C25, C26];
  - an origin tag on every hypothesis [C2];
  - a prior-exposure statement [C24];
  - a deviation log [C27];
  - every analysis run is reported, including nulls [C5, C19].

### Fix 2: Short literature scan before fixing questions
- **For:** presenting hypotheses from a post hoc literature search as a priori is a named HARKing form [C2]. Question trolling inflates bias [C4]. Reproducible search strings reduce bias towards familiar studies [C43].
- **Against:** no standard requires the scan (C, Gaps). The scan is not blind, because the data have been seen [C8]. Its quality depends on databases and strings [C44], and the evidence suggests abstract-level reading overstates results [D20].
- **Verdict: adopt.** It must include a search log (strings, at least 2 databases, date, hits), DOIs resolved on entry, rows flagged abstract-only or full-text, and a timestamp before the plan freeze [C42, C43, C45]. It adds to step 6; it does not replace it.

### Fix 3: DOI ledger with page-numbered quotes
- **For:** selective citation is among the most commonly reported questionable research practices [C46]. Existence and metadata checks are the proven control [D9, D10, D12], and journals are starting to require authors to declare that references are accurate and supportive [D17].
- **Against:**
  - No methodology source endorses a ledger of cited DOIs; it records what was cited, not what was searched or when (C, Verdict 3).
  - The evidence suggests existence checks are not enough: 64% of real AI-cited papers had at least one wrong field [A22, UNVERIFIED attribution], 24–45% metadata errors [D1, D4], and only 39–77% claim support [D16].
  - No evidence shows that page-numbered quotes themselves cut fabrication, and NotebookLM page numbers are unverified [D36].
- **Verdict: keep, and extend it to three linked parts:**
  - (a) a search-and-consultation log with "consulted before/after results" [C45, C46];
  - (b) reference rows: DOI resolved via Crossref or OpenAlex, metadata match, date and checker [D9, D10];
  - (c) claim-support rows: verbatim quote, page or section, full-text flag, and a verifier who is not the drafting model [D14–D18].
  - It also records the provenance of every AI summary, marked "not citable" [D19, D24], and the disclosure fields [D27–D32].

## 4. Proposed stage list for Phase 3
| # | Stage (stages/ file) | Goal | Main inputs | Main outputs | Model | Gate (pass/fail) | Who sees it |
|---|---|---|---|---|---|---|---|
| 1 | Data inventory | Describe data, design, dependence; record prior exposure | raw data, field protocol | data-inventory.md; prior-exposure entry in STATE.md | Sonnet 5.5 medium | Pass if every variable, n, nesting and missingness is listed with a prior-exposure statement and no outcome–predictor test appears | user |
| 2 | Pre-question scan (NEW) | Short logged scan to place the data in context | data-inventory.md, keywords | search-log.md; scan-notes.md (ledger rows) | Sonnet 5.5 medium; Opus 5.5 reads notes | Pass if strings, ≥2 databases, date and hit counts are logged and every listed DOI resolves | user |
| 3 | Question framing | Chosen RQs with origin tag and rationale | data-inventory.md, scan-notes.md | questions.md (all candidates plus chosen) | Opus 5.5 high; user ranks | Pass if each chosen RQ has an origin tag, a rationale and the user's selection mark | user |
| 4 | Method justification + plan freeze (NEW) | Justify methods; freeze a structured plan before outcomes | questions.md, data-inventory.md | method-rationale.md; analysis-plan.md (git tag) | Opus 5.5 high + Opus critic; Sonnet 5.5 low fills template | Pass if the plan is git-tagged before any outcome model runs and advisor sign-off is recorded in STATE.md | **advisors (entry 1)** |
| 5 | Analysis | Run the plan (confirmatory), then labelled exploration | analysis-plan.md, data | scripts; results/*.md; analysis-log.md; deviations.md | Sonnet 5.5 medium; Opus 5.5 medium reviews md | Pass if every analysis-log row is labelled confirmatory (with plan ID) or exploratory and every deviation is justified | user |
| 6 | Question map | Single axis; analysis-to-question table | analysis-log.md, results md, questions.md | question-map.md; analysis-to-question table | Opus 5.5 medium | Pass if the table has one row for each analysis-log row, nulls and unmapped analyses included | **advisors (entry 2)** |
| 7 | Methods & Results draft | Write M&R on the axis | question-map.md, plan, deviations.md, skeleton | methods.md; results.md; AI-use note | Opus 5.5 medium | Pass if plan date, prior exposure, deviations, model set and n/effect/uncertainty for every mapped analysis are present | user |
| 8 | Layered literature extraction | Global/regional/national/local evidence as ledger rows | search-log.md, full-text PDFs, NotebookLM notes (orientation only) | doi-ledger.md rows; layer syntheses citing row IDs | Sonnet 5.5 medium readers; Opus 5.5 reads ledger | Pass if every row has a DOI or ID, verbatim quote, page or section, full-text flag and before/after-results field | user |
| 9 | Citation verification (NEW) | Resolve, match metadata, check claim support | doi-ledger.md, skeleton claims | verified ledger with a status per row | script + Sonnet 5.5 medium (never the drafter) | Pass only if 100% of to-be-cited rows resolve, match metadata and have a checked supporting passage | user |
| 10 | Intro/Discussion, critique, submission audit | Draft to skeleton; adversarial critique; disclosure | verified ledger, question map, M&R | full draft; critique.md; disclosure statement | Opus 5.5 medium/high; critic Opus 5.5 high; Fable 5.1 escalation only | Pass if every citation maps to a verified row, critique items are resolved or logged, and the disclosure matches the live journal policy | **advisors (entry 3)** |

Advisors enter at stages 4 (plan, before outcomes), 6 (the current question-map package) and 10 (full draft). The first entry is new and is the only one that can be outcome-independent [C31].

## 5. Model routing matrix
| Task type | Recommended model and effort | Cost tier | Evidence |
|---|---|---|---|
| Read raw sources (full-text PDFs, data files) | Sonnet 5.5, medium | medium | Cached Sonnet and Opus readers differ only about 1.5x; Opus reading a 5k md hand-off costs about $0.02 (E, worked estimate); Phase 3 constraint |
| Extract claims to schema (quote, page, full-text flag) | Sonnet 5.5, low–medium | low | `low` suits subagents [E30]; verbatim schema because summaries overgeneralise [D19] |
| Write and run analysis code | Sonnet 5.5, medium | medium | Coding benchmarks only, vendor or secondary (grade C) [A14]; judgement call for R/ecology |
| Verify citations: existence and metadata | script/API lookup + Sonnet 5.5, low | low | Crossref/OpenAlex lookup is the proven control [D9]; B-grade audits agree [D10, D12] |
| Verify claim support | Sonnet 5.5 medium, separate context; human for high-risk refs | low–medium | Links ≠ support [D14, D16]; self-check weak [D18]; regional/post-2020 risk [D4, D9] |
| Propose questions and hypotheses | Opus 5.5 high; user ranks | low | Start with Opus [A5]; LLM ideas lack diversity and self-ranking fails [A24] |
| Propose and justify methods | Opus 5.5 high; Fable 5.1 high only on failed acceptance | low–medium | [A5]; evidence suggests weak agent scientific judgement [A20]; second analyst [C37] |
| Write prose (M&R, Intro, Discussion) | Opus 5.5 medium (high for Discussion) | medium | Opus 5.5 at medium matches Opus 5 at high on knowledge work (vendor) [A8]; Fable prose edge anecdotal [A28] |
| Adversarial critique | Opus 5.5 high, fresh subagent | low–medium | Self-evaluation fails [A24]; supplied records accepted [A25]; avoid "treat earlier answers as done" [A17] |
| Decide at gates | User decides; Opus 5.5 medium pre-checks the checklist via Stop hook | low | Hooks enforce, CLAUDE.md does not [B21, B23]; judgement call on who pre-checks |
| Format and check files (schema, line counts, reference style) | scripts or Sonnet 5.5 low; Haiku 4.5 not pinned | low | Haiku retirement not before 2026-10-15, no academic eval, 4,096-token cache minimum [A4, A33, E4] |
| Orchestrate the main session, update STATE.md | Opus 5.5 medium, fixed for the whole session | low–medium | Switching model re-reads history uncached [E6]; Opus is the recommended default [A5] |
| Hardest cross-paper reasoning after Opus fails | Fable 5.1 high | high | [A1, A5]; Opus 5.5 at Fable level on most tasks (vendor) [A11]; heavy token use [A26] |

Suggested agents/ set (judgement call): data-reader, lit-reader, extractor, citation-verifier, source-rechecker (Sonnet); methods-advisor, drafter, critic (Opus).

## 6. Risk → control map
| Risk | Control | Where it lives | Evidence grade |
|---|---|---|---|
| HARKing | Default exploratory; plan freeze; origin tags; complete analysis log | stages/04 and 05 gates; PreToolUse hook on analysis-plan.md | A [C2, C7, C25]; prevention effect unproven [C29] |
| Question trolling | Inventory bans association tests; cap and log candidate RQs | stages/01 and 03 gates | A [C4, C34] |
| Late literature review | Logged pre-question scan; "consulted before/after results" field | stages/02; templates/doi-ledger | A for the HARKing form [C2]; scan timing inferred (C, Gaps) |
| Citation fabrication | Retrieval only, never memory; DOI resolution; metadata match | stages/09 gate; agents/citation-verifier | A and B [D1–D12, A21] |
| Summary-of-summary drift | Verbatim-quote ledger rows; summaries cite row IDs only; NotebookLM not citable | stages/08; templates/doi-ledger | A and B by analogy [D19, D21]; no direct study (D, Gaps) |
| Abstract-only reading | Full-text flag; claim support only from full text | templates/doi-ledger; stages/09 gate | B and C [D20, A31] |
| Context rot / compaction loss | md hand-offs, STATE.md, SessionStart compact hook, manual /compact at boundaries | CLAUDE.md; STATE.md; .claude/settings.json | A [E14–E16, B22, B32]; 5.x magnitude unknown [E19] |
| Accepting supplied records (sycophancy-adjacent) | Hand-offs carry quote and source path; fresh-context critic; Sonnet source re-check | agents/critic; agents/source-rechecker | B [A25]; 5.x unmeasured [A32] |
| Early stop in long runs | Checklist and completion criterion; 2–3 continuation cap; Stop hook | stages/*; .claude/settings.json | A [A15, B21] |
| Publisher policy breach | Disclosure fields in ledger; live policy re-read; no AI-generated figures | templates/doi-ledger; stages/10 gate | A but snippet-based, wording UNVERIFIED [D27–D32] |
| Unpublished data exposure | Check Fable retention and NotebookLM terms before uploading | CLAUDE.md rule; docs/rationale.md | C, UNVERIFIED [A19]; NotebookLM terms not captured (D) |
| Over-reliance on Haiku for judgement | No Haiku in agents/; judgement tasks pinned to Opus | agents/ frontmatter | A for limits and retirement [A4]; C for missing eval [A33] |
| Model pin silently overridden | Full model IDs; CLAUDE.md forbids passing `model`; do not use FORCE=1 | agents/; CLAUDE.md | A [B3, B4, B37] |
| Cache misses | Fixed model, effort and prefix per stream; turns under 5 min apart; check /usage cache line | agents/; CLAUDE.md | A [E5–E9, E32] |

## 7. Token economy design
- **Hand-off format:** each stage writes one md file of at most about 150 lines (about 5k tokens) with a fixed schema: source ID, verbatim quote or number, location, confidence and an explicit "not found". A subagent returns at most about 2k tokens to its parent; the detail stays in the file [E22, E23, B6]. The evidence suggests default summaries and multi-agent hand-offs drop details [E26, E29].
- **Paths, not content:** agents pass file paths, and downstream agents read just in time, so outputs bypass the coordinator [E25]. Under the Phase 3 constraint, Opus and Fable read only these files. A strong model reading a 5k file costs cents; reading 300k raw tokens costs $3–9 (E, worked estimate).
- **Cache-friendly ordering:** stable content goes first (CLAUDE.md, stage file, templates) and the variable task last. Never edit CLAUDE.md or switch model mid-stream, because the cache is exact-prefix and model-scoped [E5, E6, E8]. Use per-message effort on 5.x instead of top-level changes [E7]. Put the task question and key file at the start or end, not the middle [E14].
- **What survives compaction:** root CLAUDE.md, unscoped rules, auto memory, the plan, at most 5 recent files and skill bodies capped at 5k tokens each [B32, E27]. A nested CLAUDE.md loads only on demand and is summarised away [B26, B32]. So sessions must start with the working directory set to paper-workflow/, or the root CLAUDE.md must `@`-import it [B27].
- **SessionStart compact hook:** re-inject STATE.md after every compaction [B22]. B's snippet is below; Phase 3 changes the path to the workflow's STATE.md:
```json
"SessionStart":[{"matcher":"compact","hooks":[{"type":"command","command":"cat research/STATE.md"}]}]
```
- **STATE.md discipline:** update STATE.md at every gate with the current stage, gate status, frozen-file tags, open items and the last decision. Run `/compact focus on <stage>` at stage boundaries or `/clear` between streams, and do not let auto-compact fire mid-gate [B31, E10, E28]. Keep CLAUDE.md under 200 lines with a "Compact Instructions" section [B28, B31], and put key rules at the top of each skill [B11].
- **Subagent budgets:** each agents/ file fixes `model` (full ID such as `claude-opus-5-5`), `effort`, `maxTurns` and `tools` [B2, E32]. Starting budgets (judgement call, calibrate on a pilot (E, Gaps)): readers take at most about 300k source tokens per stream; extraction files are at most 150 lines; drafters and critics read at most about 50k md tokens. Use `--max-budget-usd` per session [E32]. Task budgets are beta and UNVERIFIED [E31].
- **Pinning without breaking routing:** a per-invocation `model` outranks frontmatter [B4], so CLAUDE.md forbids the orchestrator from passing one. A PreToolUse deny hook could enforce this (inference from [B4, B20], untested). Do not set `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`: it forces every subagent onto one model [B4].
- **When not to use the cheapest model:** the evidence suggests judging cost per accepted output, not price per token [E34, E35]. Cached Sonnet and Opus readers differ only about 1.5x, and Sonnet beats Opus only above about 0.61–0.66 relative first-pass acceptance (E, worked estimate). The evidence suggests a low-price model can cost 2.3x more per success after retries [E33]. Haiku cannot hold a 300k stream, caches only prefixes of at least 4,096 tokens, and its token counts are not comparable [E4, E12]. Never use the cheapest model for judgement.
- **Cache-miss watch:** a silent miss multiplies loop cost 5–7x (E, worked estimate). Check the `/usage` cache line [E32]. Subagent caches start cold with a 5-min TTL, so keep reader turns under 5 min apart and use the 1-hour TTL only when there are idle gaps [E2, E8, E9]. On a subscription, cost appears as plan usage, but the ratios still hold (E, price table).

## 8. Changes vs the current workflow
| Current | Proposed | Why |
|---|---|---|
| "What can we produce from this?" | Descriptive data inventory plus prior-exposure statement; no association tests | Question trolling and initial-analysis bias [C4, C34] |
| (none) | Logged pre-question literature scan (NEW) | Post hoc literature-sourced hypotheses are a HARKing form [C2]; reproducible strings [C43] |
| Questions from data | Opus proposes many, user ranks; origin tag plus rationale | LLM self-ranking fails [A24]; weak theory link [C13] |
| Methods "emerge" | method-rationale.md against named protocols, reviewed by an advisor (NEW) | Accessible protocols [C33, C36]; evidence suggests weak agent judgement [A20] |
| (none) | Git-tagged, hook-protected plan freeze before outcomes (NEW) | Confirmatory only if pre-specified [C7]; access logging [C25] |
| Hypotheses tested, results emerge | Confirmatory vs exploratory split; complete analysis log | 64% omitted nulls [C5]; report all analyses [C37] |
| Question map to advisors | Kept, plus labels, nulls and unmapped rows; advisors also see the plan | Separating planned from post hoc analyses aids readers [C12] |
| M&R on the axis | Kept, plus prior exposure, deviations, model set, AI disclosure | [C19, C27, D28, D31] |
| NotebookLM summaries per layer | Full-text extraction into ledger rows; NotebookLM orientation only | LLM summaries overgeneralise [D19]; NotebookLM errors interpretive (B) [D24] |
| DOI ledger | Search log + resolution + claim-support ledger | Existence ≠ accuracy or support [D1, D4, D16] |
| (none) | Citation-verification gate before drafting (NEW) | [D9, D12, D14, D17] |
| Skeleton → text | Skeleton bullets carry ledger IDs; critic pass; submission audit | [A24, A25, D27–D32] |
| Single session, mixed models | Opus orchestrator; pinned Sonnet readers; md hand-offs; STATE.md | Cache and context economics [E6, E23, E14, B32] |

## 9. Decisions for Checkpoint 1
1. **Plan registration route.** Options: (a) internal git-tagged structured plan only; (b) (a) plus public OSF secondary-data preregistration whenever the paper will say "confirmatory"; (c) a Registered Report. **Recommend (b), with (a) always mandatory.** Evidence: a preregistration is by definition a public archive [C14], and templates exist for existing data [C23]. Prior knowledge weakens such plans [C24] and data-access logging helps [C25]. Preregistration had no robust anti-HARKing effect in matched studies [C29], and ecology editors keep it optional [C12]. Registered Report availability in ecology is UNVERIFIED [C15–C17].
2. **How existing field data earns "confirmatory".** Options: (a) everything exploratory; (b) analyses in a plan frozen before outcome inspection, with a prior-exposure statement; (c) a held-out split. **Recommend (b), with (c) only where n allows (judgement call), otherwise (a).** Evidence: [C7, C24, C25]. The held-out (ECAW) detail is UNVERIFIED [C26].
3. **Does NotebookLM stay in the loop?** Options: (a) as now, summaries feed drafting; (b) orientation and navigation only, outputs not citable, with citable evidence only from ledger extraction; (c) drop it. **Recommend (b).** Evidence: the evidence suggests it hallucinates less than chatbots [D24] and it cites passages [D33]. But it scored poorly on structured appraisal [D25], LLM summaries overgeneralise [D19], page numbers are unverified [D36], and its data and training terms were not captured (D).
4. **Is Haiku 4.5 used at all?** Options: (a) no; (b) mechanical checks only, with a Sonnet fallback; (c) as a cheap reader. **Recommend (a): scripts plus Sonnet 5.5 at low effort.** Evidence: retirement is due "not sooner than 2026-10-15" [A4]. There is no academic evaluation [A33], the 200K window cannot hold a 300k stream (E, worked estimate), and the 4,096-token cache minimum and old tokenizer apply [E4, E12].
5. **How strict is "higher models read only md"?** Options: (a) strict; (b) strict, plus a Sonnet source-recheck subagent that Opus can call on disputed rows; (c) Opus may re-open single passages. **Recommend (b).** Evidence: the evidence suggests supplied records are accepted uncritically [A25] and that re-injecting source context reduces hallucination [D21]. File E advises keeping sources reachable (E, Implications), while raw reading is the cost driver (E, worked estimate).
6. **Fable 5.1's role.** Options: none; escalation only (methods critique, final polish) after Opus fails acceptance; a fixed critic. **Recommend escalation only, after confirming its data-retention terms.** Evidence: [A5] and vendor parity claims [A11]. The retention requirement is UNVERIFIED [A19], token use is heavy [A26], and the prose edge is anecdotal [A28].
7. **Advisor entry points and surface.** Options: (a) as now, question map only; (b) add plan review (stage 4) and final-draft review (stage 10). For the surface, exported Word or PDF vs Claude Docs. **Recommend (b) with exported files and the canonical text in git; Claude Docs optional.** Evidence: outcome-independent decisions [C31] and multiple analysts [C37]. Docs needs Editor access and has no version history [B35, B36].
8. **Gate enforcement strength.** Options: (a) CLAUDE.md rules only; (b) hooks for the two hard gates (a PreToolUse plan freeze and a Stop-hook citation gate) plus CLAUDE.md for the rest; (c) one Workflow per stage. **Recommend (b), using Workflows only for fan-out inside stages 8 and 9.** Evidence: CLAUDE.md is not enforced [B23], and hooks can block [B20, B21]. Workflows take no mid-run input [B16], and the workflow model key is UNVERIFIED [B39]. Mods are new and unsandboxed, so use them for display only [B24].

## 10. Where the evidence changed a recommendation
- **Labels (the user's fix 1) are not enough.** A same-data test stays exploratory whatever its label [C7, C8]. My first instinct was to require public preregistration; I softened that to a mandatory internal freeze with optional OSF, because matched studies showed no robust anti-HARKing effect [C29] and ecology editors keep it optional [C12].
- **The timing of "literature after results" is not itself the harm.** The harm is presenting hypotheses retrieved post hoc as a priori [C2]. So step 6 keeps its place for Introduction and Discussion; the change is a small logged scan up front and a "consulted after results" field, not moving the review.
- **The DOI ledger as the user framed it checks the easy part.** Real references carry wrong fields in 24–45% of cases [D1, D4], and the evidence suggests support is only 39–77% [D16]. The methodology sources ask for the search record, not the list of what was cited (C, Verdict 3), so the ledger becomes three parts.
- **My first instinct was Haiku for bulk reading; the evidence reverses it.** Haiku has a retirement notice and a 200K window [A4], and a 4,096-token cache minimum [E4]. Cached Sonnet and Opus readers are only about 1.5x apart (E, worked estimate). Sonnet 5.5 is therefore the floor for anything that reads sources.
- **Two structural fixes from B would backfire if applied naively.** `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` puts every agent on one model and defeats routing [B4]. A paper-workflow/CLAUDE.md loaded as a nested file is summarised away at compaction [B26, B32]. Hence the explicit rules on the working directory and pinning in Section 7.

## 11. Entry modes and cascade control (added after user feedback)
- **Scope:** this section answers R1 (enter at any paper state without pretending early gates were passed) and R2 (stop one typed prompt from rewriting many files and burning plan usage).
- **Sources:** it adds two Phase 1 files to the §1 base. F (entry points) has 37 claims: 27 A, 9 A UNVERIFIED and 1 B; every F fetch was blocked, so all of them rest on abstracts or snippets. G (context and cascades) has 27 claims: 19 A, 6 A UNVERIFIED and 2 C UNVERIFIED; A in G means first-party vendor docs, not peer review.

### 11.1 Entry modes
- **Stage 0 "Intake" (NEW, first stage of every paper):** a Sonnet 5.5 reader lists what already exists: data, scripts, outputs, drafts, reviews, and dated artefacts such as commits, proposals and emails. Opus 5.5 classifies the entry as mode (a)–(e) below, and the user confirms (judgement call). intake.md maps each artefact to the stage output it stands in for: as-run scripts → analysis-log.md, for example, or draft Methods → methods.md. F built this stage mapping; no source prescribes it (F, Entry scenarios).
- **Gate statuses:** each gate S1–S10 gets one of four statuses. PASSED: the gate was passed, or a dated artefact shows the work predates outcome inspection [F11]. RETRO-AUDIT: the full checklist was run as an audit on existing material and is recorded as audited, not prospective [F16]. NOT PASSABLE: the gate's disclosure item is queued in STATE.md. OPEN: the gate is still ahead and runs normally (my addition, needed for mode (a)).
- **Stage 0 gate:** pass if every existing artefact is mapped to a stage output or marked out of scope, every gate S1–S10 has a status with its evidence, and every NOT PASSABLE gate has its disclosure item queued in STATE.md.
- **The plan freeze (S4) can never be passed retrospectively.** Retrospective registration cannot show that decisions were prespecified [F16]. Late registration is common and rarely disclosed [F13]. No source accepts registration after analysis as equivalent to preregistration (F, Gaps).
- **What the paper must then say:** every analysis is exploratory by default [F5 UNVERIFIED, F6, F26]. It carries an extended disclosure statement [F4 UNVERIFIED]. It reports every analysis run, in order, with a transparent post hoc subsection in Discussion [F1, F31]. It says "not preregistered" and never uses "registered" in a way that implies equivalence (F, scenario d). Its claims are worded as preliminary [F5 UNVERIFIED, F37].
- **Robustness bundle (its rule is written before it runs):** a multiverse or specification curve [F17–F19], a second analyst working from the raw data [F21, F22], sensitivity reporting [F36], and new data or a never-explored hold-out [F10–F12, F35]. The evidence suggests specification sets are rarely justified or jointly tested [F20]. Multiverse and second-analyst checks expose fragility but do not restore confirmatory status; only new data or a never-explored hold-out can (F, Robustness).
- **Gates that run in full at every entry (none depends on when results were seen):** citation verification of every cited source, with a retraction check (S8–S9) [F27–F29, F30 UNVERIFIED]; question-map completeness, meaning one row per as-run analysis with nulls and orphan claims flagged (S6) [F1, F31]; and the M&R reporting items, meaning the plan date or "no plan", prior exposure, deviations, the model set, and n, effect and uncertainty (S7) [F10, F11, F23]. A reconstructed stage gets RETRO-AUDIT status, but its checklist is never shortened.

| Entry | Stages run normally | Gates as RETRO-AUDIT | NOT PASSABLE | Disclosure in the paper | Evidence |
|---|---|---|---|---|---|
| (a) Data only | S1 (+ data-access log), S3, S4 if no outcome-level look, S5–S10 | S2, logged as post-design | S4 design and sample size (the freeze covers analysis only) | Collection and freeze dates; any prior looks; when the inclusion rules were fixed | F4 UNVERIFIED, F7, F8, F9 UNVERIFIED, F10–F12 |
| (b) Analysis done | S1; S7 from as-run scripts; S8, S9, S10 | S2 (flag literature HARKing), S3, S5 (as-run log), S6 (built backwards; all rows post hoc) | S4; any confirmatory label on these data | No plan; all exploratory; every analysis and its order; how the question was chosen; post hoc subsection; robustness | F1, F2, F5 UNVERIFIED, F6, F13, F14 UNVERIFIED, F15–F19, F31 |
| (c) Half draft | As (b); S8–S9 re-extract the draft's citations from full text | As (b), plus an Introduction audit (hypotheses first dated after a result are post hoc; orphan claims flagged) | As (b) | As (b), plus hypotheses written or changed after results (from version history) | F1, F2, F23, F27, F28 |
| (d) Finished manuscript | S9 on every in-text claim; S10 submission audit; S8 for sources never read in full | S1–S7 as provenance reconstruction from dated artefacts; each result tagged prior-plan or post hoc | S4, unless a dated prior plan exists | Provenance statement; extended disclosure; a label per result; "not preregistered"; robustness section | F4 UNVERIFIED, F13, F16–F19, F23, F24–F25 UNVERIFIED, F27–F29, F30 UNVERIFIED, F37 |
| (e) Under revision | S9 on new or changed citations plus a retraction check; S10 critique; S5 for requested analyses | Everything before first submission; the as-submitted version is archived as the dated baseline | As at first submission | Reviewer-requested analyses labelled; changes between versions logged like deviations; the response letter matches the labels | F23, F24 UNVERIFIED, F29, F33 |

### 11.2 Cascade control
- **Why cascades are expensive:** each file edit is a tool round, and each tool round is a new request that re-sends the whole conversation [G6]. One idea that touches six files therefore costs at least six full-context requests (inference from G6).
- **(a) Dependency direction (inference).** Per-paper files are updated upstream → downstream only, in this order: intake.md → data-inventory.md → search-log.md, scan-notes.md → questions.md → method-rationale.md → analysis-plan.md (frozen) → analysis-log.md, deviations.md, results/*.md → question-map.md → methods.md, results.md → doi-ledger.md → draft, critique.md, disclosure.
  - Only its own stage writes each file, and each file carries a header "derives from: <file>@<commit>". An upstream change marks downstream files STALE in STATE.md; it does not edit them. A change to the frozen plan is only ever a deviations.md row [F23]. STATE.md and inbox.md sit outside the chain. Support is weak: the evidence suggests one authoritative file per fact [G26, C UNVERIFIED], and no standards body covers the pattern (G, Gaps).
- **(b) One live file per session, chosen by the current stage.** STATE.md records the live file. Claude may write only that file, STATE.md and inbox.md. CLAUDE.md states the rule, but CLAUDE.md is context, not enforcement [G15] (official).
  - **Static deny rule on frozen files** (official syntax, with G's example paths, which Phase 3 replaces): `{"permissions":{"deny":["Edit(/plan.md)","Edit(/ledger/**)"]}}`. An `ask` rule forces a prompt instead: `{"permissions":{"ask":["Edit(/drafts/**)"]}}`.
  - **Live-file allowlist via a PreToolUse hook**, which blocks in every permission mode [G22] (official mechanism): `{"hooks":{"PreToolUse":[{"matcher":"Edit|Write","hooks":[{"type":"command","command":"\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/protect-files.sh"}]}]}}`. The script exits 2 unless the path is the live file, STATE.md or inbox.md. It should read the live file from a copy the user sets and Claude cannot edit, because Claude can write STATE.md (inference: the docs example is a denylist, and no built-in "edit only these files" setting exists; G, Gaps).
  - **Caveats (official):**
    - Write path rules as `Edit(path)`, which covers all built-in edit tools. A `Write(path)` rule is accepted but never consulted [G20].
    - Deny beats ask, which beats allow, and an allow rule cannot carve an exception from a deny [G20]. So propagation lifts protection through the hook, not through an allow rule.
    - Deny rules catch `sed`, `tee` and `>` but not R or Python subprocess writes [G21], so analysis scripts write only to results/ (sandbox enforcement is UNVERIFIED; G, Mechanisms).
- **(c) Append-only inbox.md (inference).** Support is the engineering post's "one feature at a time" [G13], and the evidence suggests append-only records [G27, C UNVERIFIED]. Any idea or question typed mid-stage that would change a file other than the live file becomes one dated inbox line: ID, text, target file, status OPEN. Earlier lines are never edited, and git diff checks this at the gate.
  - **Propagation** happens only in an explicit "propagate" step at the next gate: (1) Claude reads the OPEN items and proposes a change list in plan mode [G23 UNVERIFIED]; (2) the user approves it; (3) edits go upstream first, and downstream files are marked STALE; (4) each item closes with a pointer. The procedure sits in each stage file's gate section, not in CLAUDE.md, following the official costs advice (G, Implications).
- **(d) STATE.md is the only file every session updates (engineering post [G12, G13]; the name is inference).** It is overwritten, not appended, and capped at about 60 lines (judgement call); history lives in git. Gate statuses sit in a small YAML block where only status values change, as the harness post does with `passes` [G13]. Supersedes §7 "update STATE.md at every gate": STATE.md is also written at the end of each work burst, before `/clear`.
- **(e) Answers without edits (inference, consistent with G25 UNVERIFIED).** Claude answers in chat any question about content, methods, definitions or status, any "what if" scenario and any request for suggested wording, using files in context or read on demand. If an answer implies a change outside the live file, Claude appends one inbox line and stops. Claude edits the live file only when the user asks for an edit.

### 11.3 Compaction vs usage limits
- **Arithmetic (official unless marked):**
  - **Requests and cache:** every request re-sends the full history, and every tool round is another request, so "a one-line question in a session that has been open all day still draws usage for the whole conversation" [G6]. Cumulative cost grows faster than linearly in turns (inference from G6). Cached re-reads are billed at the cached rate, so they are cheaper but not free [G6]; that they "count less" against limits is UNVERIFIED [G8]. The cache lasts 1 hour on a subscription (5 minutes once usage credits are being drawn), and the first turn after a longer break reprocesses everything [G7].
  - **`/clear` and `/compact`:** `/clear` costs nothing. It reloads CLAUDE.md, auto memory and unscoped rules, and the old conversation stays resumable [G9, G16, G17]. `/compact` is itself a request that reads the whole history: a fraction of full cost with a warm cache, a full reprocess with a cold one [G9]. It is also lossy [G12, G16].
  - **Subagents:** subagent requests count against the same limits [G18]. Each subagent starts its own cold cache with a 5-minute TTL, and agent teams use about 7x the tokens [G19].
- **Where the official docs are silent (G, Gaps):** they publish no Pro/Max weights for cached, uncached and output tokens against the five-hour or weekly limits, and no tokens-per-limit figure for Pro vs Max. They do not say whether compaction saves usage compared with `/clear`, or whether subagent tokens weigh the same as main-thread tokens. The five-hour plus weekly structure [G3] and the 2026-05-06 doubling [G5] are UNVERIFIED.
- **Resolving R2 (inference from G9, G12, G16, G17):** the state lives in files, so `/clear` loses nothing that matters and costs nothing. `/compact` loses information and has not been shown to save usage. Clearing therefore replaces compacting as the default.
- **Session pattern:**
  1. Run one stage per session, starting from CLAUDE.md, the stage file and STATE.md alone (official; engineering post [G12, G13]).
  2. At the end of a stage, write STATE.md, commit, run `/rename <stage>`, then run `/clear` [G9, G17] (official). Supersedes §7 and the §6 compaction row: use `/clear`, not `/compact`, at stage boundaries.
  3. Use `/compact Focus on <task>` only mid-stage, when a stage (typically S5 or S8) cannot fit in one session. Run it at a natural break while the cache is warm [G9] (official; the choice of stages is inference).
  4. Work in focused bursts inside the 1-hour cache window. After a longer break, do not resume a session larger than 100k tokens; start fresh from STATE.md instead [G7, G10] (official).
  5. Keep the §7 SessionStart `compact` hook that re-injects STATE.md [G16] (official). Delegate reading to a subagent only when its output would otherwise bloat the main context [G18, G19] (inference). Watch the `/usage` flags for long context and cache misses [G11] (official).

### 11.4 Changes to earlier sections (first, a new first row for the §4 table)
| # | Stage (stages/ file) | Goal | Main inputs | Main outputs | Model | Gate (pass/fail) | Who sees it |
|---|---|---|---|---|---|---|---|
| 0 | Intake (NEW) | Classify entry mode (a)–(e); map existing material to stage outputs; set gate statuses | existing data, scripts, outputs, drafts, reviews, dated artefacts | intake.md; inbox.md (empty); entry mode, gate-status block and disclosure queue in STATE.md | Sonnet 5.5 medium inventories; Opus 5.5 medium classifies; user confirms | Pass if every artefact is mapped or marked out of scope, every gate S1–S10 has a status with evidence, and every NOT PASSABLE gate has a queued disclosure item | user |

- **STATE.md template:** adds the entry mode; a gate-status block for S0–S10 (PASSED, RETRO-AUDIT, NOT PASSABLE or OPEN, each with an evidence pointer); the live file; the mode (work or propagate); STALE flags; the disclosure queue; an inbox pointer with an open-item count; and a cap of about 60 lines.
- **CLAUDE.md and stages/:** CLAUDE.md adds the one-live-file, inbox and answer-without-editing rules, the 11.3 session pattern, and the 11.2 deny-rule snippet as a reference. The live config is .claude/settings.json, and the hook script joins the plan-freeze hook from §9 Decision 8. stages/ adds stages/00-intake.md. Each stage file names its live file, a RETRO-AUDIT variant of its gate checklist and a propagate step at its gate. The stage 7 and 10 gates gain the disclosure items queued at intake.
- **agents/ and templates/:** agents/ is unchanged; Stage 0 reuses data-reader. No new template is needed: intake.md and inbox.md are outputs defined in stages/00-intake.md, and the gate-status block lives in the STATE.md template. The only candidate is a disclosure-statement template, because modes (b)–(e) all need one. I recommend a checklist in the stage 7 and 10 files instead (the reviewer's call).

### 11.5 Decisions for Checkpoint 1 (additional)
9. **How strict is the one-live-file rule?** Options: (a) CLAUDE.md text only; (b) `ask` Edit rules on every non-live per-paper file; (c) static `deny` rules on frozen files plus a PreToolUse allowlist hook keyed to the live file. **Recommend (c), with (b) as the fallback until the hook is tested.** Evidence: CLAUDE.md is not enforced [G15]. Deny beats allow, and hooks block in every mode [G20, G22]. The allowlist script is inference, with no built-in equivalent (G, Gaps). R and Python writes escape deny rules [G21].
10. **Can a retrospective entry (modes b–e) use the label "confirmatory"?** Options: (a) never; (b) only on new data, or on a hold-out that the access log shows was never explored; (c) also with a retrospectively registered plan. **Recommend (b), and never (c).** Evidence: [F10–F12, F35]. Retrospective registration cannot show that decisions were prespecified [F16], and no source accepts it as equivalent (F, Gaps). Supersedes §9 Decision 2 for modes (b)–(e): its option (b) is unavailable once outcomes have been seen.
11. **Who triggers inbox propagation?** Options: (a) gates only; (b) gates, plus an explicit user command that runs the same plan-mode change list mid-stage; (c) automatic. **Recommend (b), and never (c).** Evidence: this is inference, supported by "one feature at a time" [G13] and plan mode [G23 UNVERIFIED]. Procedures belong on demand, not in CLAUDE.md (G, Implications). A `/propagate` command file would sit outside the fixed structure, so the reviewer must either allow it or accept a typed phrase that triggers the stage-file procedure.
