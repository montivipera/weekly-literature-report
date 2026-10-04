# Question map: <paper short title> (`<slug>`)
derives-from: analysis-to-question.md@<short-commit>, questions.md@<short-commit>, deviations.md@<short-commit>
Package version: <n> · date: <YYYY-MM-DD> · entry mode: <a-data-only | b-analysis-done | c-half-draft | d-finished-manuscript | e-under-revision>
Plan: <`plan-<slug>-v1` tagged YYYY-MM-DD | no plan> · stage 04 gate: <PASSED | NOT-PASSABLE> (<evidence pointer: commit, tag or file>)

This is the stage 06 output and the advisor package. The canonical text is this file in git, and advisors get a DOCX/PDF export of it.
Delete every EXAMPLE row before export. EXAMPLE values are illustrative only: they are not results and not checks that were run.

## Cover note to advisors
1. This package lists every analysis we ran. Each one is mapped to the single research question it answers, on one axis, and null results and analyses that answer no question are kept, not dropped.
2. Outcome independence: please check that every `confirmatory` row has a plan-id from the plan tagged on <YYYY-MM-DD>, before any outcome model ran, and tell us which rows you would relabel `exploratory`.
3. Missing analyses: for each question, please name any analysis a reviewer would expect that is not in the table or in "Not mapped".
4. Unsupported claims: please mark any Result or Status cell that says more than the linked results file, figure or table shows.
5. Please reply as comments on the export by <YYYY-MM-DD>. Each point becomes one line in inbox.md and is answered at the next gate, never by a silent edit.

## Single-axis table
Questions follow questions.md order, and analyses within a question follow analysis-log.md order. Each analysis gets its own line, so a question with two analyses has two lines.

| Question | Hypothesis + origin tag | Analysis ID + label | Result (incl. null) | Deviation ref | Figure/table | Status |
|---|---|---|---|---|---|---|
| <Q-id>: <question, one sentence> | <H-id>: <expected direction> · `origin: <literature \| data \| advisor>` <[ledger: <R-ids>] if literature> | <A-id> · <`confirmatory` <plan-id> \| `exploratory`> | <estimate, uncertainty, n> or <null: estimate, uncertainty, n> | <DV-id \| none> | <Fig. n \| Table n> · results/<file>.md | <consistent \| inconsistent \| inconclusive \| not-run> |
| EXAMPLE Q1: Does hydroperiod length predict odonate species richness across ponds? | H1: longer hydroperiod, higher richness · `origin: literature` [ledger: R03, R07] | A02 · `confirmatory` plan-marsh-v1:P1 | rate ratio 1.12 per extra month (95% CI 1.03–1.22), n = 48 ponds, 3 years | none | Fig. 2 · results/A02-richness-glmm.md | consistent |
| EXAMPLE Q2: Is emergent-vegetation cover associated with anuran calling activity? | H2: positive association · `origin: data` (first seen in A05 plots) | A06 · `exploratory` | null: slope 0.02 (95% CI −0.10 to 0.14), n = 48 ponds | DV1 (site random effect dropped: singular fit) | Table S3 · results/A06-calls-cover.md | inconclusive |

## Not mapped
These rows are kept on purpose. If a subsection is empty, write "none"; never leave it out.

### Analyses with no question
| Analysis ID + label | What it estimated | Result (incl. null) | Why no question | Reported where |
|---|---|---|---|---|
| <A-id> · `exploratory` | <one line> | <estimate, uncertainty, n \| null \| failed: reason> | <abandoned model \| diagnostic \| side question \| advisor request> | <methods \| results \| none: reason> |

### Questions with no analysis
Dropping a hypothesis without saying so is a form of HARKing, so a question that lost its analysis is listed here and named in the Discussion.
| Question | Hypothesis + origin tag | Why no analysis | What happens next |
|---|---|---|---|
| <Q-id>: <question> | <H-id> · `origin: <literature \| data \| advisor>` | <data cannot answer it \| dropped after <A-id> \| not yet run> | <disclose as dropped \| run as `exploratory` \| future work> |

## Changes since last advisor review
Last review: <YYYY-MM-DD>, package version <n-1>, by <advisor names>. Write "first package" if there was no earlier review.
| Date | Row(s) | What changed | Why | Source |
|---|---|---|---|---|
| <YYYY-MM-DD> | <Q-id / A-id> | <new row \| label changed \| result changed \| moved to Not mapped> | <one line> | <inbox ID \| advisor comment \| DV-id> |

## Before export (stage 06 gate)
- [ ] The table plus "Analyses with no question" has the same number of A-ids as analysis-log.md; run the count check in templates/analysis-to-question.md.
- [ ] Every `confirmatory` row has a plan-id from the tag above, and every other row is `exploratory`.
- [ ] Every null result appears in the same form as a positive one: estimate, uncertainty and n.
- [ ] Every result cell matches its results/*.md file. Cells are copied, not reworded.

## Legend
- Label: a row is `confirmatory` only with a plan-id from tag `plan-<slug>-v1` dated before any outcome model ran, or when it uses new or never-explored hold-out data. Every other row is `exploratory` (the default).
- Origin tag: `origin: literature | data | advisor`. Entry mode: `a-data-only`, `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`. Gate status: `PASSED`, `RETRO-AUDIT`, `NOT-PASSABLE`, `OPEN`.
- Status (measured against the stated hypothesis): `consistent`, `inconsistent`, `inconclusive`, `not-run`. For an `exploratory` row, the status describes the data and is never evidence for the hypothesis. A deviation ref is a DV row in deviations.md, or `none`.
