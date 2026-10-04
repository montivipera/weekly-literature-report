# Question map: <paper short title> (`<slug>`)
derives-from: analysis-log.md@<short-commit>, questions.md@<short-commit>
analysis-log rows: <N> | part A rows: <N>
Package version: <n> · date: <YYYY-MM-DD> · entry mode: <a-data-only | b-analysis-done | c-half-draft | d-finished-manuscript | e-under-revision>
Plan: <`plan-<slug>-v1` tagged YYYY-MM-DD | no plan> · stage 04 gate: <PASSED | NOT-PASSABLE> (<evidence pointer: commit, tag or file>)

This is the stage 06 output. Part A is the mechanical table and is built first; Part B is the advisor package and derives from Part A. The canonical text is this file in git, and advisors get a DOCX/PDF export of Part B; Part A goes in as an appendix.
IDs: `RQ<n>` research questions (questions.md), `H<n>` hypotheses, `A<nn>` analysis-log rows (result file results/A<nn>.md), `D<nn>` deviations, `I<nn>` inbox items. Delete every EXAMPLE row before export. EXAMPLE values are illustrative only: they are not results and not checks that were run.

## Part A: Analysis-to-question table
<Paste the Table section of templates/analysis-to-question.md here and fill one row per analysis-log row. Its copy, completeness and orphan rules apply.>

## Part B: Advisor package

### Cover note to advisors
1. This package lists every analysis we ran. Each one is mapped to the single research question it answers, on one axis, and null results and analyses that answer no question are kept, not dropped.
2. Outcome independence: please check that every `confirmatory` row has a plan-id from the plan tagged on <YYYY-MM-DD>, before any outcome model ran, and uses data with no outcome-level look before the plan or a declared, never-explored hold-out or new data. Tell us which rows you would relabel `exploratory`.
3. Missing analyses: for each question, please name any analysis a reviewer would expect that is not in the table or in "Not mapped".
4. Unsupported claims: please mark any Result or Status cell that says more than the linked results file, figure or table shows.
5. Please reply as comments on the export by <YYYY-MM-DD>. Each point becomes one line in inbox.md and is answered at the next gate, never by a silent edit.

### Single-axis table
Questions follow questions.md order, and analyses within a question follow analysis-log.md order [C12, F31]. Each analysis gets its own line, so a question with two analyses has two lines.

| Question | Hypothesis + origin tag | Analysis ID + label | Result (incl. null) | Deviation ref | Figure/table | Status |
|---|---|---|---|---|---|---|
| <RQ-id>: <question, one sentence> | <H-id>: <expected direction> · `origin: <literature \| data \| advisor>` <basis: <R-ids in scan-notes.md> if literature> | <A-id> · <`confirmatory` <plan-id> \| `exploratory`> | <estimate, uncertainty, n> or <null: estimate, uncertainty, n> | <D-id \| none> | <Fig. n \| Table n> · results/<A-id>.md | <consistent \| inconsistent \| inconclusive \| not-run> |
| EXAMPLE RQ1: Does hydroperiod length predict odonate species richness across ponds? | H1: longer hydroperiod, higher richness · `origin: literature` basis: R03, R07 | A02 · `confirmatory` plan-marsh-v1:P1 | rate ratio 1.12 per extra month (95% CI 1.03–1.22), n = 48 ponds, 3 years | none | Fig. 2 · results/A02.md | consistent |
| EXAMPLE RQ2: Is emergent-vegetation cover associated with anuran calling activity? | H2: positive association · `origin: data` (first seen in A05 plots) | A06 · `exploratory` | null: slope 0.02 (95% CI −0.10 to 0.14), n = 48 ponds | D01 (site random effect dropped: singular fit) | Table S3 · results/A06.md | inconclusive |

### Not mapped
These rows are kept on purpose. If a subsection is empty, write "none"; never leave it out.

#### Analyses with no question
| Analysis ID + label | What it estimated | Result (incl. null) | Why no question | Reported where |
|---|---|---|---|---|
| <A-id> · `exploratory` | <one line> | <estimate, uncertainty, n \| null \| failed: reason> | <abandoned model \| diagnostic \| side question \| advisor request> | <methods \| results \| none: reason> |

#### Questions with no analysis
Dropping a hypothesis without saying so is a form of HARKing [C2], so a question that lost its analysis is listed here and named in the Discussion.
| Question | Hypothesis + origin tag | Why no analysis | What happens next |
|---|---|---|---|
| <RQ-id>: <question> | <H-id> · `origin: <literature \| data \| advisor>` | <data cannot answer it \| dropped after <A-id> \| not yet run> | <disclose as dropped \| run as `exploratory` \| future work> |

#### Orphan claims (modes b–e)
| Claim (as worded) | Where (file, section) | Why no log row | Action |
|---|---|---|---|
| <one sentence> | <draft file, section> | <script lost \| never run \| number from another paper> | <inbox I-id: add log row at stage 05 \| cut> |

### Changes since last advisor review
Last review: <YYYY-MM-DD>, package version <n-1>, by <advisor names>. Write "first package" if there was no earlier review.
| Date | Row(s) | What changed | Why | Source |
|---|---|---|---|---|
| <YYYY-MM-DD> | <RQ-id / A-id> | <new row \| label changed \| result changed \| moved to Not mapped> | <one line> | <I-id \| advisor comment \| D-id> |

### Before export (stage 06 gate)
- [ ] Part A has exactly one row per analysis-log row (run the count check in templates/analysis-to-question.md), and every Part A row appears in Part B, either in the single-axis table or under "Analyses with no question".
- [ ] Every `confirmatory` row meets the label rule in the Legend, and every other row is `exploratory`.
- [ ] Every null result appears in the same form as a positive one: estimate, uncertainty and n.
- [ ] Every result cell matches its results/A<nn>.md file. Cells are copied, not reworded.

### Legend
- Label: a row is `confirmatory` only with a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data). The hold-out or new data must be declared in data-access.md at stage 00/01, before any analysis in this workflow. Every other row is `exploratory` (the default).
- Origin tag: `origin: literature | data | advisor`. Entry mode: `a-data-only`, `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`. Gate status: `PASSED`, `RETRO-AUDIT`, `NOT-PASSABLE`, `OPEN`.
- Status (measured against the stated hypothesis): `consistent`, `inconsistent`, `inconclusive`, `not-run`. For an `exploratory` row, the status describes the data and is never evidence for the hypothesis. A deviation ref is a `D<nn>` row in deviations.md, or `none`.
- `basis:` names stage 02 R rows as pointers only; it is not a citation. Drafts cite CL rows (`[ledger: CL<nn>]`) from stage 10 on.
