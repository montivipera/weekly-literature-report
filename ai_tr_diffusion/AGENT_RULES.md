# Rules for all worker agents (read fully before starting)

Project: "Global AI developments and their diffusion to Türkiye". Full brief: `ai_tr_diffusion/BRIEF.md` — read Sections 1–5 at minimum.

Hard rules
1. Never invent a citation. Every source needs a real, verifiable URL or DOI you actually saw. If you cannot source a claim, write "unsourced estimate".
2. Do NOT read papers or long documents in full. Abstracts, executive summaries, landing pages and institutional summaries are enough. This is a strategic scan, not an academic review.
3. Prefer primary/institutional sources: EU Commission, OECD, World Bank, Stanford AI Index, Türkiye Ulusal YZ Stratejisi (2021–2025 and successor), TÜBİTAK, Cumhurbaşkanlığı Dijital Dönüşüm Ofisi, Horizon Europe calls, company filings, peer-reviewed abstracts. Turkish-language sources are welcome for the Türkiye baseline.
4. Calibrated language: suggests, indicates, may. Date-stamp claims (today is 2026-10-03).
5. Return a COMPACT summary to the planner (≤25 lines). Put all detail in files, not in your reply.
6. Write files only under `ai_tr_diffusion/`. Use UTF-8, RFC-4180 CSV (quote fields containing commas), one row per item, no blank lines.
7. Driver scores are integers 1–5 (1 = weak/absent, 5 = strong). Six drivers: d1 regulatory pull, d2 funding pull, d3 cost pressure, d4 infrastructure & data readiness, d5 workforce readiness, d6 existing local activity in Türkiye.
8. Classification (apply in this order; first match wins; log the branch used in `class_branch`).
   Fields required per item: d1..d6 (1–5), analogue_count (0–5; each counted analogue needs a source), tr_funded_pilot (yes/no + source id), barrier (none|infra|language|regulation|market_size|cost + source id).

   Driver anchors (use these, not intuition):
   d1 5 = Turkish binding law/regulation in force with a dated obligation; 4 = EU (or other foreign) binding law that reaches a material share of Turkish actors in this horizon (exporters, EU-market providers, EU-supply-chain suppliers), or binding Turkish secondary regulation; 3 = Turkish law/action-plan target announced or in draft, or voluntary standard widely demanded by EU buyers/funders; 2 = soft guidance only; 1 = none.
   d2 5 = dedicated TR or EU call/programme open to TR actors with budget for this item; 4 = a named TR or EU programme open to TR actors, with an edition in the last 24 months, whose scope explicitly names this application area, but no budget reserved for the item; 3 = generic digital/AI funding usable for it; 1 = none. Private and consumer spend counts under d3, not d2.
   d3 5 = cuts a major cost line by >50% for typical Turkish actors (sourced); 4 = a sourced saving of 25–50% on a major cost line, or ≥25% less staff time on a core task (vendor claims alone stay 3); 3 = clear but moderate saving; 1 = no cost case.
   d4 5 = all needed compute/data/Turkish-language capability available off the shelf; 3 = usable with workarounds; 1 = key input absent.
   d5 5 = existing TR profession absorbs it with little retraining; 3 = skills gap but training exists; 1 = no relevant workforce.
   d6 5 = scaled national deployment; 4 = present beyond pilot in several TR orgs; 3 = at least one funded TR pilot or active university/NGO/municipal group; 2 = isolated mentions; 1 = none found.

   Definitions: tr_funded_pilot = yes ONLY for a funded OPERATIONAL pilot in Türkiye (public, NGO, municipal or corporate deployment with budget). R&D prototypes, trainings, committees and strategy documents = no.
   Clarifications (planner, 2026-10-03): a conformity requirement that is a precondition to market access (e.g. MDR-harmonised medical device rules) = d1 4; permissive type approval that only enables = d1 3. tr_funded_pilot = yes also when a primary source shows a real operational deployment with users (no budget figure needed). Scores must evidence the AI component itself, not generic digitalisation. 3–5y Likely reached only via the Certain→Likely guard is sub-labelled "Likely (lag-based)" in class_branch.
   Earlier clarifications: enabling/permissive regulation (e.g. a type-approval rule that allows but does not require a technology) is d1 = 3, not 4; d1 = 4/5 requires an OBLIGATION or a binding standard actors must meet to operate. All scores are capped at 5 after horizon adjustments. Since outbound HTTP fetch is blocked in this environment, a URL counts as 'seen' when it appears in a WebSearch result; record that in notes as 'URL via search result'.

   (1) CERTAIN   if d1 >= 4 OR d6 >= 4 OR (d6 >= 3 AND tr_funded_pilot = yes AND (d2 >= 3 OR d3 >= 4)).
   (2) LOW/DELAYED if barrier != none (sourced) OR min(d4,d5) <= 1 OR mean(d4,d5) < 2.0.
   (3) LIKELY    if (d2 >= 4 OR d3 >= 4) AND analogue_count >= 2 AND mean(d4,d5) >= 2.5.
   (4) POTENTIAL otherwise. Name the one deciding condition in `deciding_condition`.
   Any item reaching (4) with analogue_count >= 2 → write "near-Likely" in `notes` for the Opus review.

   Horizons: score for 2026–2028 first (class_1_2y). For 2028–2031 (class_3_5y) re-run the same rule after applying ONLY these dated adjustments, each with a source:
     d1 = max(d1, level of any obligation whose application date falls in 2028–2031);
     d6 += 1 if analogue_count >= 2 (analogue→TR lag assumption; a stated limitation);
     barrier may be cleared only if a source dates its removal.
   If the 3–5y class is Certain ONLY because of the assumed +1 on d6 (no sourced obligation or TR deployment), classify it Likely instead and say so in notes.
   The 3–5y class may not be lower than the 1–2y class without a written reason in `notes`.
   Planner decision (logged in STATE.md): private/consumer spend counts as "funding attached" via the d6 >= 4 branch.
9. Horizons and geographies are fixed by the brief; do not redefine them.
