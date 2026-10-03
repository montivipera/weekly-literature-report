# Opus review log (brief §6 step 3, §9 gate)

- **Date:** 2026-10-03
- **Reviewer:** Opus review agent (desk review; web search unavailable, budget exhausted)
- **Scope:** part 1 of 2. 36 rows not on the consolidated RERUN LIST: A01 A02 A03 A05 A06 A07 A11 A12 A13 A14 A15 A16 A20 A21 A22 A24 A29 A34 A36 A37 A38 A39 A40 A45 A46 A47 A51 B01 B02 B03 B10 B14 B17 B18 B19 B20. The 37 rerun rows are reviewed in part 2.
- **Method:** I re-ran rule 8 (C1→C4, horizon adjustment, the projected-Certain guard, cap at 5) on all 36 rows with a script. I checked each score of 4 or more and each score of 1 against the R8-A anchors, the planner clarifications and the cited S-ids in `sources.csv`, and resolved every STATE.md flag. `inventory.csv` was not edited.
- **Result:** the 1–2y class recomputes correctly from the recorded scores in all 36 rows, and every 3–5y adjustment was applied correctly. Disagreements come from score support, not arithmetic. **27 agree, 4 disagree, 5 open** (evidence too thin to decide; current class kept provisionally).

## Row verdicts

| id | current 1-2y / 3-5y | Opus verdict | reason (≤25 words) | action |
|---|---|---|---|---|
| A01 | Potential / Potential | agree | Calibration item. RCT −9.5% keeps d3 at 3; d6 2 (vendor pages only). Mechanics correct. | none |
| A02 | Certain / Certain | agree | C1 fires twice: d1 4 (TR MDR) and d6 4 (Hevi 35 hospitals, TÜSEB protocol). d3 4 sourced: MASAI −44% reading workload. | none (check analogue URLs in step 2h; d1 basis → P3) |
| A03 | Potential / Potential | agree | TR evidence is vendor offers only, and the voice-agent savings are vendor claims (d3 3). The title "via MHRS public deployment" has no evidence behind it. | planner decision (retitle, P7) |
| A05 | Potential / Potential | agree | Scored on agentic scope per the planner. No analogue shows agentic AML. Unsearched d1/d2 = 2, per exemplar rule 1. | none |
| A06 | Certain / Certain | open (keep provisionally) | d6 4 rests on a 2023 magazine piece and a column. The only alternative-data evidence is KKB Web Score. With d6 3 → Potential/Potential. | rerun search: "KKB alternatif veri kredi skoru bankalar kullanım 2025" |
| A07 | Potential / Potential | agree | Near-Likely flag is correct (BR/MX first live transactions, vendor-reported). Nothing supports d2 or d3 ≥ 4. | none |
| A11 | Potential / Likely | agree | Mechanics correct. 3–5y Likely comes only from the guard (d6 3+1); there is no strong pull (d2 3, d3 3). | planner decision P5 |
| A12 | Certain / Certain | open (keep provisionally) | d6 4 rests on a tax-news site plus a snippet, tax domain only. Certain holds if a primary VDK/GİB source confirms AI triage in production. | rerun search: "Vergi Denetim Kurulu yapay zeka destekli risk analizi KURGAN faaliyet raporu" |
| A13 | Potential / Potential | agree | The Korean AI-NEXT item is at procurement stage, not live, so analogue_count should be 0 (rule 6). Class unchanged. | none (data fix) |
| A14 | Certain / Certain | agree | A ministry primary page shows the AI-assisted Ürün İzleme Sistemi in operation since 2025 → d6 4. tr_funded_pilot would be yes under P1 (no class effect). | none |
| A15 | Likely / Likely | **disagree → Potential / Potential (near-Likely)** | d3 4 rests on the FAO "$30→$3" figure from a search summary with unconfirmed attribution. The A24 precedent keeps headline-only magnitudes at 3. | rerun search: "FAO generative AI agricultural advisory cost per farmer 30 to 3 dollars" |
| A16 | Potential / Likely | agree | Vendor "80%" stays 3; the independent 23–28% figure is below band. 3–5y Likely via the guard. | planner decision P5 |
| A20 | Certain / Certain | agree | Robust: d6 4 (IFR stock) or the C1 third clause (Arçelik operations, HIT-30 d2 4). The AI share of the robot stock is unsourced. | planner decision P6 |
| A21 | Potential / Potential | agree | mean(d4,d5) is exactly 2.0, so C2 does not fire. Both are unsourced 2s, so the result is fragile, but no barrier is sourced. | none |
| A22 | Certain / Certain | agree (score fix) | Only Arçelik is confirmed, so d6 should be 3, not 4. Certain still holds via the C1 third clause (funded yes from Arçelik primary bulletin, d2 3). | none (data fix: d6 3, branch) |
| A24 | Potential / Potential | agree | Calibration item. The enabling type-approval rule gives d1 3; a prototype run is not a funded pilot. | none |
| A29 | Certain / Certain | agree | Art. 50 reaches TR providers with EU-used output from 2 Aug 2026. A grace period for legacy marking would not lower d1 below 4 within 2026–28. | none (step 2h: confirm Omnibus Art. 50 date in OJ text) |
| A34 | Certain / Certain | agree | Company-reported AI personalisation at Trendyol, Hepsiburada and Migros supports d6 4. The dynamic-pricing half is thinner; report should say so. | none |
| A36 | Certain / Certain | agree | AI/ML roles are listed across many employers (Indeed TR), and World Bank LinkedIn data shows presence beyond pilot. Governance roles are thinner. | none |
| A37 | Potential / Potential | agree | Exposure estimates are not observed decline. d6 2 and 0 analogues; Potential is the correct default. | none |
| A38 | Potential / Potential | agree (low confidence) | Mostly unsourced, but nothing points to d6 ≥ 4 or any pull ≥ 4. Potential is the correct default. | none |
| A39 | Certain / Certain | agree | Calibration item. Under adopted D3 the 3–5y d1 should read max(4,4) = 4, not "4+4 capped at 5". | none (data fix: notes/branch text) |
| A40 | Potential / Likely | open (keep provisionally) | d6 3 vs 4 depends on whether several orgs run Turkish LLMs in production beyond BİLGE/MAIN, which was not searched. With d6 4 → Certain/Certain. | rerun search: "Türkçe büyük dil modeli kurumsal kullanım Turkcell Trendyol T3AI 2026" |
| A45 | Certain / Certain | agree | The BDDK remote-ID regulation requires liveness checks (d1 4), and remote onboarding has been routine since 2021 (d6 4). The class is robust. | none (d1 basis → P3) |
| A46 | Certain / Certain | **disagree → Potential / Likely (near-Likely)** | Only an Aksigorta self-report evidences AI claims. TARSİM states no AI; Anadolu is undated future tense. So d6 3, funded no; 3–5y via guard. | rerun search: "sigorta hasar tespiti yapay zeka fotoğraf Türkiye sigorta şirketleri 2026" |
| A47 | Certain / Certain | open (keep provisionally) | Certain rests on one ministry item's "AI-supported" label, and ML scheduling is unverified. If not confirmed: d6 2 → Potential/Potential. | rerun search: "DSİ sulama otomasyonu yapay zeka sulama planlaması 4.200 hektar" |
| A51 | Potential / Potential | agree | Annex III (2 Dec 2027) reaches only EU-market HR-tech providers. KVKK Art. 11(1)(g) constrains use but does not pull adoption, so d1 3. | none |
| B01 | Potential / Potential | **disagree → Likely / Likely** | R8-A: d3 stays 3 (no ≥25% time figure in sources). The planner-adopted d2 4 via S108 → C3 Likely. The branch text still says d6 1. | planner decision P2 |
| B02 | Likely / Likely | agree | d3 4 is sourced (PNAS: 99.3% of labelling automated). C3 is correct; 3–5y Likely via the guard. | none |
| B03 | Likely / Likely | agree | d3 4 is sourced (peer-reviewed −33% and −50% cost), but the saving comes from eDNA, not ML. Under P2, d2 4 keeps Likely regardless. | planner decision P6 (P2 makes it moot) |
| B10 | Potential / Potential | open (keep provisionally) | If the EKUAL national licence includes an AI research assistant (Scopus AI or WoS), d6 would be 5 with public funding → Certain/Certain. | rerun search: "EKUAL Scopus AI Web of Science Research Assistant erişim ULAKBİM" |
| B14 | Certain / Certain | agree | For a governance item the rule is the development. The YÖK national guide, university guides and the TÜBİTAK rule mean it is present in several orgs. | planner decision P4 |
| B17 | Potential / Likely | **disagree → Likely / Likely (if P2)** | Cites the same S108 as B01, so consistency gives d2 4 → C3. d1 1 should be 2 (no regulation-targeted search). | planner decision P2; rerun search: "iNaturalist Türkiye gözlem sayısı 2026" |
| B18 | Potential / Potential | agree | Calibration item; unchanged. | none |
| B19 | Potential / Potential | agree | Training and an AI office make an active group (d6 3) but not an operational assistant. 1 analogue. | none |
| B20 | Certain / Certain | agree (score fix; conditional on P1) | The Istanbul leg is vendor-only → d6 3. Melikgazi's municipal page shows production use → funded yes under P1 → C1 third clause Certain. | planner decision P1 |

### B01 re-evaluation under R8-A (requested item)
- **d3 stays 3.** No B01 source gives a sourced ≥25% staff-time or cost saving. S097 says acoustic surveys are cost-effective against point counts but not for small surveys. S092 shows accuracy parity with experts, not time saved. S013/S015/S016/S095/S099 describe tools or scale. The d3 route to Likely is not available.
- **STATE.md misstates the 1c finding.** Review 1c (`drafts/review_1c_calibration.md` §1 and §4) moved B01 to Likely through **d2 = 4**, not d3. The basis is BiodivConnect 2025–26 (S108), which is open to TR via TÜBİTAK 1071 with a "measuring restoration success" topic, edition within 24 months. The planner logged "B01 moves to Likely/Likely under R8-A". The master row was never updated.
- **Recomputed:** d = 1/4/3/4/3/2 (d6 2 after the b7 recheck, S500), analogues 2, mean(d4,d5) 3.5. At 1–2y: C1 fails, C2 fails, C3 matches → **Likely**. At 3–5y: d6 2+1 = 3, C1 fails → C3 → **Likely**.
- **Consistency risk:** B02, B03 and B17 cite the same S108 at d2 3. If S108 qualifies for B01, the same reading applies to them, so P2 is a single decision for all four.

## Systemic observations
- **tr_funded_pilot is applied inconsistently.** A20, A22 and A47 set yes for operational deployments without a budget figure. A12, A14, A46, A51 and B20 set no because "no budget line seen". This decides B20, and A12/A46 at d6 3 (→ P1).
- **Press-level d6 = 4.** In A06, A12, A22, A46 and B20, "several orgs" rests on one primary source plus press, vendor or column items. A22 and B20 drop to d6 3. A46 drops and changes class. A06 and A12 need a search.
- **The C1 third clause is permissive.** Horizon Europe association makes d2 = 3 available for almost any item. Once d2 is 3, Certain needs only d6 3 and a "yes", so the P1 definition carries the Certain/Potential boundary.
- **Governance items as "present".** A29, A39 and A45 are Certain through a binding obligation, which is correct. B14 is Certain through d6 on soft guidance. That is valid for a rules item, but the report should label these "in place (governance)", not adoption (→ P4).
- **Gate/conformity regulations are scored inconsistently.** The A02 medical-device registration (d1 4) and the A24 AV type-approval (d1 3) are both conformity gates for the AI product. A45 differs because it mandates an AI technique (liveness) for a widespread activity. No class effect in this scope (→ P3).
- **Omnibus dependencies.** A29 (Art. 50 timing), A39 (3–5y d1 via the 2 Aug 2028 Annex I date) and A51/A06/A12 (Annex III 2 Dec 2027) all take their dates from a law-firm digest (S042) and secondary notices (S112/S113). None comes from OJ text. No class effect here; confirm in step 2h.
- **Likely at 3–5y via the projected-Certain guard.** A11, A16, A40 and B17, and the 3–5y side of B02/B03, become Likely through the guard. A11, A16, A40 and B17 have d2 and d3 ≤ 3, so they do not meet brief §5's "strong cost or funding pull" criterion as written (→ P5).
- **AI attribution.** In A20 (robot stock), A46 (TARSİM satellite imagery), A47 ("AI-supported" automation), B03 (eDNA cost) and partly A14, d3/d6 evidence concerns the non-AI part of a bundled item (→ P6).
- **Headline magnitudes.** A15 is the only in-scope item whose class rests on an unconfirmed figure. That is inconsistent with the A24 exemplar ("up to 40%", headline only → d3 3).
- **Unsearched d1/d2 = 2 cluster in Tier A labour and finance** (A05, A06, A07, A34, A36, A37, A38, A45, A51). This has no class effect today. Under P1, A51 (corporate rollout, d6 3) would become Certain if a generic d2 = 3 were sourced, so the d2 default matters.

## Planner decisions required
- **P1 – Definition of tr_funded_pilot for production deployments.** Proposed rule: yes for a production deployment with real users documented by a primary source (the deployer's own or an official page, or a filing). A budget figure is not required. Headline-only, column or vendor-only evidence = no. Effects: B20 stays Certain (otherwise Potential near-Likely / Likely); A14 funded yes (no class effect); A12, A46 and A51 stay no.
- **P2 – Does S108 (BiodivConnect 2025–26, "measuring restoration success") meet R8-A d2 = 4 for monitoring-technology items?** If yes: B01 → Likely/Likely and B17 → Likely/Likely; B02 and B03 move to d2 4 with no class change. If no: reverse the step-1c log entry for B01 and record why. In either case, correct STATE.md, which says the route is d3; it is d2.
- **P3 – d1 for conformity gates.** Proposed: 3 for product-conformity or type-approval gates (A02, A24); 4 where the regulation mandates the AI technique as a condition of a widespread activity (A45). No class effect in this scope.
- **P4 – Governance items.** Accept rule adoption by several organisations as d6 ≥ 4 (B14), and label A29, A39, A45 and B14 as "in place (governance)" in the report.
- **P5 – 3–5y Likely via the guard.** Either keep it and define it in the report as "Likely (projected from analogue lag; no strong pull)", or add an explicitly defined group per brief §5. Affects A11, A16, A40 and B17.
- **P6 – AI attribution.** Should d3/d6 evidence the AI component, or may a bundled item be scored as a whole? Affects A20, A46, A47 and B03 (B03 is moot if P2 = yes).
- **P7 – Housekeeping, for Haiku after decisions, no class effects.** A03 retitle (drop "via MHRS public deployment"). A13 analogue_count 1→0. A22 d6 4→3 and branch text. A39 3–5y d1 text → max(4,4) = 4. B01 branch text (d6 2, 3–5y d6 3). B17 d1 1→2.
- **Open rows for the part-2 rerun session (one search each, listed in the table):** A06, A12, A15, A40, A46, A47, B10, B17.

## Resolutions (planner, 2026-10-03, part 1)

### Applied decisions and changes

**P1 – Definition of tr_funded_pilot for production deployments:**
- **Decision:** Accept. tr_funded_pilot = yes when a primary source shows a real operational deployment with real users documented by a primary source (the deployer's own or an official page, or a filing). Budget figure not required. Headline-only, column or vendor-only evidence = no.
- **Applied to:** B20 (Melikgazi MEGA operational deployment → tr_funded_pilot yes, class unchanged Certain/Certain via C1 third clause with d6=3).

**P2 – BiodivConnect S108 as d2 = 4 for monitoring-technology items:**
- **Decision:** Accept. S108 (Biodiversa+ BiodivConnect 2025–26 call, "measuring restoration success") meets R8-A d2 = 4 anchor. Correction: B01's route to Likely is d2 (not d3 as STATE.md mislabelled).
- **Applied to:** B01 → d2 4, class Likely/Likely (C3); B17 → d2 4, d1 2, class Likely/Likely (C3). B02, B03 d2 remains 3 (S108 cited but consistency check deferred).

**P3 – d1 for conformity gates:**
- **Decision:** Accept. d1 3 for product-conformity or type-approval gates (A24 enables but does not mandate); d1 4 where regulation mandates the AI technique as condition of widespread activity (A45 liveness for KYC). No class change in this scope.
- **Applied to:** No Opus-review rows affected by P3 changes; decision logged for future use.

**P4 – Governance items:**
- **Decision:** Accept. Rule adoption by several organisations counts as d6 ≥ 4. Label governance items "in place (rule)" in report, not deployed technology. Tag notes with "GOVERNANCE ".
- **Applied to:** A29, A39, A45, B14 → prepended "GOVERNANCE " to notes.

**P5 – Sub-label for 3–5y Likely via the guard:**
- **Decision:** Define "Likely (lag-based)" = 3–5y Likely reached only via the Certain→Likely guard (assumed analogue→TR lag with d6+1). Reported as Likely with this qualifier.
- **Applied to:** A11, A16, A40, A32, A46 → appended " [Likely (lag-based)]" to class_branch.

**P6 – AI attribution (scores evidence AI component):**
- **Decision:** Accept. d3/d6 evidence must be for the AI component itself, not bundled items. Results:
  - A15 → d3 4→3 (FAO cost figure headline-only, not sourced) → class Potential/Potential near-Likely.
  - A46 → d6 4→3 (only Aksigorta self-report; TARSİM states no AI) → class Potential/Likely.
  - A22 → d6 4→3 (only Arçelik confirmed; class unchanged Certain/Certain via C1 third clause with tr_funded_pilot=yes).
  - A47 → Open, rerun search.

**P7 – Class-neutral data fixes:**
- **Fixes applied:**
  - A03: Title "via MHRS public deployment" noted as unsourced (decision to retitle is editorial, noted in review_log).
  - A13: analogue_count 1→0 (Korean AI-NEXT is procurement stage, not live).
  - A22: d6 4→3, class_branch → "C1 third clause (d6=3, tr_funded_pilot=yes, d2=3)".
  - A39: class_branch "4+4 capped at 5" → "max(4,4) = 4".
  - B01: class_branch branch text corrected (d6 2 [sourced], 3–5y d6 assumed 3).
  - B17: d1 1→2 (no regulation-targeted search yet; placeholder score).

### Summary of disagreement resolutions

| Item | Opus verdict | Planner decision | Final class | Reason |
|---|---|---|---|---|
| A15 | d3 4 → 3 (headline) | P6: AI attribution | Potential/Potential | FAO $30→$3 figure not sourced to primary. |
| A46 | d6 4 → 3 (self-report only) | P6: AI attribution | Potential/Likely | Only Aksigorta self-report; TARSİM no AI. 3–5y Likely via guard. |
| B01 | d2 route, not d3 | P2: S108 = d2 4 | Likely/Likely | BiodivConnect S108 meets d2 anchor. |
| B17 | d2 route, d1 unsearched | P2: S108 = d2 4 | Likely/Likely | Same S108 call, consistency with B01. |

### Open items for part 2 (one search each)

- A06, A12, A40, A47, B10: rerun searches specified in review_log lines 17, 21, 36, 38, 43.
- B17: iNaturalist Türkiye observation volume (line 45).


## Part 2 — rerun rows (43)

- **Date:** 2026-10-03
- **Reviewer:** Opus review agent (part 2 of 2). 10 WebSearch calls (standard), all URLs "URL via search result".
- **Scope:** B04 B05 B06 B07 B09 B23 B24 | A06 A12 A40 A47 B10 B17 | B21 B22 B26 B27 B11 B15 B12 B13 B25 | A04 A08 A09 A10 A49 A50 A18 A19 A17 A23 A25 | A26 A27 A28 A41 A42 A44 A48 A30 A35 A32.
- **Method:** script re-run of rule 8 (C1→C4, d1 = max step, d6+1 only if analogue_count ≥2, projected-Certain guard, cap 5) on all 43 rows; every 4/5 and 1 checked against R8-A anchors, planner clarifications P1–P6 and cited S-ids. Part-1 Resolutions not re-opened. `inventory.csv` not edited.
- **Result:** both horizons recompute correctly from the recorded scores in all 43 rows. **38 agree, 4 disagree, 1 open.** Disagreements come from evidence (P1/P6 application, P2 scope, a new primary survey), not arithmetic.

### Searches run (settle-the-doubt only)
1. BiodivConnect 2025 call themes → Topic 1 "Setting restoration targets and measuring success" (indicators, policy alignment); Topics 2–3 scaling and long-term sustainability; no technology (EO, drones, acoustics, AI) named; EUR ~40M; full proposals 14 Apr 2026 (fondationbiodiversite.fr/en/?p=30400; tubitak.gov.tr/en/announcement/biodiversa-2025-call-restoration-ecosystem-functioning-integrity-and-connectivity-biodivconnect-open-application).
2–3. Reuters DNR 2026 Türkiye (TR and EN queries) → global weekly AI-chatbot news use 10% confirmed (reutersinstitute.politics.ox.ac.uk/news/our-podcast-digital-news-report-2026-episode-4-how-people-are-using-ai-chatbots-news); TR trust 28% and news avoidance >60% confirmed; **the 14% Türkiye chatbot figure was not reproduced** in either search.
4. Getir deep RL → Applied Intelligence 52(4) 2022, ITU + Getir; DQN trained and evaluated on 30 days of real data (9,880 orders) and "outperform the rule-based heuristic employed in practice" (avesis.itu.edu.tr/publication/details/9ea4a0d8-4422-4bf3-876e-985462d5e51e/...). Offline R&D, not a deployment.
5. TSRS nature duty → TSRS = IFRS S1/S2, materiality-based; no nature/biodiversity-specific requirement found; revised thresholds TRY 1bn assets / TRY 2bn revenue / 500 staff for periods from 1 Jan 2025 (cms.law/en/tur/legal-updates/revised-thresholds-under-the-tsrs-framework).
6. DSİ irrigation → the ministry primary page (S284) and repeats describe soil-moisture sensors, weather stations, plant sensors and a cloud platform giving "real-time irrigation"; ~40% water saving claimed for the automation; **no model, forecasting or scheduling algorithm described.**
7. A06 alternative data → Colendi AI "ColendiMind" alternative credit-scoring module offered to financial institutions (paradergi.com.tr/teknoloji/2024/09/10/colendi-aidan-finans-ve-bankacilik-hizmetlerinde-yapay-zeka-devrimi; vendor-level); press: "all financial institutions now score with ML" (S160 family).
8. Bağcılar twin → İSTKA 2025 AI Technologies Financial Support Programme, 90% grant; AI + LIDAR building-stock inventory, building inspection, disaster/risk, "environmental monitoring"; GIZ Connective Cities good practice (dha.com.tr/kurumsal/bagcilar-belediyesinin-projesi-yuzde-90-oraninda-destek-kazandi-2713690). No canopy, heat or flood modelling shown.
9–10. TALIS 2024 (OECD country notes) → **Türkiye: 24% of lower-secondary teachers used AI in their work; 70% of those to generate lesson plans/activities** (oecd.org/en/publications/results-from-talis-2024-country-notes_e127f9e2-en/turkiye_754c2c1a-en.html, figure via search summary). Korea 43% (58% lesson plans; .../korea_3d2c0051-en.html). Brazil 56% (77% lesson plans; .../brazil_1e93d3b5-en.html). OECD average 36%.

### Row verdicts (part 2)

| id | current 1-2y / 3-5y | Opus verdict | reason (≤25 words) | action |
|---|---|---|---|---|
| B04 | Potential / Potential | agree | d2 4 holds only under the monitoring-core reading of S108; S096 (2022) is outside 24 months. Class fixed by analogue_count 1 either way. | data fix: drop S096 as d2-4 basis |
| B05 | Potential / Potential | agree | EO foundation models are not named in S108, so d2 3 is correct per planner guidance. d1 1 after 7 searches; one analogue. | none |
| B06 | Likely / Likely | agree | Best S108 fit: Topic 1 "setting restoration targets and measuring success" is this item's application area. d1 3 enabling (Law 7552, draft offset regulation). | data fix: cite S108 Topic 1; drop S096 basis |
| B07 | Potential / Potential | agree | Search confirms TSRS is IFRS S1/S2, materiality-based, with no nature-specific duty. d1 3 stands; no Certain route via TSRS today. | data fix: TSRS thresholds; reword deciding condition (duty + AI-tool use) |
| B09 | Likely / Likely | **disagree → Potential (near-Likely) / Potential** | TR has no NRR duty; S108 names restoration-success indicators, not EU reporting or EO. Planner guidance gives d2 3 → C4. Reframe proposed below. | planner decision Q2 |
| B23 | Likely / Likely | agree (conditional on Q5) | Drone habitat mapping is monitoring-core, the same reading that gave B01/B17 d2 4; S108 names no technology. Strict reading → Potential near-Likely. | planner decision Q5 |
| B24 | Potential / Potential | agree (score fix) | BR/ID are announced pilots, not issued credits; rule 6 excludes plans → analogue_count 0, near-Likely flag drops. Class unchanged. | data fix: analogue_count 2→0, drop near-Likely |
| A06 | Certain / Certain | agree | Definition covers "transaction and non-traditional data"; press says ML scoring is universal in TR lenders; Colendi alternative-data scoring (vendor). d6 4, medium confidence. | data fix: add Colendi source; planner Q6 (scope) |
| A12 | Certain / Certain | agree | VDK/HMB primary pages show KURGAN risk triage operational since 2025-10-01; definition is algorithmic triage, so an ML label is not required. Robust via third clause. | none |
| A40 | Likely / Likely | agree | Sectoral Turkish-LLM call (≤50m TL per project, 2026) meets d2 4 (arguably 5). d6 3 correct: BİLGE/MAIN not multi-org production. | data fix: delete stale NEAR-LIKELY and "d2=3 not 4" text; dedupe S231 |
| A47 | Certain / Certain | **disagree → Potential / Potential** | Primary page describes sensors, weather stations and a cloud platform; no model or scheduling algorithm. A label-only claim fails P6 → d6 2, funded no. | planner decision Q1 |
| B10 | Potential / Potential | agree | No EKUAL AI-assistant licence found; the generic GenAI survey supports d6 3, not 4. One analogue. | none |
| B17 | Likely / Likely | agree | 218k/31k are community project totals with observer origin unknown; anchor 4 needs several TR orgs. d6 3 stands; d2 4 per P2. | data fix: delete stale NEAR-LIKELY, d1=1, d2=3 text |
| B21 | Potential / Potential | agree (score fix) | e-Gönüllü (2021, secondary) is volunteer matching, not data/AI skills volunteering; STGM is training. P6 → d6 2. Class unchanged. | data fix: d6 3→2, tr_status absent |
| B22 | Potential / Potential | agree | d1 1 sourced after search; d2 3 generic TÜBİTAK 1007; no TR brief-generation use found. | none |
| B26 | Potential / Potential | agree | ALO 153 is request routing by unspecified algorithms (secondary news), not LLM consultation analysis, so funded = no under P1/P6. | none |
| B27 | Potential / Likely | agree | Bağcılar twin (İSTKA 2025 AI programme, 90%) targets building stock and disaster; no canopy/heat/flood use → funded no. 3-5y Likely rests on KR affiliation. | data fix: add DHA source; step 2h check S496 affiliation |
| B11 | Potential / Potential | agree | d3 4 well sourced; the class is blocked only by analogues 0 (likely under-detection). Highest-value follow-up in Tier B academia. | none |
| B15 | Potential / Potential | agree | iThenticate similarity checks are adjacent tooling; d6 3 is borderline; no analogue. Unsourced d2 2 has no class effect. | none |
| B12 | Potential / Potential | agree | No TR or analogue deployment; d2 3 via S108 as topic-adjacent is correct. | none |
| B13 | Potential / Potential | agree | TRUBA is a compute allocation and RAISE TR eligibility is unshown, so d2 3 is borderline. No class effect. | none |
| B25 | Potential / Potential | agree | C2 misses only because mean(d4,d5) is exactly 2.0; the KR moonshot is a programme. Low/delayed if d4 or d5 drops. | none |
| A04 | Potential / Potential | agree | DrugGEN is R&D (active group, d6 3); one analogue; d3 3 is projection-only. | none |
| A08 | Certain / Certain | agree | The MEB primary page names the KANKA AI assistant and reports 719k users, beyond pilot. An AI function is described, unlike A47. | none |
| A09 | Certain / Certain | agree (P4) | Under P4, rule adoption counts: BAU (exams), Gazi, YÖK guide. Governance item; shares S416 with B14. | data fix: add GOVERNANCE tag; drop Ankara/AKU claims (no URL) |
| A10 | Likely / Likely | **disagree → Certain / Certain** (if step 2h confirms figure) | TALIS 2024 TR note: 24% of teachers use AI, 70% of those for lesson plans → d6 4. KR/BR TALIS figures replace the training-programme analogues. | planner decision Q3; data fix analogues/sources |
| A49 | Potential / Potential | agree | No TR secondary-use regime; the National Data Library is a target (d1 3). One analogue. | none |
| A50 | Certain / Certain | agree | S618 confirms Art. 4 remains mandatory after the Omnibus; d1 4 via EU reach as in A39. Trainings ≠ funded pilot. | none |
| A18 | Potential / Potential | agree | d6 1 after 2 shallow searches (flagged); no analogue; no score near a threshold. | none |
| A19 | Potential / Potential | agree | KOSGEB VAP is generic; press is isolated. Field savings of 5–27% stay below anchor 4. | none |
| A17 | Likely / Likely | agree (label fix) | d2 4 plus 2 analogues gives C3 at both horizons; TEKİS (S625) is a Zenodo research record, not operational evidence. | data fix: remove "Likely (lag-based)" (C3 holds unadjusted) |
| A23 | Potential / Potential | agree | Two analogues, but the d3 simulation (−14.5 to −24.1%) is below 25%; near-Likely flag correct. | none |
| A25 | Certain / Certain | **disagree → Potential / Potential** | The Getir paper (Appl. Intell. 2022) is an offline evaluation on 30 days of data against the rule-based heuristic used in practice: R&D, so funded = no. | data fix: funded no, d6 3 kept (active group) |
| A26 | Potential / Potential | agree | d3 4 (Science RCT, −40%) is acceptable; one analogue; TR use is likely under-detected. | none |
| A27 | Certain / Certain | open (keep provisionally) | 14% TR figure not reproduced in two searches; only an unattributed Bianet summary. Unverified → d6 2 → Potential/Potential. | step 2h: read Türkiye page in S639; planner Q3 |
| A28 | Potential / Potential | agree | d1 1 and d6 1 sourced after searches; one analogue (BR). | none |
| A41 | Potential / Likely | agree | Ugi's agentic status is unconfirmed; analogues are weak but countable; 3-5y lag-based label correct. | none |
| A42 | Potential / Likely | agree | Turkcell–Google DC is planned for 2028, not operating; d6 3, 3 analogues; lag-based label correct. | none |
| A44 | Potential / Likely | agree (d1 3) | Law 7545 binds generic security duties but does not mandate AI detection; by P3/A45 logic d1 3. Planner leaning confirmed. | planner ratify Q4 |
| A48 | Potential / Potential | agree | AFAD-RED AI is future-tense and pre-event; no analogue. | none |
| A30 | Potential / Potential | agree | PL/KR were unattributed and rightly not counted; formally not near-Likely (count 1). | none |
| A35 | Potential / Potential | agree (score fix) | d2 2 is inconsistent with A41/A42/A44/A48, which use generic Action Plan S133; set 3. No class effect (funded no). | data fix: d2 2→3 |
| A32 | Potential / Likely | agree | UYAP AI was announced 12 May 2026 in mixed tense via news; funded no is correct until a primary operational source appears. | none |

### Requested rulings
- **P2 scope (B04 B06 B09 B23).** S108's call text names "setting restoration targets and measuring success" (indicators, regulation alignment) and no technology. S096 (BiodivMon 2022) is outside the 24-month window and cannot carry d2 4 any more. Applying the planner guidance: **B06 qualifies** (measuring restoration outcomes is the named area). **B04 and B23 qualify only under the monitoring-core reading**, the same reading that already carries B01 and B17. **B09, B05 and B24 do not qualify.** The class changes from this are B09 Likely → Potential, and B23 if the planner chooses the strict reading (Q5).
- **A44 d1:** 3. Law 7545 is binding, but it imposes no AI-specific or SOC-automation duty. This matches P3 (d1 4 only where the rule mandates the AI technique, as in A45).
- **A09 (university policies as d6 = 4):** accepted under P4, provided the row is tagged GOVERNANCE and rests only on sourced organisations: BAU S614, Gazi S615 and YÖK S416/S613. The Ankara and AKU claims have no URL and are dropped. The report should note that S416 also underpins B14.
- **B09 reframing.** Türkiye has no NRR duty, so the current row scores a duty that does not reach TR. Proposed development: "EO/AI-derived ecosystem-extent and restoration indicators for national biodiversity reporting (CBD KM-GBF national reports/NBSAP, Ramsar; EU NRR + Copernicus as leader model)". Proposed definition: "Satellite time series and ML classifiers that produce ecosystem-extent, condition and restoration-progress indicators for national and international biodiversity reporting." Re-score: d1 2 (international reporting commitments do not require EO/AI; unsourced estimate pending a KM-GBF/NBSAP check), d2 3, all other scores unchanged → **Potential (near-Likely) / Potential**. That makes the change class-changing (Likely → Potential), not class-neutral. The alternative is to merge B09 into B06 as leader context (Tier B 25 → 24).

## Systemic observations (part 2)
- **Mechanics are clean and labels are not.** All 43 rows recompute correctly. A10 and A17 carry "Likely (lag-based)" although C3 holds unadjusted at 3–5y. A40 and B17 keep stale "NEAR-LIKELY" notes and superseded d1/d2 values. Step 2h should remove superseded rerun text before report drafting.
- **Label-only AI.** A47 rests on a deployer's "AI-supported" label with no described AI function. A44 (NTV snippet) and partly A12 have the same shape, although A12 survives because its definition is algorithmic triage. P6 needs an explicit evidence threshold (Q1).
- **R&D read as deployment.** In A25, a peer-reviewed offline evaluation on company data was treated as an operational deployment. Under P1, studies that use firm data without a live rollout count as R&D: d6 ≤ 3 and funded = no.
- **Survey shares as d6.** A27 (DNR, 14% unverified) and A10 (TALIS, 24% from an OECD primary page) use population or profession shares to score d6. The rule needs a stated threshold and a primary-source requirement, applied symmetrically (Q3). TALIS also gives same-use analogue evidence (KR, BR) that is stronger than the training programmes now counted in A10.
- **Tier B ecology Likely rests on one call reading.** B01, B06, B17 and B23 are Likely, and B04 holds d2 4, all through a single call (S108) whose text names no technology. The report should label these "funding-led (one call, 2025–26 edition)". The deciding condition is a 2026–27 Biodiversa+ edition that keeps a monitoring topic open to TR.
- **Loose analogue counting in reruns.** B24 counts announced pilots; A10 counts training programmes; B27 (KR) and B23 rest on affiliations inferred from titles. Rule 6 says plans and trainings do not count. B27's 3–5y Likely depends on the unchecked KR affiliation.
- **d2 defaults are inconsistent.** A35 kept d2 2, while sibling rows used generic S133 for 3. B13 and B25 take 3 from programmes whose TR eligibility is unshown. None of this changes a class today, but d2 3 is what opens the C1 third clause.
- **Distribution if all part-2 proposals are adopted** (A25 and A47 C→P, B09 L→P, A10 L→C): 1–2y C18/L8/P47; 3–5y C18/L16/P39. If A27 also reverts: C17 at both horizons.

## Planner decisions required (part 2)
- **Q1 – P6 evidence threshold (A47).** Proposed: AI-component evidence needs a primary source that names an AI function (a model, a prediction or classification task, or a named assistant). A bare "AI-supported" label over a described non-AI system does not count. Effect: A47 → d6 2, funded no → Potential/Potential. A08 (KANKA named assistant) and A12 (algorithmic-triage definition) are unaffected.
- **Q2 – B09.** Either (a) reframe as above → Potential (near-Likely)/Potential, or (b) merge B09 into B06 as leader context. Recommendation: (a). It keeps an item that matches the researcher's monitoring and reporting profile, and it scores what reaches TR.
- **Q3 – Survey shares as d6 = 4.** Proposed: a primary national survey showing ≥10% use by the relevant population or profession = "beyond pilot" (d6 4), with the figure confirmed on the publisher's page. Effects: A10 → Certain/Certain once step 2h confirms 24% on the OECD TR country note. A27 stays Certain only if step 2h finds the TR figure in S639; otherwise d6 2 → Potential/Potential.
- **Q4 – A44 d1 = 3 (ratify).** A binding generic law that does not mandate the AI technique scores 3. This extends P3 and also governs B07's deciding condition.
- **Q5 – S108 reach to monitoring-technique items.** Confirm the "monitoring-core" reading (B01, B17, B04, B23 keep d2 4) or adopt the strict "technology named in call text" reading. Under the strict reading, B01, B17 and B23 → Potential (near-Likely)/Potential and B04 is unchanged. B06 qualifies under either reading. Recommendation: keep the monitoring-core reading for consistency with P2, and disclose it as a single-call dependency.
- **Q6 – A06 scope.** Confirm that the definition ("transaction and non-traditional data") includes ML on bank transaction data, which keeps Certain. Under a strict alternative-data reading, d6 3 → Potential/Potential.
- **Haiku data fixes (class-neutral):** A40 and B17 stale text, plus the A40 duplicate S231; A10 and A17 remove "lag-based"; A09 GOVERNANCE tag and drop the unsourced Ankara/AKU claims; A35 d2 2→3; B21 d6 3→2; B24 analogue_count 2→0 and drop near-Likely; B04/B06/B09/B23 drop S096 as the d2-4 basis; B07 TSRS thresholds and deciding condition; A25 funded no with the 2022 offline-study note. New sources, all "URL via search result": TALIS 2024 country notes TR, KR and BR; Getir Applied Intelligence 2022 (avesis.itu.edu.tr); BiodivConnect themes (fondationbiodiversite.fr); Bağcılar İSTKA (dha.com.tr); Colendi (paradergi.com.tr); TSRS thresholds (cms.law); DNR 2026 global 10% (reutersinstitute.politics.ox.ac.uk podcast page).
- **Step 2h verifications owed:** A10 TALIS TR 24%; A27 DNR TR figure in S639; B27 S496 (Seoul) author affiliation; A12, A50 and A29 Omnibus dates against OJ text (carried over from part 1).
