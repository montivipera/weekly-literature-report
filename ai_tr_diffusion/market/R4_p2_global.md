# R4 — P2 global comparators (biodiversity screening for EIA / lender due diligence)

Date accessed: 2026-10-05. Method: 39 WebSearch calls (fetch blocked). Per AGENT_RULES rule 8 note, every URL below "counts as seen via search result" (URL via search result); no page was read in full. Facts marked "(snippet)" come from the search-result summary of that URL and were not checked on the page. Source IDs (R4-nnn) map to `R4_sources.csv`. Prices are as shown in search results on 2026-10-05 and may have changed; currencies are not converted.

## 0. Top findings (for planner)
1. IBAT is the incumbent global screen and its pricing is public: Free $0, Basic $5,000/yr, Pro $15,000/yr, Enterprise $25,000/yr, Enterprise Plus $35,000/yr; pay-as-you-go (PAYG) $750 per proximity or freshwater report, $1,250 per PS6/ESS6 critical-habitat report, $5,000 multi-site report [R4-001][R4-002][R4-004]. A Türkiye pre-screen priced near the PAYG band would be benchmarked against that.
2. IBAT is explicitly a global-scale, desk screening: critical habitat was assessed only at global level, and the PS6 report supports "initial risk screening and scoping, not a complete assessment" [R4-006][R4-010][R4-004]. IFC PS6 requires external experts with regional experience for critical habitat and species specialists for CR/EN triggers [R4-012]. This is the structural opening for an expert-verified national layer.
3. Lender-facing Turkish CHAs already exist as consultant-written documents: Enerjisa's 750 MW, 180-turbine wind package (Aegean/Marmara) has per-plant Critical Habitat Assessments (apparently by Mott MacDonald) that start from a high-level screening using IUCN CR/EN, restricted-range and migratory species ranges, then update with 2024 baseline surveys [R4-051][R4-052]. That is the workflow P2 would pre-populate.
4. Cheap, per-project, AI-assisted tools are proven in the UK BNG niche (Joe's Blooms £495–995 per project; bng.ai £249–£1,999 per project depending on whether an ecologist is included) [R4-021][R4-022]. The pattern "automated draft + optional human expert tier" is sold at roughly 2x–8x price steps, which is a usable template for an expert-verified premium tier.
5. No evidence was found (in ~39 searches) that any global tool uses Nuh'un Gemisi or TÜBİVES, outputs Turkish, or offers local expert verification; IBAT's own tutorials mention only Spanish as an added language [R4-015]. Nuh'un Gemisi (DKMP) holds ~2 million records and 13,404 recorded species as of Dec 2024 [R4-060][R4-061][R4-062]; TÜBİVES is described as not updated for ~10 years [R4-063] (snippet). Absence of evidence is not proof of absence; vendors may have unpublicised features.

## Q1–Q2. IBAT: report types, inputs/outputs, data, tiers, users, limits

Report types (IBAT services catalogue and pricing page): Proximity Analysis, IFC and World Bank PS6/ESS6 Critical Habitat report, Freshwater Report, Multi-site Analysis (GRI), Species Threat Abatement and Restoration (STAR) report, Disclosure Preparation Report (DPR), and an Estimated Species report [R4-003][R4-001][R4-004][R4-005] (snippets).
- PS6/ESS6 report: screens a project-level Area of Interest for potential Critical Habitat; contents are protected areas, Key Biodiversity Areas (KBAs) and IUCN Red List species [R4-001][R4-004]. Updated in 2025 with expanded scope; PAYG price now $1,250 [R4-004] (snippet).
- Estimated Species report (2025): 1 km x 1 km resolution (25x finer), reptiles added to mammals, amphibians and birds, updated STAR layer (Red List 2025 v1), species disaggregation [R4-005] (snippet).
- Data layers: IUCN Red List of Threatened Species, World Database on Protected Areas (WDPA), World Database of KBAs, STAR layer, rarity-weighted species richness [R4-001][R4-003]. IBAT map layers include nationally designated sites (IUCN categories I–VI) and international designations (Ramsar, UNESCO, Natura 2000) [R4-014] (2012 BirdLife PDF; layer list may have changed). So IBAT does carry national protected-area polygons via WDPA, but not national species or inventory databases; this refines the "no national data" premise.
- Inputs/outputs: user draws or uploads an area of interest; outputs are downloadable reports and GIS packages (reports list above; GIS downloads of Red List, WDPA, KBA in higher tiers) [R4-001][R4-002].
- Provider: IBAT Alliance = BirdLife International, Conservation International, IUCN, UNEP-WCMC [R4-071] (snippet). It is "freemium" (free account; paid reports/downloads/web services) [R4-075][R4-071].
- Users: "100s of users" incl. World Bank Group, Shell, Mitsubishi, WWF (older description) [R4-071]; "over 70 companies" in an older press release [R4-073]; "over 200 private sector organisations" and a record $2.5 M of 2024 investment in biodiversity data reported in June 2025 [R4-007] (secondary summary). Consultancies such as ERM and The Biodiversity Consultancy are cited as users, and PAYG lets consultancies run screenings on behalf of clients [R4-008][R4-072] (snippet). Listed in the TNFD "locate" tools guidance [R4-070].
- Limits: global-scale only: tools like IBAT provide global screening, not local impact data; companies must verify species and threats via local surveys and expert consultation, after which IBAT's estimated impacts are replaced with site-specific ones [R4-006] (snippet). Critical Habitat was assessed only at global level [R4-010]. The IFC-aligned global screening layer says that after screening, Critical Habitat "must be assessed in-situ by a qualified assessor" [R4-011] (snippet). Half of marine Critical Habitat identified in 2015 is not formally protected, so WDPA-only screening misses it [R4-009] (snippet). No field validation by design.

### IBAT tiers and prices (USD)
See pricing table in section "Pricing table". Tier contents [R4-001][R4-002] (snippets): Free = country profiles, map of protected areas/KBAs/Red List species, STAR 50 km layer, PAYG reports; Basic = site catalogue, upload and save sites, up to 10 proximity reports; Pro = 5 km STAR layer, up to 30 WBG-risk/proximity/freshwater/STAR reports, up to 1 M km2 GIS download, up to 3 multi-site reports; Enterprise = unlimited GIS downloads (Red List, WDPA, KBA) and unlimited reports; Enterprise Plus = adds API, QGIS vector tile service, unlimited Estimated Species reports, unlimited STAR/rarity GIS. Licensing: embedding IBAT data in a product sold to customers requires a data request reviewed by all four partners [R4-008] (snippet).

## Q2. Other screening / assessment products

| Product | Who uses it | Core features | Pricing signal | URL |
|---|---|---|---|---|
| NatureServe Explorer / Network (US/Canada) | US agencies, consultants, state Natural Heritage programmes | Species/ecosystem data; Environmental Review Tool; Explorer Pro licences | Data licence: $10,000 minimum base fee; comprehensive regional dataset from $100,000; national about $300,000 [R4-016]. NC example: $600/yr per user, $100 per project review, $65/hr custom [R4-017] | R4-016, R4-017 |
| UK statutory Biodiversity Metric (Defra/Natural England) | Developers, ecologists, LPAs (mandatory BNG) | Free statutory calculation tool [R4-018]; | Tool free; consultant metric report £1,200–3,500 and from £399+VAT [R4-019][R4-020] (snippets) | R4-018 |
| Joe's Blooms BNG Tool | UK developers, consultants, LPAs | Self-service BNG tool with AI habitat features; LPA portal; exemption checker | £495–995 incl. VAT per project; £1,250 premium video-guided; £250/h consulting; enterprise by quote [R4-021] | R4-021 |
| bng.ai (AiDASH) | UK developers, planners | AI BNG assessment and plan | £249 quick; £599 with own ecologist; £1,499 with AiDASH ecologist; £1,999 with on-site PEA; >50 ha by quote [R4-022] | R4-022, R4-023 |
| MAGIC (Natural England/Defra) | Everyone in Great Britain | Free map portal, 400+ layers from ~30 bodies; ~3,500 daily sessions | Free; no permission needed [R4-024] | R4-024 |
| EU Natura 2000 Viewer (EEA) | Planners, consultants in EU | Site, species and habitat viewer with download | Free [R4-026] | R4-026 |
| ENCORE (NCFA/UNEP-WCMC) | Banks and financial institutions | Sector dependency/impact and location maps for natural-capital risk; not a species-level screen | Free [R4-027][R4-028] | R4-027 |
| NatureAlpha (Geoverse) | Asset managers, banks | AI geospatial nature-risk; 28 layers, 8.5 M asset locations; TNFD-aligned | Free "Geoverse Explorer" tier; enterprise pricing not found [R4-036][R4-037] | R4-036 |
| Kuyua (Germany) | Corporates (CSRD) | Five-module nature/climate/deforestation/finance-risk platform | Subscription; price not found [R4-038] | R4-038 |
| Ecometrica | Corporates, TNFD working group | Global Biodiversity Metric from satellite drivers for site portfolios | Price not found [R4-039] | R4-039 |
| NatureMetrics (eDNA + Nature Intelligence platform) | Infrastructure, mining, finance; platform pitched for lender due diligence and PS6 baselines | eDNA kits and lab; platform with 0–1 site risk score and Portfolio Assessment (Sept 2025) | eDNA GBP160–300/sample incl. kit, ex VAT, by turnaround; kit alone GBP35 [R4-029]; platform listed GBP5,000–7,500 per site per year [R4-033][R4-034] (aggregator snippets) | R4-029, R4-031, R4-032, R4-035 |
| Kayrros Nature Impact; Habitat Forward | FIs; EU corporates | Asset-level ML/satellite nature impact; EU-wide site due diligence and CSRD/TNFD reports | Not found [R4-040][R4-041] | R4-040, R4-041 |
| Ecobot (US) | Wetland/stream consultants (USACE 404) | Field app + web manager; AI vegetation/soil suggestions; report-ready exports; 3,796 users, 334,551 reports (vendor claim) | Not found [R4-042] | R4-042 |
| V7 Go EIA review; generative-AI urban ecological assessments | EIA reviewers | LLM extraction from EIA documents; a 2026 study found automated reports needed substantial expert revision | Not found [R4-043][R4-044] | R4-043, R4-044 |
| Wildlife Acoustics (Song Meter, Kaleidoscope Pro) | Consultancies, researchers (bats, birds, anurans) | Recorders and classifier software | SM4 $799; Kaleidoscope Pro GBP354.17/yr professional, GBP262.50 university [R4-045][R4-046] | R4-045, R4-046 |
| AudioMoth (Open Acoustic Devices) | Researchers, NGOs, consultancies | Open low-cost recorder | $99.99 / GBP79.99 [R4-047] | R4-047 |
| Rainforest Connection (Guardian, Arbimon) | Conservation NGOs, forest monitoring | Free no-code ecoacoustic platform; tiers Free / Pro / Enterprise | Pro/Enterprise prices not found [R4-048][R4-049] | R4-048 |

Not found (searches returned nothing relevant): "EcoAssess", "Nature Positive AI", "Fieldmaps" as ecology-EIA products; "Rewild" not tested individually. Do not cite them.

### Feature x product matrix (Y = stated in a source; N = source states absence or scope excludes; ? = not found)

| Feature | IBAT | NatureServe | UK BNG metric / Joe's Blooms / bng.ai | MAGIC / Natura 2000 viewer | ENCORE | NatureAlpha / Kuyua / Ecometrica | NatureMetrics | AI EIA (V7, Ecobot) | Acoustic kits |
|---|---|---|---|---|---|---|---|---|---|
| Polygon-in report | Y | Y (US states) | Y (UK) | map view only | N (sector/location tiles) | portfolio / asset points | site score | N | N |
| Species-level protected-species likelihood | partial (Red List ranges, 1 km estimate) | Y (US) | N (habitat units) | partial (EU Natura species) | N | N (risk scores) | eDNA detection (field sample) | N | detection after survey |
| Protected-area layer | Y (WDPA, KBA) | Y (US) | UK designations | Y | partial | Y | ? | N | N |
| IFC PS6 critical-habitat screen | Y (PS6/ESS6 report) | N | N | N | N | ? (TNFD-oriented) | claimed for baselines [R4-032] | N | N |
| Expert verification / sign-off | N [R4-006] | agency staff | ecologist tiers (bng.ai, JB) | N | N | N | lab-based, field samples | N (needs revision [R4-044]) | N |
| Turkish national data (Nuh'un Gemisi, TÜBİVES) | ? none found | N | N | N | N | ? | ? | N | N |
| Turkish-language output | N (Spanish only found [R4-015]) | N | N | N | N | ? | ? | ? | N |
| Bern Convention / Turkish protected-species list | ? | N | N | EU Natura only | N | ? | ? | N | N |
| Public price | Y | Y | Y | free | free | partial | partial | partial | Y |

## Q3. Lender frameworks and what a screen must output
- IFC PS6 (2012) and Guidance Note 6: critical habitat (CH) determination uses tiers by vulnerability/irreplaceability; projects in CH need net gain; external experts with regional experience must be involved, species specialists for CR/EN-triggered CH [R4-012][R4-013] (snippets). Global screening layer: 12 biodiversity features aligned with IFC guidance, classed "likely" or "potential" CH, followed by in-situ assessment by a qualified assessor [R4-010][R4-011].
- EBRD PR6 (updated 1 Jan 2020): revised criteria for priority biodiversity features and critical habitat [R4-050] (snippet). Enerjisa wind projects in Türkiye are EBRD- and DFC-disclosed with per-plant CHAs [R4-051][R4-052].
- Equator Principles: 126–128 EPFIs in 2026 (figures differ by source/date; some US exits in 2024, Nordea leaving April 2026) [R4-053] (snippet; unverified). EP4 Principle 2 requires E&S assessment for Category A/B projects; for projects outside high-income OECD countries, alignment with IFC Performance Standards [R4-054] (snippet). EP biodiversity data-sharing guidance asks clients to share baseline data (GBIF) and notes KBAs as likely CH [R4-055][R4-056].
- Consultancy scope/cost signals: no public tender value for a CHA or biodiversity baseline was found (one generic tender search; results irrelevant) [R4-059]. Indirect signals: UK senior ecologist freelance rates GBP280–450/day [R4-058]; one UK consultancy's published hourly rates GBP25 (graduate) to GBP60 (director) [R4-058]; Joe's Blooms consulting GBP250/h [R4-021]. Turkish side: R3 covers; the Ministry's ÇED fee table is a regulator charge, not consultant cost [R4-064].
- What a screen must output to be accepted: sources suggest (not prove) that lenders accept a screen as scoping input only. IBAT's own PS6 report is positioned as "initial risk screening and scoping" [R4-004]; the final CHA remains a consultant document with surveys [R4-051]. A P2 report should therefore: list triggering features by PS6 criterion (1–5) and EBRD PR6 priority-feature test, cite IUCN/KBA/WDPA plus national sources, state data gaps and recommended surveys, carry a named expert's review, and be formatted so a consultant can drop it into a CHA. This is a design inference, not a lender-published template (none found).

## Q4. Business models and evidence consultancies pay
- Freemium portal + paid reports/data: IBAT (free account, PAYG reports, subscriptions) [R4-001][R4-075]; NatureAlpha Explorer free; ENCORE free; MAGIC/Natura 2000 free.
- Per-report credits: IBAT PAYG $750/$1,250/$5,000 [R4-001][R4-004]; NC NatureServe $100 per project review [R4-017]; Joe's Blooms per project [R4-021].
- Tiered subscription: IBAT $5k–35k/yr; NatureMetrics platform listed per site per year [R4-033]; Kuyua subscription modules [R4-038].
- Expert-verified premium tier: bng.ai £599 (own ecologist) to £1,999 (AiDASH ecologist + on-site PEA) [R4-022]; Joe's Blooms £1,250 premium [R4-021].
- Data licence: NatureServe $10k–300k [R4-016]; IBAT data embedding licence by partner review [R4-008].
- White-label / reseller to consultancies: IBAT PAYG allows consultancies to run screenings for clients [R4-008]; Ecobot sells to consultancies [R4-042]; Joe's Blooms offers enterprise/LPA portal [R4-021]. No explicit "white-label" product page found.
- Evidence consultancies pay for screening tools: ERM and The Biodiversity Consultancy listed as IBAT users [R4-008][R4-072] (snippets); Ecobot claims 3,796 users at consultancies/agencies [R4-042] (vendor claim); The Biodiversity Consultancy publishes a biodiversity-screening note built around IBAT [R4-072]. No revenue figures found.

## Q5. Gaps for Türkiye (what a Turkish expert-verified pre-screen could do)
Baseline facts:
- Nuh'un Gemisi (DKMP): vascular plants, mammals, birds, reptiles, amphibians, freshwater fish; province-level queries; ~1.8–2 M records; 13,404 species (3,703 endemic) at Dec 2024 [R4-060][R4-061][R4-062]. Invertebrates such as Odonata are not in the listed taxa in that description, which suggests a taxon gap for dragonflies in the national database (inference from the snippet; check).
- TÜBİVES (plants) reportedly not updated ~10 years [R4-063] (snippet).
- Herpetofauna: 35 amphibian + 145 reptile species; 38 not IUCN-assessed, 6 DD; 12 species on Bern Appendix II and 15 on Appendix III in one regional study [R4-066] (snippet from a ResearchGate listing; verify before reuse).
- Odonata: Mediterranean Red List assessed in 2007–2008 with one fifth threatened; European Red List (2024) covers Türkiye-in-Europe only [R4-067][R4-068] (snippets). Anatolian Odonata are thus partly outside the newest assessment.
- Bern Convention Emerald Network: Türkiye is among participating countries; candidate/adopted lists published on the Council of Europe reference portal [R4-069] (snippet).
Gaps vs. incumbents (no source found indicating otherwise):
1. No Turkish-language output (IBAT: Spanish only mentioned) [R4-015]. Turkish regulators and ÇED files are in Turkish; a bilingual (TR/EN) output serves both ministry and lender.
2. No integration of Nuh'un Gemisi / TÜBİVES / Emerald candidate sites / Turkish legal protection status (Bern, national lists) in any global tool found.
3. IBAT's species layer is range-based (IUCN) and global; local presence needs local data [R4-006]; P2 can add record-level evidence (Nuh'un Gemisi, GBIF, literature, own field data) plus an expert statement.
4. Taxon strength: herpetofauna and Odonata, with many unassessed or outdated assessments, is where a specialist can add value over range maps; this is an advantage only if the team holds validated occurrence data.
5. Expert verification: tools rarely include it (bng.ai and Joe's Blooms do in the UK; IBAT does not). IFC requires regional experts for CH [R4-012], so "tool + named Turkish expert sign-off" matches lender process.
Where P2 would likely not win: global KBA/Red List screening (IBAT is cheap relative to a CHA and lender-recognised); marine and birds (BirdLife-linked); corporate TNFD portfolio screens (NatureAlpha free tier, NatureMetrics); competing with big consultancies who write the CHA itself. P2 is best framed as a pre-screen that feeds the consultant's CHA and ÇED flora-fauna report, and possibly as a reseller layer on top of IBAT data (licence terms permitting).

## Pricing table (as seen 2026-10-05)
| Product | Unit | Price | Source |
|---|---|---|---|
| IBAT Free | account | $0 | R4-001 |
| IBAT PAYG proximity / freshwater | per site report | $750 | R4-001 |
| IBAT PAYG PS6/ESS6 | per report | $1,250 (updated) | R4-004 |
| IBAT PAYG multi-site | per report | $5,000 | R4-001 |
| IBAT STAR layer download (PAYG) | per download | $10,000 | R4-004 |
| IBAT Basic / Pro / Enterprise / Ent. Plus | per year | $5,000 / $15,000 / $25,000 / $35,000 | R4-001, R4-004 |
| NatureServe Explorer Pro data licence | licence | $10k minimum; $100k regional; ~$300k national | R4-016 |
| NatureServe NC project review | per user-year / per project | $600 / $100 | R4-017 |
| UK statutory metric tool | tool | free; consultant GBP399+VAT to GBP3,500 | R4-018, R4-019 |
| Joe's Blooms BNG | per project | GBP495–995 incl. VAT; GBP1,250 premium; GBP250/h | R4-021 |
| bng.ai | per project | GBP249 / 599 / 1,499 / 1,999 | R4-022 |
| MAGIC, Natura 2000 viewer, ENCORE | access | free | R4-024, R4-026, R4-027 |
| NatureAlpha Explorer | access | free tier | R4-036 |
| NatureMetrics eDNA | per sample | GBP160–300 ex VAT (kit GBP35) | R4-029 |
| NatureMetrics platform | per site per year | GBP5,000–7,500 (aggregator) | R4-033 |
| Wildlife Acoustics SM4; Kaleidoscope Pro | unit; per year | $799; GBP354.17 (university GBP262.50) | R4-045, R4-046 |
| AudioMoth 1.2.0 | unit | $99.99 / GBP79.99 | R4-047 |
| Kuyua, Ecometrica, Ecobot, Kayrros, Habitat Forward, Arbimon Pro | - | not found | R4-038 etc. |

## Caveats
- Many prices come from search-result summaries; re-check on vendor pages before external use.
- IBAT user counts come from differently dated sources (older press, 2025 secondary summary); they are not a current audited figure.
- The Equator Principles count differs by source/date (126 vs 128).
- Turkish-gap claims are absence-of-evidence from ~39 searches, not product audits.
