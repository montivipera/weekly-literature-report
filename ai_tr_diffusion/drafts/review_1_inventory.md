# Review 1: inventory coverage and structure (step 1r)

Reviewer: Opus review/advisory agent. Date: 2026-10-03.
Inputs: `BRIEF.md` §1–9, `AGENT_RULES.md`, `drafts/inventory_A.csv` (43), `drafts/inventory_B.csv` (22), and both `*_sources.csv`.
Scope: a desk review of coverage, structure, classifiability and the rule 8 thresholds. No web searches were run. Facts that I name below from background knowledge are marked "(verify)" where I am not sure of them. All of them must be sourced in step 2 under AGENT_RULES rule 1.

## 0. Before anything else: the flag IDs do not match the CSV

Several flags from the Tier A drafting agent point at the wrong rows. The agent's numbering seems to have shifted during drafting:

| Flag as reported | What the CSV actually holds | Likely intended |
|---|---|---|
| "A29 may merge into A40 (AI Act Art. 50)" | A29 = synthetic-media labelling; A40 = sovereign/Turkish LLMs; **A39** = EU AI Act | A29 into **A39** |
| "A23 humanoids may overlap A22" | A23 = warehouse robotics; **A21** = humanoids; **A20** = cobots; A22 = predictive maintenance | A21 vs A20 |
| "A41 freelance AI-service models unsourced" | A41 = enterprise agentic AI; **A38** = freelance/AI-service models | A38 |
| "A43 open-weight models" | A43 = open-weight models | correct |

The decisions below use the **CSV IDs**. STATE.md "Step 1 notes" should be corrected so that later agents do not act on the wrong rows.

---

## 1. Missing developments, Tier A (8)

Sector counts now: health 4, finance 3, education 3, public admin 3, agriculture 3, energy 3, manufacturing 3, logistics 3, media 4, law 3, retail 3, labour 3, cross-cutting 5. Every sector in §2 is present. The four "thin" sectors are thin in **sourcing**, not in item count: law rests on a Harvey press release and a CADE summary, and retail on one McKinsey survey. The real gaps are developments with a distinct Türkiye diffusion path that are missing altogether:

| # | Proposed item | Sector | One-line definition | Why it matters for TR |
|---|---|---|---|---|
| MA1 | AI-enabled cyber offence and AI-driven cyber defence | cross_cutting | Attackers use LLMs and agents for phishing, malware and vulnerability discovery, and defenders answer with AI-automated security operations (SOC triage, threat hunting). | It has a domestic regulatory pull: the Cybersecurity Law (No. 7545, 2025) and the new Siber Güvenlik Başkanlığı (verify). It is a large and fast-moving global development that no row covers. |
| MA2 | Deepfake and voice-clone fraud, and AI-based identity verification (eKYC liveness) | finance | Generative impersonation of customers and executives, with banks answering through AI liveness and deepfake detection in remote onboarding. | TR banks rely on remote video onboarding under the BDDK remote-identification rules (2021) (verify), so the attack surface is real. This is separate from A05 (transaction AML) and A29 (labelling). |
| MA3 | AI in insurance underwriting and claims, including satellite-based agricultural loss assessment | finance / agriculture | Computer vision and remote sensing used to price risk and settle claims (motor damage photos, parametric or satellite-based crop loss). | The TARSİM state-backed agri-insurance pool is a concrete diffusion channel (verify use of remote sensing). It fills both finance and agriculture. |
| MA4 | AI-driven irrigation scheduling and agricultural water management | agriculture | Sensor, satellite-evapotranspiration and ML models that schedule irrigation and allocate water at farm and basin scale. | Agriculture is the dominant water user in water-stressed TR, so DSİ and irrigation unions are plausible adopters. Cost and regulatory pull differ from A14 and A16. |
| MA5 | AI for disaster risk and rapid damage assessment | public_administration | Satellite, SAR, drone and ML for post-event building-damage mapping, plus seismic and flood early warning and urban-transformation risk triage. | Since the 2023 earthquakes this is arguably the most TR-salient public-sector AI use case, and AFAD and municipalities are actors. It also bridges to the researcher's remote-sensing skills. |
| MA6 | Secondary use of national health data for AI (EHDS-type health data spaces) | health | Governed reuse of national electronic health records for training and validating clinical AI, as under the EU European Health Data Space Regulation (2025/327). | TR already has a centralised record system (e-Nabız), so the deciding condition is governance under KVKK, not data. This is a distinct path from A01–A04. |
| MA7 | AI literacy and workforce reskilling programmes | labour_market | Employer and state training to give staff working AI skills, made a legal duty for AI deployers by EU AI Act Art. 4 (in force since Feb 2025). | Brief §2 asks for the labour market, and A36–A38 cover roles but not the training market. İŞKUR, universities and the BTK Akademi type of provider are TR channels (verify). |
| MA8 | Algorithmic management and AI in hiring/HR | labour_market | AI CV screening, interview scoring, scheduling and worker monitoring, classed high-risk under AI Act Annex III and touched by the EU Platform Work Directive (transposition by Dec 2026). | Large TR employers and platform firms (couriers, ride-hailing) will feel EU-aligned pressure. It is a distinct labour development from A36 and A37. |

Considered and left out:
- **Tourism.** It is a major TR sector but is not in the §2 list. The planner should decide whether to add a single row (AI travel agents and dynamic pricing), but by default it stays out.
- **AI dubbing and localisation for Turkish TV-series exports.** Use it as a named TR case inside A26 rather than a new row.
- **AI in tax administration (GİB e-invoice analytics).** Use it as a named case inside A12.

## 2. Missing developments, Tier B (6), checked against the §7 profile

Profile checklist from the planner's prompt:

| Profile need | Current coverage | Verdict |
|---|---|---|
| Restoration MRV | B06, but framed on forest carbon (Verra/Pachama) | Present but mis-framed. A wetland restoration ecologist mostly works on non-carbon outcomes. **Reword** (see table in §3). |
| Drone/UAV vegetation mapping | Hidden inside B04 alongside satellite | **Missing as its own row.** Split B04 (MB6). |
| eDNA | B03 | Present. The AI component is thin, so **reword** it. |
| Nature credits / biodiversity credit markets | none | **Missing** (MB1) |
| Horizon Europe mission-driven calls | none | This is a **funding driver (d2), not a development**. Do not add it as a row. Capture the AI-relevant part as EU monitoring infrastructure folded into B09 (see §3) and score it in d2 for B rows. |
| AI for grant writing | B18 | Present. Broaden it to include the funder side. |
| Multi-agent research workflows | Only B13 (coding agents) | **Missing** (MB2) |
| Evidence synthesis for institutions | B10, B11, B12, B22 | Well covered |
| Municipality and NGO work | B19, B20, B21 | Thin, with no participation or urban-nature items (MB3, MB4) |

| # | Proposed item | Sector | One-line definition | Named examples (to verify in step 2) |
|---|---|---|---|---|
| MB1 | Biodiversity / nature credit markets with digital MRV | ecology_environment | Tradeable or claimable units for measured biodiversity gain or restoration outcome, verified increasingly through remote sensing, acoustics and eDNA. | EU Nature Credits Roadmap (July 2025); UK statutory Biodiversity Net Gain (Feb 2024); Verra Nature Framework; Plan Vivo PV Nature; IAPB framework |
| MB2 | Multi-agent and autonomous AI research systems ("AI co-scientists") | academia_research | Orchestrated agent teams that generate hypotheses, run analyses, and draft and critique outputs with limited human steps. Diffusion runs through labs and institutions, unlike B13's individual tool. | Google AI co-scientist (2025); FutureHouse / Edison; Sakana AI Scientist; Agents4Science 2025 conference; arXiv 2603.15914 (already in B sources) |
| MB3 | LLM analysis of public consultations and participatory input | civil_society | LLMs cluster and summarise thousands of citizen submissions, survey answers and deliberation transcripts for municipalities and NGOs. | UK i.AI "Consult"; Talk to the City (AI Objectives Institute); Pol.is; Decidim (Barcelona) |
| MB4 | AI urban-nature and climate-adaptation mapping and local digital twins for municipalities | civil_society (municipal) | Tree-canopy, green-infrastructure, heat-island and flood models built on EO plus AI, packaged as municipal digital twins for adaptation and nature planning. | EU Local Digital Twins toolbox; EU Cities Mission (İzmir reportedly a participant, verify); DestinE |
| MB5 | AI-supported restoration prioritisation and project-tracking platforms | ecology_environment | Platforms that combine ML habitat-suitability or species-distribution models with EO to choose sites, set baselines and track restoration projects. | Restor (ETH Zürich spin-off); GBIF + ML SDMs. Could merge into B06 if the planner prefers a smaller list (see §3). |
| MB6 | UAV / drone vegetation and habitat mapping with deep learning (split from B04) | ecology_environment | Multispectral or RGB drone imagery with segmentation and object-detection models for plant communities, reed beds, nesting colonies and fine-scale change. | DeepForest; OpenDroneMap; Pix4D. TR condition: SHGM drone registration and permit rules (verify) |

Civil society goes from 6 to 8 items with MB3 and MB4, and both fit the municipality collaborator.

---

## 3. Merge / split / drop / reword decisions

Rule applied: each row must be **one development with one diffusion path to Türkiye**. Two rows that would have the same TR status, drivers and deciding condition should merge. A row that holds two developments with different gates should split.

### Tier A

| ID(s) | Decision | Reason / new wording |
|---|---|---|
| A29 (flag said "into A40") | **Keep separate. Reword.** | The flag's target is wrong (see §0). Even against A39 it should stay separate. Labelling and provenance reach TR through **global platforms and C2PA/SynthID adoption**, plus RTÜK and election rules, which do not depend on EU alignment. New wording: "AI content provenance, watermarking and labelling (C2PA, SynthID, AI Act Art. 50)". |
| A39 | **Keep. Reword.** | Change it from "implementation and delays" to the development TR actually receives: "EU AI Act compliance obligations reaching Turkish providers and exporters (extraterritorial scope, staged deadlines)". Without this, d1 cannot be scored sensibly. |
| A43 | **Merge into A40.** | Open-weight models are an enabler. Their diffusion path to TR is exactly the local fine-tunes (Turkish LLMs from TÜBİTAK, HAVELSAN, Trendyol and Turkcell are largely built on open-weight bases, verify). New A40: "Turkish-language and sovereign LLMs, largely built on open-weight base models". Move the US–China parity point to cross-cutting patterns (§8.1 part 5). |
| A21 humanoids (flag said A23 vs A22) | **Keep separate.** | It is a distinct development with a distinct path (China-led, cost-curve-gated). It is **not** the same as A20 cobots, which are already in TR plants. "Premature" describes its adoption, not its inclusion. It will legitimately fall in Low/Potential, which the matrix needs. Remove the "~7,000 units sold in 2025" figure until a primary IFR source confirms it, because the TNW anchor is about industrial robots. |
| A38 freelance (flag said A41) | **Keep. Reword. Must be sourced in step 2.** | §2 requires freelance and service models. New wording: "AI-enabled freelancing and AI-implementation micro-agencies". Sources should be the ILO/Oxford Online Labour Index, platform reports (Upwork, Fiverr) and WEF. Label it "unsourced estimate" until then. |
| A07 + A33 | **Merge** into "Agentic commerce and agent-initiated payments". | Both depend on the same global rails (card-network agent protocols, platform checkouts) and would get an identical TR status (absent) and deciding condition (BDDK/TCMB stance on agent-initiated payments). Finance keeps enough rows with MA2 and MA3. |
| A30 + A31 | **Merge** into "Generative legal AI for drafting, research and contract review". | Same tools, same buyers' path in TR (law firms and in-house teams), and one anchor source. A32 (courts, UYAP) stays as the public-justice path. |
| A41 | **Keep. Narrow it.** | It is an umbrella over A05, A13 and A33. Narrow it to "agent platforms in enterprise back-office (IT, HR, procurement, finance operations)" so it does not double-count sector agent rows. |
| A11 | **Keep. Scope it.** | Scope it to **central government** (e-Devlet, ministries). Municipal assistants are Tier B19 and B20, so add that cross-reference in the notes. A11 currently mixes citizen-facing and internal use. The split is done in Tier B, so Tier A does not split. |
| A03 | **Keep. Reword.** | It overlaps A35 (generic customer-service agents). The TR path differs because hospital appointments are centralised through MHRS, which makes it a public deployment. Reword with that scope. |
| A09 | **Reword.** | "Student use" is already universal, so it would be trivially Certain and carry no information. The development is the **institutional response**: "Assessment redesign and integrity policy for generative AI in schools and universities". |
| A12 | **Reword.** | Add a named TR case (GİB tax-risk analytics, verify). Note that the AI Act high-risk status (Annex III) does not bind TR public bodies; see the classifiability flags. |
| A18 | **Keep.** | It has low TR relevance, but it gives an informative "Low/delayed" row. |
| A02, A28 | **Keep. Fix the anchors.** | A02's anchor is about ambient scribes, not imaging devices; replace it with the FDA AI-enabled device list. A28's anchor is a Malay Mail news-habits article, not licensing deals. |
| A26 | **Keep.** | Add TR dubbing and localisation for series exports as a named case. |

### Tier B

| ID(s) | Decision | Reason / new wording |
|---|---|---|
| B04 | **Split** into B04a and B04b (MB6). | Satellite and drone have different gates. Satellite uses free Copernicus data and cloud compute. Drone needs hardware, SHGM permits and field teams. B04a: "Deep-learning wetland and habitat mapping from Sentinel-1/2". Named tools: Google Earth Engine, Copernicus HRL Water & Wetness, JRC Global Surface Water, Dynamic World. **Drop the EGU session as an anchor**, because a conference session is not evidence of a development. |
| B05 | **Keep.** | GeoFMs are a distinct wave with a distinct compute gate. Add the AlphaEarth satellite-embedding dataset in GEE as the low-compute access route. |
| B08 | **Merge into B07.** | ESRS E4 is a regulation, and its AI content is the same disclosure tooling as B07. New B07: "AI and data tooling for nature-related disclosure (TNFD LEAP, ESRS E4, ISSB nature work)". The TR path for both runs through EU supply-chain data requests and KGK's TSRS (ISSB-aligned, verify). Score the mixed voluntary and mandatory status in d1 with a note. |
| B09 | **Keep. Reword.** Fold the Horizon/EU monitoring infrastructure in. | Make it an AI development: "EO/AI-based biodiversity and restoration monitoring for EU reporting (NRR plans, Copernicus indicators, Biodiversa+ monitoring, EuropaBON, BioDT/DestinE digital twins)". The TR path is Horizon Europe association and alignment, not binding law. |
| B06 | **Keep. Reword.** | Widen it from forest carbon to "Digital MRV of restoration outcomes (carbon, wetland extent, vegetation, biodiversity)". Add Restor and the WRI TerraFund guide as named examples. MB5 can merge here if the planner wants to save a row. |
| B03 | **Keep. Reword.** | Make the AI part explicit: "eDNA metabarcoding with ML-assisted bioinformatics, reference-gap filling and portfolio nature-risk analytics". Add a second named provider beyond NatureMetrics (for example SPYGEN/Vigilife, verify). |
| B10 / B11 | **Keep both. Sharpen the boundary.** | B10 is individual discovery tools, which diffuse by subscription and are already used in TR. B11 is LLM automation inside **formal** systematic reviews, gated by methods bodies (Cochrane, Campbell, JBI and CEE "RAISE" guidance, verify). The paths differ. |
| B12 | **Keep. Reword.** | Frame it as a practitioner and institutional evidence service: "AI-maintained living evidence databases for conservation decisions". This is the row closest to the profile's "evidence synthesis for institutions". |
| B13 | **Keep. Narrow it.** | "Agentic coding assistants for researcher data analysis" (individual use). Autonomous multi-agent systems move to MB2. |
| B14 + B16 | **Merge** into "Publisher, funder and university rules on generative AI in research (authoring, peer review, grant applications)". | Both are governance responses, not technologies. Publisher rules already bind TR authors, and funder rules reach TR through TÜBİTAK and YÖK (YÖK published a gen-AI research-ethics guide in 2024, verify). One row with the TR condition "TÜBİTAK adopts EC-Living-Guidelines-equivalent rules" is enough. **Planner call** (see the reply). |
| B15 | **Keep.** | |
| B17 | **Keep.** | Add TR iNaturalist and Pl@ntNet activity as baseline evidence in step 2. |
| B18 | **Keep. Broaden it.** | "Generative AI in grant writing and in funder-side screening": funders now cap or screen AI-generated applications (NIH application caps in 2025, verify). |
| B19 / B20 | **Keep both.** | B19 is internal, gated by self-hosting and KVKK. B20 is citizen-facing, gated by Turkish-language quality and service integration. B20: **downgrade the İBB example to "to verify"** because its only source is a 2023 vendor PDF. Add non-TR named examples (a Dutch or Nordic municipality) and BELSIS.NET only if it is confirmed. |
| B21 | **Keep. Reword** from a single organisation to a development. | "Tech-for-good intermediaries and skills-based AI volunteering for NGOs". Named examples: DataKind, Tech To The Rescue (founded in Poland, an analogue), Omdena (local chapters, verify), Google.org Fellowship. If the planner needs Tier B ≤ 25, this is the row to drop. |
| B22 | **Keep. Reword.** | Make LLM evidence-to-policy brief generation the development. Overton (policy-citation tracking) becomes the named measurement tool, not half the row. |

---

## 4. Classifiability flags

Under the current rule 8, all items can be scored on d1–d6. The following will give a **misleading** class if the rule is applied mechanically:

1. **Regulation-as-item rows are circular.** These are A39, A29, B07 (with B08), B09 and B14/B16. If d1 is scored as "how binding is this regulation", the item is Certain by construction. Worse, EU acts do not bind Türkiye. NRR, ESRS E4 and AI Act Annex III public-sector duties reach TR only through exporters, EU-market providers or alignment. Without a precise d1 anchor, agents will score d1 = 4–5 and output a false Certain. Fix: use the d1 anchors in §5.
2. **Already-diffused, organically adopted items cannot reach Certain.** These are A26, A27, A09, B10, B13, B17 and probably A20 and A35. They are present in TR well beyond pilot scale, but through private or consumer spend, which d2 (public/ESG funding) does not measure. With d2 ≤ 2 they fall to Likely, or to Potential if analogue evidence was not collected. That understates the most certain rows. Fix: add a "present at scale" branch (§5).
3. **Labour-market rows (A36, A37, A38, MA7, MA8) fit the drivers poorly.** "Funding pull" and "regulatory pull" for a *declining* role are not meaningful. Instruction: score the drivers of the **underlying automation** (for A37, clerical automation adoption by TR employers), and read the class as "certainty that the labour effect becomes observable in TR within the horizon". Write this into the notes column.
4. **Infrastructure rows are circular on d4.** A40 and A42 are themselves infrastructure. Score d4 on their **prerequisites**: power, chip access, US export-control status (TR was a mid-tier country under the January 2025 AI diffusion rule, later rescinded, verify), and Turkish corpora.
5. **Cost-barrier items cannot reach Low.** A21 humanoids, A24 autonomous trucks and A16 autonomous machinery are blocked by capex and market size, not by d4 or d5 ≤ 1. TR infrastructure and workforce will rarely score 1. The rule's "explicit market-size block" covers this only if agents name it, so make it a required field (§5).
6. **A12, MA8 and MA6 hit the AI Act high-risk timing issue.** High-risk duties were postponed to Dec 2027 / Aug 2028 under the Omnibus (per A39's anchor). For TR public bodies they are not binding at all. 1–2y d1 should be ≤ 2. 3–5y may be higher only for TR firms selling into the EU.
7. **B06, MB1 and B09 carry voluntary-framework risk.** EU CRCF, nature credits and TNFD are voluntary or certification frameworks, so d1 must stay ≤ 3 unless a TR or EU obligation is cited. The TR Climate Law (2025, ETS) pulls carbon, not biodiversity (verify).
8. **The analogue test has no data field.** "Present in ≥ 2 analogues" is not a driver score, and the inventory schema has only free-text `analogue_status`. Agents will guess. Add `analogue_count` (0–5) and `analogue_list` with a source per analogue.
9. **There is no horizon mechanism.** One set of static scores yields one class, but two horizons are required. Agents will either copy the class or diverge on intuition, which breaks §4 ("classification must follow from the scores"). See the fix in §5.
10. **Tier B d6 needs a broader definition.** For B rows, "existing local activity" should count university groups, NGO and municipal pilots, and TÜBİTAK-funded projects, not only startups. Otherwise most B rows score d6 = 1–2 and fall to Potential regardless of real activity in İzmir and Ankara labs.

## 5. Threshold critique (AGENT_RULES rule 8)

The structure follows §5 of the brief faithfully. The cut-offs are broadly reasonable, but the rule is **not mechanically complete**:

- **No precedence.** One item can satisfy Certain (d1 ≥ 4) and Low (d4 = 1) at the same time.
- **No fall-through.** Example: d2 = 3, d3 = 3, 3 analogues, d4 = 2, d5 = 2, d6 = 2. That is not Certain, not Likely (no driver ≥ 4), not Potential (more than one analogue), and not Low (nothing ≤ 1). Such items will be common.
- **Single-driver Certain is too permissive.** d1 ≥ 4 alone triggers it, and "applies to Türkiye/EU-aligned firms" is undefined.
- **Funding wording mismatch.** "Pilot scale with funding attached" is proxied by d2, which measures *pull*, not attached funding.
- **Low is nearly unreachable.** d4/d5 ≤ 1 is rare for Türkiye.
- **No horizon logic, and no score anchors.** Three or more Sonnet agents scoring in batches will drift.

### Proposed replacement for rule 8 (precise text)

```
8. Classification (apply in this order; first match wins; log the branch used in `notes`).
   Fields required per item: d1..d6 (1–5), analogue_count (0–5, each with a source),
   tr_funded_pilot (yes/no + source id), barrier (none|infra|language|regulation|
   market_size|cost + source id).

   Driver anchors (use these, not intuition):
   d1 5 = Turkish binding law/regulation in force with a dated obligation;
      4 = EU (or other foreign) binding law that reaches a material share of Turkish
          actors in this horizon (exporters, EU-market providers, EU-supply-chain
          suppliers), or binding Turkish secondary regulation;
      3 = Turkish law/action-plan target announced or in draft, or voluntary standard
          widely demanded by EU buyers/funders; 2 = soft guidance only; 1 = none.
   d2 5 = dedicated TR or EU call/programme open to TR actors with budget for this item;
      3 = generic digital/AI funding usable for it; 1 = none.
      Private and consumer spend counts under d3, not d2.
   d6 5 = scaled national deployment; 4 = present beyond pilot in several TR orgs;
      3 = at least one funded TR pilot or active university/NGO/municipal group;
      2 = isolated mentions; 1 = none found.

   (1) CERTAIN if  d1 >= 4
                   OR d6 >= 4
                   OR (d6 >= 3 AND tr_funded_pilot = yes AND (d2 >= 3 OR d3 >= 4)).
   (2) LOW / DELAYED if barrier != none (sourced)
                   OR min(d4, d5) <= 1
                   OR mean(d4, d5) < 2.0.
   (3) LIKELY if (d2 >= 4 OR d3 >= 4) AND analogue_count >= 2 AND mean(d4, d5) >= 2.5.
   (4) POTENTIAL otherwise. Name the one deciding condition.
   Any item that reaches (4) with analogue_count >= 2 must be flagged "near-Likely"
   for the Opus review.

   Horizons: score for 2026–2028. For 2028–2031, re-run the same rule after applying
   only these dated adjustments, each with a source:
     d1 += the level of any obligation whose application date falls in 2028–2031;
     d6 += 1 if analogue_count >= 2 (analogue→TR lag assumption, state it as a
           limitation);
     barrier may be cleared only if the source dates its removal.
   The 3–5y class may not be lower than the 1–2y class without a written reason.
```

Why each change:

- **Precedence with Certain first.** A binding obligation forces compliance even when readiness is poor. Ranking Low above Likely stops strong cost pull from masking a hard barrier.
- **`d6 ≥ 4` as a Certain branch.** It fixes flag 2: organic diffusion is the most certain of all.
- **Explicit `barrier` field.** It makes Low reachable for cost- and market-size blocks (flag 5) and forces a source.
- **Lowering the Low readiness threshold to mean < 2.0.** This is an addition, not a replacement. It closes the fall-through gap together with the Potential default.
- **Dated horizon adjustment.** It makes the two horizons follow from the scores, as §4 of the brief demands, instead of from intuition.
- **The new d6 anchor at 3.** It counts university, NGO and municipal groups (flag 10).

Brief compliance: this stays within §5. The Certain criterion "already present … with funding attached" is honoured: `d6 ≥ 4` means present beyond pilot, which implies spend. The only reinterpretation is that private or consumer spend counts as "funding attached". The planner should log that decision in STATE.md.

Process recommendation: before step 2 fans out, have one Sonnet agent score **five calibration items** (for example A01, A24, A39, B01, B18). Opus checks them against the anchors, and the scored examples are then pasted into the batch prompts.

## 6. Final recommended item count

| Tier | Start | Adds | Splits | Merges | Drops | Result |
|---|---|---|---|---|---|---|
| A | 43 | +8 (MA1–MA8) | 0 | −3 (A43→A40, A07+A33, A30+A31) | 0 | **48** (within 30–50) |
| B | 22 | +5 (MB1–MB5) | +1 (B04 → B04a + B04b/MB6) | −2 (B08→B07, B14+B16) | 0 | **26** |
| Total | 65 | | | | | **74** |

Options to reach Tier B ≤ 25:
- **26 → 25:** drop B21, or merge MB5 into B06.
- **26 → 24:** do both.

My preference is to keep B21 reworded, merge MB5 into B06, and land at **25**. That way civil society keeps 8 rows and the restoration line stays a single row.

Sector balance after changes:
- **Tier A:** finance 4, agriculture 4 (MA3 shared), labour 5, law 2, retail 3 (A33 incl. A07, A34, A35).
- **Tier B:** ecology 10–11, academia 7, civil society 8.

Law at 2 is acceptable at survey depth. The planner may restore 3 by keeping A30 and A31 split.

Source hygiene for step 2 (not a structure issue, logged here):
- **Replace secondary anchors:** ai2.work, ppc.land, Malay Mail, Yahoo Finance, TNW, the etradeforall reprint, the Coolset vendor page, and the 2023 CBOT vendor PDF.
- **Replace mismatched anchors:** A02, A21 and A28 point to sources that do not support the row.
