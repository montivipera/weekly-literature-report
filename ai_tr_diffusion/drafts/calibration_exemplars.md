# Calibration exemplars for scoring batches (rule 8, reviewed 2026-10-03)

These five items were scored, reviewed by Opus and corrected. Copy the form and the reasoning style. Source ids refer to `drafts/sources_calib.csv`. The full rows are in `drafts/scores_calib_reviewed.csv`.

## Common mistakes to avoid
1. **Scoring 1 without a search.** A score of 1, 4 or 5 needs a source id. "Not searched" is not "none". If you did not search, give d1/d2 a 2 and write "unsourced estimate". A d6 = 1 needs "none found after N searches (EN+TR)". In calibration, B18 got d2 = 1 with no source and A24 got d2 = 1 without a search. Both should be 3.
2. **Skipping EU funding.** Türkiye is associated to Horizon Europe. Before you set d2 ≤ 2, check Horizon Europe cluster and partnership calls (CCAM, Biodiversa+), TÜBİTAK 1071/1001, development agencies (kalkınma ajansları) and the Action Plan. A topic-adjacent call open to TR actors is d2 = 3. Use d2 = 5 only when a call has budget reserved for this item.
3. **Setting tr_funded_pilot = yes loosely.** Use yes only for a funded operational pilot of the development in Türkiye, meaning real users or operations. R&D prototype tests, trainings, committees and vendor offers do not count. They may still support d6 = 3 as an "active group". This field decides the C1 third clause: with d2 ≥ 3, a wrong yes produces a false Certain (see A24).
4. **Scoring d1 from leader guidance.** d1 measures pull on Turkish actors. UK or US guidance is context, not TR pull. Enabling or permissive regulation and funder conditions (e.g. the TÜBİTAK AI-disclosure rule) score at most 3. A score of 4 needs an obligation that actors must meet, either Turkish secondary regulation or an EU law that reaches TR exporters/providers.
5. **Calling a time saving "strong".** d3 ≥ 4 needs a sourced magnitude. Write the effect size you found (e.g. "RCT: −9.5% note time"). "Saves time" with no figure, or a vendor claim, stays at 3.
6. **Counting analogues too generously.** Count one sourced country at a time, and only when the source shows this development in that country (same actor type, same use). These do not count: national general-AI adoption statistics, bills or drafts, a different use case (e.g. mining instead of public highways), or foreign teams using that country's data. Academic fieldwork by in-country institutions counts for research-practice items. Vendor-reported reach in independent news counts if you mark it "vendor-reported".
7. **Mis-running the branches.** Run C1 → C2 → C3 → C4 and stop at the first match. Write every comparison with its number. For 3–5y, apply only the dated adjustments: d1 for an obligation dated 2028–31, d6 +1 only if analogue_count ≥ 2, and barrier cleared only with a dated source. Cap at 5. Keep tr_status consistent with d6: absent = 1–2, pilot = 3, exists = ≥ 4. For regulation items, "exists" means the obligation applies to TR actors now. Flag "near-Likely" when C4 is reached with analogue_count ≥ 2. Name exactly one deciding condition.
8. **Weak source hygiene.** Use primary sources over aggregators and law-firm digests where you saw both. The domain must match the publisher you name. If a figure came only from a headline or search snippet, say so. Write "URL via search result" in notes.

---

### A01 AI scribes / ambient clinical documentation — Potential / Potential (near-Likely)
- d1 2: TR has only a generic health-AI mention in the 2026–30 Action Plan (calib-008). UK/US guidance is not TR pull.
- d2 2: a health programme is announced, but no call or budget line was seen (calib-008).
- d3 3: moderate saving. NEJM AI RCT: −9.5% time-in-note, DAX −1.7% n.s. (calib-055/056). Far below >50%.
- d4 3: Turkish medical ASR is available from vendors (calib-007). No validated TR clinical scribe and no HBYS/e-Nabız integration.
- d5 3: unsourced estimate. Physicians review drafts; governance training is needed.
- d6 2: vendor pages only. No TR hospital deployment after 6 searches EN+TR.
- analogue_count 3: KR Asan, 16 departments (calib-004/005); BR and MX vendor-reported (calib-006). tr_funded_pilot no. barrier none.
- 1–2y: C1 fail (d1 2<4, d6 2<4, funded no) → C2 fail (barrier none, min(d4,d5) 3>1, mean 3.0≥2.0) → C3 fail (d2 2, d3 3, both <4) → **C4 Potential**.
- 3–5y: no dated TR obligation. d6 2+1 = 3 (analogues ≥2). C1 fail (d6 3<4, funded no) → C2 fail → C3 fail → **C4 Potential**.
- Deciding condition: a funded Turkish hospital pilot with Turkish-language validation.

### A24 Autonomous trucking — Potential / Potential
- d1 3: the 1 Dec 2024 type-approval regulation enables but does not oblige (calib-016/017). Planner rule: enabling = 3.
- d2 3: Horizon Europe CCAM calls are open to TR actors (calib-051; association calib-039). This is generic R&D funding, not a TR deployment budget. (The draft had 1 without a source.)
- d3 3: the minister claims savings "up to 40%" (calib-015, headline only), which is below the >50% for 5.
- d4 3: Ford Trucks L4 stack and an ITS-equipped motorway (calib-013). No commercial enablers.
- d5 2: unsourced estimate.
- d6 3: an active group. The Ford Otosan–AVL L4 programme ran a minister-attended test (calib-013/014/052).
- analogue_count 1: KR highway trials (calib-009). BR is mining only and is excluded. tr_funded_pilot **no**: a prototype run with a safety driver on a closed section is R&D, not an operational pilot. barrier none: no source states a block.
- 1–2y: C1 fail (d1 3, d6 3, funded no) → C2 fail (min 2>1, mean 2.5≥2.0) → C3 fail (d2 3, d3 3, analogues 1<2) → **C4 Potential**.
- 3–5y: no dated obligation. d6 unchanged (analogues <2). Same chain → **C4 Potential**.
- Deciding condition: legal authorisation of driverless live-traffic operation on TR highways, plus a first commercial hub-to-hub operator.

### A39 EU AI Act obligations reaching Turkish providers/exporters — Certain / Certain
- d1 4: binding EU law reaching TR providers serving the EU (Art. 2; calib-020/030). Prohibitions apply since Feb 2025 and GPAI duties since Aug 2025 (calib-021/022). Not 5 because no Turkish AI law is in force (calib-031 is a bill).
- d2 2: unsourced estimate. No compliance call found.
- d3 1: compliance adds a cost line and saves none (obligations per calib-020).
- d4 3: guidance exists, but harmonised standards are still being finalised (unsourced).
- d5 3: unsourced estimate. The legal/advisory profession exists (calib-024).
- d6 3: active group: the TSE mirror committee (calib-025).
- analogue_count 2: PL directly bound as an EU member (calib-020); KR AI Basic Act in force Jan 2026 (calib-026). BR/ID drafts are not counted. tr_funded_pilot no. barrier none.
- 1–2y: **C1 Certain** (d1 4≥4). Stop here; later branches are not evaluated.
- 3–5y: Annex I high-risk obligation dated 2 Aug 2028 (S042; Omnibus in force 27 Jul 2026, calib-053/054). d1 4+4 → capped at 5. d6 3+1 = 4. **C1 Certain**.
- Deciding condition: none needed (no Potential).

### B01 Passive acoustic monitoring with AI classifiers — Potential / Potential (near-Likely)
- d1 1: no TR or TR-reaching obligation found. The EU Nature Restoration Law binds member states only.
- d2 3: Biodiversa+ calls are open to TR via TÜBİTAK 1071: BiodivMon 2022 (calib-037) and BiodivConnect 2025–26 with a "measuring success" topic (calib-049). Topic-adjacent, with no budget reserved, so 3.
- d3 3: cost-effective against point counts, but not for small surveys (calib-038). No >50% figure.
- d4 4: BirdNET has 6,500+ classes, Western Palearctic included (calib-036). Not 5 because amphibian and insect coverage is weaker.
- d5 3: unsourced estimate. Ecologists exist; bioacoustic data skills are thin.
- d6 1: none found after 5 searches EN+TR. LOW confidence, likely under-detection. Run a targeted check before finalising.
- analogue_count 2: BR Pantanal (calib-034) and PL AMU (calib-035), both in-country academic fieldwork. tr_funded_pilot no. barrier none.
- 1–2y: C1 fail (d1 1, d6 1, funded no) → C2 fail (min 3>1, mean 3.5≥2.0) → C3 fail (d2 3, d3 3, both <4) → **C4 Potential**, flagged near-Likely.
- 3–5y: d6 1+1 = 2. No dated obligation. Same chain → **C4 Potential**.
- Deciding condition: an open call that explicitly funds biodiversity-monitoring technology for TR actors (d2≥4 → Likely).

### B18 Generative AI in grant writing and funder-side screening — Potential / Potential
- d1 3: funder conditions, not law. TÜBİTAK requires disclosure and bans evaluator use (calib-041/042); Horizon Europe requires disclosure (calib-043).
- d2 3: development-agency technical-support funds are usable. Example: OKA-funded AI-supported project-development training (calib-057). (The draft had 1 without a source.)
- d3 3: proposal writing is a main nonprofit AI use (calib-047; S048), but no quantified saving was found.
- d4 3: no source for 4. TÜBİTAK bans entering confidential data into tools (calib-041).
- d5 3: unsourced estimate. NGO technical gaps are noted (calib-048).
- d6 2: isolated or indirect signals only. tr_status = absent, to match d6.
- analogue_count 1: BR, one-third of nonprofits use GenAI, mainly for text (calib-045). tr_funded_pilot no (training is not a pilot). barrier none.
- 1–2y: C1 fail (d1 3, d6 2, funded no) → C2 fail (min 3>1, mean 3.0) → C3 fail (d2 3, d3 3, analogues 1<2) → **C4 Potential**.
- 3–5y: no dated obligation. d6 unchanged (analogues <2). Same chain → **C4 Potential**.
- Deciding condition: sourced operational use by TR NGOs, municipalities or agency beneficiaries beyond isolated cases (d6≥4 → Certain).
