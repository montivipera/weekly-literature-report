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
