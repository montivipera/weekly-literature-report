# Stage 05 — Analysis
Goal: run exactly the frozen plan (5a, confirmatory), then labelled exploration (5b), and log every run, nulls and abandoned models included.

## Entry modes
- `a-data-only` with S04 `PASSED`: 5a then 5b, as below.
- S04 `NOT-PASSABLE` (modes b–e, or `a-data-only` after an outcome-level look): there is no 5a. Every row is `exploratory`, except a run with a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data); "declared" is defined in stage 04 [F10–F12, F35]. The robustness rule tagged at stage 04 runs as part of 5b.
- RETRO-AUDIT (every variant below): before any legacy script runs, commit data/ and run `chmod -R a-w papers/<slug>/data` (if stage 01 has not), because script writes escape the deny rule [G21].
- RETRO-AUDIT in `b-analysis-done` and `c-half-draft`: rebuild analysis-log.md from the as-run scripts and outputs in run order (dated by commits or file dates), every row `exploratory`, abandoned models included where artefacts exist. Re-run each script once; an output that does not reproduce becomes an inbox.md item.
- RETRO-AUDIT in `d-finished-manuscript`: provenance reconstruction; each result in the manuscript gets a log row tagged `prior-plan` (only with a dated prior plan) or `post hoc` in notes.
- `e-under-revision`: runs normally for reviewer-requested analyses, each labelled (`exploratory` unless the confirmatory rule holds), with the reviewer comment ID in notes; changes against the `submitted-<slug>-v<n>` baseline are logged in deviations.md like deviations.
- NOT-PASSABLE: the `confirmatory` label on same data in modes b–e; its disclosure ("no plan; all exploratory; every analysis and its order") was queued at intake and is checked here. If the as-run order cannot be rebuilt, queue "analysis order unknown" (stage 00 rule).

## Inputs · Live file(s) · Outputs
- **Inputs:** analysis-plan.md at tag `plan-<slug>-v1`, data/ (read-only), SHA256SUMS, data-inventory.md, method-rationale.md, data-access.md.
- **Live files:** `scripts/, results/, analysis-log.md, deviations.md` (one comma list for the whole stage; data-access.md is always writable).
- **Outputs:**
  - `scripts/A<nn>_<name>.R` (or .py; `A<nn>` = its first run): reads data/ read-only, writes only under results/ (deny rules do not catch R or Python subprocess writes [G21]).
  - `results/A<nn>.md` (≤100 lines, one per run; written by the script, or by the analyst with Write from the saved output only): header `derives-from: scripts/<file>@<short-commit>`; model formula, n (total and per grouping level), effect with direction, uncertainty (95% CI or SE), test statistic, diagnostics; a null is reported in the same form [C19, C39]. Raw output sits beside it as `results/A<nn>_*`.
  - `analysis-log.md`: one row per run, these nine columns (canonical; analyst.md and templates/analysis-to-question.md copy them): `ID | date | label | plan-id or "exploratory" | script | inputs | output file | result incl. null | notes`. ID is `A<nn>`; script is `scripts/<file>@<short-commit>`; output file is `results/A<nn>.md`. Failed runs and abandoned models are included and say so in `result incl. null`.
  - `deviations.md`: `D<nn> | date | plan-id | what changed | why | effect on label | user OK` [C27].
  - `data-access.md`: one row per run (`date | who | what was seen/run | outcome-level? yes|no`).

## Model and agent
- `agents/analyst.md` (claude-sonnet-5-5, effort medium, maxTurns 60, input ≤120k tokens; one analysis per turn; results ≤100 lines each). Its coding strength rests on vendor or secondary coding benchmarks only [A14, grade C].
- Main session (Opus 5.5, effort medium): reviews analysis-log.md, deviations.md and results/*.md as md only; never reads data/ or raw model output.
- Early-stop control [A15]: the checklist is the plan-id list in the tagged plan; the completion criterion is "every plan-id has a log row with a result, or a deviations.md row saying why not"; at most 3 automatic continuations, each naming the open plan-ids, then the main session stops and asks the user.
- Mid-stage `/compact Focus on stage 05` is allowed here, at a natural break while the cache is warm; it is the only mid-stage compaction in stages 00–05. At stage end use `/clear`.

## Procedure
1. Check S04 in STATE.md and `git tag -l 'plan-<slug>-*'`, and that data/ is committed and read-only (RETRO-AUDIT: commit and `chmod` now); if S04 is not `PASSED`, there is no 5a, and every row is `exploratory` unless the confirmatory rule holds.
2. Confirm `live_file: scripts/, results/, analysis-log.md, deviations.md` (set at stage 04 step 10) and send the analyst the plan-ids still open.
3. 5a: analyst writes one script per plan-id exactly as planned, commits it, runs it, and results/A<nn>.md is written from the saved output.
4. Analyst appends one analysis-log.md row and one data-access.md row per run, including failed runs, nulls and abandoned models.
5. Any departure from the plan (data fix, non-convergence, changed exclusion or model) gets a deviations.md row with its reason before the run is reported [C27].
6. If analyst stops with plan-ids open, main session sends a continuation naming them, at most 3 times, then asks the user [A15].
7. 5b starts only after the 5a checklist is complete (judgement call); each further analysis is labelled `exploratory` and logged the same way [C7].
8. The sensitivity and robustness checks named in the plan run and are logged (multiverse, second analyst, preprocessing choices) [C37].
9. Main session reviews analysis-log.md, deviations.md and results/*.md as md only and appends any issue to inbox.md.
10. Run the gate, commit, and set `live_file: question-map.md` for stage 06.

## Gate (pass/fail)
Run gate commands from paper-workflow/ (the project root for Claude Code).
- [ ] Every analysis-log.md row has an `A<nn>` ID and all nine fields, and its label is `confirmatory` (with a plan-id) or `exploratory`.
- [ ] Every `confirmatory` row's plan-id appears with label `confirmatory` in `git show plan-<slug>-v1:./papers/<slug>/analysis-plan.md`, and its script was first committed after the tag (`git merge-base --is-ancestor plan-<slug>-v1 <first commit of the script>`).
- [ ] Hold-out (modes b–e, or `a-data-only` after an outcome-level look): every `confirmatory` row uses a dataset declared in data-access.md, the declaring commit is an ancestor of the first results/ commit (commands as in the stage 04 gate), and no `outcome-level? yes` row for that dataset predates the tag; otherwise the gate fails.
- [ ] Completion: every plan-id has at least one log row, or a deviations.md row explaining why not.
- [ ] Every results/A<nn>.md file gives n, effect with direction and uncertainty; nulls are reported in the same form.
- [ ] Every deviations.md row has a `D<nn>` ID, why, its effect on the label and the user's OK.
- [ ] The plan is untouched: `git diff --quiet plan-<slug>-v1 -- papers/<slug>/analysis-plan.md` succeeds.
- [ ] data/ is untouched: `(cd papers/<slug> && sha256sum -c SHA256SUMS)` passes.
- [ ] No script wrote outside results/: `git status --porcelain papers/<slug>/` lists only scripts/, results/, analysis-log.md, deviations.md, STATE.md, inbox.md, data-access.md.
- [ ] Each results file has a log row and each successful run has a results file (failed runs say so in the log).
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is a stage 05 file or an upstream file. Write the change list in plan mode and wait for user approval. Set `mode: propagate`; items targeting analysis-plan.md become deviations.md rows (never plan edits); items targeting data-inventory.md or questions.md are edited upstream first and the affected results and log rows are marked `stale:` in STATE.md, then re-run as new log rows (old rows stay). Close each item by appending its row with status `CLOSED -> <file>@<commit>`, then set `mode: work`.

## Evidence
- [C7] A: only pre-specified analyses are confirmatory; others are allowed but labelled exploratory.
- [F10] A, [F11] A, [F12] A, [F35] A: prior data knowledge, data checkout log, Explore-and-Confirm, and a fresh dataset as the routes to a confirmatory test on secondary data.
- [C5] A: 64% of ecologists admitted omitting non-significant results.
- [C19] A: ecology papers often omit sample sizes, effect directions and uncertainty; [C39] A: report what meta-analyses need.
- [C27] A: report and justify deviations from a plan.
- [C37] A: preprocessing sensitivity, multiple models and analysts, multiverse analysis.
- [A15] A: long unattended runs stop early; checklist, continuation naming open items, cap of 2–3 continuations.
- [G21] A (vendor docs): deny rules catch sed/tee/> but not R or Python subprocess writes.
