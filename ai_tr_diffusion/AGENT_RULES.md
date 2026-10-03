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
8. Classification rule (apply mechanically, then note any doubt in `notes`):
   - Certain: binding regulation applies to Türkiye/EU-aligned firms (d1 ≥ 4) OR already present in TR at pilot scale with funding attached (d6 ≥ 3 AND d2 ≥ 3).
   - Likely: strong cost or funding pull (d3 ≥ 4 OR d2 ≥ 4) AND present in ≥ 2 diffusion analogues (Poland, Brazil, Mexico, Indonesia, South Korea).
   - Potential: present in leaders (USA, UK, EU, China) only or in ≤ 1 analogue; TR partial readiness (mean of d4,d5 ≥ 2.5); you MUST name one deciding condition.
   - Low probability / delayed: a structural barrier (any of d4, d5 ≤ 1, or an explicit regulatory/market-size block) dominates.
   - Give one class for 1–2 years (2026–2028) and one for 3–5 years (2028–2031). They may differ.
9. Horizons and geographies are fixed by the brief; do not redefine them.
