# STATE.md — AI → Türkiye Diffusion Study

Working dir: `ai_tr_diffusion/`. Brief: `BRIEF.md` (Sections 1–9 define everything).
Planner: Fable (coordination only). Workers: Haiku (mechanical), Sonnet (scan/extract/draft/HTML), Opus (review, pre-decision advice).

## Status
- Current step: 2 reruns running (r1 r2 r3 r4a r4b).
- Last updated: 2026-10-03

## Step plan (model per step)
| # | Step | Model | Status |
|---|------|-------|--------|
| 0 | Create STATE.md, inventory.csv, present plan | Fable | done (approved) |
| 1 | Build inventory: Tier A (~30–50) + Tier B (~15–25), one-line definitions | Sonnet ×2 (A, B in parallel) | done (A43, B22) |
| 1r | Opus check of inventory coverage/gaps before scanning | Opus | done (review_1_inventory.md) |
| 1c | Calibration: Sonnet scores 5 items (A01,A24,A39,B01,B18), Opus checks → exemplars for batch prompts | Sonnet + Opus | done (drafts/calibration_exemplars.md, scores_calib_reviewed.csv) |
| 2 | Per-item evidence: leader / analogue / TR status, driver scores (1–5 ×6), provisional class ×2 horizons, sources → inventory.csv + sources.csv | Sonnet ×N batches (~8–10 items each) | in progress (9 batches b1–b9) |
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

## Step 1c decisions (Fable, 2026-10-03) — all Opus proposals adopted
- R8-A: added d2=4 and d3=4 anchors (Likely was artificially rare because levels 4 were undefined). B01 moves to Likely/Likely under R8-A.
- tr_funded_pilot = funded OPERATIONAL pilot in TR only (R&D prototypes, trainings, committees = no).
- d1 horizon step = max(d1, level) not addition. A 3–5y Certain that rests only on the assumed +1 to d6 → Likely.
- Calibration final: A01 Pot/Pot (near-Likely), A24 Pot/Pot, A39 Cert/Cert, B01 Likely/Likely (R8-A; d6 recheck still owed), B18 Pot/Pot. Reviewed rows: drafts/scores_calib_reviewed.csv.
- Source fixes owed at merge: calib-027 attribution (hlc.com), calib-028/029 aggregators → primary, calib-008 → primary 2026–2030 Action Plan text.

## Step 2 batch map
b1 health+education: A02 A03 A04 A49 A08 A09 A10 A50 | b2 finance+retail+law: A05 A06 A07 A45 A46 A34 A35 A30 A32 | b3 public_admin+cross_cutting: A11 A12 A13 A48 A40 A41 A42 A44 | b4 agriculture+energy: A14 A15 A16 A47 A17 A18 A19 | b5 manufacturing+logistics+media: A20 A21 A22 A23 A25 A26 A27 A28 A29 | b6 labour_market: A36 A37 A38 A51 | b7 ecology: B02 B03 B04 B05 B06 B07 B09 B23 B24 (+B01 d6 recheck) | b8 academia: B10 B11 B12 B13 B14 B15 B25 | b9 civil_society: B17 B19 B20 B21 B22 B26 B27

## Step 2 incident (2026-10-03)
- b7 (ecology) stopped: WebSearch budget exhausted ("200 of 200 per session") mid-B04. Scored: B02 Likely/Likely, B03 Likely/Likely (d3=4 borderline → Opus), B04 PROVISIONAL (rerun needed). Not scored: B05 B06 B07 B09 B23 B24. B01 recheck: suggest d6=2 (TRDizin Aras CNN/LSTM paper; İTÜ ARIS lab unverified), class unchanged.
- Risk: if the 200-search cap is shared session-wide, other batches will hit it too. Awaiting other hand-backs; user to be told. Fallback: Consensus/Scholar Gateway MCP + Haiku-free reruns in a fresh session.
- b6 done (4/4): A36 Cert/Cert (d6=4 on LinkedIn/World Bank data — Opus to confirm), A37 Pot/Pot, A38 Pot/Pot (largely unsourced estimate), A51 Pot/Pot (d1 borderline 3/4: AI Act Annex III employment 2 Dec 2027; KVKK Art.11 unverified → Opus). b6 also hit the 200-search cap near the end.
- b1 done but DEGRADED: A02 Cert/Cert (high), A50 Cert/Cert (AI Act Art.4; check Omnibus), A03 Pot/Pot (med); A04 A49 A08 A09 A10 Pot/Pot at LOW confidence — no TR/analogue web search (budget). RERUN LIST (TR + analogue search only): A04 A08 A09 A10 A49, plus A50 Omnibus check, A02 analogue URL check.
- b9 done but DEGRADED: B17 Pot(near-Likely)/Likely, B19 Pot/Pot, B20 Cert/Cert (borderline: d6=4 rests on Melikgazi MEGA + vendor-only İBB; if İBB dropped → Pot near-Likely; Opus), B21 B22 B26 B27 Pot/Pot LOW (Consensus only). RERUN LIST (TR + analogue): B21 B22 B26 B27.
- b5 done but DEGRADED: A20 Cert/Cert, A22 Cert/Cert, A29 Cert/Cert (Omnibus Art.50 grace-period check), A21 Pot/Pot; A23 A25 A26 A27 A28 Pot/Pot LOW (no TR search). RERUN LIST: A23 A25 A26 A27 A28.
- b4 done (DEGRADED tail): A14 Cert/Cert, A15 Likely/Likely (d3=4 on FAO cost figure, unconfirmed page), A16 Pot(near-Likely)/Likely, A47 Cert/Cert (shaky: DSİ "AI-supported" label; Opus), A17 Likely/Likely; A18 A19 Pot/Pot LOW. RERUN LIST: A18 A19 (+A17 EPDK/TEİAŞ check).
- b8 done (DEGRADED): B14 Cert/Cert (governance item; d6=4 on YÖK/TÜBİTAK guides — Opus to rule whether policy existence = "present"); B10 B11 B12 B13 B15 B25 Pot/Pot (analogue counts = "none sourced"). RERUN LIST (analogue + TR): B11 B15 (likeliest flips), B12 B13 B25.
- b3 done (DEGRADED tail): A12 Cert/Cert (d6=4 on KURGAN/GİB press; Opus), A11 Pot(near-Likely)/Likely, A40 Pot(near-Likely)/Likely (BİLGE announced, HAVELSAN MAIN vendor-only; Opus to rule d6/d2), A13 Pot/Pot; A41 A42 A44 A48 Pot/Pot LOW. RERUN LIST: A41 A42 A44 A48. Dedupe calib-008 vs b3 row at merge.
- Only b2 (finance+retail+law) outstanding.
- b2 done (DEGRADED tail): A06 A45 A46 A34 Cert/Cert (A06 d6=4 press-level; Opus), A05 Pot/Pot (scope question: agentic vs generic fraud detection → planner: keep agentic scope as defined), A07 Pot(near-Likely)/Pot, A32 Pot/Likely; A35 A30 Pot/Pot LOW. RERUN LIST: A30 A35 A32.
- ALL 9 BATCHES IN. Haiku merging → inventory.csv, sources.csv, drafts/merge_log.md.

## Consolidated RERUN LIST (TR baseline + analogue searches only; needs raised WebSearch cap)
A04 A08 A09 A10 A49 A50(Omnibus Art.4) | A18 A19 A17(EPDK) | A23 A25 A26 A27 A28 | A41 A42 A44 A48 | A30 A35 A32 | B04(provisional) B05 B06 B07 B09 B23 B24 (not scored at all) | B21 B22 B26 B27 | B11 B15 B12 B13 B25
= 6 unscored Tier B items + ~28 degraded items.
## Opus review flags collected (step 3 input)
A36 d6=4?, A51 d1 3/4, A02 analogue URLs, A50 Omnibus, A29 Omnibus Art.50, B20 d6 3 vs 4, B17 3-5y, B14 governance=present?, A12 d6 press-only, A40 d6/d2, A47 DSİ AI label, A15 FAO cost figure, A06 d6 press-level, B03 d3=4, A21 mean 2.0 borderline, B25 near-Low.
- MERGE DONE: inventory.csv 73 rows (67 scored), sources.csv S001–S500. Class dist 1-2y: C16/L4/P47 (6 blank); 3-5y: C16/L9/P42. Haiku's NEEDS_RERUN flag hit 66 rows (over-inclusive regex) — the consolidated RERUN LIST above is authoritative.
- B01 still Potential/Potential in master: scores_calib_reviewed.csv predates R8-A adoption (Opus said B01 → Likely under R8-A if d3=4 is sourced). → step 3 Opus review item.

## Step 3 (part 1 of 2) — Opus review of 36 robust rows → review_log.md. 27 agree / 4 disagree / 5 open.
Planner decisions (Fable, 2026-10-03):
- P1 ACCEPT: tr_funded_pilot = yes when a primary source shows a real operational deployment with users; no budget figure required. (B20 stays Certain via third clause with d6=3.)
- P2 ACCEPT: Biodiversa+ BiodivConnect call (S108) = d2 4 for biodiversity-monitoring items (R8-A anchor met). B01 → Likely/Likely, B17 → Likely/Likely. Correction: B01's Likely route is d2 (not d3) as earlier noted.
- P3 DECIDE: conformity requirement that is a precondition to market access (A02 MDR-harmonised devices) = d1 4; permissive type approval that only enables (A24) = d1 3. Both current scores stand; rule text clarified.
- P4 ACCEPT: governance items (A29, A39, A45, B14) get tag GOVERNANCE in notes and are labelled "in place (rule), not a deployed technology" in the report.
- P5 DEFINE new sub-label: "Likely (lag-based)" = 3–5y Likely reached only via the Certain→Likely guard (assumed analogue→TR lag). Reported as Likely with this qualifier; defined explicitly in report §2 (brief §5 allows defined additions). Applies A11, A16, A40, B17(if via guard), A32.
- P6 ACCEPT: scores must evidence the AI component itself. A46 → Potential/Likely(near-Likely) with d6 3; A15 → Potential/Potential near-Likely (FAO figure headline-only → d3 3); A22 d6 4→3 (class unchanged); A47 → open, rerun search.
- P7: class-neutral data fixes → Haiku.
- Open (one search each, added to RERUN LIST): A06, A12, A40, A47, B10, B17 (iNaturalist TR volume).
- Resolutions part 1 APPLIED to inventory.csv and review_log.md. Dist 1-2y: C15/L5/P47/blank6; 3-5y: C15/L10/P42/blank6.
- Step 3 part 2 (Opus review of the 37 rerun rows) happens after reruns.

## Step 2 RERUNS (2026-10-03, user: "web araması da yap")
- WebSearch cap found RESET on the new user turn (test query succeeded). Launched 5 rerun agents with strict per-agent budgets (total ≈160): r1 ecology unscored (B04 B05 B06 B07 B09 B23 B24, ≤52 searches), r2 six open targeted searches (A06 A12 A40 A47 B10 B17, ≤12), r3 degraded Tier B (B21 B22 B26 B27 B11 B15 B12 B13 B25, ≤38), r4a degraded Tier A (A04 A08 A09 A10 A49 A50 A18 A19 A17 A23 A25, ≤34), r4b degraded Tier A (A26 A27 A28 A41 A42 A44 A48 A30 A35 A32, ≤31). Outputs drafts/scores_r*.csv + sources_r*.csv → Haiku merge → step 2h → step 3 part 2.
