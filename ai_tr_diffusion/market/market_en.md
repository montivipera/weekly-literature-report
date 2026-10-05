# Market study: product models for P1 (Gediz wetland benchmark) and P2 (ÇED biodiversity pre-screening)

Date 2026-10-05. Opus synthesis of the four workstreams R1–R4 (`R1_p1_global.md`, `R2_p1_turkiye.md`, `R3_p2_turkiye.md`, `R4_p2_global.md`). No new searches were run. Every workstream figure is "via search result": the URL appeared in a search result, most pages were not read in full, and many numbers come from search-engine summaries. Prices are as seen on 2026-10-05 in the original currency. "Unsourced estimate" means my own judgement with no source behind it. Citations such as [R3-012] map to `sources_market.csv` (352 rows, the union of R1–R4, ids kept). Points taken from general knowledge rather than the workstreams are marked "(general knowledge, verify)".

**Constraints that shape every model** (researcher profile, BRIEF §7):
- The team is one researcher (wetland/delta ecologist at Ege University; herpetofauna, Odonata, vegetation, remote sensing) plus a science-and-culture cooperative that can invoice and receive grants. It holds no ÇED Yeterlik Belgesi, and only certified firms may prepare ÇED reports [R3-020]. P2 therefore sells to or through certified firms, developers and lenders; it never acts as the ÇED author.
- Partners: a metropolitan municipality (assumed to be İzmir BB; still unconfirmed in STATE.md), WWF-Türkiye, Tour du Valat and a national nature NGO.
- Build mode: multi-agent Claude Code workflows, no hand coding. MVPs have to be agent pipelines that produce standard files (GeoPackage, CSV/XLSX, DOCX/PDF, COG, FLAC). Custom SaaS platforms are out of reach.
- Season: a 90-day window that starts in October 2026 falls mostly outside the Odonata flight season and the main anuran calling season. MVPs therefore rely on existing field data and desk work. New field capture is planned for spring 2027.

---

## 1. Evidence summary

**P1: field-labelled wetland data**
- **No payer for labels.** The main EO and bioacoustic benchmarks are open (CDLA-Permissive, CC-BY, CC0), and FM teams use them for free. No case of an FM team paying for labels was found, and no model team calls for regional ground truth [R1-011][R1-030][R1-006].
- **The only cash buyers of ground truth are forest-carbon MRV firms**, and their spending covers forest biomass only. Sylvera reports spending more than USD 10M on LiDAR and plot data; BeZero and Chloris swap plots for maps. Nothing covers wetland or fauna labels [R1-082][R1-079].
- **The need is documented; purchases are not.** AlphaEarth says labels are scarce [R1-047]. EarthShift finds a 15–20% drop in performance out of distribution [R1-107]. WorldCover is weak on herbaceous wetland [R1-015]. BigEarthNet has no Turkish area [R1-008], and AnuraSet is Neotropical [R1-030]. No reptile acoustic benchmark, field-verified Odonata image set or co-located multimodal wetland site was found.
- **Türkiye: no purchase, licence or tender for labelled data** (R2). Money flows through DKMP provincial inventory tenders, for example Ankara IKN 2026/1788766 (amounts not shown) [R2-011]. It also flows through grants: TÜBİTAK 1071 pays up to €160k per project, and the Turkish BiodivConnect pot is €350k [R2-034][R2-032]. The AI Action Plan's 2,000-dataset library is a publication channel, not a buyer [R2-001].
- **Validation need.** MWO/Tour du Valat validates its maps against local inventories [R2-053], and no Turkish partner was found. Copernicus HRL Water & Wetness is weak on temporary wet areas [R2-058].
- **Prices come only from adjacent markets.** Annotators cost USD 30–50/h [R1-074]; expert audio annotators cost 5–15× crowd rates [R1-075]; BirdCLEF+ 2025 offered USD 50k in prizes and drew 9,636 entrants [R1-056]. **No price exists for species- or habitat-labelled data.**

**P2: ÇED biodiversity pre-screening**
- **Volume.** Reported 2025 figures: 716 olumlu, 3,056 "gerekli değildir", 304 olumsuz; energy accounted for 422 of the olumlu decisions. The totals are inconsistent, so they need verification [R3-004]. On 05.03.2026 the "gerekli değildir" outcome was abolished [R3-011], which plausibly means more full reports. DKMP requires ecosystem reports for wind (RES) and mining, and ornithological reports (ODR) for RES/GES [R3-018][R3-019]. The 05.09.2026 wetland amendment allows renewables in sustainable-use zones of wetlands [R3-013].
- **Court risk.** The olumlu decision for Gaia RES was annulled for insufficient flora and bird monitoring, and re-issued with the turbines already erected [R3-053][R3-054]. The Germencik expert panel found 6 amphibians and 6 reptiles listed where the literature indicated substantially more [R3-055].
- **No fee data.** There is no public price for flora-fauna reports. One consultancy lists an ODR at 140–176k TL (unverified) [R2-085]. No Turkish screening tool was found.
- **IBAT is the priced incumbent.** Subscriptions are $0–35k per year; pay-as-you-go reports cost $750 (proximity), $1,250 (PS6) and $5,000 (multi-site) [R4-001][R4-004]. It is global-only and positioned as scoping [R4-010]. **IFC PS6 guidance requires external experts with regional experience** [R4-012]. Embedding IBAT data in another product needs partner review [R4-008], and there is no Turkish output [R4-015].
- **Lender work is concentrated.** Enerjisa's 750 MW wind portfolio has public critical habitat assessments (CHAs) written by Mott MacDonald and ERM [R4-051][R3-028][R3-029].
- **Expert-tier template.** bng.ai charges £249–1,999 across its tiers, and Joe's Blooms charges £1,250 for its premium tier [R4-022][R4-021]. AI-drafted ecological reports needed substantial expert revision [R4-044].
- **Data gaps.** Nuh'un Gemisi (about 2M records) has **no Odonata** [R4-060]. TÜBİVES is about 10 years stale [R4-063]. 38 Turkish herp species have no IUCN assessment (snippet) [R4-066].

**Absent, stated bluntly:** no cash buyer for wetland or fauna labels; no Turkish fee or willingness-to-pay figure for any P2 model; no public CHA fee; no count of certified ÇED firms; no known reuse terms for Nuh'un Gemisi.


---

## 2. Product models

Overview (the demand-evidence grade covers demand only, not feasibility):

| ID | Model | Main buyer | Revenue type | Demand evidence |
|---|---|---|---|---|
| P1-1 | Open benchmark + commercial licence (dual licence) | Commercial FM, acoustic-model and MRV teams | Licence | Weak |
| P1-2 | Validation partner (work packages) | MWO/Tour du Valat, wetland-map producers, Biodiversa+/Horizon consortia | Grant-funded work package or subcontract | Medium |
| P1-3 | Benchmark inclusion / competition track | FM and bioacoustics research community | None (academic capital) | Strong for uptake, none for cash |
| P1-4 | Gediz living lab (paid reference site) | EU projects, sensor and MRV firms | Per-campaign fee | Weak |
| P1-5 | Inventory-tender subcontracting with AI-assisted labelling | DKMP/ÇŞB tender winners | Service contract | Medium |
| P2-1 | Tiered polygon pre-screen (automated + expert-verified) | RES/GES/JES developers, ÇED consultancies | Per report | Medium |
| P2-2 | Lender-grade PS6/PR6 critical-habitat screen + survey design | Developers seeking IFI/Equator finance; Mott MacDonald/ERM | Per site or day rate | Medium |
| P2-3 | Litigation-risk audit of ÇED biodiversity chapters | Developers before submission, or NGOs/municipalities/law firms (choose one side) | Per audit | Medium need / weak WTP |
| P2-4 | White-label biodiversity-chapter drafter for ÇED consultancies | Yeterlik-certified consultancies | Per chapter or subscription | Weak |
| P2-5 | Wetland-zone and cumulative-impact assessment for renewables | Developers in or near designated wetlands; wetland commissions | Per project | Weak–medium |
| P2-6 | Turkish herpetofauna/Odonata reference layer (data/API) | Nature-risk platforms, international consultancies, DKMP | Data licence | Weak |

Note on the brief's P2 candidates. Candidates (a) per-polygon report and (b) expert-verified tier are **merged into P2-1**: the bng.ai template shows they are tiers of one product, not separate models. Candidate (e) white-label is kept as P2-4, but redefined around a different output (the consultancy's draft ÇED chapter, not a screening report) so that it is distinct. P2-5 is new: it rests on the regulatory hook of the 05.09.2026 wetland amendment, which fits the researcher's profile more closely than any other P2 model.

### P1-1 Open benchmark + commercial licence (BirdNET-style dual licence)
- **Purpose:** make Gediz the reference Mediterranean wetland test set, and charge the few commercial users who cannot work with non-commercial data.
- **Buyer and why they pay:** commercial FM, acoustic-model and MRV teams that need commercially clean, expert-verified labels. The licence gap is documented: BirdNET models are CC BY-NC-SA, with a commercial licence on request [R1-051]; xeno-canto-derived sets drop ND-licensed recordings [R1-026]; Maxar open data is NC [R1-070]; the GBIF API can return NC images [R1-067]. **No evidence of anyone paying for such labels** [R1-006][R1-082].
- **Inputs → outputs:** Sentinel-1/2 time-series chips (COG/Zarr), drone orthomosaics (COG), habitat polygons (GeoPackage, crosswalked to EUNIS/IUCN GET and to WorldCover/CORINE), passive acoustic monitoring (PAM) audio (FLAC) with strongly labelled calls (Raven tables/CSV), Odonata and herp photos (JPEG + Darwin Core CSV). Also a datacard, fixed splits and baseline scores, hosted on Zenodo, Hugging Face or Source Cooperative [R1-063][R1-064].
- **Must-have features:** (1) field-verified labels with observer and date provenance; (2) a spatially held-out test area; (3) multi-season labels (R1 gap 3); (4) class crosswalks so that map producers can compute accuracy; (5) a TerraTorch/PANGAEA-compatible loader and baselines [R1-002]; (6) licence split: CC-BY test set, NC training extension, commercial licence on request.
- **Pricing:** there is no price anchor for labelled ecology data. Adjacent figures: marketplace datasets USD 5–500 [R1-077]; one AWS geospatial licence at USD 150k/yr, for US building footprints and not comparable [R1-078]; Planet at USD 1.1–12k/yr [R1-068]. Unsourced estimate: €3–10k per commercial licensee per year. Realistic year-1 licence revenue is close to zero.
- **90-day MVP:** agents assemble a v0 release from existing thesis and partner data: one season of habitat polygons, matching Sentinel-2 chips, and whatever anuran/Odonata material already exists. Then a Zenodo DOI, a Hugging Face card, and a baseline run (e.g., Prithvi/TerraMind via TerraTorch, scripted by agents). Also a data-paper outline (Scientific Data/ESSD).
- **Moat:** expert-verified species- and habitat-level labels at a permitted, long-term site. No co-located multimodal set exists (R1 gap 8). Once data are released openly the moat in the data itself is weak; the durable moat is the continuing time series and the team that can re-label.
- **Main risk:** the open release cannibalises the paid licence, and commercial demand may never appear. Data rights also need settling (Ege University IP, partner-collected data, DKMP permit conditions).
- **Demand evidence: weak.**

### P1-2 Validation partner: field validation sold as work packages
- **Purpose:** sell independent accuracy assessment of wetland map products in the Eastern Mediterranean as a funded work package or subcontract, not as data. Candidate products: MWO/GEOclassifier maps, Copernicus HRL Water & Wetness, Global Wetland Watch typologies, SAYBİS/DKMP inventories, and EU-consortium maps.
- **Buyer and why they pay:** consortia and programmes with grant budgets, for whom validation is a standard deliverable. MWO validates against local inventories [R2-053] and has no Turkish partner (R2). Mediterranean wetland remote sensing needs ecological field knowledge; "good-looking maps can be wrong" [R2-054][R1-025]. HRL W&W is weak on temporary wet areas [R2-058]. Global Wetland Watch calls field validation "vital" [R1-022]. Funding pools: BiodivMon funded 33 projects (>€46M) [R2-036]; BiodivConnect funded 36 projects (>€50M) [R2-031]; TÜBİTAK 1071 pays up to €160k per project [R2-034]; an EU-funded technical assistance project to the Water Management GD on wetlands was worth €2.725M [R2-025].
- **Inputs → outputs:** the partner's map, its class legend and its area of interest go in. Out come: a stratified probability sample design; a field and drone reference dataset (GeoPackage/CSV, with photos); a confusion matrix with area-adjusted accuracy and confidence intervals; error maps; a validation report (PDF); and a DOI for the reference set.
- **Must-have features:** (1) probability sampling stratified by map class; (2) a field protocol for seasonal/temporary wet and aquatic-vegetation classes [R1-104]; (3) drone orthophoto reference; (4) accuracy statistics with uncertainty; (5) ecological diagnosis of errors (why each class fails); (6) a reusable reference set that can validate several products ("collect once, validate many").
- **Pricing:** paid as work-package budgets. Anchors: the TÜBİTAK 1071 cap (€160k per project, €100k per institution) [R2-034]; annotators at USD 30–50/h [R1-074]; UK senior ecologists at £280–450/day [R4-076] as an international day-rate reference. Unsourced estimate: €25–80k per work package over 2–3 years, and €8–20k for a one-off validation of one product at one site.
- **90-day MVP:** use existing Gediz field points and drone flights to validate 2–3 open products: WorldCover herbaceous wetland [R1-015], GWL_FCS30 [R1-024], and HRL W&W if it covers Türkiye (general knowledge: Copernicus pan-European layers cover EEA38 including Türkiye; verify). Deliver a 6-page "Gediz validation note" as a calling card to Tour du Valat and Global Wetland Watch. Get the cooperative an EU Participant Identification Code (PIC) and add it as partner or third party to one proposal in preparation (Biodiversa+, Horizon Cluster 6, or a TÜBİTAK 1071 national leg).
- **Moat:** the Tour du Valat relationship; site access and permits; the ecological interpretation of seasonal wetlands; Turkish-language liaison with DKMP/SAYBİS. A remote academic group cannot copy this quickly.
- **Main risk:** cash arrives 12–18 months after a call and only if the consortium wins. Academic partners may also do validation with students at no charge.
- **Demand evidence: medium.** The validation need and the grant money are documented; a case of an external validator being paid was not found.

### P1-3 Benchmark inclusion / competition track (academic capital)
- **Purpose:** place Gediz tasks in the venues that model teams already use: a PANGAEA/GEO-Bench-2 task, a BEANS/BirdSet-compatible Mediterranean anuran-and-bird evaluation set, or a LifeCLEF/BirdCLEF-style challenge. This buys citations, co-authorships and visibility, which feed P1-2 and P2-2 ("regional expert" credentials).
- **Buyer and why:** no cash buyer. Hosts fund the prizes: BirdCLEF+ 2025 offered USD 50k, drew 9,636 entrants and included amphibians [R1-056][R1-057]. Maintainers are looking for geographic spread (PANGAEA added Africa and SE Asia) [R1-001]. Perch 2.0 trains on amphibians but its evaluation is bird-led [R1-054]. Reviews call for standardised anuran datasets [R1-100], and open amphibian classifiers are "largely absent" [R1-101]. No Turkish anuran acoustic dataset exists (R2).
- **Inputs → outputs:** a curated test set with hidden labels, a task definition, a metric, a baseline notebook, and a pull request to maintainers or a challenge proposal; plus a data paper.
- **Must-have features:** (1) strong, time-stamped labels for anurans; (2) hidden test labels; (3) BirdSet/BEANS-compatible formats; (4) a CC-BY licence; (5) a baseline; (6) the data paper with a DOI.
- **Pricing:** none. The researcher bears the curation cost, and the value is non-monetary.
- **90-day MVP:** (a) send a one-page task specification to the PANGAEA and BEANS maintainers through GitHub issues; (b) build "Gediz-Anura v0" (unsourced target: 10–20 h of strongly labelled clips) from existing recordings, if they exist; (c) with Tour du Valat or an acoustic group, draft a proposal for a Mediterranean soundscape task for a future LifeCLEF round.
- **Moat:** first mover for a Turkish/Eastern Mediterranean task, and label quality.
- **Main risk:** no revenue; maintainers or challenge hosts may decline; curation competes with thesis time.
- **Demand evidence: strong for uptake** (open benchmarks and Kaggle challenges are heavily used), **none for cash.**

### P1-4 Gediz living lab (paid multimodal reference site)
- **Purpose:** offer a permitted, instrumented reference site with permanent plots, a PAM grid, repeat drone flights and labelled time series. Model teams, MRV firms, sensor vendors and EU projects could run their tests there.
- **Buyer and why:** EU projects that need a Mediterranean demonstration or pilot site; sensor and software vendors (Wildlife Acoustics, Arbimon) [R4-045][R4-048]; FM pilot programmes (AlphaEarth ran unpaid pilots with more than 50 organisations [R1-048]). The local in-kind base exists: the municipality has supported Doğa Derneği's Gediz monitoring since 2020 [R2-080][R2-082]. **No evidence was found of anyone paying for site access.**
- **Inputs → outputs:** the site package (plot network, permits, logistics, baseline data) in, campaign data and a validation report out, with open core data and paid campaigns.
- **Must-have features:** (1) permanent georeferenced plots and transects; (2) a timestamped PAM grid; (3) repeat drone flights; (4) permit and logistics handling; (5) a data-sharing agreement template; (6) a public calendar of seasonal windows.
- **Pricing:** no anchor. Unsourced estimate: €10–30k per pilot campaign, or budgeted as demonstration-site costs inside EU proposals.
- **90-day MVP:** a one-page offer, a site map, an inventory of existing data, and a letter of support from the municipality. List the site as a demo site in one proposal.
- **Moat:** physical and permit-based (DKMP research permit, municipality, NGO), plus multi-year continuity. It is the hardest model to copy.
- **Main risk:** no demand evidence and high fixed costs (equipment theft, maintenance, disturbance of breeding birds at a key bird site).
- **Demand evidence: weak.**

### P1-5 Inventory-tender subcontracting with AI-assisted labelling
- **Purpose:** earn from state inventories that are already funded. The cooperative would deliver herpetofauna, Odonata and PAM modules to tender winners, using AI pre-labelling (BirdNET/Perch, image classifiers) checked by experts to cut labelling time. P1 data are a by-product, if the contract's data rights allow it.
- **Buyer and why they pay:** DKMP regional directorates tender provincial terrestrial and freshwater inventories (Muğla 540 days; Ankara 730 days, IKN 2026/1788766) [R2-010][R2-011]. ÇŞB TVK tenders ecological research for natural sites [R2-016]. Winners include consultancies (Alfaeko markets this work) [R2-015] and universities (Hacettepe, Patara) [R2-014]. Multi-taxon UBENİS specifications need herp and Odonata specialists, and the national database lacks Odonata [R4-060].
- **Inputs → outputs:** the tender specification goes in. Out come field and PAM data, occurrence records in Nuh'un Gemisi format (CSV), distribution maps, Turkish report chapters, and an audio and photo voucher archive.
- **Must-have features:** (1) export ready for Nuh'un Gemisi; (2) an AI pre-labelling log with expert-verification flags; (3) an Odonata module; (4) an anuran and bird PAM module; (5) photo and audio vouchers; (6) QA traceability per record.
- **Pricing:** tender amounts were not found. The order-of-magnitude anchor is one firm's ODR price for 30+30 field days: 140–176k TL including VAT (unverified) [R2-085]. Unsourced estimate: 150–400k TL per taxon module per province over the contract.
- **90-day MVP:** agents list all DKMP and ÇŞB inventory tenders on EKAP for 2024–26 with their winners and, where visible, approximate costs. Contact three winners about herp/Odonata subcontracts. Prepare a capability statement and price sheet. Check the cooperative's eligibility (work-experience certificates) and university rules on outside work.
- **Moat:** expertise in hard taxa, regional presence, and AI-assisted throughput.
- **Main risk:** DKMP owns the data, which may block reuse in P1. Margins are low, and university employment may conflict with tender work.
- **Demand evidence: medium.** The spending is real and recurring; the amounts and winners' appetite for subcontracting are unverified.

### P2-1 Tiered polygon pre-screen (automated + expert-verified)
- **Purpose:** a fast, cheap, fully sourced answer to "which biodiversity issues will this site raise?" before a land lease, a YEKA bid or a ÇED application file.
- **Buyer and why they pay:** RES/GES/JES developers (energy accounted for about half or more of 2025 olumlu decisions [R3-004]) and ÇED consultancies doing scoping. They pay because a missed species costs months: Gaia was annulled and re-processed [R3-053][R3-054]. The 2026 amendment also removed the "gerekli değildir" route [R3-011], and DKMP requires ecosystem reports and ODRs [R3-018][R3-019]. The price model is proven abroad: IBAT pay-as-you-go [R4-001] and bng.ai tiers [R4-022].
- **Inputs → outputs:** a polygon (KML/KMZ/SHP/GeoJSON, or the e-ÇED coordinate table) plus project type goes in. Out come a bilingual TR/EN PDF report of 8–15 pages, an XLSX species table, a GeoPackage of layers and a source log. The expert tier adds a signed statement.
- **Must-have features:** (1) Turkish data layers: Nuh'un Gemisi province data [R4-060], the Amphibians of Türkiye database [R2-072], GBIF limited to CC0/CC-BY [R1-065], Ramsar and SAYBİS wetlands [R2-017][R2-021], ÇED Ek-5 sensitive areas [R3-012], Emerald sites [R4-069]; (2) a species-likelihood table with IUCN, Bern II/III and national status, the evidence, the distance to the nearest record, and the season; (3) a data-gap and survey calendar (taxon × month × method); (4) TR/EN output; (5) the expert tier: a named herp/Odonata specialist marks each row confirmed, downgraded or added, with an optional one-day site visit; (6) row-level provenance (every claim cites a record or a paper).
- **Pricing:** three tiers, all in TL at the rate on the invoice date. The structure copies bng.ai (£249 / £1,499 / £1,999 [R4-022]) and sits below IBAT's USD 750 proximity report [R4-001]. Joe's Blooms' £1,250 premium tier [R4-021] is a second anchor for the middle tier.

  | Tier | Price (unsourced estimate) |
  |---|---|
  | Automated desk screen | €150–350 |
  | Expert-verified desk screen | €700–1,500 |
  | Expert-verified + site visit | €1,500–3,000 |

- **90-day MVP:** build the agent pipeline (Section 3A) and backtest it on the Germencik case: does it flag the amphibian and reptile species the expert panel said were missing [R3-055]? Run the same test on Gaia. Then produce 10 free reports for Aegean consultancies and developers in exchange for feedback and a price conversation, and publish one anonymised sample.
- **Moat:** Turkish layers, Turkish grey literature, the researcher's own Aegean records, and a named regional expert. IBAT cannot sign as a regional expert [R4-012], and global tools do not output Turkish [R4-015]. Consultancies rarely have herp/Odonata depth [R3-055].
- **Main risk:** data licensing. Nuh'un Gemisi reuse terms are unknown. WDPA, KBA and IUCN range data restrict commercial use (general knowledge, verify; IBAT's embedding rule [R4-008] points the same way). Turkish willingness to pay is unknown, and a missed species creates liability.
- **Demand evidence: medium.** Volume, regulatory pressure, court risk and a priced foreign template are documented; Turkish WTP is not.

### P2-2 Lender-grade PS6/PR6 critical-habitat screen + survey-design package
- **Purpose:** deliver the first two steps of a CHA, formatted so that the lead consultant can drop them into the CHA. Step one is screening for triggers by IFC PS6 criteria 1–5 and EBRD PR6 priority features, using national data. Step two is a baseline survey design that the lender will accept.
- **Buyer and why they pay:** developers seeking IFI or Equator finance (the Enerjisa pattern: per-plant CHAs, one-year baselines including herpetofauna) [R4-051][R2-086]; international consultancies (Mott MacDonald, ERM) [R3-028][R3-029], who must involve **external experts with regional experience** and species specialists for CR/EN triggers [R4-012]; Turkish Equator banks for pre-due-diligence (TSKB's critical-habitat exclusion [R3-049], Garanti BBVA [R3-051]). IBAT's PS6 report is explicitly scoping only [R4-004], and its critical habitat analysis is global-level [R4-010].
- **Inputs → outputs:** the area of interest and project description go in. Out come an English CH screening memo (table of features × PS6 criterion × likely/potential CH, following the global screening layer logic [R4-011]), maps of the Ecologically Appropriate Area of Analysis (EAAA), species-specialist statements, a survey design (methods, effort, seasons) and a GIS package.
- **Must-have features:** (1) a PS6/PR6 criterion matrix with thresholds; (2) EAAA delineation; (3) reconciliation of national and global data (the client's IBAT report is an input when available); (4) signed species-specialist statements for herpetofauna and Odonata, with a named network for birds and bats; (5) a survey design with effort and seasonality; (6) a lender-format English deliverable.
- **Pricing:** the floor is IBAT's PS6 report at USD 1,250 (desk, global) [R4-004]. No public CHA fee exists [R4-059]. Unsourced estimate: €4–12k per site, or a subcontract day rate of €350–600, with the UK senior-ecologist rate of £280–450/day [R4-076] as reference.
- **90-day MVP:** turn the public Enerjisa CHAs into a template (Ihlamur's priority features: 6 birds, 3 plants, 13 mammals, 1 reptile [R3-044]). Produce a blind "shadow screening" for one disclosed project and compare it with the published CHA. Pitch the comparison to the Mott MacDonald Türkiye and ERM biodiversity leads as a regional herp/Odonata specialist offer.
- **Moat:** the regional-expert requirement [R4-012], national data, and a publication record. Neither IBAT nor a non-Turkish consultancy can supply a Turkish regional expert from its own resources.
- **Main risk:** the market is concentrated in 2–3 consultancies and moves slowly. For wind projects, birds and bats usually dominate critical habitat, so herp/Odonata may be minor features (Ihlamur: 1 reptile out of 23 features [R3-044]). The model needs a bird/bat partner.
- **Demand evidence: medium.** The workflow and the regional-expert requirement are documented; prices and outsourcing practice are not.

### P2-3 Litigation-risk audit of ÇED biodiversity chapters
- **Purpose:** a systematic gap analysis of a draft or filed ÇED flora-fauna chapter. It compares the species listed with those expected from the literature and national records, and the survey timing and methods with taxon seasonality.
- **Buyer and why they pay:** there are two possible sides, and **the cooperative must choose one**. The defensive side is developers and consultancies before submission, or after a lawsuit is filed; Gaia shows the cost of a weak baseline [R3-053]. The adversarial side is municipalities, NGOs, bar associations and law firms in ÇED lawsuits (the Germencik expert panel [R3-055]; academic critiques of reused species lists and same-day flora/fauna visits [R3-031][R3-058]). Danıştay reversals go both ways [R3-057], so both sides face uncertainty.
- **Inputs → outputs:** the ÇED report (Turkish PDF) and polygon go in. Out come a gap matrix (expected vs listed species, survey timing vs season, method adequacy), a risk rating per gap, and a Turkish memo with citations, signed by the expert.
- **Must-have features:** (1) extraction of species lists from the PDF; (2) the expected-species list from the P2-1 engine; (3) a season and method checker; (4) a legal-status cross-check (Bern, IUCN, national); (5) a risk score per gap; (6) an expert-signed memo.
- **Pricing:** no source for court expert-panel fees. Unsourced estimate: €1,000–3,000 per audit. NGO-side work would be grant-funded.
- **90-day MVP:** audit 5 public Aegean RES/GES ÇED reports plus the Germencik file, and publish an anonymised methods note.
- **Moat:** herp/Odonata depth and court-proof sourcing.
- **Main risk:** **conflict of interest.** Working for NGOs or municipalities undercuts sales to developers in P2-1, P2-2 and P2-4, and the reverse also holds. Paid party work may also be incompatible with being appointed as a court expert (bilirkişi). WWF-Türkiye and the NGO partner are reputational stakeholders.
- **Demand evidence: medium for need, weak for willingness to pay.**

### P2-4 White-label biodiversity-chapter drafter for ÇED consultancies
- **Purpose:** under the consultancy's brand, produce the draft flora-fauna/ecosystem section in the regulatory format (Ek-3/Ek-4 [R3-010]). The draft includes species tables, status columns, maps and citations, for the consultancy's biologists to field-verify and sign.
- **Buyer and why they pay:** Yeterlik-certified firms (the count is unknown) [R3-020][R3-021]. Mid-size firms market ecosystem and flora-fauna reports [R3-026][R3-027][R3-018][R3-019] and would pay to cut desk time. Consultancies abroad do pay for screening tools: ERM and The Biodiversity Consultancy use IBAT [R4-008][R4-072], and Ecobot reports 3,796 users (vendor claim) [R4-042]. **No Turkish evidence.**
- **Inputs → outputs:** polygon and project type in; out comes an editable Turkish DOCX chapter with tables, a GeoPackage and a field-verification checklist.
- **Must-have features:** (1) a DOCX template matching the ÇED format; (2) status columns filled automatically; (3) a literature list; (4) a field-verification checklist that flags the rows still unconfirmed; (5) versioning; (6) volume pricing.
- **Pricing:** anchors are IBAT Basic at USD 5k/yr and Pro at USD 15k/yr [R4-001], and NatureServe NC at USD 600 per user-year plus USD 100 per project [R4-017]. Unsourced estimate: €150–400 per chapter, or €2–5k per year per firm.
- **90-day MVP:** draft chapters for live projects at 3 consultancies and measure the desk hours saved.
- **Moat:** thin. Once the data layers exist, a consultancy could rebuild the template with a general LLM. The only moat is the herp/Odonata content and data layers.
- **Main risk:** commoditisation, and liability inside signed reports. It could also make the copy-paste species lists criticised in the literature [R3-031] faster to produce. It conflicts with P2-3 if the cooperative later audits its clients' reports.
- **Demand evidence: weak.**

### P2-5 Wetland-zone and cumulative-impact assessment for renewables
- **Purpose:** assess energy projects proposed in or near designated wetlands, now that the 05.09.2026 amendment allows renewables in sustainable-use zones and adds environmental-flow and cumulative-impact requirements [R3-013][R3-014]. The assessment covers inundation dynamics, habitat, wetland-dependent herpetofauna, Odonata and waterbirds, and the cumulative footprint of clustered RES/GES.
- **Buyer and why they pay:** developers who need permits in wetland zones; wetland commissions and DKMP as reviewers. The context: dense Aegean wind capacity (İzmir 1,886 MW and Balıkesir 1,375 MW in 2019) [R3-007]; 14 Ramsar sites (184,487 ha) [R2-021]; 6,418 wetlands in SAYBİS [R2-018]; annual monitoring duties in protected zones [R2-022]. The rule is new and no supplier was found (inference; no buyer evidence).
- **Inputs → outputs:** project and wetland boundary/zone in. Out come a Turkish report, a Sentinel-1/2 inundation time series (COG), a habitat map, a cumulative-projects map (built from monthly ÇED decision digests [R3-006][R3-063]), and mitigation and environmental-flow flags.
- **Must-have features:** (1) a zone check against wetland protection zones; (2) an EO inundation history; (3) a cumulative map of neighbouring projects; (4) a wetland-dependent species table; (5) hydrology and environmental-flow flags; (6) expert sign-off.
- **Pricing:** no anchor. Unsourced estimate: €3–8k per project.
- **90-day MVP:** a public "renewables × wetland zones" screening atlas for Aegean Ramsar and national-importance wetlands, overlaid with 2024–26 energy ÇED decisions. It doubles as a demand test and a calling card, and could be co-branded with a partner if positions align.
- **Moat:** wetland EO, delta ecology, Tour du Valat methods and local permits. This is the researcher's exact profile.
- **Main risk:** the rule is contested. Conservation partners may oppose renewables in wetlands, so working for developers here is reputationally exposed. Volume is unknown.
- **Demand evidence: weak–medium.** The regulatory hook is documented; buyers are not.

### P2-6 Turkish herpetofauna/Odonata reference layer (data/API)
- **Purpose:** a curated, expert-validated layer of occurrences and modelled distributions for Turkish amphibians, reptiles and Odonata, with legal status. It would be licensed to platforms and consultancies, and it fills the Odonata gap in Nuh'un Gemisi [R4-060].
- **Buyer and why they pay:** nature-risk platforms (NatureAlpha, the NatureMetrics platform) [R4-036][R4-031]; international consultancies writing Turkish CHAs; DKMP as a data partner. The case: IBAT uses global range maps [R4-006]; 38 herp species are unassessed [R4-066]; the Mediterranean Odonata assessment is from 2007–08 [R4-068]. **No buyer found.**
- **Inputs → outputs:** literature, GBIF CC0/CC-BY records, the Amphibians of Türkiye database [R2-072] and the researcher's own records go in. Out come a Darwin Core occurrence table, 1 km species distribution model (SDM) rasters (COG), a status table, a GeoPackage and an API, with versioned DOIs.
- **Must-have features:** (1) records with expert validation and confidence flags; (2) SDMs per species; (3) status columns; (4) Odonata included; (5) versioned releases; (6) licence tiers (coarse layer open; fine-resolution and commercial use paid), with location obfuscation for species targeted by collectors and traders.
- **Pricing:** anchors are NatureServe's data licences, from a USD 10k minimum base fee up to USD 100k regional [R4-016], and IBAT's embedding review [R4-008]. Unsourced estimate: €5–15k per year per commercial licensee; free for research.
- **90-day MVP:** "Odonata of western Anatolia v0", built from literature, CC-BY iNaturalist research-grade records and the researcher's own records, with a data-paper draft. Offer it to DKMP as an Odonata contribution to Nuh'un Gemisi.
- **Moat:** expert validation in a neglected taxon.
- **Main risk:** a very small buyer pool. Source records may carry NC licences [R1-067], and location leakage could harm sensitive species.
- **Demand evidence: weak.**

---

## 3. Design sketches

### 3A. P2-1 Tiered pre-screen (the core engine for P2-1, P2-2, P2-3 and P2-4)

**Intake.** In the MVP this is a form or e-mail, not a web app. The client gives a polygon file, project type (RES/GES/JES/mine/other), phase (site selection, ÇED file, finance), tier and language.

**Pipeline (agent stages):**
1. *Geometry agent:* validates geometry and CRS (WGS84/TUREF), and builds 1/5/10 km buffers and a provisional EAAA.
2. *Context agent:* administrative units; land cover (WorldCover/CORINE); Sentinel-2 indices for wet/vegetated classes; overlaps with Ramsar/SAYBİS wetlands, Ek-5 sensitive areas, Emerald sites and KBAs (licence flag on each layer).
3. *Records agent:* Nuh'un Gemisi province export (manual if there is no API), GBIF filtered to CC0/CC-BY, the Amphibians of Türkiye database, iNaturalist research-grade records, and the researcher's own records. It deduplicates and computes the nearest-record distance.
4. *Literature agent:* DergiPark papers, theses and checklists. It extracts species-locality claims with page-level citations.
5. *Likelihood agent:* a rule-based High/Medium/Low/Unknown score from record distance, habitat match and season. The rules are versioned and printed in the report.
6. *Status agent:* IUCN, Bern Appendices II/III, CITES, national lists, endemism.
7. *Gap and survey agent:* a taxon × month calendar with recommended methods and effort.
8. *Composer:* TR/EN PDF, XLSX, GeoPackage.
9. *QA agent:* every row must have at least one source; citations must resolve; counts must be consistent across PDF, XLSX and GeoPackage.

**Expert verification sits between stages 8 and 9 (expert tiers only).** The researcher works through the XLSX, marking each species row as accept, downgrade, add or comment. Unsourced estimate: 30–90 minutes per report. The researcher then signs a statement of scope and limits, and adds an optional site visit.

**Deliverable as the buyer sees it (PDF):**
1. One-page summary with a traffic light for designated areas, high-likelihood protected species, data gaps and litigation-sensitive taxa.
2. Site map.
3. Designated and sensitive areas.
4. Species-likelihood table.
5. Data gaps.
6. Recommended survey programme by season.
7. "Species a court expert would expect to see" (the Germencik lesson).
8. Sources and provenance.
9. Expert statement and limitations: a pre-screen, not a ÇED report or a CHA.

### 3B. P2-2 Lender PS6/PR6 package (extends 3A)

**Additional stages:**
- Stage 10, *PS6/PR6 agent:* maps each feature to criteria 1–5 and PR6 priority features, using global screening-layer logic (likely/potential) [R4-011].
- Stage 11, *EAAA agent:* delineates the EAAA by taxon group.
- Stage 12, *reconciliation agent:* compares national records with the IBAT/IUCN picture, when the client supplies an IBAT report.

**Expert role.** This is the heaviest expert step. The researcher writes species-specialist statements for herp/Odonata triggers, and a named bird/bat partner covers those groups. It takes about 1–2 days per site (unsourced estimate).

**Deliverable (English, lender format):**
1. Executive summary for the lender's E&S team.
2. PS6 trigger matrix.
3. EAAA maps.
4. Specialist statements.
5. Baseline survey design, with effort, seasons and methods that the lender's adviser can audit.
6. Data annex (GeoPackage, XLSX).
7. Statement that the CHA remains the lead consultant's document.

### 3C. P1-2 Validation work package

**Framing.** The work package is written into a partner's proposal ("WPx: Independent field validation, Eastern Mediterranean").

**Pipeline:**
1. Ingest the partner's map and legend.
2. Agent-built stratified sample design (sample sizes per class, documented).
3. Field and drone campaign plan by season.
4. Field data entry (QField/ODK forms exported to GeoPackage).
5. Agents compute accuracy and area estimates.
6. Expert error diagnosis by habitat.
7. Report and reference-set release (DOI).

**Expert verification.** The researcher labels or verifies every reference unit, and records the reason for each ambiguous unit (seasonal water, emergent vegetation).

**What the partner receives:** a validation report with confusion matrices and confidence intervals, an error atlas, an open reference dataset, and a co-authored paper. Each additional product validated on the same reference set costs only stages 1, 5 and 6, which keeps the work package cheap for second and third clients.

---

## 4. Cross-product synergies and sequencing

**Which model funds or de-risks which**

| Model | What it does for the others |
|---|---|
| P2-1 | The engine for P2-2, P2-3 and P2-4. Its expert-verified records accumulate into P2-6. It is the fastest route to small invoices (weeks, not grant cycles), and that cash can pay for spring 2027 field equipment for P1. |
| P1-3 and P1-1 (data paper, benchmark tasks) | Produce the citable track record that makes the researcher a credible "regional expert" for P2-2 [R4-012] and a credible partner for P1-2. |
| P1-2 and P1-5 | Pay for fieldwork that produces labels and occurrence records. P1-5 data may belong to DKMP; check the contract before planning reuse. |
| P2-5 | Bridges both products: the same Sentinel inundation and habitat time series serves the P1 benchmark and the P2 wetland-zone assessment. |

**Conflicts to manage**
- P2-3 on the NGO side conflicts with P2-1, P2-2 and P2-4. Pick the side early.
- P2-5 sits in tension with conservation partners.
- An open P1-1 release cannibalises a commercial P1-1 licence.

**Suggested sequencing**

| When | P2 | P1 |
|---|---|---|
| Months 0–3 (Oct–Dec 2026) | P2-1 pipeline, Germencik/Gaia backtest, 10 free pilot reports, price interviews | P1-2 validation note on existing Gediz data; contact Tour du Valat and Global Wetland Watch; get the cooperative's PIC; P1-3 task specs to maintainers |
| Months 3–9 (Jan–Jun 2027) | Paid P2-1 tiers; P2-2 shadow screening and pitch to Mott MacDonald/ERM; P2-5 atlas if pilot interviews show interest | Spring field season: PAM grid, Odonata transects, drone flights. This feeds the P1-1/P1-3 data release and P2-6. One proposal with Tour du Valat or a Biodiversa+ consortium. Bid as subcontractor on one DKMP inventory (P1-5) if a winner wants herp/Odonata. |
| Months 9–18 | Decide on P2-4 (white-label) only if consultancies asked for it during the P2-1 pilots. Release P2-6 v1 once there are enough validated records. | Data paper and benchmark inclusion. P1-1 commercial licence only after visible adoption. P1-4 living lab only inside a funded project. |

---

## 5. Open questions to verify before building

| # | Question | Cheapest way to verify |
|---|---|---|
| 1 | Will Aegean ÇED consultancies and RES/GES developers pay for a desk pre-screen, and how much? | Five phone calls (e.g., the firms behind [R3-019][R3-026][R3-027][R3-018]) with one sample report and three price points. |
| 2 | What do flora-fauna, ecosystem and ODR reports and biologist days actually cost in Türkiye? | Search EKAP for awarded "ekosistem değerlendirme raporu" / "biyolojik çeşitlilik envanter" service tenders and read the approximate cost and award values. Ask the same in the calls for question 1. |
| 3 | May Nuh'un Gemisi data, WDPA/KBA polygons and IUCN ranges be used in a paid report? | One e-mail to DKMP (Nuh'un Gemisi terms) and one data-request form via IBAT/UNEP-WCMC [R4-008]. |
| 4 | Can a cooperative that is not Yeterlik-certified sell expert-signed biodiversity content that ends up in a ÇED annex? Does Ege University allow paid outside work through the cooperative, or require the döner sermaye route? | One call to the university legal/technology transfer office. Read the Yeterlik Tebliği staff rules [R3-020]. |
| 5 | Do DKMP inventory winners subcontract herp/Odonata work, and at what contract values? Who owns the data? | EKAP record for Ankara IKN 2026/1788766 after bid opening (16 Oct 2026) [R2-011], then one call to the winner. |
| 6 | Do Mott MacDonald Türkiye and ERM buy regional herp/Odonata specialist days, and at what rate? | One call or LinkedIn message to their Türkiye biodiversity leads, attaching the shadow screening. |
| 7 | Do Tour du Valat/MWO, or Global Wetland Watch, have budget for an Eastern Mediterranean validation partner in their next cycle? | One call with the existing Tour du Valat contact. |
| 8 | What are the true 2025 ÇED counts, the Aegean share and the RES/GES split (the reported totals do not add up)? | Download the tables on the Ministry statistics page [R3-001]. |
| 9 | Is Odonata really absent from Nuh'un Gemisi, and does the database accept external records? | Query the public portal for any Odonata species (5 minutes), then one e-mail to DKMP. |
| 10 | Will PANGAEA/GEO-Bench-2 or BEANS maintainers accept a Gediz task? | One GitHub issue to each maintainer with a one-page task specification [R1-002][R1-036]. |

---

## 6. Limits of this synthesis

- Every number is inherited from R1–R4 and is "via search result". Several are search-summary snippets: the ODR fee, the 2025 ÇED counts, the 38 unassessed herp species, and the NatureMetrics platform price. Recheck them on the primary page before external use.
- All Turkish willingness-to-pay and price figures for the proposed models are unsourced estimates. Absence claims (no Turkish screening tool, no data buyer) rest on about 160 searches, not on a market audit.
- Points marked "general knowledge, verify" are not from the workstreams: WDPA/IUCN commercial-use terms and the HRL coverage of Türkiye.
- The municipality partner is assumed to be İzmir BB; this is not confirmed.

## 7. Ranking (planner)

The ranking below weighs four things in this order: whether anyone has been shown to pay, how fast the first invoice can arrive, how much of the researcher's unfair advantage (Aegean field records, herpetofauna and Odonata expertise, Tour du Valat relationship, multi-agent pipelines) the model uses, and whether it builds the assets the next model needs. Demand grades are the synthesis agent's; the order and the reasons are mine.

**1. P2-1 Tiered polygon pre-screen.** First because it is the only model with volume, a regulatory push, documented failure cost and a priced foreign template all at once: roughly 3,800 ÇED decisions a year with energy at about half, the March 2026 amendment forcing more full reports, two court cases that turned on missing herpetofauna and bird data, IBAT at USD 750 per proximity report and the UK expert-verified tier at GBP 1,250–1,999. Nothing in Türkiye does this today and no global tool outputs Turkish or carries Odonata. It also builds the engine every other P2 model reuses. The one thing it lacks, Turkish willingness to pay, can be tested in 90 days with ten free reports. Do this first; the Germencik backtest is the go/no-go.

**2. P1-2 Validation partner sold as work packages.** Second, and the right form of the dataset idea. The research killed the naive version: no model team pays for labels and the only cash buyers of ground truth are forest-carbon firms. But the validation need is documented (WorldCover weak on herbaceous wetland, Copernicus HRL inadequate for temporary wet areas, MWO validating against local inventories with no Turkish partner), and consortia do pay for it as work packages at the TÜBİTAK 1071 scale of about EUR 160k per project. The same fieldwork produces the occurrence records P2-1 needs and the "regional expert" track record IFC PS6 requires. Pursue it through Tour du Valat and the next Biodiversa+ edition, not as a product.

**3. P2-2 Lender-grade PS6/PR6 screen and survey design.** Third because the buyers are few but pay in a different currency: Enerjisa's 750 MW Aegean package already has public critical-habitat assessments by international consultancies, IFC guidance requires regional experts those consultancies lack in Türkiye, and TSKB and Garanti BBVA apply Equator-type rules. It depends on P2-1's engine and on a visible regional-expert record, so it follows rather than leads. Pitch it to Mott MacDonald and ERM as a subcontracted module, not to developers directly.

**Carry along, do not lead with.** P1-3 (benchmark inclusion, data paper) costs little and is the cheapest way to become citable; do it as a by-product of the 2027 field season. P1-5 (DKMP inventory subcontracting) is worth one bid if a tender winner needs herpetofauna or Odonata; the Ankara tender closes 16 October 2026, which is too soon, so target the next. P2-6 (reference layer) emerges from P2-1 records and should not be built separately.

**Rejected for now.** P2-3 litigation audit for NGOs: real need, no payer, and it forecloses P2-1 and P2-2 through conflict of interest; if the cooperative chooses the NGO side instead, it becomes the lead product and P2-1 is dropped. P2-4 white-label: wait until consultancies ask. P1-1 commercial licence: no evidence anyone pays; release open and keep the option. P1-4 living lab: only inside a funded project. P2-5 wetland-zone assessment: watch the 05.09.2026 regulation, revisit after pilot interviews.

**The decision the researcher must make before any of this:** which side of the ÇED table the cooperative sits on. Developers and consultancies pay; municipalities and NGOs do not. The ranking above assumes the paying side, with the product confined to pre-screening and survey design rather than impact verdicts. Second, three cheap checks before building: five calls to Aegean consultancies with a sample report, one email to DKMP on Nuh'un Gemisi reuse terms, one call to the university legal office on paid work through the cooperative.
