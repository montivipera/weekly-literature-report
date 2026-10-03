# Step 4c: Opus review of report_en.md (full report)

- Reviewer: Opus review agent, 2026-10-03. Inputs: BRIEF.md (§6, §8.1, §9), STATE.md, report_en.md (11,041 words in §1–§6), inventory.csv (73 rows), sources.csv (682 rows), review_log.md, drafts/synthesis_memo.md.
- report_en.md was not edited.
- **Scripted checks run:**
  - §3 table: 48 rows parsed; scores, 1–2y/3–5y classes, near-Likely flags, lag-based labels and GOVERNANCE tags all compared with inventory.csv.
  - §4: 25 headings and Classification sentences compared with inventory.csv.
  - §1, §2 and §5 counts recomputed from inventory.csv.
  - Every [S###] in §1–§6 checked against §7 and sources.csv. §7 URLs compared with sources.csv, and "(secondary source)" labels compared with verified = weak.
  - Every number in the prose searched for in the CSVs and logs.
- **What already passes:**
  - Seven sections are present in §8.1 order, and the executive summary is 484 words (≤1 page).
  - All 48 Tier A score strings and every class in §3 and §4 match the CSV. Near-Likely flags match analogue_count ≥ 2 in Tier A.
  - "Likely (lag-based)" is applied to exactly the 8 Potential→Likely rows (A11 A16 A32 A41 A42 A44 A46 B27). GOVERNANCE is applied to exactly A09 A29 A39 A45 B14, and both definitions are in §2.
  - Totals match the CSV: 17/8/48 and 17/16/40, Tier A 15/2/31 and 15/9/24, Tier B 2/6/17 and 2/7/16, Low 0. barrier = none in all 73 rows, min(d4,d5) ≥ 2, and A21 and B25 sit at mean 2.0.
  - §1–§6 cite 372 unique ids. All 372 are in §7 and in sources.csv, and §7 contains no uncited entries. Every §7 URL equals its sources.csv URL, every weak source carries "(secondary source)", and no orphan or duplicate row is cited.
  - Every number in the prose traces to the CSVs or logs, with the exceptions listed below. The report has no emoji, and spelling is British throughout.

## Findings

1. **blocker**: §3.1 table, A15/A17/A25/A46/A47 rows: "not recorded". §3.1 note: "'not recorded' means the inventory holds no deciding condition". §4 B09: "The inventory records none; from the branch…"
   - **Problem:** These cells are stale. inventory.csv now holds a deciding_condition for all six rows. The report therefore contradicts its data file and shows five Potential rows with no named condition, against brief §5. Worse, the A46 condition in the CSV is wrong: it reads "Operational Turkish deployment of an algorithmic hiring tool". That text belongs to A51, and A46 is insurance. Copying the CSV as it stands would publish the error, and the TR HTML would inherit it.
   - **Fix:**
     - (a) Fix inventory.csv A46 deciding_condition to: "A primary source showing an operational AI claims-handling or underwriting deployment with users at a Turkish insurer or TARSİM (tr_funded_pilot = yes gives Certain via the C1 third clause, with d6 3 and d2 3)."
     - (b) Fix A25 "ML-based ride optimization" to "ML-based route optimisation or dispatching".
     - (c) Regenerate the deciding-condition column of Table 3.1 from the CSV, and delete the sentence '"not recorded" means the inventory holds no deciding condition for the row.'
     - (d) Replace the B09 deciding-condition text with: "*Deciding condition.* Türkiye adopting a restoration-reporting duty equivalent to the EU Nature Restoration Law, or a binding CBD/GBF reporting duty (d1 ≥ 4), would make it Certain. A sourced d2 = 4 (a call naming Earth-observation reporting indicators) or a d3 = 4 saving would give Likely, since two analogues exist. Evidence is thin, and the item may remain a reporting aid rather than a service."

2. **blocker**: §6 heading: "## 6. Synthesis / <!-- PLANNER --> / ## 6. Synthesis"
   - **Problem:** This is an assembly artefact. The section heading appears twice (lines 229 and 233), with an HTML comment between the two. It is visible in the rendered deliverable and breaks the §8.1 section list.
   - **Fix:** Delete lines 229–232 (the first "## 6. Synthesis", the blank line, "<!-- PLANNER -->" and the following blank line), so that one "## 6. Synthesis" remains, directly followed by "### 6.1 General landscape".

3. **blocker**: §1 "Evidence was gathered on 3 October 2026 from 676 sources". §2 *Source checking*: "Of 674 source rows, 593 passed, 73 are labelled weak… 7 are orphans and 1 is a duplicate."
   - **Problem:** Both counts are stale. sources.csv has 682 rows:
     - 593 format_ok
     - 7 format_ok;orphan
     - 7 format_ok with "URL via search result"
     - 74 weak
     - 1 duplicate (S378 of S500)

     The statement that STATE.md requires in §2 is also missing: §7 lists only the 372 sources cited in the text, while sources.csv holds the full register.
   - **Fix:**
     - §1: "Evidence was gathered on 3 October 2026 from a register of 682 source records (372 of them cited in this report)."
     - §2: "Of 682 source rows, 607 passed the structural check (7 of these are orphans kept for inventory-stage provenance and 7 are flagged 'URL via search result'), 74 are labelled weak (secondary, vendor or summary-level) and 1 is a duplicate (S378 of S500). Weak sources carry '(secondary source)' in Section 7. Section 7 lists only the 372 sources cited in this text; the full register is in `sources.csv`."

4. **blocker**: §6.2 Direction 3, When: "on the İSTKA model that funded Bağcılar at 90 percent (S593)"
   - **Problem:** Neither S593 (title: "…ISTKA-supported, AI-supported analysis (CNN Turk…)") nor B27's notes contain a 90% figure. The figure is attributed to a source that does not show it. This is the one citation-integrity failure found in the text (brief §6: never invent a citation).
   - **Fix:** Either record the 90% figure with its own source in sources.csv, or replace the sentence with: "or a development-agency AI programme on the model of the İSTKA support for Bağcılar's digital twin (S593); an equivalent İZKA programme is an unsourced estimate."

5. **should-fix**: §1: "two independent Opus review passes challenged every classification"
   - **Problem:** This over-claims. Pass 1 covered 36 rows and pass 2 covered 43 rerun rows (6 overlap). The passes were not independent re-reviews of the same rows.
   - **Fix:** "and two Opus review passes, which between them covered every row, challenged the classifications before they were finalised."

6. **should-fix**: §2 Limitations, *Depth*: "Only abstracts, summaries and landing pages were read, by design."
   - **Problem:** The limitations omit several items from synthesis_memo §6 and STATE.md:
     - the 200-search session cap and the degraded batches
     - the non-systematic nature of the study
     - uneven analogue counting and inferred affiliations
     - the unverified TÜBİTAK participation in BiodivFuture, on which §6 Direction 1 rests

     (Tourism, the lag assumption, S108, the survey-share rule, no Low, HTTP and Omnibus dating are present.)
   - **Fix:** Add these bullets after *Depth*:
     - "*Search-only sourcing.* Evidence comes from web-search results and Consensus/Scholar abstracts. A session cap of 200 searches degraded batches b1 and b3–b9, which were partly re-run; Turkish grey literature is under-detected, so d6 = 1–2 and analogue_count = 0 often mean 'not found' rather than 'absent' (explicitly B11, B13, A18). This is a structured snapshot, not a systematic review."
     - "*Analogue counting.* Plans, trainings and announced pilots were excluded after review, and some affiliations were inferred from titles (B23, B27), so analogue counts are uneven."
     - "*Calls named in Section 6.* Whether TÜBİTAK participates in the 2026–27 Biodiversa+ BiodivFuture call (S675, S676) was not verified, and whether that call carries a monitoring or restoration-success topic was not checked."

7. **should-fix**: §2 Limitations, *No item reached Low*: "In 71 of 73 rows at least one score is flagged"
   - **Problem:** A text search of the notes column finds "unsourced" in 72 of 73 rows (all except A46).
   - **Fix:** Verify the count. If unverifiable, use: "In almost every row (72 of 73 by a text search of the notes) at least one score is flagged as an unsourced estimate."

8. **should-fix**: §5 pattern 2: "Items classified Certain on deployment tend to be run by a ministry or municipality"
   - **Problem:** The data does not support this. Of the Certain items that rest on deployment or use, 6 are private or professional (A02, A06, A10, A20, A22, A34) and 4 are public (A08, A12, A14, B20).
   - **Fix:** "**2. Operational public platforms are the clearest public-sector signal.** Where the state deploys, it does so on platforms it owns: the MEB assistant (A08), the KURGAN tax-triage system (A12), the Ürün İzleme Sistemi (A14) and, at municipal level, Melikgazi's assistant (B20). Certain items on the private side (A06, A20, A22, A34) rest more often on company or press reports. Where the evidence was only an 'AI-supported' label (A47) or an offline study (A25), the review downgraded the item."

9. **should-fix**: §5 pattern 1: "the Machinery Regulation reaches robot makers more than adopters (A20, A23)."
   - **Problem:** This factual claim has no citation. Support exists in the inventory (S315; S316; A23 notes: "makers' duty, enabling for adopters").
   - **Fix:** "…and the EU Machinery Regulation, applicable from 20 January 2027, reaches robot makers more than adopters (A20, A23) [S315; S316, secondary source]."

10. **should-fix**: §5 pattern 3: "TÜBİTAK 1007 and sectoral Turkish-LLM grants of up to 50 million TL per project underpin A40 and the d2 = 3 scores…"
    - **Problem:** The sentence merges two programmes. The 50 million TL cap belongs to the sectoral LLM call (S567), and TÜBİTAK 1007 yields only d2 = 3. The Horizon claim for A17 and A24 is uncited.
    - **Fix:** "The sectoral Turkish-LLM adaptation call (up to 50 million TL per project [S567; S568]) gives A40 its d2 = 4, while TÜBİTAK 1007 Kamu YZ Ekosistemi [S588; S589] lifts B22, B26 and B27 only to d2 = 3. Biodiversa+ underpins B01, B17, B06 and B23, but through a single call (S108), a dependency to watch. Horizon Europe association [S098] supports A17 [S293] and A24 [S110], and Sivil Düşün supports B21 and B26 [S582; S583]."

11. **should-fix**: §6.1 para 1: "Where a binding rule exists, it was written in Brussels or copied from an EU framework"
    - **Problem:** This over-claims. A45 rests on a BDDK remote-identification rule, and no source shows it was derived from an EU framework. "Copied" is also a loaded word. "slowly when several agencies… must agree" is inference, because no speed data were collected.
    - **Fix:** "Most binding pull comes from EU law or EU-harmonised rules (A39, A29, A50, A02); the main domestic exception is a sectoral banking rule (A45)… The state has moved fast where it controls the whole stack (KURGAN went into production in October 2025; MEBİ's KANKA assistant was used by about 719,000 students [S610]), while services that need several agencies or external providers are still mostly announced (A03, A11, A32, A48)."
    - This also removes the unsourced "within a year".

12. **should-fix**: §6.1 para 2: "Every documented civil-society deployment in the inventory is municipal (… B19 İzmir staff training…)" and "This is not because NGOs lack the tools… but because nobody has yet documented…"
    - **Problem:** The first claim is contradicted by the inventory. e-Gönüllü (B21, S579) operates AI-assisted volunteer matching, and the Tür Say events (B17) are NGO/university-run. Staff training (B19) is not a deployment. The causal claim, and the parenthesis "cheap and often free", are unsourced.
    - **Fix:** "Civil society follows the same logic one level down. Most documented civil-society AI activity in the inventory is municipal: Melikgazi's assistant (B20), İzmir's staff training (B19), Bağcılar's İSTKA-supported twin (B27) and Kahramanmaraş's call routing (B26). The NGO side is thin (B18 none found, B21 one adjacent volunteer-matching service, B22 none found). This may partly reflect what is documented online rather than what NGOs do, which is why a single documented, funded use would count for a lot."

13. **should-fix**: §6.1 para 3: "eDNA surveys at Ankara University and Boğaziçi"
    - **Problem:** The citation is missing, and the Boğaziçi item is a TÜBİTAK 3501 lagoon project, not a survey.
    - **Fix:** "camera-trap detection at İYTE [S382], a national fish eDNA survey at Ankara University [S390] and a TÜBİTAK-funded lagoon eDNA project at Boğaziçi [S391], a TRDizin paper on Aras bird calls [S500]".

14. **should-fix**: §6.2 Direction 2, Why: "B11 has the strongest cost evidence in the inventory"
    - **Problem:** The comparative claim is unsupported. Several items have d3 = 4 (A10, A26, A30, B02, B03), and B11's figures are retrospective or simulated (notes: "not 5").
    - **Fix:** "LLM-assisted screening and extraction (B11) has sourced cost evidence (d3 = 4: screening workload cut by 33–93% [S406], though extraction is less reliable [S408]) and is Potential only because analogue use was not detected."

15. **should-fix**: §6.2 intro: "ground truth every Earth-observation model in Türkiye lacks". Also Direction 1 Why: "Nobody currently runs a field-validated AI monitoring product for a Turkish delta."
    - **Problem:** Both are absolute claims from search-only evidence.
    - **Fix:**
      - Intro: "field expertise… that can produce the ground truth that Turkish wetland-mapping studies report as scarce (S401)".
      - Direction 1: "No operational, field-validated AI monitoring product for a Turkish delta was found in the searches (B04, B06)."

16. **should-fix**: §6.2 Direction 1, First step and Main risk: "Four Likely classes rest on one reading of the Biodiversa+ call text"
    - **Problem:** The report does not link BiodivFuture to the deciding condition of B01, B06, B17 and B23. Those classes reverse if the 2026–27 edition "no longer carries a monitoring topic open to Türkiye" (§4 B01, B06, B17). BiodivFuture's theme is novel ecosystems, and whether it names monitoring or restoration success was not checked. The reader should know that the first step also tests the main classification assumption.
    - **Fix:** Add to Main risk: "Note that the 2026–27 BiodivFuture call is themed on novel ecosystems; whether it names monitoring or restoration success, and whether TÜBİTAK takes part, was not verified (S675, S676). If it does neither, the deciding condition for B01, B06, B17 and B23 is not met for this edition and those classes should be read as Potential (near-Likely) until the next call."

17. **should-fix**: §6.2 intro and §6.3: "If only one can be pursued, Direction 1 is the choice"
    - **Problem:** The ranking is asserted, not fully defended. §1 says the directions are "in order", but no sentence explains why Direction 2 ranks above Direction 3. §6.3 then says Direction 2 "can start this month", which mixes sequence with rank.
    - **Fix:** Append to §6.3: "The ranking reflects expected value, not start order. Direction 1 ranks first because three of its four items are already Likely (B01, B06, B23) and it uses the researcher's rarest asset, field ground truth. Direction 2 ranks second because it needs no external decision to start and directly creates the missing Turkish evidence for B11 and B12, but it faces cheap competing tools (B10). Direction 3 ranks third because it depends on one municipal department and its operational service is a 2028–2031 prospect (B27 Likely only on the lag assumption). Start Direction 2 first in time; give Direction 1 the most effort."

18. **should-fix**: §6.2 intro: "corporate nature disclosure and biodiversity credits (B07, B24) depend on a binding duty the researcher cannot influence"
    - **Problem:** This misstates B24's condition, which is a legal or ministry basis for credits with an MRV protocol (d1 ≥ 3 and d2 ≥ 4), not a binding duty. The rejections also do not say what would reopen them.
    - **Fix:** "corporate nature disclosure (B07) waits for a binding Turkish or EU-buyer duty, and biodiversity credits (B24) for a Turkish legal basis and MRV protocol, with no analogue market yet; neither is something the researcher can create, so both are watch items for 2028–2031 rather than directions (they would reopen if TSRS added a nature duty or the ministry recognised nature credits)."

19. **should-fix**: §6.2 Direction 3, Why: "Expert validators for difficult taxa are the bottleneck automated identification cannot remove"
    - **Problem:** This is not sourced in B17's row or anywhere in the CSVs. It reads as fact, but it is the planner's judgement.
    - **Fix:** "In our judgement (not sourced in the inventory), expert validators for difficult taxa remain the bottleneck that automated identification does not remove, and Odonata and herpetofauna are such taxa."

20. **should-fix**: §6.2 Direction 2, When: "but require a public customer institution"
    - **Problem:** The memo's hedge was dropped: whether a metropolitan municipality qualifies was not checked. In addition, "moving it to Certain under the rule" may read as gaming the classification.
    - **Fix:**
      - "…but require a public customer institution (whether a metropolitan municipality qualifies was not checked)".
      - After "moving it to Certain under the rule", add: "(mechanically, through the C1 third clause, and only if a primary source documents users; one pilot would not by itself show national diffusion)".

21. **should-fix**: §6.2 Direction 1, Main risk: "pursuing TÜBİTAK 1001 or a Horizon EO topic in parallel"
    - **Problem:** TÜBİTAK 1001 is not assessed or cited anywhere in the report. It appears only as "generic" in B11's notes.
    - **Fix:** "…by pursuing a generic TÜBİTAK research grant (e.g. 1001; not assessed in this study) or a Horizon EO topic (S514) in parallel."

22. **should-fix**: §3.1 table, A27: "Verify the 14% Turkiye figure on the Reuters DNR 2026 primary PDF (S639); if…". A40: "1-2y: C3 via d2=4 (Turkish LLM sectoral-adaptation grant call…"
    - **Problem:** Neither cell is a deciding condition. A27's cell is a to-do whose "reverts to Potential" is already the case. A40's cell is class-branch text.
    - **Fix (CSV and table):**
      - A27: "A primary national survey showing that at least 10% of Turks use AI chatbots for news (survey-share rule; d6 4 → Certain)."
      - A40: "Sourced production use of Turkish LLMs in several named Turkish organisations (d6 ≥ 4 → Certain); lapse of the sectoral-LLM call would drop it to Potential (near-Likely)."

23. **should-fix**: inventory.csv A46 class_branch: "d6 3+1=4 (analogue_count 1<2 so no +1, stays 3) … reclassified Likely via lag-based guard"
    - **Problem:** The text contradicts itself and the field: analogue_count = 2 (PL PZU S183, KR KIDI S184). The report's A46 Likely (lag-based), and therefore the counts of 16 and 8, are right only on the field value. B09's branch similarly says "3-5y: … analogue_count<2", while the field is 2. The report shows B09 as near-Likely at 1–2y but plain Potential at 3–5y, unlike every Tier A row with analogue_count ≥ 2.
    - **Fix:**
      - A46 branch 3–5y: "d6 3+1=4 (analogue_count 2>=2) → C1 only via assumed +1 → Likely (lag-based)."
      - B09 branch 3–5y: "d6 2+1=3 (analogue_count 2>=2); C4 Potential (near-Likely)."
      - Report §4 B09: "Potential (near-Likely) at both horizons (C4): d1 = 2, d2 = 3."
      - Synchronise rapor_tr.html.

24. **should-fix**: §7 [S639]: "https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2026-06/DNR 2026 FINAL_2.pdf"
    - **Problem:** The URL contains literal spaces. It is not a valid URL as written (§9: verifiable URL), and Markdown renderers break it.
    - **Fix:** "https://reutersinstitute.politics.ox.ac.uk/sites/default/files/2026-06/DNR%202026%20FINAL_2.pdf". Apply the same fix in sources.csv.

25. **nit**: §1: "using a fixed rule rather than judgement"
    - **Problem:** The scores are judged; only the mapping from scores to class is fixed.
    - **Fix:** "applying a fixed rule to the scores rather than assigning classes by judgement."

26. **nit**: §1: "only a label, an offline study or an unverified figure stood behind the 'AI' claim (A47, A25, A27, A46)"
    - **Problem:** A46 was downgraded on a single self-report, which is not in the list.
    - **Fix:** "only a label, an offline study, an unverified figure or a single self-report stood behind the 'AI' claim (A47, A25, A27, A46)."

27. **nit**: §2 Workflow: "Sonnet agents ran the scans and this draft."
    - **Problem:** The wording is left over from the draft.
    - **Fix:** "Sonnet agents ran the scans and drafted Sections 2–5 and 7; the planner wrote Sections 1 and 6."

28. **nit**: §2 *Scope reading of S108*: "The d2 = 4 scores for B01, B04, B17 and B23"
    - **Problem:** B06 also takes d2 = 4 from S108, on the call's named restoration-success topic.
    - **Fix:** Add: "B06 also rests on S108, but on the call's named topic of measuring restoration success, so it does not depend on the monitoring-core reading."

29. **nit**: §4 B02: "the assumed d6 increase would reach 4, but the guard keeps Likely rather than Certain."
    - **Problem:** The reader may take B02 to be lag-based. It is not, because C3 holds unadjusted.
    - **Fix:** "Likely at 3–5 years: C3 still holds; the assumed d6 rise to 4 would otherwise give Certain, which the guard does not allow, so B02 is not a lag-based item."

30. **nit**: §3.1 table: "Saglik Bakanligi", "Turkiye", "TEIAS", "TUSEB"
    - **Problem:** These cells are ASCII transliterations copied from the CSV. The prose uses diacritics (Türkiye, TÜSEB).
    - **Fix:** Use "Sağlık Bakanlığı", "Türkiye", "TEİAŞ", "TÜSEB" in the table cells.

31. **nit**: §3.1 table: "none needed (Certain)" vs "none recorded (Certain)"; §4 B20 CSV: "none needed (no Potential)"
    - **Problem:** The phrasing for Certain rows is inconsistent.
    - **Fix:** Use "n/a (Certain)" for all Certain rows.

32. **nit**: §6.2: "at least 20 percent" and "at 90 percent"
    - **Problem:** The rest of the report uses "%".
    - **Fix:** "at least 20%".

33. **nit**: §6.2 Direction 3, When: "the citizen-science layer, which needs no new funding"
    - **Problem:** Bioblitz events and validation time have costs. This is an unsourced assertion.
    - **Fix:** "the citizen-science layer, which can start on existing partner resources".

34. **nit**: inventory.csv notes (A46, A47, B17, B20, B27)
    - **Problem:** The notes are stale and contradict the current classes:
      - A46: "d6=4 rests on…"
      - A47: "possible false Certain… tr_funded_pilot=yes"
      - B17: "(C4 with analogue_count=2). … d2=3"
      - B20: "d6=4 rests on two production deployments"
      - B27: "(pre-r3)… All of d1, d2, d6 = 2"

      This does not change the report, but the step-5 HTML builder and later readers of the CSV may pick these notes up.
    - **Fix:** At the 5h Haiku pass, prepend "SUPERSEDED (see review_log):" to the pre-review sentences, or trim them.

## §6 against the user's advisory requirement (summary)

- **Advisory voice and structure:** these meet the requirement. Each direction has Why / When / First step (next 90 days) / Main risk with a hedge, is tied to ids (B01 B04 B06 B23 B09 B27; B10 B11 B12 B14 B15 B22; B17 B19 B26 B27), and uses imperative, concrete steps.
- **Unverified facts:** the three the brief flagged are disclosed: BiodivFuture TÜBİTAK participation ("participation unconfirmed"), İzmir ("if the partner is İzmir Büyükşehir Belediyesi") and S514 ("per search summary").
- **Remaining weaknesses:** these are fixable and are listed above. The ranking is under-defended (17). Unsourced specifics remain: 90% (4), "within a year" (11), the expert-validator bottleneck (19) and TÜBİTAK 1001 (21). Several absolute or comparative claims need calibrating (14, 15, 12). The link between BiodivFuture and the deciding conditions of the four Likely ecology items is missing (16).
- **Generic advice:** none of the guidance is generic enough to remove. The Direction 2 hedge ("sell domain judgement, Turkish-language output and an audit trail") and the Direction 3 budget-cycle risk are the most generic lines, but each is paired with a concrete mechanism (a verification protocol, an MoU with an open-data clause).

## Verdict

After blockers 1–4 are fixed, the report meets the §9 gates that apply to report_en.md:
- every development has both classes and at least one source;
- the review log exists, with resolutions;
- every citation resolves to a URL or DOI, once S639 is URL-encoded (24).

The §9 gate on EN↔TR consistency depends on applying 1 and 23 to the CSV before rapor_tr.html is synchronised. Should-fix items 5–24 are recommended before delivery, because they concern over-claiming and calibration, which the user's brief (§6) makes a requirement.
