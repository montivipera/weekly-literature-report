# Stage 06 — Question map
Goal: put every analysis that was run onto one axis of questions, with nulls and unmapped analyses kept, and hand that map to the advisors as entry 2.

## Entry modes
- Runs normally in `a-data-only` after stage 05, because analysis-log.md was written prospectively. Gate status: `PASSED`.
- `RETRO-AUDIT` in `b-analysis-done`, `c-half-draft` and `d-finished-manuscript`, and for everything before first submission in `e-under-revision`. In this variant the map is built backwards:
  - each result claim in the existing draft or outputs is traced to the analysis-log row (`A<nn>`) that produced it;
  - every row is marked post hoc and labelled `exploratory`;
  - claims with no analysis behind them are listed as orphan claims;
  - analyses with no claim go to "Not mapped" [F1, F31].
  The checklist is never shortened (judgement call).
- In `e-under-revision`, analyses requested by reviewers (run in stage 05) are added as new rows marked `reviewer-requested`. This part is a normal run.
- `NOT-PASSABLE` only when the set of analyses actually run cannot be reconstructed, for example because scripts or outputs were lost. Queue this disclosure item (one STATE.md line, ID + ≤6 words; full text goes to inbox.md as an item with target file `disclosure.md` and is written into disclosure.md at stage 10): "The full set of analyses run could not be reconstructed; the reported analyses are those recoverable from <artefacts>."

## Inputs / Live file / Outputs
- **Inputs:**
  - STATE.md, analysis-log.md (the nine columns of stage 05), results/A<nn>.md, questions.md, deviations.md, data-access.md;
  - analysis-plan.md as of tag `plan-<slug>-v1`, for plan-ids;
  - templates/analysis-to-question.md and templates/question-map.md;
  - in modes b–e, also intake.md and the existing draft it points to.
- **Live file:** `live_file: question-map.md`. The mechanical table is Part A of this file, not a separate file.
- **Output:** question-map.md, with header `derives-from: analysis-log.md@<short-commit>, questions.md@<short-commit>` and a count line `analysis-log rows: N | part A rows: N`. It has two parts:
  - **Part A, analysis-to-question** (from templates/analysis-to-question.md). Columns: ID (`A<nn>`) | RQ | label | plan-id or "exploratory" | script | output file | result incl. null | reported where | notes. One row per analysis-log row, in log order.
  - **Part B, advisor package** (from templates/question-map.md): the five-line cover note; the single-axis table (question | hypothesis + `origin: literature | data | advisor` | analysis ID + label | result incl. null | deviation ref `D<nn>` | figure/table | status); "Not mapped"; in modes b–e, the orphan-claims list; changes since the last review.

## Model and agent
- **Main session only:** Opus 5.5 (`claude-opus-5-5`) at effort medium. It reads md files only, never data/ or scripts/.
- **No subagent.** Part A is mechanical copying. Deciding which question an analysis answers stays with the main session and the user (judgement call).
- **Budget:** ≤80k input tokens, md only; question-map.md ≤150 lines (judgement call). If results/A<nn>.md files would exceed the budget, read the result column of analysis-log.md and open a results file only when its row is ambiguous.
- **Unclear results or labels:** if a result or label upstream is unclear or wrong, append one line to inbox.md targeting that file. Never fix an upstream file in this stage.

## Procedure
1. Read STATE.md and stop if any input is listed under `stale:` or stage 05 is not `PASSED` or `RETRO-AUDIT`.
2. Count the analysis-log.md rows and write N into the header count line.
3. Fill Part A mechanically, one row per analysis-log row in log order, copying ID, label, plan-id, script, output file and result verbatim and adding only the RQ and where the result is reported.
4. Copy each result exactly as it appears in its results/A<nn>.md file, including nulls, non-convergence and failed fits, with no rounding or rewording.
5. Check every `confirmatory` row against the tagged plan (`git show plan-<slug>-v1:./papers/<slug>/analysis-plan.md | grep <plan-id>`) and against the label rule in the gate below; log any mismatch as an inbox.md item targeting analysis-log.md, never as an edit here.
6. Put every row that answers no question under "Not mapped", with a one-line reason and the flag `orphan analysis`.
7. Build the Part B table grouped by question in questions.md order, one line per analysis, each carrying the hypothesis `origin:` tag, the deviations.md row ID and the figure/table pointer.
8. In modes b–e, link every result claim in the existing text to a Part A row, mark every row post hoc, and list claims with no row as orphan claims.
9. Write the five-line cover note (what the axis is; counts of mapped, not mapped and null rows; what advisors are asked) and export the package (see Advisor touchpoint).
10. Run the gate, write STATE.md, commit, run `/rename <slug>-S06`, then `/clear`.

## Gate (pass/fail)
Run gate commands from paper-workflow/ (the project root for Claude Code).
- [ ] Header `derives-from:` is present, with short commits.
- [ ] The number of Part A rows equals the number of analysis-log.md rows (count check in templates/analysis-to-question.md). Both numbers are in the header count line.
- [ ] Every null, non-significant, non-converged or failed result in analysis-log.md appears in Parts A and B with its result, checked by count match [C2 form c, C19].
- [ ] Every Part A row has an RQ or sits under "Not mapped" with a reason. Orphan analyses are flagged.
- [ ] Every `confirmatory` row carries a plan-id found in the tagged plan.
- [ ] `confirmatory` only with a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data). In modes b–e, and in a after any outcome-level look recorded in data-access.md, the data-access.md row declaring the hold-out or new data is dated before the first results/ commit; otherwise the row is `exploratory`.
- [ ] Every hypothesis in Part B has `origin: literature | data | advisor`.
- [ ] Every deviation ref resolves to a `D<nn>` row in deviations.md.
- [ ] Modes b–e: every row is marked post hoc, and the orphan-claims list is present ("none" if empty) [F1].
- [ ] The advisor export path and date are recorded in STATE.md.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count. Next: `live_file: methods.md, results.md`.

## Propagate step
This runs at this gate, or when the user types "propagate inbox".
1. Read the OPEN inbox.md items that target question-map.md or the files it is built from: questions.md, analysis-log.md, deviations.md, results/A<nn>.md.
2. Set `mode: propagate` and list the changes in plan mode.
3. Get user approval.
4. Edit upstream first. A change to the frozen plan is only ever a deviations.md row.
5. Regenerate the affected question-map rows.
6. Mark methods.md, results.md, doi-ledger.md and draft/ as `stale:` where they exist.
7. Close each item as `CLOSED -> <file>@<commit>`, then set `mode: work`.

A question added at this point gets `origin: advisor`. It is post hoc, and every analysis for it is `exploratory` [C2].

## Advisor touchpoint (entry 2)
- **Export:** `pandoc papers/<slug>/question-map.md -o papers/<slug>/question-map-<date>.docx`, or `.pdf`, with the cover note first. Send nothing else: there is no draft prose at this stage.
- **What the advisors are asked:**
  1. Is each question worth answering, and is its origin tag honest?
  2. Does every analysis you know was run appear, including failed and null ones?
  3. Which "Not mapped" analyses go to the supplement list? All of them are reported somewhere.
  4. Which nulls carry the paper's argument?
  5. Is any label or figure/table pointer wrong?
- Each reply point becomes one dated inbox.md line. Nothing is edited until the propagate step.

## Evidence
- [C2] A: three HARKing forms. Form (c), silently dropping unsupported a priori hypotheses, is what keeping null rows prevents. The common harm is non-disclosure.
- [C12] A: editors of Evolution and of Ecology and Evolution say that distinguishing pre-planned from post hoc analyses can greatly aid readers.
- [C19] A: ecology papers often omit sample sizes, effect directions and uncertainty, especially for weak results.
- [C47] C: in one forestry-biodiversity review, unexpected findings were often dampened or rationalised (single commentary).
- [F1] A: report post hoc analysis openly in a dedicated Discussion subsection; secret HARKing in the Introduction has no justification.
- [F31] A: of 807 ecologists and evolutionary biologists, 51% reported unexpected findings as if hypothesised and 64% omitted non-significant results.
