# Stage 03 — Question framing
Goal: generate many candidate research questions from the inventory and the scan, let the user rank and choose a few, and log every candidate with its origin.

## Entry modes
- Normal in `a-data-only`.
- RETRO-AUDIT in `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`: rebuild questions.md from dated artefacts instead of generating candidates. Each existing question or hypothesis gets the date it first appears and a mark showing whether that date precedes the first outcome result. Anything first dated after a result is `post hoc` [F1, F2]. In `c-half-draft` this includes the Introduction audit: orphan claims (no question, no analysis) are flagged. Questions the user adds now are candidates like any other, all marked `post hoc`.
- NOT-PASSABLE: not by mode. If no dated artefact shows when a question was chosen, mark it `post hoc` and queue the disclosure item "how the question was chosen".

## Inputs · Live file(s) · Outputs
- **Inputs:** data-inventory.md, scan-notes.md (key rows), the `prior_exposure:` statement in STATE.md. No results, no raw data.
- **Live file:** `questions.md`.
- **Outputs:** `questions.md`, header `derives-from: data-inventory.md@<short-commit>, scan-notes.md@<short-commit>`, then two tables:
  - Candidates: `C-ID | question | origin: literature|data|advisor | inventory variables used | scan rows (SCnn) | design note (n per unit, dependence) | user rank | chosen (yes/no)`.
  - Chosen RQs: `RQ-ID | C-ID | question | origin: literature|data|advisor | rationale (one line linking the question to theory or a scan row) | chosen by user (date) | post hoc (RETRO-AUDIT only)`.

## Model and agent
- Main session (Opus 5.5, effort high) does this stage itself: open-ended judgement, the suggested starting model for such work [A5]. It reads md hand-off files only (about 5k tokens). No subagent.
- The user ranks and chooses. The model never ranks, scores or recommends its own candidates, because models fail at evaluating their own ideas [A24].

## Procedure
1. Set `live_file: questions.md`; main session reads data-inventory.md, the key rows of scan-notes.md and the prior-exposure statement, and nothing else.
2. Main session writes at least 15 candidate questions (judgement call) that span the variables, the design and the scan's concept blocks, listed in inventory order with no ranking.
3. Each candidate names the inventory variables and scan rows it rests on and a design note from n per unit and dependence, never from outcome values.
4. Ideas from the user or an advisor are added as candidates with `origin: data` or `origin: advisor`; `origin: literature` needs at least one RESOLVED scan row.
5. When the prior-exposure level is `outcome-looked` or higher, every `origin: data` candidate is noted as possibly shaped by results.
6. The user ranks the candidates and chooses at most 4 RQs (cap is a judgement call against question trolling [C4]); more than 4 needs a one-line reason in questions.md.
7. Main session writes the origin tag and a one-line theoretical rationale for each chosen RQ [C2, C13], and the user confirms the wording.
8. Unchosen candidates stay in the table with `chosen: no`, so every candidate is logged.
9. Run the gate, commit, and set `live_file: method-rationale.md` for stage 04.

## Gate (pass/fail)
- [ ] At least 15 candidates are logged, and `git log -p -- questions.md` shows no candidate row deleted.
- [ ] No candidate row cites a result, effect or p-value; each cites only inventory variables and scan rows.
- [ ] The table has no model-assigned score or order column; the `user rank` values were entered by the user.
- [ ] At most 4 RQs are chosen, or the reason for more is recorded.
- [ ] Each chosen RQ has an `origin: literature | data | advisor` tag, a one-line rationale and the user's selection date.
- [ ] Each `origin: literature` RQ cites at least one RESOLVED scan-notes.md row.
- [ ] RETRO-AUDIT: each RQ has its first-seen date and a `post hoc` mark where that date follows a result; orphan claims are listed (`c-half-draft`).
- [ ] questions.md starts with its derives-from header.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is questions.md or an upstream file. Write the change list in plan mode and wait for user approval. Set `mode: propagate` and edit upstream files first (data-inventory.md, scan-notes.md), then questions.md: a new idea is appended as a new candidate, never as an edit to a chosen RQ. Mark method-rationale.md and every later file `stale:` in STATE.md. Close each item by appending a CLOSED row with its pointer, then set `mode: work`. After the plan tag, a new RQ can only be exploratory and becomes a deviations.md row at stage 05.

## Evidence
- [A24] A: LLM ideas are rated more novel but less feasible, lack diversity, and models fail at self-evaluation.
- [A5] A: Anthropic's selection rule starts with Opus 5.5 for open-ended work.
- [C4] A: question trolling across many relationships gives substantial upward bias.
- [C2] A: three HARKing forms, including hypotheses from a post hoc literature search.
- [C13] A: an exploratory/confirmatory split does not repair a weak theory-to-hypothesis link.
- [C33] A: formulating relevant questions against the data is step one of the Zuur & Ieno protocol.
- [F2] A: the wrong in HARKing is the misrepresentation of when a hypothesis arose.
