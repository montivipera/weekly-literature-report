# Section skeleton: <paper short title> (`<slug>`)
Headers, copied from the stage files: methods.md and results.md start `derives-from: question-map.md@<short-commit>` (stage 07); draft/*.md start `derives-from: doi-ledger.md@<short-commit>` (stage 10).

Two stages use this skeleton:
- Stage 07: the drafter copies the Methods, Results and Data and code availability blocks into methods.md and results.md.
- Stage 10: the drafter copies the Abstract, Introduction and Discussion blocks into draft/abstract.md, draft/intro.md and draft/discussion.md. The main session (never the drafter) fills the Disclosure statement block into disclosure.md.

Markers, and no other forms: `[ledger: <CL-ids>]` cites claim-support rows (for example `[ledger: CL12, CL15]`); `[log: <A-ids>]` points to the analysis-log row behind a number (for example `[log: A03]`, whose result file is results/A03.md). An unfillable slot is `[GAP: <slot> — <reason>]`.

## Rule
1. A draft cites only CL rows whose status is `SUPPORT-CHECKED`. A slot whose CL row is at any other status stays a `[GAP: …]` and fails the gate.
2. Every bullet names its rows: `[ledger: <CL-ids>]` for a literature claim and `[log: <A-ids>]` for a number or result. A bullet with neither is cut or sent to inbox.md.
3. Numbers are copied from results/A<nn>.md through their analysis-log row. They are never retyped from memory or recomputed in prose.
4. At stage 07 the ledger does not exist yet: a method citation is written `[GAP: cite — <what it must support>]` with an inbox.md line targeting doi-ledger.md. Stage 08 makes its CL row; stage 10 replaces the GAP with `[ledger: CL<nn>]`.
5. The reference list (draft/references.md, stage 10) is generated from the R rows of the cited CL rows, each at `METADATA-OK`. It is never typed.
6. Before advisors see the draft, the critic checks every `[ledger: CL…]` against a grep-extracted slice of doi-ledger.md (those CL rows and their R rows) and every `[log: A…]` against analysis-log.md and results/A<nn>.md.

## Abstract (stage 10, written last; word limit <n>)
- Context and gap, one sentence each [ledger: <CL-ids>]
- Aim and questions (RQ-ids in question-map.md order), naming the label of each main analysis [log: <A-ids>]
- Data: an existing dataset of <sites, years, n> collected under <design> [log: <A-ids>]
- Main results with effect and uncertainty, nulls included [log: <A-ids>]
- Conclusion worded to match the labels, with exploratory results stated as preliminary [ledger: <CL-ids>]

## Introduction (stage 10)
- Global context [ledger: <CL-ids>]
- Regional, national and local context, using human-checked rows only [ledger: <CL-ids>]
- The gap these data can address [ledger: <CL-ids>]
- Questions and hypotheses. Only hypotheses with `origin: literature` or `origin: advisor`, dated before the plan tag, are stated as a priori. Hypotheses with `origin: data` go to the Discussion subsection below [C2, F1] [ledger: <CL-ids>]
- Rows whose R row is `consulted: after-results` may give context, but they are never presented as the source of an a priori hypothesis [C2] [ledger: <CL-ids>]

## Methods (stage 07): mandatory items [C19, C23, C27, C36, D28, D31]
- Study area, sampling design and period [log: <A-ids>]
- The dataset pre-existed: it was collected <dates> by <who> under <protocol>, before this analysis was planned [C23]
- Prior exposure: what the authors had seen or analysed in these data before the plan, taken from the prior-exposure statement in STATE.md [C24, F10]
- Plan, one of these two sentences [C7, F16]:
  - "The analysis plan was fixed on <date> (git tag `plan-<slug>-v1`)."
  - "No analysis plan was fixed before the outcomes were inspected."
- Deviations from the plan: for each deviations.md row (D-id), what changed, why and the effect on the label; otherwise "none" [C27, F23]
- Candidate model set and selection rule: response distribution, random-effect structure and dependence, the selection criterion, and the protocol followed [C33, C35, C36] [GAP: cite — <protocol>]
- Labels: by question, which analyses are `confirmatory` (with plan-ids) and which are `exploratory` [log: <A-ids>]
- n, effect and uncertainty: Results gives them for every mapped analysis, and Methods states the estimand of each [C19, C39] [log: <A-ids>]
- Robustness and sensitivity checks, with each rule written before the check ran (required in every mode except `a-data-only`) [F17, F18, F36] [log: <A-ids>]
- Software and package versions [log: <A-ids>]
- Data and code availability: the block below, or a cross-reference to it if the journal puts it in Methods [C18, C20]
- AI-use statement, placed where the target journal requires it (Methods, Acknowledgements or a declaration section); stage 10 checks its wording against disclosure.md [D27–D32]

## Results (stage 07, in question-map.md order)
- RQ<n>: for each analysis row give the label, n, effect estimate, uncertainty and figure or table [log: <A-ids>]
- State null and inconclusive results in the same form as positive ones [C5, C19] [log: <A-ids>]
- Put exploratory analyses under their own labelled sub-heading [log: <A-ids>]
- Analyses with no question get one sentence each or a supplementary table [log: <A-ids>]
- Results carries no literature citations unless a method needs one [GAP: cite — <method>]

## Discussion (stage 10)
- Principal findings by question, worded to match each label [log: <A-ids>]
- Comparison with the literature, layer by layer from global to local [ledger: <CL-ids>]
- Unexpected and null results are discussed, not played down [C47] [log: <A-ids>]
- Limitations: design, dependence, prior exposure and deviations [log: <A-ids>]
- Conclusion: exploratory findings are stated as preliminary until new data test them [F5 UNVERIFIED] [ledger: <CL-ids>]

### Transparent post hoc analyses [F1, F31]
This subsection is mandatory in modes `b-analysis-done` to `e-under-revision`. In `a-data-only` it is required whenever an `exploratory` row is discussed.
- Each post hoc analysis: what it was, when it ran (after which result), why it was run, and that it is hypothesis-generating [log: <A-ids>]
- Hypotheses with `origin: data`, and the new data that would test them [ledger: <CL-ids>]
- Robustness results (multiverse or specification curve, second analyst, never-explored hold-out) [F17–F22] [log: <A-ids>]
- Questions with no analysis and dropped hypotheses, taken from question-map.md "Not mapped" [C2] [log: <A-ids>]

## Disclosure statement (stage 10, main session, in disclosure.md) [F4 UNVERIFIED, F16]
Required in modes `b-analysis-done`, `c-half-draft`, `d-finished-manuscript` and `e-under-revision`, and in `a-data-only` when any gate is `NOT-PASSABLE`.
Fill this from the queued items in disclosure.md (STATE.md keeps one line per item: ID + ≤6 words) and delete the slots that do not apply. Never use "preregistered" or "registered" for a plan written after the outcomes were seen [F16].
- Registration: "This study was not preregistered." or "The analysis plan was fixed on <date> (git tag `plan-<slug>-v1`) after data collection and before any outcome model was run."
- Prior exposure: "Before this analysis, the authors had <never worked with these data | analysed <variables> for <purpose or publication>>." (from the STATE.md prior-exposure statement)
- Completeness: "We report all analyses we ran, in the order they were run, including null results and abandoned models (analysis log: <repository or DOI>)." [F1, F31]
- How hypotheses were chosen: "Hypotheses <H-ids> were stated before the outcomes were inspected, based on <the literature | advisor input>. Hypotheses <H-ids> were formed after <A-ids> and are exploratory." [C2, F16]
- Criteria: "Inclusion and exclusion criteria were fixed <before | after> data analysis." [F4 UNVERIFIED]
- Labels: "<n> analyses are labelled confirmatory because each has a plan-id from a pre-outcome tag and uses <data with no outcome-level look before the plan | a declared, never-explored hold-out | new data>. All others are exploratory."
- Revision (`e-under-revision`): "The analyses requested by reviewers (<A-ids>) are labelled exploratory, and changes between versions are listed in <file>." [F23]
- Pointer: "Post hoc analyses are reported in the Discussion under '<subsection title>'."

## Data and code availability (stage 07; checked at stage 10) [C18, C20, C37]
- Data: <repository>, <DOI>, <licence>; any restricted fields (for example sensitive species locations) and how to request them
- Code: <repository>, tag or commit <id>, R and package versions
- Analysis log and deviations: <archived path or DOI>
- Plan: tag `plan-<slug>-v1` (<public link | internal git tag, available on request>) or "no plan"
