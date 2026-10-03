# Review 1c: calibration batch (A01, A24, A39, B01, B18)

Reviewer: Opus, 2026-10-03. Inputs: BRIEF §3–5, AGENT_RULES rule 8 (with the planner clarifications), SCORING_TASK.md, drafts/scores_calib.csv, drafts/sources_calib.csv.

Method: desk check of every score against the rule 8 anchors and the cited sources, plus 8 WebSearch spot-checks (§6). Fetch is blocked, so every new URL is "via search result". No documents were read in full.

Outputs:
- `drafts/scores_calib_reviewed.csv`: the corrected rows, all 25 columns.
- `drafts/sources_calib.csv`: calib-049 to calib-057 appended, flagged "URL via search result".
- `drafts/calibration_exemplars.md`: the standard for the batch prompts.

## 0. Verdict in brief
- **Classes:** all five classes stand. A01 Pot/Pot, A24 Pot/Pot, A39 Cert/Cert, B01 Pot/Pot, B18 Pot/Pot.
- **Scores:** two corrected. A24 d2 1→3 and B18 d2 1→3. Both drafts scored 1 with no source, and a search found usable funding.
- **Fields:** B18 tr_status corrected from exists to absent. Notes and sources updated for all five.
- **Mechanics:** C1→C4 order, horizon adjustments and the cap were applied correctly in all five drafts.
- **Potential-heaviness:** it mostly reflects the sample. There is also one specific defect. The Likely gate sits at d2/d3 ≥ 4, but the anchors define only levels 5, 3 and 1, so agents with no level-5 evidence round to 3. **Analogue sourcing is not the bottleneck.** Both near-Likely items cleared the analogue gate (3 and 2 analogues) and failed only on d2/d3. Amendment R8-A (§4) adds level-4 anchors. In this sample it would move only B01 to Likely/Likely.
- **Hinge risk:** the C1 third clause turns on `tr_funded_pilot`, which is undefined. With the d2 corrections, a loose "yes" would make A24 Certain/Certain on a corporate prototype test. Definition D1 (§5) is needed before fan-out.

## 1. Item findings

### A01 AI scribes: class unchanged, Potential / Potential, near-Likely
- **(a) Scores.**
  - d1 2: acceptable, but the draft justified it partly from UK/NHS guidance, which is leader context. The valid basis is the generic TR Action Plan mention (calib-008, a secondary tax-news site; replace it with the primary DDO or Ministry text in step 2).
  - d2 2: fine.
  - d3 3: confirmed by spot-check. The NEJM AI RCT (238 physicians) found −9.5% time-in-note for Nabla and −1.7% (n.s.) for DAX (calib-055/056). That is far below any 4/5 threshold, so A01 stays 3 even under R8-A.
  - d4, d5 3: fine.
  - d6 2: fine. The review search again found only vendor and transcription pages.
- **(b) Mechanics.** Correct, including the d6 2→3 increase at 3–5y, which does not reach C1.
- **(c) Sources.** These are plausible and specific.
  - calib-006 (TNW on Telepatia) supports BR and MX only as vendor-reported reach. Keep the count at 3 at medium confidence; if it is discarded, the count is 1 and the near-Likely flag drops, with the class unchanged.
- **Deciding condition.** Rewritten to a single condition: a funded TR hospital pilot.

### A24 Autonomous trucking: class unchanged, Potential / Potential
- **(a) Scores.**
  - d1 3: per the planner decision.
  - **d2 1→3.** The draft wrote "no source for any call" but did not search EU programmes. Horizon Europe CCAM Partnership calls on automated road transport are open to TR actors as an associated country; a 2026 flagship-pilot call is listed (calib-051). This is R&D funding, not a deployment budget, so 3 rather than 5.
  - d3 3: correct, since the claimed 40% is below 50%.
  - d6 3: kept, but its basis changes from "funded pilot at lower bound" to "active group" (Ford Otosan–AVL L4 programme, calib-052).
- **(a) tr_funded_pilot = no is right, for a different reason.** The Ford Trucks run was a corporate R&D prototype with a safety driver on a closed section. It was not an operational pilot. The draft said a yes "would not change the class". After the d2 correction that is no longer true: with d6 3, funded yes and d2 3, C1 fires and the item becomes Certain/Certain. That result would be wrong on the evidence. See D1.
- **barrier.** none. A regulation barrier (no live-traffic authorisation) is plausible but not sourced as a block, so no change.
- **(b) Mechanics.** Correct.
- **(c) Sources.**
  - calib-011 (SEC 6-K exhibit) is an unverified mapping, used for leader status only. Keep it, but step 2h should check it.
  - calib-009 uses an old-style Korea Times URL; add it to the 2h list.

### A39 EU AI Act reaching TR actors: class unchanged, Certain / Certain
- **(a) Scores.**
  - d1 4: textbook use of the "EU binding law reaching TR providers" anchor; not 5 because no TR law is in force.
  - d3 1: definitional; I added the obligation source so the "≤1 needs a source" rule is met.
- **The open caveat is resolved.** The Digital Omnibus on AI was adopted and entered into force on 27 July 2026 (calib-053, calib-054). The exact final high-risk dates (2 Dec 2027 and 2 Aug 2028 per the agreement) should be confirmed from the adopted text. This is class-neutral.
- **(b) Mechanics.** Correct: C1 at both horizons. At 3–5y the literal "d1 += level" gives 8, capped to 5 (see D3).
- **(c) Sources.**
  - calib-027's URL is on `hlc.com` but is attributed to Hogan Lovells (domain `hoganlovells.com`). This is a possible attribution error, so verify it. The PL analogue does not depend on it, because Poland is bound directly (calib-020).
  - calib-028 and calib-029 are aggregator pages with generated-looking IDs. They are not counted; replace them with primary sources (e.g. the Brazilian Senate page for PL 2338/2023) if they are ever used.
  - calib-021 is the Mayer Brown zh-hans path; the /en/ path is preferable.

### B01 Passive acoustic monitoring: class unchanged under the current anchors, Potential / Potential, near-Likely
- **(a) Scores.**
  - d2 3: correct under the current anchors. I added a more recent basis: Biodiversa+ BiodivConnect 2025–26 (calib-049) is open to TR via TÜBİTAK 1071, with a topic on measuring restoration success. It is topic-adjacent with no reserved budget. The draft's only call was from 2022.
  - The EU funds acoustic AI monitoring at scale (TABMON, calib-050), which is leader evidence.
  - Under R8-A, d2 becomes 4 and the item becomes Likely/Likely.
  - d4 4: sourced.
  - d6 1: formally valid ("none found"), and a review search also found nothing. Confidence is low: TR bat-detector auto-ID and university bird studies very likely exist. A sourced active university group gives d6 3; a TÜBİTAK-funded field project gives d6 3 plus funded yes, which with d2 3 makes C1 fire and the item Certain. Run a targeted search (Ege, Doğa Derneği, WWF-Türkiye, bat acoustics) before final.
- **(b) Mechanics.** Correct.
- **(c) Sources.**
  - The analogues are academic fieldwork by in-country institutions. I accept them for a research-practice item and have written this into the exemplars as the standard.
  - calib-039 (Hürriyet Daily News) is weak support for Horizon Europe association; use a primary EC or ufukavrupa.org.tr source in step 2.

### B18 GenAI in grant writing: class unchanged, Potential / Potential
- **(a) Scores.**
  - **d2 1→3.** The draft scored 1 with no source, against the "≤1 needs a source" rule. Development-agency technical-support funds are usable; OKA and Samsun BB funded an "AI-supported project development training" (calib-057). Its scope (grant proposals or student projects) is unverified, but it is still sufficient for "generic funding usable".
  - d1 3: correct. These are permissive funder conditions, consistent with the enabling = 3 decision.
  - d6 2: kept. If calib-057 is confirmed as grant-writing training, d6 becomes 3, but tr_funded_pilot stays no because training is not an operational pilot.
- **tr_status exists→absent.** The draft said "exists" while d6 = 2. Only the funder-side rule exists in TR.
- **(b) Mechanics.** Correct. With d2 now 3, the C1 third clause becomes reachable through a funded pilot, so the deciding condition was rewritten.
- **(c) Sources.**
  - calib-048 is about AI in NGO recruitment, so it is weak evidence for "low NGO AI use". Keep it only for the NGO skills-gap point.
  - calib-043 (Thesify) is a secondary summary; cite NIH NOT-OD-25-132 directly.

## 2. Mechanics check (all items)
- **Branch order.** C1→C4 with first match wins was respected in all five. A39 correctly stops at C1.
- **Horizon adjustments.**
  - d6 +1 was applied only where analogue_count ≥ 2 (A01, A39, B01).
  - No undated barrier clearance was used.
  - The d1 dated obligation was used only for A39.
- **Cap at 5.** Applied (A39).
- **near-Likely flags.** Correct: A01 and B01.
- **3–5y class.** Never lower than 1–2y.

## 3. Systemic check: why 4 of 5 landed in Potential
**Sample effects (most of it).**
- A24 is a frontier, capex-heavy item, so Potential or Low is expected.
- B18 is organically diffused but poorly documented, so Potential follows from missing d6 evidence, not from the rule.
- A39 is a regulation item, so Certain.
- Only A01 and B01 were real Likely candidates.

**The analogue hypothesis is rejected for this sample.** Search-only conditions did not prevent analogue sourcing. A01 found 3, B01 found 2 and A39 found 2, all with plausible URLs. The concern about analogues is legitimate for Asian analogues (ID, KR) in niche Tier B items, but it was not the binding constraint here.

**Defect: an anchor gap at the Likely gate.**
- C3 requires d2 ≥ 4 or d3 ≥ 4. The anchors define d2 only at 5, 3 and 1, and d3 only at 5, 3 and 1.
- Both near-Likely drafts reasoned "not 4/5" because nothing met the level-5 text (dedicated call with budget; >50% cost cut). They fell back to 3.
- Level 4, the exact threshold that matters, has no definition. Agents therefore treat Likely as needing level-5 evidence, which makes Likely artificially rare.
- Expect this to recur across all ~70 items. Many leader-scaled items will collect 2–3 analogues and still stop at C4.

**Secondary observation (class-neutral here).** The 3–5y adjustment never raises d2 or d3. So the only route from Potential at 1–2y to a higher class at 3–5y is through d6 reaching 4 (Certain) or a dated d1 obligation. Potential→Likely across horizons is impossible by construction. I do not propose changing this; it follows the brief's "strong pull" criterion. Name it as a method limitation.

## 4. Proposed amendment R8-A (minimal; adds two anchor lines, changes no threshold)
Insert into the rule 8 anchors:

```
d2 4 = a named TR or EU programme/call open to TR actors, with an edition open or closed in the
       last 24 months, whose published scope explicitly names this application area
       (e.g. "biodiversity monitoring", "automated road transport"), but no budget reserved for
       this item. (5 = budget reserved for this item; 3 = generic digital/AI or topic-adjacent funding.)
d3 4 = sourced saving of 25–50% on a major cost line, or a >=25% reduction in staff time on a core
       task, for typical actors (leader or analogue study acceptable if the cost structure is
       comparable; vendor claims alone stay 3).
```

**Effect in this sample.** B01 becomes Likely/Likely (BiodivConnect's monitoring topic, edition 2025 → d2 4; 2 analogues; mean(d4,d5) 3.5). A01 stays Potential (RCT −9.5%, so d3 stays 3). A24 stays Potential (d2 could reach 4 via CCAM, but it has only 1 analogue). A39 and B18 do not change.

**What it keeps.** It preserves the brief's "strong cost or funding pull", because level 4 still requires item-specific scope or a quantified saving. If R8-A is adopted, change the B01 exemplar as follows:
- d2 line: "4: BiodivConnect 2025–26 explicitly covers restoration monitoring".
- Classes: Likely/Likely, branch C3.
- Deciding condition: optional.
- Delete the "(d2≥4 → Likely)" text.

## 5. Decisions the planner must make (new; not the three already logged)
- **D1 (needed before fan-out): define tr_funded_pilot.** Proposed text: "yes only for a funded operational pilot of the development in Türkiye (real users or operations; funding source named). R&D prototypes, trainings, committees and vendor offers = no; they may support d6 = 3 as an active group." Without it, A24 (and B18 if d6 reaches 3) flips to Certain on weak evidence. The exemplars already apply this definition.
- **D2: adopt or reject R8-A (§4).** If rejected, record "Likely is reserved for level-5-like evidence" as a method limitation and expect very few Likely items.
- **D3 (optional, class-neutral): restate the d1 horizon adjustment** as `d1 := max(d1, anchor level of the obligation dated 2028–2031)`. The literal "+=" adds levels (A39: 4+4 = 8, capped at 5) and shows d1 = 5 ("Turkish law") for a foreign-law item. Every obligation is level ≥ 4, so classes do not change. The exemplars currently follow the literal rule; if D3 is adopted, change A39's 3–5y d1 to "max(4, 4) = 4".
- **D4 (optional): a projected-Certain guard.** At 3–5y, an item with d6 = 3 and analogue_count ≥ 2 becomes Certain purely from the lag assumption (d6 3+1 = 4). Option: "If C1 at 3–5y holds only through the adjusted d6, classify Likely." No calibration item is affected (A39 is Certain via d1). Several batch items may be.

## 6. Spot-check log (8 WebSearch calls)

| # | Query (short) | Finding | Effect |
|---|---|---|---|
| 1 | TR passive acoustic BirdNET | no TR study surfaced | B01 d6 1 kept, low confidence |
| 2 | Horizon CL6 acoustic monitoring | TABMON (Biodiversa+/HE), BioacAI | leader evidence (calib-050) |
| 3 | "yapay zeka ile proje yazma" agencies | OKA/Samsun AI project-development training | B18 d2 1→3 (calib-057) |
| 4 | TR hospital AI clinical notes | radiology pilots, vendor transcription pages only | A01 d6 2 kept |
| 5 | AI Act Omnibus adoption | adopted; in force 27 Jul 2026 | A39 caveat resolved (calib-053/054) |
| 6 | Ford Otosan Horizon/CCAM | AVL R&D cooperation; CCAM 2026 flagship call | A24 d2 1→3; funded no confirmed (calib-051/052) |
| 7 | Biodiversa+ 2025–26 TÜBİTAK | BiodivConnect, TR via TÜBİTAK 1071, deadline 2025-11-07 | B01 d2 basis updated (calib-049) |
| 8 | Ambient scribe RCT effect size | NEJM AI RCT: −9.5% / −1.7% n.s. | A01 d3 3 confirmed (calib-055/056) |

## 7. Corrected values (diff against drafts/scores_calib.csv)

| id | field | old | new | reason |
|---|---|---|---|---|
| A24 | d2_funding | 1 | 3 | CCAM calls open to TR (calib-051), not searched in the draft |
| A24 | notes / branch / deciding_condition | — | rewritten | tr_funded_pilot reasoning; hinge warning |
| A39 | notes / source_ids | — | + calib-053/054 | Omnibus adopted; source-hygiene flags |
| B01 | notes / source_ids / deciding_condition | — | + calib-049/050 | recent call; R8-A sensitivity; d6 check |
| B18 | d2_funding | 1 | 3 | unsourced 1; development-agency funds (calib-057) |
| B18 | tr_status | exists… | absent… | consistency with d6 = 2 |
| A01 | notes / source_ids / deciding_condition | — | + calib-055/056 | d3 effect size; d1 basis |

The class columns are unchanged in all five rows.
