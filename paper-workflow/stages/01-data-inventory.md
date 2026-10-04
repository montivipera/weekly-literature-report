# Stage 01 — Data inventory
Goal: describe what the dataset is (variables, design, dependence, gaps, effort) and record what the user has already seen, without testing any outcome against any predictor.

## Entry modes
- Normal in `a-data-only`, `b-analysis-done` and `c-half-draft`.
- In `b-analysis-done` and `c-half-draft` the prior-exposure statement must also list every analysis already run on these data (from intake.md), not only what was looked at.
- RETRO-AUDIT in `d-finished-manuscript` and `e-under-revision`: build the same inventory from the raw data, then compare it with the manuscript's data description (n, variables, units, exclusions). Each mismatch becomes one inbox.md item targeting the file that holds the draft text (for example methods.md).
- NOT-PASSABLE: when the raw data are not available (only summaries or model outputs). Queue the disclosure item (stage 00 rule) "raw data not inventoried: <reason>; n, design and dependence taken from <source>".

## Inputs · Live file(s) · Outputs
- **Inputs:** `data/` (raw, read-only: `.claude/settings.json` denies `Edit(/papers/*/data/**)`, and step 1 commits data/ and removes write permission), the field protocol or sampling notes, intake.md.
- **Live files:** `data-inventory.md, SHA256SUMS`. The prior-exposure statement goes into STATE.md and access rows into data-access.md (both always writable).
- **Outputs:**
  - `SHA256SUMS` in papers/<slug>/, beside data/ and never inside it: plain `sha256sum` output for every file under data/, paths written `data/<file>`, no header, so `sha256sum -c SHA256SUMS` run from papers/<slug>/ checks it.
  - `data-inventory.md` (≤150 lines): header `derives-from: intake.md@<short-commit>`, then six sections:
    1. files: `path | sha256 | rows | columns`;
    2. variables: `name | type | unit | levels or range | n non-missing | n missing | notes (file; codebook role)`;
    3. design: `sampling unit | n per unit | nested in (site, plot) | repeated over (year, season) | sampling effort`;
    4. missingness: by unit and period;
    5. outliers and impossible values: `variable | value | unit/row | rule`;
    6. prior-exposure evidence and gaps: `path | date | kind (script, output, figure, draft)` for every artefact showing earlier analysis (results never opened), then every `NA — <what is missing>` item.
  - `data-access.md`: data-reader's rows for what it opened or ran (`outcome-level? no`), one row per earlier look the user reports, and any hold-out or new-data declaration (`outcome-level? no`).
  - `STATE.md`: `prior_exposure:` = level (`none` · `descriptive` · `outcome-looked` · `analysed` · `published`) + dates, and the prior-exposure statement: one line on what was seen or run, by whom, when [F10].

## Model and agent
- `agents/data-reader.md` (claude-sonnet-5-5, effort medium, ≤100k input tokens, output ≤150 lines). It may run R or Python through Bash for counts, tables and checksums only, and writes SHA256SUMS, data-inventory.md and its data-access.md rows with Write or Edit. It extracts to the schema above and never summarises in prose.
- Main session (Opus 5.5, effort medium): never reads data/. It reads data-inventory.md only, asks the user the prior-exposure questions, and writes the statement into STATE.md.
- Hard ban for every agent in this stage: no correlation, test, model, plot or grouped summary of any response against, by or with any predictor [C4, C34]. Univariate summaries of single variables (including responses) are allowed.

## Procedure
1. Set `live_file: data-inventory.md, SHA256SUMS`, check that the data/ deny rule is in `.claude/settings.json`, then, before data-reader or any script touches the data, commit data/ (`git add papers/<slug>/data && git commit -m "data: <slug>"`) and run `chmod -R a-w papers/<slug>/data`.
2. data-reader writes SHA256SUMS and copies each checksum into section 1, so later stages can show the raw data never changed.
3. data-reader lists every variable with type, unit, levels or range, and non-missing and missing counts.
4. data-reader describes the design: sampling units, n per unit, nesting and dependence (site, plot, year, season, observer) and sampling effort per unit [C32, C33].
5. data-reader tabulates missingness by unit and period, flags outliers and impossible values by a stated univariate rule (removing nothing), records prior-exposure evidence by path and date, and appends its data-access.md rows.
6. Main session reads data-inventory.md and, if any outcome–predictor content appears, deletes it and re-runs data-reader with the ban restated.
7. Main session asks the user what they have already seen or analysed in these data, and when; it writes the prior-exposure statement into STATE.md and one data-access.md row per reported look (`outcome-level? yes|no`) [C23, C24, C25].
8. If the level is `outcome-looked` or higher, main session sets S04 to `NOT-PASSABLE` and queues its disclosure item (any prior looks; all analyses exploratory).
9. Last chance to declare a hold-out or new dataset (stage 00 step 9): any dataset to be analysed `confirmatory` outside `a-data-only` with no outcome-level look needs its data-access.md row (path, `outcome-level? no`) committed now, before any analysis [F10–F12, C25].
10. Run the gate, commit, and set `live_file: search-log.md, scan-notes.md` for stage 02.

## Gate (pass/fail)
Run gate commands from paper-workflow/ (the project root for Claude Code).
- [ ] SHA256SUMS is in papers/<slug>/ (not in data/), has one line per file (`find papers/<slug>/data -type f | wc -l` equals `wc -l < papers/<slug>/SHA256SUMS`), and `(cd papers/<slug> && sha256sum -c SHA256SUMS)` passes.
- [ ] data/ is committed and read-only: `git status --porcelain papers/<slug>/data/` is empty and `find papers/<slug>/data -perm -u=w` prints nothing.
- [ ] Every variable has type, unit, levels or range, n non-missing and n missing.
- [ ] The design section gives n per unit, every nesting or dependence level (site, year, season) and the sampling effort.
- [ ] The missingness and outlier sections exist, the outlier rule is stated, and no row was removed.
- [ ] No outcome–predictor content: every hit of `grep -inE 'correl|regress|p *[<=]|t-test|anova|chi-sq|r2|effect of' papers/<slug>/data-inventory.md` is checked by the user and is univariate or predictor-only.
- [ ] STATE.md has `prior_exposure:` with level, dates and what was seen; a level of `outcome-looked` or higher has set S04 to `NOT-PASSABLE` with its disclosure queued.
- [ ] data-access.md has data-reader's rows for this stage, one row per look the user reported, and a committed declaration row for every hold-out or new dataset meant for `confirmatory` use.
- [ ] data-inventory.md starts with its derives-from header, has the six sections and is ≤150 lines.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is intake.md, data-inventory.md or SHA256SUMS. Write the change list in plan mode and wait for user approval. Set `mode: propagate`, edit intake.md first, then data-inventory.md (re-running data-reader for any fact taken from data/), and mark every file that derives from data-inventory.md `stale:` in STATE.md. Close each item by appending its row with status `CLOSED -> <file>@<commit>`, then set `mode: work`. A request to change data/ itself is refused: raw data stay as delivered, SHA256SUMS is never regenerated to fit changed data, and any cleaning is done by a stage 05 script with its own analysis-log.md row.

## Evidence
- [C34] A: initial data analysis is pre-planned and does not evaluate outcome–predictor associations.
- [C4] A: question trolling (searching many relationships for notable results) gives substantial upward bias.
- [C32] A: data-exploration protocol for outliers and dependence; [C33] A: Zuur & Ieno start from design, sampling layout and dependence.
- [C23] A: preregistering analyses of pre-existing data is useful even though design and sample size are already fixed (template exists); [C24] A: analyst prior knowledge weakens such plans.
- [C25] A: log data access ("checkout") so later confirmatory claims on secondary data are credible (data-access.md).
- [F10] A: disclose prior knowledge of a dataset on a scale from "never worked with these data" to publications; use hold-out subsamples.
- [F11] A: a data checkout log shows plans predate data access; [F12] A: Explore-and-Confirm on secondary data (script on a subset, register, then the rest).
- [G21] A (vendor docs): deny rules do not catch R or Python subprocess writes (hence `chmod -R a-w` and the data/ commit).
