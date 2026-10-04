# Stage 05 — Analysis
Goal: run exactly the frozen plan (5a, confirmatory), then labelled exploration (5b), and log every run, nulls and abandoned models included.

## Entry modes
- `a-data-only` with S04 `PASSED`: 5a then 5b, as below.
- S04 `NOT-PASSABLE` (modes b–e, or `a-data-only` after an outcome-level look): there is no 5a. Every row is `exploratory`, except analyses on new data or on a hold-out the data-access log shows was never explored, run under a tagged plan [F10–F12, F35]. The robustness rule tagged at stage 04 runs as part of 5b.
- RETRO-AUDIT in `b-analysis-done` and `c-half-draft`: rebuild analysis-log.md from the as-run scripts and outputs in run order (dated by commits or file dates), every row `exploratory`, abandoned models included where artefacts exist. Re-run each script once; an output that does not reproduce becomes an inbox.md item.
- RETRO-AUDIT in `d-finished-manuscript`: provenance reconstruction; each result in the manuscript gets a log row tagged `prior-plan` (only with a dated prior plan) or `post hoc` in notes.
- `e-under-revision`: runs normally for reviewer-requested analyses, each labelled (`exploratory` unless on new data), with the reviewer comment ID in notes; changes against the `submitted-<slug>-v1` baseline are logged in deviations.md like deviations.
- NOT-PASSABLE: the `confirmatory` label on same data in modes b–e; its disclosure ("no plan; all exploratory; every analysis and its order") was queued at intake and is checked here. If the as-run order cannot be rebuilt, queue "analysis order unknown".

## Inputs · Live file(s) · Outputs
- **Inputs:** analysis-plan.md at tag `plan-<slug>-v1`, data/ (read-only), data-inventory.md, method-rationale.md.
- **Live files (one at a time, switched in STATE.md):** `scripts/` while writing a script; `analysis-log.md` while logging; `deviations.md` while recording a departure. results/ is written only by the scripts themselves.
- **Outputs:**
  - `scripts/<run-ID>_<name>.R` (or .py): reads data/ read-only, writes only under results/ (deny rules do not catch R or Python subprocess writes [G21]).
  - `results/<run-ID>.md` (≤100 lines, written by the script): header `derives-from: scripts/<file>@<c>`; model formula, n (total and per grouping level), effect with direction, uncertainty (95% CI or SE), test statistic, diagnostics; a null is reported in the same form [C19, C39].
  - `analysis-log.md`: one row per run: `ID | date | label | plan-id or "exploratory" | script | inputs | output file | result incl. null | notes` (failed runs and abandoned models included).
  - `deviations.md`: `ID | date | plan-id | planned | done | reason | effect on label or test severity | user OK (date)` [C27].

## Model and agent
- `agents/analyst.md` (claude-sonnet-5-5, effort medium, maxTurns 60; one analysis per turn; results ≤100 lines each). Its coding strength rests on vendor or secondary coding benchmarks only [A14, grade C].
- Main session (Opus 5.5, effort medium): reviews analysis-log.md, deviations.md and results/*.md as md only; never reads data/ or raw model output.
- Early-stop control [A15]: the checklist is the plan-id list in the tagged plan; the completion criterion is "every plan-id has a log row with a result, or a deviations.md row saying why not"; at most 3 automatic continuations, each naming the open plan-ids, then the main session stops and asks the user.
- Mid-stage `/compact Focus on stage 05` is allowed here, at a natural break while the cache is warm; it is the only mid-stage compaction in stages 00–05. At stage end use `/clear`.

## Procedure
1. Check S04 in STATE.md and `git tag -l plan-<slug>-v1`; if S04 is not `PASSED`, skip 5a and label every row `exploratory`.
2. Main session sends analyst the plan-ids still open and sets `live_file: scripts/`.
3. 5a: analyst writes one script per plan-id exactly as planned, runs it, and the script writes results/<run-ID>.md.
4. Analyst sets `live_file: analysis-log.md` and appends one row per run carrying its plan-id, including failed runs, nulls and abandoned models.
5. Any departure from the plan (data fix, non-convergence, changed exclusion or model) gets a deviations.md row with its reason before the run is reported [C27].
6. If analyst stops with plan-ids open, main session sends a continuation naming them, at most 3 times, then asks the user [A15].
7. 5b starts only after the 5a checklist is complete (judgement call); each further analysis is labelled `exploratory` and logged the same way [C7].
8. The sensitivity and robustness checks named in the plan run and are logged (multiverse, second analyst, preprocessing choices) [C37].
9. Main session reviews analysis-log.md, deviations.md and results/*.md as md only and appends any issue to inbox.md.
10. Run the gate, commit, and set `live_file: question-map.md` for stage 06.

## Gate (pass/fail)
- [ ] Every analysis-log.md row has all nine fields, and its label is `confirmatory` (with a plan-id) or `exploratory`.
- [ ] Every `confirmatory` row's plan-id appears in `git show plan-<slug>-v1:papers/<slug>/analysis-plan.md`, and its script was first committed after the tag.
- [ ] Completion: every plan-id has at least one log row, or a deviations.md row explaining why not.
- [ ] Every results/*.md file gives n, effect with direction and uncertainty; nulls are reported in the same form.
- [ ] Every deviation row has a reason, its effect on the label and the user's OK.
- [ ] The plan is untouched: `git diff --quiet plan-<slug>-v1 -- papers/<slug>/analysis-plan.md` succeeds.
- [ ] data/ is untouched: `sha256sum -c` against the checksums in data-inventory.md passes.
- [ ] No script wrote outside results/: `git status --porcelain papers/<slug>/` lists only scripts/, results/, analysis-log.md, deviations.md, STATE.md, inbox.md.
- [ ] Each results file has a log row and each successful run has a results file (failed runs say so in notes).
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is a stage 05 file or an upstream file. Write the change list in plan mode and wait for user approval. Set `mode: propagate`; items targeting analysis-plan.md become deviations.md rows (never plan edits); items targeting data-inventory.md or questions.md are edited upstream first and the affected results and log rows are marked `stale:` in STATE.md, then re-run as new log rows (old rows stay). Close each item by appending a CLOSED row with its pointer, then set `mode: work`.

## Evidence
- [C7] A: only pre-specified analyses are confirmatory; others are allowed but labelled exploratory.
- [C5] A: 64% of ecologists admitted omitting non-significant results.
- [C19] A: ecology papers often omit sample sizes, effect directions and uncertainty; [C39] A: report what meta-analyses need.
- [C27] A: report and justify deviations from a plan.
- [C37] A: preprocessing sensitivity, multiple models and analysts, multiverse analysis.
- [A15] A: long unattended runs stop early; checklist, continuation naming open items, cap of 2–3 continuations.
- [G21] A (vendor docs): deny rules catch sed/tee/> but not R or Python subprocess writes.
