# Stage 00 — Intake
Goal: list everything that already exists for this paper, classify the entry mode, and give every gate S00–S10 an honest status before any other work starts.

## Entry modes
- Runs first in every mode (`a-data-only`, `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`). It is the audit set-up itself, so it has no RETRO-AUDIT variant.
- NOT-PASSABLE: never as a whole. An artefact whose date cannot be shown gets `date evidence: none`, is treated as made after outcome inspection, and queues the disclosure item "provenance of <artefact> unknown".
- Mode table (condensed from synthesis §11.1; S01–S10 = stage files 01–10):
  - `a-data-only`: normal S01 (+ data-access log), S03, S04 if no outcome-level look, S05–S10 · RETRO-AUDIT S02 (logged post-design) · NOT-PASSABLE S04 for design and sample size (the freeze covers analysis only) · disclose collection and freeze dates, any prior looks, when inclusion rules were fixed.
  - `b-analysis-done`: normal S01, S07 (from as-run scripts), S08–S10 · RETRO-AUDIT S02 (flag literature HARKing), S03, S05 (as-run log), S06 (built backwards, all rows post hoc) · NOT-PASSABLE S04 and any `confirmatory` label on these data · disclose no plan, all exploratory, every analysis in order, how the question was chosen, post hoc subsection, robustness.
  - `c-half-draft`: as b, plus S08–S09 re-extract the draft's citations from full text and an Introduction audit (hypotheses first dated after a result are post hoc; orphan claims flagged) · disclose as b, plus hypotheses written or changed after results (from version history).
  - `d-finished-manuscript`: normal S08 (sources never read in full), S09 on every in-text claim, S10 · RETRO-AUDIT S01–S07 as provenance reconstruction, each result tagged prior-plan or post hoc · NOT-PASSABLE S04 unless a dated prior plan exists · disclose provenance statement, extended disclosure, a label per result, "not preregistered", robustness section.
  - `e-under-revision`: normal S05 (requested analyses), S09 (new or changed citations + retraction check), S10 critique · RETRO-AUDIT everything before first submission (as-submitted version archived as dated baseline) · NOT-PASSABLE as at first submission · disclose labelled reviewer-requested analyses, version changes logged like deviations, response letter matching the labels.
- Status rules: `PASSED` only if the gate was passed or a dated artefact shows the work predates outcome inspection [F11]; `RETRO-AUDIT` = the full checklist run on existing material, recorded as audited, not prospective [F16]; `NOT-PASSABLE` = its disclosure item is queued in STATE.md; `OPEN` = the gate is still ahead.
- S04 (plan freeze) can never be passed retrospectively [F16, F13]. The S06, S07, S08 and S09 checklists are never shortened in any mode.

## Inputs · Live file(s) · Outputs
- **Inputs:** everything the user points to: data, scripts, outputs, drafts, reviews, and dated artefacts (git history, proposals, emails, permit or ethics dates); the template `paper-workflow/STATE.md`.
- **Live file:** `intake.md` (STATE.md and inbox.md are always writable). Paths below are relative to `papers/<slug>/`.
- **Outputs:**
  - `intake.md`: header `derives-from: none (first file)`; one table `artefact | path | date evidence | stands in for which stage output` (a stage output path such as `analysis-log.md`, or `out of scope`).
  - `STATE.md`: `entry_mode:`, gate block S00–S10 (status + evidence pointer), disclosure queue, `live_file:`, `mode: work`.
  - `inbox.md`: exactly this 5-line header and no rows:
```
# inbox.md — papers/<slug>/ — append-only: never edit or delete a line
Close an item by appending a row with the same ID and status `CLOSED -> <commit or row ID>`.
target file = the per-paper file the item would change; status = OPEN or CLOSED.
| ID | date | text | target file | status |
|---|---|---|---|---|
```

## Model and agent
- `agents/data-reader.md` (claude-sonnet-5-5, effort medium, ≤100k input tokens, output ≤150 lines): lists artefacts, reads dates from `git log`, file metadata and document headers, and writes the intake.md rows. It does not analyse content.
- Main session (Opus 5.5, effort medium): reads intake.md only, proposes the mode with a one-line reason, and sets the gate statuses with the user. It never opens raw data.
- The user confirms the mode (judgement call; no source prescribes the artefact-to-stage mapping, F Entry scenarios).

## Procedure
1. Create `papers/<slug>/`, copy the STATE.md template into it, and set `live_file: intake.md` and `mode: work`.
2. Ask the user to point to every existing artefact: data, scripts, outputs, drafts, reviews and dated documents.
3. data-reader writes one intake.md row per artefact with its path, date evidence and the stage output it stands in for (as-run scripts → analysis-log.md, draft Methods → methods.md) or `out of scope`.
4. Main session reads intake.md and proposes one entry mode from `a-data-only` … `e-under-revision` with a one-line reason.
5. The user confirms or corrects the mode, and it is written as `entry_mode:` in STATE.md with the confirmation date.
6. Main session sets every gate S00–S10 from the mode table: gates already settled get their final status, all others `OPEN` with the variant (`normal` or `retro-audit`) noted, each with an evidence pointer (intake.md row or commit).
7. For every NOT-PASSABLE gate, and for the S04 design-and-sample-size item in `a-data-only`, queue the disclosure item from the mode table in STATE.md.
8. In `e-under-revision`, the user commits the as-submitted manuscript and tags it `submitted-<slug>-v1` as the dated baseline.
9. Create inbox.md with its 5-line header and no rows.
10. Run the gate, commit as `intake: <slug>`, and set `live_file: data-inventory.md` for stage 01.

## Gate (pass/fail)
Pass if every existing artefact is mapped to a stage output or marked out of scope, every gate S01–S10 has a status with its evidence, and every NOT-PASSABLE gate has its disclosure item queued in STATE.md.
- [ ] Every artefact the user named has an intake.md row, mapped to a stage output or `out of scope`.
- [ ] Every row has a date evidence entry (commit, file date, document date, or `none`).
- [ ] `entry_mode:` is one of the five mode strings, with the user's confirmation date.
- [ ] Every gate S00–S10 carries exactly one of `PASSED`, `RETRO-AUDIT`, `NOT-PASSABLE`, `OPEN` and an evidence pointer.
- [ ] S04 is `PASSED` only if a dated plan artefact predates outcome inspection; otherwise it is `OPEN` (`a-data-only`) or `NOT-PASSABLE`.
- [ ] Every NOT-PASSABLE gate has its disclosure item in the STATE.md disclosure queue.
- [ ] `e-under-revision`: tag `submitted-<slug>-v1` exists.
- [ ] inbox.md exists with the 5-line header and zero rows.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is intake.md (for example, a newly found artefact). Write the change list in plan mode and wait for user approval. Set `mode: propagate`, add or correct the intake.md rows first, then re-set the affected gate statuses and mark every downstream file `stale:` in STATE.md. Close each item by appending a CLOSED row with its pointer, then set `mode: work`. A newly found artefact can raise a gate to `PASSED` only if it is dated before outcome inspection; S04 moves only for a dated prior plan.

## Evidence
- [F11] A: a data checkout/access log lets authors show that plans predate data access (basis for `PASSED` via a dated artefact).
- [F16] A: retrospective registration cannot show decisions were prespecified (S04 never passed retrospectively; RETRO-AUDIT wording).
- [F13] A: late registration is common and rarely disclosed.
- [F1] A: transparent post hoc analysis belongs in a dedicated Discussion subsection.
- [F4] A UNVERIFIED: a disclosure statement is usable at any stage.
- [F23] A: deviations are reported with their effect, not hidden.
- F, Entry scenarios: the stage mapping is F's construction; no source prescribes it (judgement call).
