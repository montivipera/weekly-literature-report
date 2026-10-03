# Inventory Build Log (Review 1)

**Date:** 2026-10-03  
**Agent:** Data-editing agent  
**Input files:** drafts/inventory_A.csv (43 rows), drafts/inventory_B.csv (22 rows), drafts/review_1_inventory.md

## Counts

- **Tier A rows:** 48
- **Tier B rows:** 25
- **Total inventory rows:** 73
- **Unique sources:** 59

## Merges Applied

1. **A30 + A31 → A30** (Generative legal AI for drafting, research and contract review)
   - A31 removed
   - Anchor URLs combined with " | "

2. **A07 + A33 → A07** (Agentic commerce and agent-initiated payments)
   - A33 removed
   - Anchor URLs combined

3. **A40 + A43 → A40** (Turkish-language and sovereign LLMs, largely built on open-weight base models)
   - A43 removed
   - Anchor URLs combined
   - Reword: merged open-weight models into A40

4. **B07 + B08 → B07** (AI and data tooling for nature-related disclosure)
   - B08 removed
   - Anchor URLs combined

5. **B14 + B16 → B14** (Publisher, funder and university rules on generative AI in research)
   - B16 removed
   - Anchor URLs combined
   - Scope: authoring, peer review, grant applications

## Splits Applied

1. **B04 split** into:
   - **B04** (satellite): Deep-learning wetland and habitat mapping from Sentinel-1/2
   - **B23** (drone/UAV): UAV / drone vegetation and habitat mapping with deep learning
   - Satellite uses free Copernicus data; drone requires hardware and field permits (SHGM)

## New Rows Added

### Tier A (8 new: A44–A51)

| ID | Development | Sector |
|----|---|---|
| A44 | AI-enabled cyber offence and AI-driven cyber defence | cross_cutting |
| A45 | Deepfake and voice-clone fraud, and AI-based identity verification (eKYC liveness) | finance |
| A46 | AI in insurance underwriting and claims, including satellite-based agricultural loss assessment | finance |
| A47 | AI-driven irrigation scheduling and agricultural water management | agriculture |
| A48 | AI for disaster risk and rapid damage assessment | public_administration |
| A49 | Secondary use of national health data for AI (EHDS-type health data spaces) | health |
| A50 | AI literacy and workforce reskilling programmes | labour_market |
| A51 | Algorithmic management and AI in hiring/HR | labour_market |

### Tier B (5 new: B23–B27)

| ID | Development | Sector |
|----|---|---|
| B23 | UAV / drone vegetation and habitat mapping with deep learning | ecology_environment |
| B24 | Biodiversity / nature credit markets with digital MRV | ecology_environment |
| B25 | Multi-agent and autonomous AI research systems ("AI co-scientists") | academia_research |
| B26 | LLM analysis of public consultations and participatory input | civil_society |
| B27 | AI urban-nature and climate-adaptation mapping and local digital twins for municipalities | civil_society |

**Note:** MB5 (AI-supported restoration prioritisation) was folded into B06's definition rather than added as a new row, per planner decision.

## Rewords Applied

Tier A rewords:
- A29: Added C2PA/SynthID and Art. 50 watermarking/provenance focus
- A39: Reframed to EU AI Act extraterritorial compliance obligations
- A38: Changed to AI-enabled freelancing and micro-agencies
- A03: Scoped to MHRS public deployment
- A09: Reframed to institutional response (assessment redesign) rather than student use
- A26: Added TR dubbing/localisation case

Tier B rewords:
- B04: Satellite-only focus, named tools added (Google Earth Engine, Copernicus HRL, Dynamic World)
- B03: Highlighted ML-assisted bioinformatics component
- B06: Broadened from carbon to all restoration outcomes; folded in restoration prioritisation and site-selection models; added Restor
- B07: Consolidated TNFD LEAP, ESRS E4, and ISSB frameworks
- B09: Added EU monitoring infrastructure (NRR, Copernicus, EuropaBON, BioDT/DestinE)
- B12: Reframed as institutional living evidence databases
- B13: Narrowed to individual coding assistants (multi-agent systems move to B25)
- B14: Merged with B16; broadened to publisher, funder, and university rules
- B18: Broadened to include funder-side screening
- B21: Generalized from DataKind to tech-for-good intermediaries
- B22: Reframed to evidence-to-policy brief generation (Overton moved to named tool)

## Ambiguities and Notes

1. **Anchor URLs for new rows:** All new rows (A44–A51, B23–B27) have empty `anchor_source_url` and notes "added in review 1; needs source". Step 2 agent must source these.

2. **MB5 folding decision:** The review proposed MB5 (restoration prioritisation platforms) as a new row, but the planner elected to fold it into B06 rather than add it separately. This is correctly reflected in B06's expanded definition and named examples.

3. **B04 satellite/drone split:** B04 retains its original ID for the satellite component; the drone component is new row B23. Both have "needs source" notes pending step 2 verification and final sourcing.

4. **Tier A count (48) and Tier B count (25):** These match the review's final recommendations (§6). Law remains at 2 rows post-merge (A30, A32); planner did not restore to 3 by keeping A30 and A31 split.

5. **Reword ambiguities:** 
   - A11 scoping to central government was recommended but full segregation not applied (municipal assistants remain in B19, B20 as separate rows with notes). Tier A does not split.
   - B10/B11 boundary sharpening noted but both rows retained. Paths differ as documented.
   - A21 humanoid-robot figure ("7,000 units sold 2025") requires IFR primary source verification in step 2.

## CSV Validation

- **inventory.csv:** 73 rows × 25 columns. RFC-4180 compliant. Header: id, tier, sector, development, definition, named_examples, anchor_source_url, leader_status, analogue_status, analogue_count, tr_status, tr_funded_pilot, barrier, d1_regulatory, d2_funding, d3_cost, d4_infra_data, d5_workforce, d6_local_activity, class_1_2y, class_3_5y, class_branch, deciding_condition, source_ids, notes.
- **sources.csv:** 59 rows × 6 columns. RFC-4180 compliant. Header: id, title, url, date_accessed, used_for, verified.

All rows parsed correctly by Python csv module. No blank lines or malformed entries detected.

---

**Build completed:** 2026-10-03 09:07:38 UTC
