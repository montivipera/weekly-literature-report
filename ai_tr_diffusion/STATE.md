# STATE.md — AI → Türkiye Diffusion Study

Working dir: `ai_tr_diffusion/`. Brief: `BRIEF.md` (Sections 1–9 define everything).
Planner: Fable (coordination only). Workers: Haiku (mechanical), Sonnet (scan/extract/draft/HTML), Opus (review, pre-decision advice).

## Status
- Current step: 1c — calibration batch (A01,A24,A39,B01,B18) being scored by Sonnet → drafts/scores_calib.csv; next: Opus checks it, then step 2 fans out in ~8 batches of 8–10 items using SCORING_TASK.md.
- Last updated: 2026-10-03

## Step plan (model per step)
| # | Step | Model | Status |
|---|------|-------|--------|
| 0 | Create STATE.md, inventory.csv, present plan | Fable | done (approved) |
| 1 | Build inventory: Tier A (~30–50) + Tier B (~15–25), one-line definitions | Sonnet ×2 (A, B in parallel) | done (A43, B22) |
| 1r | Opus check of inventory coverage/gaps before scanning | Opus | done (review_1_inventory.md) |
| 1c | Calibration: Sonnet scores 5 items (A01,A24,A39,B01,B18), Opus checks → exemplars for batch prompts | Sonnet + Opus | in progress |
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
- SCORING_TASK.md — step 2 instructions for scoring agents (outputs to drafts/scores_<batch>.csv, drafts/sources_<batch>.csv; planner merges)
- AGENT_RULES.md — shared rules + mechanical classification thresholds for all worker agents
- drafts/ — intermediate agent outputs (inventory_A.csv, inventory_B.csv, *_sources.csv)

## Step 1 notes (Tier A agent hand-back, 2026-10-03)
- 43 items (A01–A43), 23 URLs. Thin sectors: agriculture, law, energy, retail; A41 (freelance AI-service models) unsourced so far.
- (ID-corrected by Opus review) Flags referred to A29 vs A39, A21 vs A20 (humanoids), A38 (freelance, unsourced). Decisions in review_1_inventory.md §3.
- Secondary anchors to replace in step 2: WEF via etradeforall reprint; Gibson Dunn, Bolster, Asian Banker, Malay Mail, ai2.work, TNW, Yahoo Finance, Moroğlu Arseven. TR Action Plan 2026–2030 / TÜBİTAK facts came from search summaries only → verify in step 2.

## Step 1 notes (Tier B agent hand-back, 2026-10-03)
- 22 items (B01–B22): ecology 9, academia 7, civil society 6. 36 URLs. Strong examples: B01 BirdNET/Perch, B02 MegaDetector/SpeciesNet, B05 EO foundation models, B10 Elicit/Consensus, B15 integrity screeners, B17 iNaturalist/Pl@ntNet.
- Verify in step 2: B08 ESRS E4 Omnibus facts (vendor blog only), B20 İBB assistant (search summary only), B11 DOI seen only via Consensus. Possible merges: B16→B14, B10/B11 overlap. B21 DataKind weak.
- Step 1r: Opus coverage review running → drafts/review_1_inventory.md

## Step 1r decisions (Fable, 2026-10-03) — all Opus recommendations accepted
- Tier A: 43 + 8 adds − 3 merges (A43→A40, A07+A33, A30+A31) = 48. Tier B: 22 + 5 adds + B04 split − 2 merges (B08→B07, B16→B14), restoration-prioritisation folded into B06 = 25. Total 73. No drops; tourism excluded (not in brief §2; note in limitations).
- Rule 8 replaced: precedence Certain → Low → Likely → Potential; driver anchors; new fields analogue_count, tr_funded_pilot, barrier, class_branch; dated horizon adjustment. Decision: private/consumer spend counts as "funding attached" via d6 ≥ 4 branch.
- IDs are stable (no renumbering); new rows A44+, B23+.
- inventory.csv now 73 rows × 25 cols (A48, B25); sources.csv S001–S059. Build log: drafts/inventory_build_log.md.

## Step 1c notes (calibration hand-back, 2026-10-03)
- 5 items scored: A01 Pot/Pot (near-Likely), A24 Pot/Pot, A39 Cert/Cert, B01 Pot/Pot (near-Likely, d6=1 doubtful), B18 Pot/Pot. 48 new sources (calib-001..048).
- Decisions: enabling regulation = d1 3 (A24 stays Potential); scores capped at 5; outbound HTTP (curl/WebFetch) is BLOCKED by environment network policy → URL verification must rely on WebSearch results; logged as a method limitation. User to be told (can widen network access in environment settings).
- Concern for Opus check: 4/5 landed in Potential — is the rule too Potential-heavy, or is the sample biased?
