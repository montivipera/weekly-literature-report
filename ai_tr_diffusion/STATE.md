# STATE.md — AI → Türkiye Diffusion Study

Working dir: `ai_tr_diffusion/`. Brief: `BRIEF.md` (Sections 1–9 define everything).
Planner: Fable (coordination only). Workers: Haiku (mechanical), Sonnet (scan/extract/draft/HTML), Opus (review, pre-decision advice).

## Status
- Current step: 1 — Tier A and Tier B inventories being built by two Sonnet agents (drafts/inventory_A.csv, drafts/inventory_B.csv). Plan approved by user 2026-10-03.
- Last updated: 2026-10-03

## Step plan (model per step)
| # | Step | Model | Status |
|---|------|-------|--------|
| 0 | Create STATE.md, inventory.csv, present plan | Fable | done (approved) |
| 1 | Build inventory: Tier A (~30–50) + Tier B (~15–25), one-line definitions | Sonnet ×2 (A, B in parallel) | in progress |
| 1r | Opus check of inventory coverage/gaps before scanning | Opus | pending |
| 2 | Per-item evidence: leader / analogue / TR status, driver scores (1–5 ×6), provisional class ×2 horizons, sources → inventory.csv + sources.csv | Sonnet ×N batches (~8–10 items each) | pending |
| 2h | URL verification of every source row (HTTP reachable, DOI resolves) | Haiku | pending |
| 3 | Review pass: Opus checks each classification vs Section 5 rules, flags disagreements → review_log.md | Opus | pending |
| 3r | Resolve disagreements (Fable decides, logs reasons in review_log.md; Haiku applies CSV edits) | Fable + Haiku | pending |
| 4a | Opus recommendation memo for synthesis (3 directions for Section 7 profile) | Opus | pending |
| 4b | Draft report_en.md sections (method, Tier A, Tier B, cross-cutting, references) | Sonnet | pending |
| 4c | Fable writes exec summary + synthesis; Opus reviews full report_en.md | Fable + Opus | pending |
| 5 | Build rapor_tr.html (plain Turkish, inline SVG: matrix, timeline, heatmap, 3 Tier B charts) | Sonnet | pending |
| 5h | Consistency check EN↔TR classifications; HTML self-contained check; Section 9 gates | Haiku + Opus | pending |
| 6 | Commit + push to `ccr-bf7d0111-jooe1h` | Fable | pending |

## Files
- BRIEF.md — the research brief (copy)
- STATE.md — this file
- inventory.csv — one row per development (schema in header)
- sources.csv — id,title,url,date_accessed,used_for,verified
- review_log.md — Opus disagreements + resolutions (created at step 3)
- report_en.md, rapor_tr.html — deliverables (steps 4–5)

## Open questions
- None yet (awaiting plan approval).

## Decisions log
- 2026-10-03: Driver scores on 1–5 scale; classification rule mapping to be fixed before step 2 (see inventory.csv header comment).
- 2026-10-03 (user): Do NOT read papers in full this session; abstracts/summaries suffice. Not an academic study, but what academia recommends matters and should be checked against global practice. Peer-reviewed sources used for direction and corroboration, not exhaustive reading.
- AGENT_RULES.md — shared rules + mechanical classification thresholds for all worker agents
- drafts/ — intermediate agent outputs (inventory_A.csv, inventory_B.csv, *_sources.csv)
