# Scoring task (step 2) — instructions for Sonnet scoring agents

Read `AGENT_RULES.md` fully (rule 8 is the classification rule with driver anchors) and Brief §3–§5.

You will be given a list of inventory ids. For each id, take the row from `inventory.csv` and research it with WebSearch (standard mode; ~3–5 searches per item; use "extended" only if standard is thin). Consensus MCP (load via ToolSearch "select:mcp__Consensus__search") may be used for peer-reviewed abstracts, max 3 calls at a time. Never read documents in full; abstracts, summaries and landing pages suffice. Turkish-language searches are expected for the Türkiye baseline (e.g. "yapay zeka" + sector term, TÜBİTAK, Dijital Dönüşüm Ofisi, Ulusal Yapay Zeka Stratejisi 2021–2025, 2026–2030 eylem planı, Sanayi ve Teknoloji Bakanlığı, belediye, üniversite).

For each item fill these columns:
- leader_status: ≤25 words on USA/UK/EU/China status (scaled / growing / pilot), with source id(s).
- analogue_status: ≤30 words naming which of Poland, Brazil, Mexico, Indonesia, South Korea show the development, each with a source id; analogue_count = number of analogues you could SOURCE (0–5). Unsourced analogues do not count.
- tr_status: one of exists / pilot / absent, then ≤30 words with Turkish evidence and source id(s). tr_funded_pilot: yes/no (yes only with a source showing funding attached: TÜBİTAK, EU, ministry, municipality budget, corporate programme).
- barrier: none | infra | language | regulation | market_size | cost — only with a source; otherwise none.
- d1..d6: integers 1–5 following the anchors in rule 8. Do not score from intuition; each score ≥4 or ≤1 needs a source id in `notes`.
- class_1_2y, class_3_5y: Certain | Likely | Potential | Low — computed mechanically from rule 8 (state the branch in class_branch as e.g. "1-2y: C1 (d1>=4); 3-5y: C1"). Show the horizon adjustment you applied, with its source, in notes.
- deciding_condition: required when either horizon is Potential; otherwise optional one-liner.
- source_ids: semicolon-separated S-ids.
- notes: compact; include "near-Likely" where rule 8 requires; flag anything you could not source as "unsourced estimate".

Sources: append every NEW source as a row to `sources.csv` (id continues from the current max S-id; check the file first; use `used_for` = the inventory ids; `verified` empty). Do not duplicate URLs already present — reuse their ids. Never invent a URL or DOI.

Writing: do NOT edit `inventory.csv` directly (other agents work in parallel). Write your rows to `drafts/scores_<batch>.csv` with the exact inventory.csv header (all 25 columns, copy unchanged fields from inventory.csv). Append new sources to `drafts/sources_<batch>.csv` with the sources.csv header, using provisional ids `<batch>-001`, `<batch>-002`... (the planner will renumber). In source_ids you may mix existing S-ids and provisional ids.

Reply to the planner in ≤15 lines: per item one line "id — class_1_2y / class_3_5y — branch — confidence (high/med/low)"; then any item where the mechanical rule gave a result you think is wrong, with one sentence why.
