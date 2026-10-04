# Stage 00 — Intake
Goal: list everything that already exists for this paper, classify the entry mode, and give every gate S00–S10 an honest status before any other work starts.

## Entry modes
- Runs first in every mode (`a-data-only`, `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`). It is the audit set-up itself, so it has no RETRO-AUDIT variant.
- New paper: papers/<slug>/ does not exist yet; every step runs.
- Existing paper (a re-run on papers/<slug>/, e.g. the next revision round in `e-under-revision`): keep STATE.md and update its fields only (`entry_mode:`, gate rows, `live_file:`, `mode:`, disclosure queue); keep inbox.md and data-access.md with all their rows; append intake.md rows for the new artefacts (reviews, revised files); tag the as-submitted version `submitted-<slug>-v<n>` (step 8) as the new baseline.
- NOT-PASSABLE: never as a whole. An artefact whose date cannot be shown gets `date evidence: none`, is treated as made after outcome inspection, and queues the disclosure item "provenance of <artefact> unknown".
- Mode table (condensed; sources in docs/rationale.md; gates S01–S10 = stage files 01–10; the stage files are authoritative):
  - `a-data-only`: normal S01, S03, S04 if no outcome-level look, S05–S10 · S02 runs in full and is `PASSED`, with a queued "post-design" item (the scan informs questions and plan, not design or sample size) · NOT-PASSABLE S04 for design and sample size (the freeze covers analysis only) · disclose collection and freeze dates, any prior looks, when inclusion rules were fixed.
  - `b-analysis-done`: normal S01, S07 (from as-run scripts), S08–S10 · RETRO-AUDIT S02 (flag literature HARKing), S03, S05 (as-run log), S06 (built backwards, all rows post hoc) · NOT-PASSABLE S04 and any `confirmatory` label on the same data · disclose no plan, all exploratory, every analysis in order, how the question was chosen, post hoc subsection, robustness.
  - `c-half-draft`: as b, except RETRO-AUDIT S08 (the draft's citations re-extracted from full text) and S10 (Introduction audit: hypotheses first dated after a result are post hoc; orphan claims flagged) · disclose as b, plus hypotheses written or changed after results (from version history).
  - `d-finished-manuscript`: normal S09 (every in-text claim) · RETRO-AUDIT S01–S03 and S05–S07 (provenance reconstruction, each result tagged prior-plan or post hoc), S08 (existing reference list audited; sources never read in full are extracted) and S10 · NOT-PASSABLE S04 unless a dated prior plan exists · disclose provenance statement, extended disclosure, a label per result, "not preregistered", robustness section.
  - `e-under-revision`: normal S05 (requested analyses), S09 (new or changed citations + retraction check), S10 critique · RETRO-AUDIT everything before first submission (baseline tag `submitted-<slug>-v<n>`) · NOT-PASSABLE as at first submission · disclose labelled reviewer-requested analyses, version changes logged like deviations, response letter matching the labels.
- Status rules: `PASSED` only if the gate was passed or a dated artefact shows the work predates outcome inspection [F11]; `RETRO-AUDIT` = the full checklist run on existing material, recorded as audited, not prospective [F16]; `NOT-PASSABLE` = its disclosure item is queued; `OPEN` = the gate is still ahead.
- S04 (plan freeze) can never be passed retrospectively [F16, F13]. The S06, S07, S08 and S09 checklists are never shortened in any mode.

## Inputs · Live file(s) · Outputs
- **Inputs:** everything the user points to: data, scripts, outputs, drafts, reviews, and dated artefacts (git history, proposals, emails, permit or ethics dates); the STATE.md template (paper-workflow/STATE.md).
- **Live file:** `intake.md`; in modes b–e step 7 switches to `disclosure.md` (the only switch in this stage). STATE.md, inbox.md and data-access.md are always writable. Paths below are relative to `papers/<slug>/`.
- **Outputs:**
  - `intake.md`: header `derives-from: none (first file)`; one table `artefact | path | date evidence | stands in for which stage output` (a stage output path such as `analysis-log.md`, or `out of scope`). data-reader creates it with Write if absent and appends rows.
  - `STATE.md`: `entry_mode:`, gate table S00–S10 (status, variant `normal|retro`, evidence pointer, date), disclosure queue, `live_file:`, `mode: work`.
  - `inbox.md`: exactly this 5-line header and no rows (the one definition of the inbox format; CLAUDE.md quotes it):
```
# inbox.md — papers/<slug>/ — append-only: never edit or delete a line
Row: `I<nn> | date | text | target file | status`; status is `OPEN` or `CLOSED -> <file>@<commit>`.
Close an item by appending a new row with the same ID, text and target file and status `CLOSED -> <file>@<commit>`.
| ID | date | text | target file | status |
|---|---|---|---|---|
```
  - `data-access.md` (every mode; append-only, always writable): one row each time a person or an agent opens or runs anything on data/; a hold-out or new dataset is declared here (stage 00 or 01) before any analysis in this workflow. Rows: `date | who | what was seen/run | outcome-level? yes|no`. Header:
```
# data-access.md — papers/<slug>/ — append-only: never edit or delete a line
| date | who | what was seen/run | outcome-level? |
|---|---|---|---|
```
  - `disclosure.md` (modes b–e): `# disclosure.md — papers/<slug>/`, then `## Queue` with rows `ID | gate | full text the paper must state | queued date`; stage 10 completes the file.
- **Queueing a disclosure item (every stage uses this rule):** one line in the STATE.md disclosure queue (ID = queuing stage + number, e.g. `S04.1`, plus ≤6 words). disclosure.md is live only at step 7 here (modes b–e) and at stage 10; from any other stage the full text goes to inbox.md as an item with target file `disclosure.md` and is written into disclosure.md at stage 10, under the same ID.

## Model and agent
- `agents/data-reader.md` (claude-sonnet-5-5, effort medium, ≤100k input tokens, output ≤150 lines): lists artefacts, reads dates from `git log`, file metadata and document headers, and writes the intake.md rows. It does not analyse content.
- Main session (Opus 5.5, effort medium): reads intake.md only, proposes the mode with a one-line reason, and sets the gate statuses with the user. It never opens raw data.
- The user confirms the mode (judgement call; no source prescribes the artefact-to-stage mapping, F Entry scenarios).

## Procedure
1. New paper: create `papers/<slug>/`, copy the STATE.md template into it, set `live_file: intake.md` and `mode: work`, and create inbox.md and data-access.md with their headers and no rows. Existing paper: keep all three files and set only `live_file: intake.md`, `mode: work`.
2. Ask the user to point to every existing artefact: data, scripts, outputs, drafts, reviews and dated documents.
3. data-reader creates intake.md if absent and writes one row per artefact with its path, date evidence and the stage output it stands in for (as-run scripts → analysis-log.md, draft Methods → methods.md) or `out of scope`; on an existing paper it only appends.
4. Main session reads intake.md and proposes one entry mode from `a-data-only` … `e-under-revision` with a one-line reason.
5. The user confirms or corrects the mode, and it is written as `entry_mode:` in STATE.md with the confirmation date.
6. Main session sets every gate S00–S10 from the mode table: gates already settled get their final status, all others `OPEN`; each row gets its variant (`normal` or `retro`) in the gate table's variant column and an evidence pointer (intake.md row or commit).
7. For every NOT-PASSABLE gate, and for the S04 design-and-sample-size item in `a-data-only`, queue the disclosure item from the mode table. In modes b–e set `live_file: disclosure.md`, create it if absent and write the full texts there, then set `live_file: intake.md` again.
8. In `e-under-revision`, the user commits the as-submitted manuscript and runs `git tag -a submitted-<slug>-v<n> -m "as submitted"` (n = 1 at first intake, the next number on re-entry) as the dated baseline.
9. If the user holds a hold-out or new dataset that nobody has explored, they declare it now (or at stage 01) as a data-access.md row naming its path, with `outcome-level? no`; outside `a-data-only` this is the only route to a `confirmatory` label (stage 04).
10. Run the gate, commit as `intake: <slug>`, and set `live_file: data-inventory.md, SHA256SUMS` for stage 01.

## Gate (pass/fail)
Run gate commands from paper-workflow/ (the project root for Claude Code). Pass if every existing artefact is mapped to a stage output or marked out of scope, every gate S01–S10 has a status with its evidence, and every NOT-PASSABLE gate has its disclosure item queued.
- [ ] Every artefact the user named has an intake.md row, mapped to a stage output or `out of scope`.
- [ ] intake.md starts with `derives-from: none (first file)` and the four-column table header; every row has a date evidence entry (commit, file date, document date, or `none`).
- [ ] `entry_mode:` is one of the five mode strings, with the user's confirmation date.
- [ ] Every gate S00–S10 carries exactly one of `PASSED`, `RETRO-AUDIT`, `NOT-PASSABLE`, `OPEN`, a variant and an evidence pointer.
- [ ] S04 is `PASSED` only if a dated plan artefact predates outcome inspection; otherwise it is `OPEN` (`a-data-only`) or `NOT-PASSABLE`.
- [ ] Every NOT-PASSABLE gate has its line in the STATE.md disclosure queue; in modes b–e its full text is in disclosure.md.
- [ ] inbox.md and data-access.md exist with their headers; on a new paper inbox.md has zero rows (an existing paper keeps its rows).
- [ ] `e-under-revision`: `git tag -l 'submitted-<slug>-v*'` lists the baseline tag for this round, and `git cat-file -t` on it returns `tag`.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is intake.md (for example, a newly found artefact). Write the change list in plan mode and wait for user approval. Set `mode: propagate`, add or correct the intake.md rows first, then re-set the affected gate statuses and mark every downstream file `stale:` in STATE.md. Close each item by appending its row with status `CLOSED -> <file>@<commit>`, then set `mode: work`. A newly found artefact can raise a gate to `PASSED` only if it is dated before outcome inspection; S04 moves only for a dated prior plan.

## Evidence
- [F11] A: a data checkout/access log lets authors show that plans predate data access (basis for `PASSED` via a dated artefact, and for data-access.md).
- [F10] A: disclose prior knowledge of a dataset; use hold-out subsamples (step 9).
- [F16] A: retrospective registration cannot show decisions were prespecified (S04 never passed retrospectively; RETRO-AUDIT wording).
- [F13] A: late registration is common and rarely disclosed.
- [F1] A: transparent post hoc analysis belongs in a dedicated Discussion subsection.
- [F4] A UNVERIFIED: a disclosure statement is usable at any stage.
- [F23] A: deviations are reported with their effect, not hidden (version changes in `e-under-revision`).
- F, Entry scenarios: the stage mapping is F's construction; no source prescribes it (judgement call).
