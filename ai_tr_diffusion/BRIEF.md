# Research Brief: Global AI Developments and Their Diffusion to Türkiye

## 1. Objective
Identify which AI-driven developments (technologies, services, business models, regulations, professions) are gaining momentum globally, estimate how and when each will reach Türkiye, and classify them by diffusion certainty and time horizon. End with a synthesis: a general landscape, then opportunities that fit the researcher's profile (Section 7).

## 2. Scope
Two tiers, run as separate work packages.

- **Tier A – Broad scan.** All major sectors: health, finance, education, public administration, agriculture, energy, manufacturing, logistics, media, law, retail, and the AI labour market (new roles, declining roles, freelance/service models).
- **Tier B – Deep focus.** Ecology and environment (biodiversity monitoring, remote sensing, nature-related reporting, restoration), academia and research (AI-assisted literature synthesis, data analysis, publishing, research integrity), and civil society (NGOs, cooperatives, municipalities: automation, grant work, evidence for policy).

Tier A is survey depth; Tier B is evidence depth with case examples and named organisations.

## 3. Reference geographies
- **Leaders:** USA, UK, EU (incl. Germany, Netherlands, France), China.
- **Diffusion analogues** for estimating lag to Türkiye: Poland, Brazil, Mexico, Indonesia, South Korea (upper-middle / newly industrialised, EU-adjacent or export-dependent). Use them to calibrate how fast a development moved from leaders to comparable economies.
- **Türkiye baseline:** current state for each development (exists / pilot / absent), using Turkish sources where available.

## 4. Diffusion drivers to assess for each development
Score each development on these; the classification in Section 5 must follow from the scores, not from intuition.

1. Regulatory pull (EU alignment, Green Deal, CSRD/TNFD/Nature Restoration Law spillover, national AI strategy, KVKK/data rules).
2. Funding pull (Horizon Europe, TÜBİTAK, development banks, corporate ESG budgets).
3. Cost pressure (does the development cut costs sharply for Turkish actors?).
4. Infrastructure and data readiness (compute, Turkish-language models, open data).
5. Workforce readiness (skills gap, existing professions that can absorb it).
6. Existing local activity (startups, university groups, public pilots).

## 5. Classification scheme
Classify every development into one group per horizon. Add groups if the evidence demands it, but define any new group explicitly.

| Group | Criterion |
|---|---|
| **Certain** | Driven by binding regulation or already present in Türkiye at pilot scale with funding attached |
| **Likely** | Strong cost or funding pull; present in ≥2 diffusion analogues |
| **Potential** | Present in leaders only; Türkiye has partial readiness; outcome depends on one identifiable condition (name it) |
| **Low probability / delayed** | Blocked by a structural barrier (infrastructure, language, regulation, market size) |

Horizons: **1–2 years** (2026–2028) and **3–5 years** (2028–2031), reported separately.

## 6. Method and workflow
Follow the multi-model pattern: planner decides; Sonnet agents run scans and source extraction; Opus agents review evidence and challenge classifications before they are finalised; planner synthesises.

Steps:
1. Build the development inventory (Tier A ~30–50 items, Tier B ~15–25 items) with a one-line definition each.
2. For each item: leader status, analogue status, Türkiye status, driver scores, classification, key sources.
3. Review pass: an Opus agent checks each classification against Section 5 criteria and flags disagreements; resolve and log the reasoning.
4. Synthesis (Section 8).

Source rules:
- Prefer primary and institutional sources: EU/OECD/World Bank, Stanford AI Index, national strategies (Türkiye Ulusal YZ Stratejisi and its successor), TÜBİTAK, Dijital Dönüşüm Ofisi, company filings, funding calls, peer-reviewed work.
- Every claim about a specific development carries a source. Never invent a citation; if a claim cannot be sourced, label it "unsourced estimate".
- Use calibrated language (suggests, indicates, may). State the limitations of the method in the final report.

Compaction safeguards:
- Keep `STATE.md` with: completed steps, current step, open questions, file list. Update after every step.
- Store the inventory in `inventory.csv` (one row per development) so progress survives context loss.
- Store sources in `sources.csv` (id, title, url, date accessed, used-for).

## 7. Researcher profile (for the synthesis only)
Doctoral researcher in ecological restoration (Ege University, İzmir): wetland/delta monitoring, herpetofauna, Odonata, vegetation, remote sensing. Co-founder of a science-and-culture cooperative. Collaborates with a metropolitan municipality, WWF-Türkiye, Tour du Valat, and a national nature NGO. Heavy, workflow-level user of Claude Code and multi-agent setups; does not write code manually. Career aim: combine ecology with AI, academic work plus projects with civil society; interested in evidence synthesis for institutions.

## 8. Deliverables
Two reports plus data files.

**8.1 `report_en.md` – detailed English report (primary deliverable)**
1. Executive summary (≤1 page).
2. Method and limitations.
3. Tier A landscape: table of developments with classification per horizon and driver scores; short narrative per sector.
4. Tier B deep focus: per development, evidence, named examples, Türkiye status, classification, the condition that decides its outcome.
5. Cross-cutting patterns (what drives diffusion to Türkiye in general).
6. Synthesis: general landscape, then opportunities matching Section 7. At most three recommended directions, each with: why, when it applies, first concrete step, main risk.
7. Full reference list.

**8.2 `rapor_tr.html` – Turkish visual report (self-contained HTML artifact)**
- Plain, fluent Turkish for a non-specialist reader; no jargon without a one-line explanation; no emoji.
- Visuals as inline SVG or CSS (no external images or scripts): a diffusion matrix (certainty × horizon), a timeline of expected arrival in Türkiye, a sector heatmap, and one chart per Tier B domain.
- Structure: what is happening in the world → what will come to Türkiye and when → what this means for the reader → three recommendations in simple language.
- Length: readable in 15–20 minutes. Content must be consistent with `report_en.md`; it is a translation-and-simplification, not a separate analysis.

**8.3 Data files:** `inventory.csv`, `sources.csv`, `STATE.md`.

## 9. Quality gates before finishing
- Every development has a classification for both horizons and at least one source.
- Opus review log exists and disagreements are resolved with reasons.
- No citation without a verifiable URL or DOI.
- Turkish report opens correctly as a single HTML file and matches the English report's classifications.
