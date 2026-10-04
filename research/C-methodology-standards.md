# C. Methodology standards for a data-first wetland-ecology workflow (compiled 2026-10-04)

Scope: what the methodology literature says about exploratory vs confirmatory analysis, HARKing, (secondary-data) preregistration, reporting/reproducibility, method choice and literature-search documentation.
Grades: A = peer-reviewed paper or official journal/guideline text; B = independent systematic non-peer-reviewed; C = blog/commentary/snippet-only. UNVERIFIED = full text or live policy page not read.
Access limit: all 8 WebFetch attempts (COS, PCI RR, BMC, Wiley, BES, OSF) were blocked by the egress proxy, so journal/guideline claims rest on search snippets. 14/14 searches used. Years marked + are journal years recalled where the index showed a preprint year.

## Claims

| # | Claim | Source (authors, year, DOI/URL) | Source date | Grade |
|---|-------|--------------------------------|-------------|-------|
| 1 | HARKing = presenting a post hoc hypothesis (based on or informed by the results) in the report as if it were a priori; Kerr judged its costs likely exceed benefits but called this an open question | Kerr, Pers Soc Psychol Rev, 10.1207/s15327957pspr0203_4 | 1998 | A |
| 2 | Three forms of HARKing: (a) post hoc hypotheses reported as a priori; (b) hypotheses retrieved from a post hoc literature search and reported as a priori; (c) unsupported a priori hypotheses silently dropped. Harm depends on form and context; the common element is non-disclosure | Rubin, Rev Gen Psychol, 10.1037/gpr0000128 | 2017 | A |
| 3 | Critique: Kerr's 12 costs are misconceived, misattributed, lack evidence, or ignore peer review and open data; premature to say HARKing caused low replication | Rubin, Br J Philos Sci, 10.1093/bjps/axz050 | 2019 | A |
| 4 | Simulation: HARKing by cherry-picking biases effects little; "question trolling" (searching many constructs/relationships for notable results) gives substantial upward bias when many effects are available | Murphy & Aguinis, J Bus Psychol, 10.1007/s10869-017-9524-7 | 2019 | A |
| 5 | Survey of 807 researchers (494 ecologists, 313 evolutionary biologists): 51% reported an unexpected finding as if hypothesised from the start (HARKing), 64% omitted non-significant results, 42% added data after checking significance; rates similar to psychology | Fraser et al., PLOS ONE, 10.1371/journal.pone.0200303 | 2018 | A |
| 6 | Caveat on prevalence: "ever used" rates overstate how often QRPs occur; frequency-adjusted estimates are far lower (psychology; cross-field survey: self-reported prevalence ~3x below use, 9/10 used at least one QRP) | Fiedler & Schwarz, SPPS, 10.1177/1948550615612150; Schneider et al., PLOS ONE, 10.1371/journal.pone.0304342 | 2016; 2024 | A |
| 7 | Only analyses specified before seeing the data deserve the label "confirmatory" and only for them are standard tests valid; other analyses are allowed but must be labelled "exploratory". De Groot: tests in exploratory work "do not have evidential impact" | Wagenmakers et al., Perspect Psychol Sci, 10.1177/1745691612463078; de Groot (1956, transl.), Acta Psychol, 10.1016/j.actpsy.2014.02.001 | 2012; 2014 | A |
| 8 | Postdiction (generating hypotheses from observations) must be distinguished from prediction (testing on new observations); mistaking one for the other reduces credibility, and hindsight bias makes this hard to avoid | Nosek et al., PNAS, 10.1073/pnas.1708274114 | 2018 | A |
| 9 | Exploration, "rough confirmatory" and confirmatory analysis form a continuum; the proper approach depends on intentions and transparency; legitimate exploration differs from p-hacking, HARKing and data mining | Fife & Rodgers, Am Psychol, 10.1037/amp0000886 | 2021 | A |
| 10 | Exploratory research is legitimate and necessary; defined by data-driven analysis where Type I/II error cannot be controlled; its hypotheses should be severely tested in a later confirmatory study; gives write-up guidelines (sport science) | Ditroilo et al., J Sports Sci, 10.1080/02640414.2025.2486871 | 2025 | A |
| 11 | Applied ecology: hypothesis-testing sensu stricto and experimental protocols are uncommon; both modes needed; asks for a clearer distinction (journal sections, preregistration, registering post hoc hypotheses from exploration for later testing, causal-inference methods) | Nilsen et al., J Appl Ecol (preprint 10.32942/osf.io/75a6f; journal DOI UNVERIFIED) | 2019/2020+ | A |
| 12 | Editors of Evolution and Ecology and Evolution: preregistration should stay optional, but distinguishing pre-planned from post hoc analyses can greatly aid readers | Shaw et al., Ecol Evol, 10.1002/ece3.2291 (also 10.1111/evo.12977) | Jul 2016 | A |
| 13 | Critique: preregistration and the exploratory/confirmatory split do not fix a weak theory-to-hypothesis link; discovery-oriented research inherently carries high Type I risk | Oberauer & Lewandowsky, Psychon Bull Rev, 10.3758/s13423-019-01645-2 | 2019 | A |
| 14 | Preregistration = plan filed in a public archive, not binding; Registered Report = journal reviews plan, in-principle acceptance. In ecology/conservation, undisclosed exploratory analysis and HARKing are judged common | Parker, Fraser & Nakagawa, Conserv Biol 33:747, 10.1111/cobi.13342 | 10 May 2019 | A |
| 15 | BMC Ecology began accepting Registered Reports on 24 Aug 2017 (first ecology journal); journal since merged into BMC Ecology and Evolution (recalled) | BMC series blog, blogs.biomedcentral.com/bmcseriesblog/2017/08/24/bmc-ecology-is-now-accepting-registered-reports/ | 2017 | C (UNVERIFIED now) |
| 16 | Few specialist ecology/evolution journals offer RRs; those named: Ecology and Evolution, Ethology, Conservation Biology, Ecological Solutions and Evidence | "Opportunities and challenges for registered reports in ecology and evolution", ecoevorxiv.org/repository/view/12377/ (snippet only) | date not captured | B (UNVERIFIED) |
| 17 | Peer Community In Registered Reports is a free supra-journal platform that reviews/recommends RRs in all fields; its handling of existing-data submissions not checked | rr.peercommunityin.org (search summary only; page blocked) | not captured | C (UNVERIFIED) |
| 18 | Ecology Letters adopted TOP: level 1 for study and analysis-plan preregistration (encouraged, link shown), level 2 for data and code, level 3 for citation standards; authors tick which tools they used | Ecology Letters editorial note, 10.1111/ele.12611 | Jun 2016 | A (current policy UNVERIFIED) |
| 19 | TTEE: ecology papers often omit sample sizes, effect directions, uncertainty, especially for weak results; advocates journal-level transparency guidelines beyond data archiving | Parker, Nakagawa & Gurevitch, Ecol Lett, 10.1111/ele.12610 | Jun 2016 | A |
| 20 | Review of 20 open-science guideline papers and 17 ecology/evolution journal policies: 15/17 expected or encouraged data sharing, 10 required it at submission; policies vary widely; long-term experiments and physical samples rarely covered | Koivisto & Mäntylä, Ecol Evol, 10.1002/ece3.11698 | Jul 2024 | A |
| 21 | TOP 2025 reorganises into Research Practices (disclosed / shared and cited / certified), Verification Practices, Verification Studies; aim = verifiability of claims; seven practices incl. registration and analysis plan (list recalled) | COS, cos.io/blog/new-preprint-introduces-major-update-to-the-top-guidelines; AMPPS 2025 (DOI UNVERIFIED) | 2025 | A (UNVERIFIED detail) |
| 22 | Secondary (pre-existing) data analysis can be exploratory or confirmatory; transparency practices change how results should be interpreted | Weston et al., AMPPS, 10.1177/2515245919848684 | 2019+ | A |
| 23 | Preregistering analyses of pre-existing data is useful although major design aspects (manipulations, sample size) cannot change; template and tutorial exist | Mertens & Krypotos, Psychol Belg, 10.5334/pb.493; van den Akker et al. template, 10.15626/mp.2020.2625 | 2019 | A |
| 24 | Secondary-data preregistration is hampered by analyst prior knowledge of the data; proposed fixes include handling prior knowledge, registering non-hypothesis-driven work, checking plan fits data | Baldwin et al., Eur J Epidemiol, 10.1007/s10654-021-00839-0 | 2022+ | A |
| 25 | Primary vs secondary data is unnecessarily confounded with exploratory vs confirmatory; log data access ("checkout") so confirmatory secondary analysis is credible | Scott et al., AMPPS, 10.1177/2515245918815849 | 2019 | A |
| 26 | Explore-and-Confirm Analysis Workflow (ECAW) proposed as extra protection beyond preregistration for secondary data (held-out confirmation subset: recalled, UNVERIFIED) | Thibault et al., R Soc Open Sci, 10.1098/rsos.230568 | 2023 | A (UNVERIFIED detail) |
| 27 | Deviations from a preregistration are not all problematic; report them transparently and justify them | Lakens, Collabra Psychol, 10.1525/collabra.117094 | 2024 | A |
| 28 | Registered Reports: 44% positive first hypotheses vs 96% in standard psychology papers (71 RRs vs 152 papers) | Scheel et al., AMPPS, 10.1177/25152459211007467 | 2021+ | A |
| 29 | 193 preregistered vs 193 matched non-preregistered psychology studies: no lower share of positive results, smaller effects or fewer errors; more power analyses and larger samples; no robust evidence preregistration prevents p-hacking/HARKing | van den Akker et al., Behav Res Methods, 10.3758/s13428-023-02277-0 | 2023 | A |
| 30 | Structured preregistration limits researcher degrees of freedom better than unstructured, yet neither eliminates them; coders agreed on number of hypotheses only 14% of the time | Bakker et al., PLOS Biol, 10.1371/journal.pbio.3000937 | 2020+ | A |
| 31 | Preregistration reduces bias via outcome-independent decisions and lets readers calibrate confidence; meta-research supports benefits but a preregistration can be used "mindlessly" as a quality proxy | Hardwicke & Wagenmakers, Nat Hum Behav, 10.1038/s41562-022-01497-2; Lakens et al., Evid-Based Toxicol, 10.1080/2833373x.2024.2376046 | 2023; 2024 | A |
| 32 | Data-exploration protocol (outliers, collinearity, dependence etc.); authors estimated half of their own pre-training work contained assumption violations | Zuur, Ieno & Elphick, Methods Ecol Evol, 10.1111/j.2041-210x.2009.00001.x | 2010 | A |
| 33 | 10-step regression protocol: from study design and data organisation (formulating relevant questions, visualising sampling, exploration, dependency) through fitting/validating to presenting results and simulation | Zuur & Ieno, Methods Ecol Evol, 10.1111/2041-210x.12577 | 2016 | A |
| 34 | Initial data analysis should be pre-planned, documented in the analysis plan, and should not evaluate outcome-predictor associations, to limit biased inference | Heinze et al., BMC Med Res Methodol, 10.1186/s12874-024-02294-3 | 2024 | A |
| 35 | GLMM best practice for ecology/evolution; complex GLMMs are hard to fit and hypothesis testing remains difficult | Bolker et al., Trends Ecol Evol, 10.1016/j.tree.2008.10.008 | 2009 | A |
| 36 | Accessible mixed-model "code of best practice" incl. pitfalls and model selection/multimodel inference; multimodel inference is hard without formal information-theory background and some issues are unresolved | Harrison et al., PeerJ, 10.7717/peerj.4794; Grueber et al., J Evol Biol, 10.1111/j.1420-9101.2010.02210.x | 2018; 2011 | A |
| 37 | Transparent statistics: visualise data, assess preprocessing choices, report multiple models, involve multiple analysts, share data and code; multiverse analysis shows how arbitrary processing choices change conclusions | Wagenmakers et al., Nat Hum Behav, 10.1038/s41562-021-01211-8; Steegen et al., Perspect Psychol Sci, 10.1177/1745691616658637 | 2021; 2016 | A |
| 38 | R workflow template for (G)LM(M)s from data exploration to presentation, needing minimal coding skills | Santon et al., Front Ecol Evol, 10.3389/fevo.2023.1065273 | 2023 | A |
| 39 | Reporting guidelines so primary ecology/evolution studies can enter meta-analyses (essential data often omitted); useful whether or not a meta-analysis follows | Gerstner et al., Methods Ecol Evol, 10.1111/2041-210x.12758 | 2017 | A |
| 40 | Ellison 2010, "Repeatability and transparency in ecological research" (Ecology 91:2536); DOI 10.1890/09-0032.1 and content recalled, not retrieved | Ellison, Ecology | 2010 | A (UNVERIFIED) |
| 41 | BES Guides to Better Science: Guide to Reproducible Code (file organisation, readable code, reproducible reports, version control, archiving) and Guide to Data Management for early-career ecologists | britishecologicalsociety.org/publications/better-science (search snippet only) | ~2017 | A (UNVERIFIED) |
| 42 | ROSES = pro forma and flow diagram for systematic reviews/maps in conservation and environmental management (PRISMA fits poorly); critique: developed by interviews/questionnaires, not a consensus process, uptake plan unclear | Haddaway et al., Environ Evid, 10.1186/s13750-018-0121-7; Sharp et al., 10.1186/s13750-018-0132-4 | 2018 | A |
| 43 | litsearchr builds reproducible search strings from keyword co-occurrence networks; reduces bias towards familiar studies; cuts search-building from ~17-34 h to <2 h; deduplicates results | Grames et al., Methods Ecol Evol, 10.1111/2041-210x.13268 | 2019 | A |
| 44 | Only about half of 28 search systems suit evidence synthesis without caveats; Google Scholar inappropriate as principal system | Gusenbauer & Haddaway, Res Synth Methods, 10.1002/jrsm.1378 | 2020 | A |
| 45 | Open meta-analysis tips: preregister protocol, share search syntax and scripts, use version control | Moreau & Wiebels, PLOS Comput Biol, 10.1371/journal.pcbi.1012252 | 2024 | A |
| 46 | "Select citation" is among the most commonly reported QRPs; QRPs cluster in interpretation, analysis and citation and usually involve omission | Fanelli et al., Sci Eng Ethics, 10.1007/s11948-026-00589-w | 2026 | A |
| 47 | Commentary: in a forestry-biodiversity review, unexpected findings were often dampened or rationalised; normative bias may colour which literature is cited | Sjolie, Silva Fenn, 10.14214/sf.24034 | 2024 | C |

## Verdict on the user's three proposed fixes

1. Exploratory/confirmatory labels. For: the labelling norm originates with Wagenmakers [7]; ecology editors say it helps readers [12]; transparent exploration is legitimate [9,10,11]; the harm in HARKing is non-disclosure [2,3]. Against: a label does not turn a same-data test into confirmation [7,8,26]; self-applied labels after seeing results are open to hindsight bias [8]; preregistration quality is uneven and outcome effects unproven [29,30,31]. Verdict: adopt, necessary but not sufficient. Default every same-data analysis to "exploratory"; allow "confirmatory" only for a plan time-stamped before outcome inspection, or tested on held-out/new data [25,26].
2. Literature scan before fixing questions. For: literature retrieved after results and presented as a priori is a named HARKing form [2]; reproducible search methods reduce familiarity bias [43]; question-trolling inflates bias [4]. Against: no standard found that requires a pre-question scan for data-first studies (Gap); the analyst has already seen the data, so the scan cannot be blind [8]; a short scan is only as good as its databases and strings [43,44]. Verdict: adopt, but log it (strings, databases, date, hits) and place it before a time-stamped plan freeze [42,43,45].
3. DOI/citation ledger. For: selective citation is a surveyed QRP [46], and TOP/Ecology Letters have citation standards [18,21]. Against: no source recommends a cited-DOI ledger; the standards ask for search-string and screening records [42,43,45]; a ledger of what was cited does not show what was searched or when. Verdict: keep, but extend into a search-and-consultation log with a "consulted before/after results seen" field; the ledger alone is weak protection.

## What the standards require of a data-first workflow

- Disclose that the dataset pre-existed and what the analyst had already seen or analysed before the plan was written [23,24,25].
- Only analyses specified in advance count as confirmatory; everything else is exploratory and p-values are not evidence of a tested hypothesis [7,10].
- Never present a post hoc hypothesis, or one found in a post hoc literature search, as a priori; label each hypothesis by origin [1,2].
- Report all analyses run, exclusions, transformations and candidate models, not only significant ones [5,19,37].
- Secondary-data preregistration = register hypotheses, variables, exclusion rules, models and decision criteria before analysis, with a data-access statement; report deviations openly [23,27].
- Genuine confirmation from existing data needs data-access logging or a held-out split (ECAW detail UNVERIFIED), otherwise new data [25,26].
- Archive data and code and cite datasets (TOP levels in Ecology Letters; BES guides; journal policies vary) [18,20,21,41].
- Report basic statistics (n, means, variance, effect sizes) so the study can be reused [39].

## Method choice for a non-statistician

- Follow the Zuur & Ieno 10-step protocol; it starts from formulating relevant questions and dependence structure, which fits a plan-freeze step [33].
- Do data exploration per Zuur et al. 2010, but keep outcome-predictor association screening out of the screening stage where inference matters [32,34].
- For nested/repeated wetland data use Bolker and Harrison as the accessible references; Santon's template lowers coding barriers [35,36,38].
- Report model selection explicitly: candidate set, criterion, all models compared; multimodel inference is difficult without background [36,37].
- Test sensitivity to preprocessing choices (multiverse) and consider a second analyst [37].
- "Consult a statistician": no retrieved source states it explicitly (UNVERIFIED); closest is the multiple-analyst recommendation [37].

## Gaps

- Live policy pages (COS TOP, PCI RR, BMC, Wiley, BES) were unreachable; journal RR offerings [15-17] and TOP/BES details [21,41] need checking before use, as does whether any journal takes RRs on already-existing data.
- No ecology-specific evidence that preregistration or RRs change outcomes; all outcome evidence is psychology [28-30]. HARKing prevalence in ecology is self-report only [5,6].
- No source found on when to consult literature in data-first ecological work, nor endorsing a DOI ledger; verdict 2 and 3 rest on inference from [2,43,46].
- Not retrieved: Ellison 2010 content [40], Hollenbeck & Wright 2017 (transparent post hoc analysis), Szollosi et al. 2020 and Devezer et al. critiques, Kerr's own deterrence suggestions, a "consult a statistician" source.
- Years marked + come from memory where the index showed a preprint year (Weston, Scheel, Bakker, Baldwin, Nilsen); verify.

## Implications for the workflow

- Treat all same-data analyses as exploratory by default; confirmatory status must be earned by a time-stamped plan before outcome inspection, or by held-out or new data [7,25,26].
- Add a "plan freeze" step after the literature scan and before modelling: commit questions, variables, models and decision rules (git or OSF timestamp); later analyses are labelled exploratory [8,23,27].
- Turn the DOI ledger into a search-and-consultation log (strings, databases, dates, hit counts, screening, date relative to plan freeze) [42,43,45,46].
- Anchor method choice in a named protocol and report model-selection and preprocessing decisions; seek statistician review of the plan (not a retrieved requirement) [33,36,37].
- Check target-journal RR/TOP pages live before choosing a venue, and expect labelling to improve transparency rather than guarantee fewer false positives [29-31].
