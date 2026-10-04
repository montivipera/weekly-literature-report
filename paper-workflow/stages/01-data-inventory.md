# Stage 01 — Data inventory
Goal: describe what the dataset is (variables, design, dependence, gaps, effort) and record what the user has already seen, without testing any outcome against any predictor.

## Entry modes
- Normal in `a-data-only`, `b-analysis-done` and `c-half-draft`. In `a-data-only` this stage also opens the data-access log [F11].
- In `b-analysis-done` and `c-half-draft` the prior-exposure statement must also list every analysis already run on these data (from intake.md), not only what was looked at.
- RETRO-AUDIT in `d-finished-manuscript` and `e-under-revision`: build the same inventory from the raw data, then compare it with the manuscript's data description (n, variables, units, exclusions). Each mismatch becomes one inbox.md item targeting the file that holds the draft text (for example methods.md).
- NOT-PASSABLE: when the raw data are not available (only summaries or model outputs). Queue the disclosure item "raw data not inventoried: <reason>; n, design and dependence taken from <source>".

## Inputs · Live file(s) · Outputs
- **Inputs:** `data/` (raw, read-only: `.claude/settings.json` denies `Edit(/papers/*/data/**)`), the field protocol or sampling notes, intake.md.
- **Live file:** `data-inventory.md`. The prior-exposure statement goes into STATE.md (always writable).
- **Outputs:**
  - `data-inventory.md` (≤150 lines): header `derives-from: intake.md@<short-commit>`, then six sections:
    1. files: `path | sha256 | rows | columns`;
    2. variables: `name | type | unit | levels or range | n non-missing | n missing | notes`;
    3. design: `sampling unit | n per unit | nested in (site, plot) | repeated over (year, season) | sampling effort`;
    4. missingness: by unit and period;
    5. outliers and impossible values: `variable | value | unit/row | rule`;
    6. data-access log: `date | who | what was opened | why`.
  - `STATE.md`: `prior_exposure:` = level (`none` · `descriptive` · `outcome-looked` · `analysed` · `published`) + dates + one line on what was seen or run [F10].

## Model and agent
- `agents/data-reader.md` (claude-sonnet-5-5, effort medium, ≤100k input tokens, output ≤150 lines). It may run R or Python through Bash for counts, tables and checksums only. It extracts to the schema above and never summarises in prose.
- Main session (Opus 5.5, effort medium): never reads data/. It reads data-inventory.md only, asks the user the prior-exposure questions, and writes the statement into STATE.md.
- Hard ban for every agent in this stage: no correlation, test, model, plot or grouped summary of any response against, by or with any predictor [C4, C34]. Univariate summaries of single variables (including responses) are allowed.

## Procedure
1. Set `live_file: data-inventory.md` and check that the data/ deny rule is present in `.claude/settings.json`.
2. data-reader records a sha256 checksum for every file in data/, so later stages can show the raw data never changed.
3. data-reader lists every variable with type, unit, levels or range, and non-missing and missing counts.
4. data-reader describes the design: sampling units, n per unit, nesting and dependence (site, plot, year, season, observer) and sampling effort per unit [C32, C33].
5. data-reader tabulates missingness by unit and period and flags outliers and impossible values by a stated univariate rule, removing nothing.
6. Main session reads data-inventory.md and, if any outcome–predictor content appears, deletes it and re-runs data-reader with the ban restated.
7. Main session asks the user what they have already seen or analysed in these data, and when, and writes the prior-exposure statement into STATE.md [C23, C24, C25].
8. If the level is `outcome-looked` or higher, main session sets S04 to `NOT-PASSABLE` and queues its disclosure item (any prior looks; all analyses exploratory).
9. In `a-data-only` the user adds the first data-access log row; every later opening of data/ by a person adds a row [F11].
10. Run the gate, commit, and set `live_file: search-log.md` for stage 02.

## Gate (pass/fail)
- [ ] Every file in data/ is listed with a sha256 checksum, and `sha256sum -c` against those values passes.
- [ ] Every variable has type, unit, levels or range, n non-missing and n missing.
- [ ] The design section gives n per unit, every nesting or dependence level (site, year, season) and the sampling effort.
- [ ] The missingness and outlier sections exist, the outlier rule is stated, and no row was removed.
- [ ] No outcome–predictor content: every hit of `grep -inE 'correl|regress|p *[<=]|t-test|anova|chi-sq|r2|effect of' data-inventory.md` is checked by the user and is univariate or predictor-only.
- [ ] data/ untouched: `git status --porcelain papers/<slug>/data/` is empty and the checksums match.
- [ ] STATE.md has `prior_exposure:` with level, dates and what was seen; a level of `outcome-looked` or higher has set S04 to `NOT-PASSABLE` with its disclosure queued.
- [ ] `a-data-only`: the data-access log has at least one row.
- [ ] data-inventory.md starts with its derives-from header and is ≤150 lines.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is intake.md or data-inventory.md. Write the change list in plan mode and wait for user approval. Set `mode: propagate`, edit intake.md first, then data-inventory.md (re-running data-reader for any fact taken from data/), and mark every file that derives from data-inventory.md `stale:` in STATE.md. Close each item by appending a CLOSED row with its pointer, then set `mode: work`. A request to change data/ itself is refused: raw data stay as delivered, and any cleaning is done by a stage 05 script with its own analysis-log.md row.

## Evidence
- [C34] A: initial data analysis is pre-planned and does not evaluate outcome–predictor associations.
- [C4] A: question trolling (searching many relationships for notable results) gives substantial upward bias.
- [C32] A: data-exploration protocol for outliers and dependence; [C33] A: Zuur & Ieno start from design, sampling layout and dependence.
- [C23] A: preregistering analyses of pre-existing data is useful even though design and sample size are already fixed (template exists); [C24] A: analyst prior knowledge weakens such plans.
- [C25] A: log data access ("checkout") so later confirmatory claims on secondary data are credible.
- [F10] A: disclose prior knowledge of a dataset on a scale from "never worked with these data" to publications.
