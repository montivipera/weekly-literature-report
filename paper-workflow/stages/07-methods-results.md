# Stage 07 — Methods and Results
Goal: write methods.md and results.md along the question-map axis, with every mandatory reporting item present and every number traceable to a results/*.md file.

## Entry modes
- Runs normally in `a-data-only`. In `b-analysis-done` and `c-half-draft` it also runs normally, working from the as-run scripts and the `RETRO-AUDIT` question map. Gate status: `PASSED`.
- `RETRO-AUDIT` in `d-finished-manuscript`, and for the as-submitted text in `e-under-revision`:
  - the existing Methods and Results are committed into methods.md and results.md as the dated baseline;
  - they are audited item by item against the gate below, and gaps are filled;
  - each result is tagged prior-plan or post hoc.
  The checklist is never shortened [F23].
- Modes b–e add two things:
  - a disclosure block in methods.md: "not preregistered"; every analysis reported in run order; how the questions were chosen; when the inclusion rules were fixed [F4 UNVERIFIED];
  - a pointer in results.md to the post hoc subsection of the Discussion [F1, F31].
- `e-under-revision`: analyses requested by reviewers are reported and labelled as such, and changes since submission are listed the way deviations are [F23].
- `NOT-PASSABLE` when a mandatory item cannot be established from any artefact, for example unknown prior exposure, or a reported number whose script is lost. Queue this disclosure item in STATE.md: "<item> could not be established and is stated as unknown in Methods."

## Inputs / Live files / Outputs
- **Inputs:**
  - STATE.md, for the entry mode and the disclosure queue;
  - intake.md, for the target journal;
  - question-map.md, analysis-plan.md and the plan tag date (`git log -1 --format=%ci plan-<slug>-v1`);
  - method-rationale.md, deviations.md, data-inventory.md and results/*.md;
  - templates/section-skeleton.md: the Methods, Results and Data/code availability blocks.
- **Live files, one at a time:** first `live_file: methods.md`, then `live_file: results.md`. Switch in STATE.md between the two drafter runs.
- **Outputs:**
  - **methods.md:** header `derives-from: question-map.md@<short-commit>`. Skeleton bullets first, then prose. The mandatory items appear in gate order. Citations appear only as `[ledger: Rn]` placeholders.
  - **results.md:** the same header. One subsection per question, in question-map order. For each analysis: label, plan-id or `exploratory`, n, effect, uncertainty, and a null stated as a null. Each paragraph ends with `<!-- src: results/<file>.md -->`.
- **Where the AI-use statement goes.** This table is a starting point only; it is snippet-based, and stage 10 re-reads the live policy.

| Publisher / standard | Placement | Ref |
|---|---|---|
| Elsevier | Declaration section before the References (tool, purpose, oversight) | [D27] A |
| Springer Nature | Methods | [D28] A |
| Wiley | Methods, a disclosure section, or Acknowledgements | [D29] A UNVERIFIED |
| Taylor & Francis | Methods or Acknowledgements (tool name, version, how and why) | [D30] A |
| COPE (default) | Materials and Methods, or similar | [D31] A |
| ICMJE journals | Cover letter and manuscript: writing help in Acknowledgements, analysis use in Methods | [D32] A UNVERIFIED |

## Model and agent
- **agents/drafter.md:** Opus 5.5 (`claude-opus-5-5`) at effort medium. One section per run, so two runs. It reads md only, never data/ or scripts/.
- **Main session (Opus 5.5):**
  - sets live_file and passes paths, not contents;
  - runs the number-trace check and the gate;
  - does not rewrite drafter prose unless the user asks.
- **Budget:** each drafter run ≤60k input tokens (judgement call). The return message is ≤10 lines.

## Procedure
1. Read STATE.md and stop unless stage 06 is `PASSED` or `RETRO-AUDIT` and question-map.md is not under `stale:`.
2. Set `live_file: methods.md` and call the drafter with the input paths and the Methods block of templates/section-skeleton.md.
3. The drafter writes skeleton bullets first, then prose covering each mandatory Methods item in gate order, citing methods sources only as `[ledger: Rn]` placeholders.
4. In modes b–e the drafter adds the disclosure block and copies into it every Methods-bound item from the STATE.md disclosure queue.
5. The drafter places the AI-use statement where the target journal requires it (table above) and names every AI tool actually used, including help with analysis.
6. Set `live_file: results.md` and call the drafter for Results, one subsection per question in question-map order, with nulls included and not-mapped analyses in a supplement list.
7. Each Results paragraph reports label, n, effect and uncertainty and ends with its `src` pointer, so every number traces to one results/*.md file (judgement call) [C19].
8. The main session checks that every number in results.md occurs in the file its paragraph points to (a grep per paragraph), fixes drafter misses in results.md, and sends errors inside results/*.md to inbox.md.
9. Any method reference not yet in the ledger becomes an inbox.md line targeting doi-ledger.md, to be resolved in stages 08–09.
10. Run the gate, write STATE.md, commit, run `/rename stage-07`, then `/clear`.

## Gate (pass/fail)
Methods (methods.md):
- [ ] **Dataset pre-existed:** states whether the data existed before the questions were framed, and who collected them [C22, C23].
- [ ] **Prior exposure:** what the authors had seen of the data before analysis, taken from data-inventory.md and intake.md [C24, F10].
- [ ] **Plan:** the date and commit of tag `plan-<slug>-v1`, or the words "no plan". Modes b–e also say "not preregistered".
- [ ] **Deviations:** every deviations.md row is reported with its reason and effect. Checked by count match [C27, F23].
- [ ] **Candidate model set and selection rule:** taken from method-rationale.md. In mode b they come from the as-run scripts, and if the rule was chosen after seeing results, the text says so [C36].
- [ ] **Data and code availability:** a statement giving the repository, or the reason for not sharing [C18, C20].
- [ ] **AI-use statement:** in the location the target journal requires [D27–D32].
- [ ] **Modes b–e:** the disclosure block is present, and every Methods-bound disclosure item from STATE.md is copied, checked by count match [F4].

Results (results.md):
- [ ] There is one subsection per question, and every part A row of question-map.md appears, nulls included. Checked by count match.
- [ ] Every mapped analysis has n, effect, uncertainty and its label [C19].
- [ ] Every paragraph has a `src` pointer, and the number-trace check finds 0 misses.
- [ ] Modes b–e: results.md points to the Discussion's post hoc subsection [F31].
- [ ] There are no citations except `[ledger: Rn]` placeholders, and no literature claims in Results.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count. Next: `live_file: doi-ledger.md`.

## Propagate step
This runs at this gate, or when the user types "propagate inbox".
1. Read the OPEN inbox.md items that target methods.md, results.md or upstream files.
2. Set `mode: propagate` and list the changes in plan mode.
3. Get user approval.
4. Edit upstream first: question-map.md before results.md. A change to the frozen plan is only ever a deviations.md row.
5. Mark doi-ledger.md and draft/ as `stale:` where they exist.
6. Close each item with a commit pointer, then set `mode: work`.

## Evidence
- [C19] A: ecology papers often omit sample sizes, effect directions and uncertainty, especially for weak results.
- [C18] A, current policy UNVERIFIED: Ecology Letters adopted TOP, covering analysis-plan preregistration and data and code.
- [C20] A: 15 of 17 ecology and evolution journals expect or encourage data sharing, and 10 require it.
- [C23] A: preregistering analyses of pre-existing data is useful, but major design aspects cannot change.
- [C27] A: deviations are not all problematic; report them transparently and justify them.
- [C36] A: mixed-model best practice covers model selection; multimodel inference is hard without formal training.
- [F4] A UNVERIFIED: a disclosure statement can be used at any stage, including whether inclusion criteria were set before analysis.
- [D27–D32] A (D29 and D32 are A UNVERIFIED; all snippet-based): where publishers and standards require AI use to be disclosed.
