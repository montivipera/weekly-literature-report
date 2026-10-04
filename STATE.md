# STATE.md — job state for "paper-workflow" design task

Re-read this file first after any /compact.

## Layout (decided 2026-10-04)
- `STATE.md` (this file): job state. Updated at the end of every phase.
- `research/<stream>.md`: Phase 1 outputs (A–E), max 150 lines each, English.
- `analysis/synthesis.md`: Phase 2 output (Opus), English.
- `paper-workflow/`: Phase 3 deliverable (after user approval). Its own `STATE.md` is a *template* for future papers, not this job's state.
- Final Turkish HTML report: Phase 5, published as an artifact.

## Model routing for this job
Sonnet 5.5 = research streams; Opus 5.5 = synthesis, structure drafting, fresh audit; Fable 5.1 = decisions at Checkpoint 1 and 2 only; Haiku 4.5 = formatting / consistency checks.
Higher models read only md outputs, never raw sources.

## Phase status
- [x] Phase 1 — Research (5 parallel Sonnet streams) — DONE 2026-10-04. Files: research/A..E (77–111 lines each). Haiku check: all ≤150 lines, sections present; 5 grade cells normalised (A UNVERIFIED = official source read via secondary copy; C UNVERIFIED = open question).
- [ ] Phase 2 — Synthesis (Opus) + Checkpoint 1 (Fable) → STOP, 10-line Turkish summary, wait for approval — IN PROGRESS
- [ ] Phase 3 — Build `paper-workflow/` (after approval)
- [ ] Phase 4 — Fresh Opus audit, fixes, Checkpoint 2 (Fable)
- [ ] Phase 5 — Turkish HTML report (≥5 inline SVGs)

## Decisions so far
- D1: research/ and analysis/ live at repo root beside paper-workflow/ so Phase 4 can audit the structure against the evidence files.
- D2: Evidence grades: A = official docs / peer-reviewed; B = systematic independent test; C = anecdote / blog.

## Open questions
- OQ1: Egress proxy denies CONNECT (403) to publisher/COPE/ICMJE/COS/arxiv hosts (e.g. www.elsevier.com, www.springer.com, publicationethics.org). Policy wording in research/D rests on search snippets, marked UNVERIFIED. Tell user at Checkpoint 1; fix is the environment's Network access setting.

## Next step
Opus writes analysis/synthesis.md (≤300 lines) from research/*.md only. Then Fable reviews, records decisions here, commits, and STOPS with a 10-line Turkish summary for user approval.
