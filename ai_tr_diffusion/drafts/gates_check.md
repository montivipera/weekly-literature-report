# Gate check (brief section 9)

Run 2026-10-03 against report_en.md v2 (4ed9bce plus the Turkish sync), `inventory.csv`, `sources.csv`, `review_log.md` and `rapor_tr.html`. The script is `drafts/gates_check.py`; run it from `ai_tr_diffusion/`.

| Gate | Result |
|---|---|
| (a) every development has a class for both horizons and at least one source | PASS |
| (b) Opus review log exists, disagreements resolved with reasons | PASS |
| (c) no citation without a verifiable URL or DOI | PASS |
| (d) rapor_tr.html is a single file and its classes match report_en.md | PASS |

## (a) Classes and sources: PASS

`inventory.csv` has 73 rows. All 73 have `class_1_2y` and `class_3_5y` in {Certain, Likely, Potential, Low}, so none is missing or invalid. All 73 carry at least one S-id in `source_ids`, with 5 to 21 per row.

## (b) Review log: PASS

`review_log.md` has both parts and both Resolutions sections.
- Part 1 covers 36 rows ("Row verdicts"): 27 agree, 4 disagree and 5 open. Its "Resolutions (planner, part 1)" section includes a "Summary of disagreement resolutions" table. A15, A46, B01 and B17 are each resolved with a planner decision, a final class and a reason. The 5 open items went to part 2.
- Part 2 ("Part 2 — rerun rows (43)") has 38 agree, 4 disagree (B09, A47, A10, A25) and 1 open (A27). Its "Resolutions (planner, part 2)" section holds decisions Q1–Q6 and a "Changed rows (old class → new class)" table with reasons. A27 is closed as Potential/Potential, because the S639 figure was not verified.
- The 55 "agree" rows in part 1 and part 2 are logged one by one.
- `drafts/review_4c_report.md` and `review_4c_applied.md` add the later Opus pass (34 of 34 findings applied).

## (c) Citations and URLs: PASS

- The body of report_en.md (sections 1–6) cites 376 distinct S-ids. All 376 are listed in section 7, and none is missing from `sources.csv`.
- `inventory.csv` references 666 distinct S-ids across all columns. The union with the report is 668.
- All 668 have a non-empty `http(s)://` URL in `sources.csv`, so there are zero failures. S639 now has a percent-encoded URL.
- Labelled weak:
  - 74 of the 682 register rows are labelled `weak`.
  - 31 of the 376 cited in the report are weak, and each carries "(secondary source)" in section 7.
  - 73 of the 668 in the union are weak.
- The other register flags are not cited. Seven rows are orphans, one is a duplicate (of S500), and 7 are marked "URL via search result".
- Caveat: "verified" means that the URL appeared in a search result and passed a structural check, as section 2 states. HTTP was blocked, so no URL was fetched.

## (d) Turkish file against English report: PASS

- `rapor_tr.html` is one file of about 152 KB. A static scan found no external `src`, `href`, `url()` or `@import`, and no `http(s)` string. Its only script tag is the inline JSON `#classes`.
- I parsed the `#classes` JSON (73 ids). I also extracted classes from the report_en.md Table 3.1 (48 Tier A rows, with "(near-Likely)" and "(lag-based)" sub-labels stripped) and from the "Classification" line of each section 4 item (25 Tier B items).
- All three sources agree for every one of the 73 ids, so there are 0 mismatches. They are the report_en.md table and section 4, the HTML JSON, and `inventory.csv`.

## Other checks

- **Word count.** The visible Turkish text has 4,768 words, excluding SVG labels and the collapsed list. At about 250 words per minute that is about 19 minutes, which is within the 15–20 target but near its top. At 200 words per minute it is about 24 minutes. The v2 additions (ranking defence, limitations, calibration notes) added about 15% over v1, and I trimmed some back.
- **Visual types.** All four are present:
  - Matrix: Figure 1, `#sekil1`.
  - Timeline: Figure 2, `#sekil2`, with a text-list alternative.
  - Heatmap: Figure 3, `#sekil3`.
  - One chart per Tier B domain: Figures 4, 5 and 6, for ecology, academia and civil society.
- **No emoji.** None found in the HTML.
- **Narrow-screen layout.** Playwright and Chromium are not available: the browser download was blocked by the proxy. This is a static check only. All SVGs use `width:100%` with `max-width:560px`, and the tables collapse to block layout under the 390px media query. No fixed widths exceed 390px. A real 390px render was not run.
