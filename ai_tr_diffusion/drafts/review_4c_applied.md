# Step 4c fixes applied to report_en.md and CSVs

Applied 2026-10-03. 34 of 34 findings applied, 0 skipped. Deviations from the proposed wording are noted per row.

| # | Severity | Status | Note |
|---|---|---|---|
| 1 | blocker | applied | A46 deciding_condition rewritten (CSV); A25 "ride optimization" corrected (CSV); Table 3.1 deciding-condition column regenerated from inventory.csv (80-char truncation rule as before); the "not recorded" sentence deleted; B09 deciding-condition text replaced. A15, A17, A47 now show their CSV conditions. Certain rows with an empty condition show "n/a (Certain)". |
| 2 | blocker | applied | Duplicate "## 6. Synthesis" heading and the PLANNER comment removed. |
| 3 | blocker | applied | Counts from sources.csv `verified`: 682 rows = 593 format_ok + 7 format_ok;orphan + 7 "URL via search result" + 74 weak + 1 duplicate. 607 passed the structural check. §1 and §2 text updated. The §7-versus-register sentence is added. Deviation: the cited-source count is 376, not 372, because findings 9 and 10 add four citations (S098, S110, S315, S316), now in §7. The duplicate is written "a duplicate of S500", without naming S378, so that no duplicate row is cited. |
| 4 | blocker | applied | S679 (Bağcılar DHA/İSTKA, weak, dha.com.tr) has the title "Bağcılar Disaster and Hazard Assessment. İSTKA 2025 AI Programme.", which does not support a 90% figure. The figure is removed and S679 is not cited. The text now reads "the model of the İSTKA support for Bağcılar's digital twin (S593)". |
| 5 | should-fix | applied | §1 review-pass wording. |
| 6 | should-fix | applied | Three bullets added after Depth: search-only sourcing (200-search cap, degraded then re-run batches), analogue counting, and calls named in §6 (BiodivFuture). |
| 7 | should-fix | applied | Count verified: "unsourced" appears in 72 of 73 note fields (all except A46). Reviewer's wording used. |
| 8 | should-fix | applied | §5 pattern 2 replaced as proposed. |
| 9 | should-fix | applied | Machinery Regulation citation [S315; S316, secondary source]. S316 is weak in sources.csv, so the label is consistent. |
| 10 | should-fix | applied | §5 pattern 3 replaced as proposed. |
| 11 | should-fix | applied | §6.1 para 1 as proposed. The middle clauses on ministry-owned platforms and funding-led Likely classes are kept. |
| 12 | should-fix | applied | §6.1 para 2 replaced as proposed. |
| 13 | should-fix | applied | §6.1 para 3 eDNA and camera-trap citations; list grammar adjusted. |
| 14 | should-fix | applied | Direction 2 Why, B11 cost evidence. |
| 15 | should-fix | applied | §6.2 intro (S401) and Direction 1 Why. |
| 16 | should-fix | applied | BiodivFuture caveat added to Direction 1 Main risk. It also covers the user's request for an unverified monitoring-fit caveat. |
| 17 | should-fix | applied (merged) | Resolved with the user-supplied ranking-defence paragraph ("Why this order", 112 words) inserted at the end of §6.2, plus the reviewer's start-order sentence ("expected value, not start order"). The reviewer's separate §6.3 paragraph was not added, to avoid duplicating it. The existing §6.3 closing sentence is unchanged. |
| 18 | should-fix | applied | B07/B24 rejection reasons corrected, with reopening conditions. The sentence is split into "the first" and "the second" for readability. |
| 19 | should-fix | applied | Expert-validator bottleneck labelled as the planner's judgement. |
| 20 | should-fix | applied | Municipality hedge and C1-clause qualifier added. |
| 21 | should-fix | applied | TÜBİTAK 1001 labelled "generic ... not assessed in this study"; Horizon EO topic cited (S514). |
| 22 | should-fix | applied | A27 and A40 deciding_condition replaced in the CSV and the table. |
| 23 | should-fix | applied | A46 and B09 class_branch 3-5y corrected in the CSV (analogue_count 2); §4 B09 now "Potential (near-Likely) at both horizons (C4)". rapor_tr.html was not synchronised (outside this task). |
| 24 | should-fix | applied | S639 URL percent-encoded in sources.csv and in §7. |
| 25 | nit | applied | §1 fixed-rule wording. |
| 26 | nit | applied | "single self-report" added. |
| 27 | nit | applied | Workflow sentence. |
| 28 | nit | applied | B06/S108 sentence added to the S108 scope bullet. |
| 29 | nit | applied | B02 wording. |
| 30 | nit | applied | Diacritics (Sağlık Bakanlığı, Türkiye, TEİAŞ, TÜSEB) fixed in the CSV deciding_condition column and therefore in the table. |
| 31 | nit | applied | "n/a (Certain)" for all Certain rows, including the CSV values for A02, A50 and B20. |
| 32 | nit | applied | "at least 20%". The "90 percent" text is gone (finding 4). |
| 33 | nit | applied | "can start on existing partner resources". |
| 34 | nit | applied | Instead of waiting for the 5h pass, "SUPERSEDED (see review_log):" is prepended to the stale sentences in the notes of A46, A47, B17, B20 and B27. |

## CSV changes (Python csv, row order, columns and CRLF preserved)
- inventory.csv: 16 rows touched (A46, B09, A25, A27, A40, A02, A50, B20, A03, A04, A11, A18, A42, A47, B17, B27). No class or score changed.
- sources.csv: S639 URL only.

## Validation
All checks pass: single H2 per section; every cited S### (bracketed or plain) is in §7 and sources.csv; §7 holds exactly the 376 cited ids with URLs equal to sources.csv; 48 table rows equal inventory.csv (classes, near-Likely, lag-based, deciding condition); portfolio 17/8/48 and 17/16/40; §1 and §2 counts equal CSV-derived figures; no "not recorded" and no "<!--".
