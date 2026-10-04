# Analysis-to-question table (template for Part A of question-map.md)
Stage 06 pastes the Table section below into papers/<slug>/question-map.md under "## Part A: Analysis-to-question table" and fills it before writing Part B. Its sources (analysis-log.md, questions.md and the plan tag) are named in the `derives-from:` header of question-map.md.
It is a lookup, not prose: no interpretation and no rewording of results. EXAMPLE rows show the format only. They are not results; delete them at first use.

## Table
| Log row | Question | Label | Plan-id | Script | Result (incl. null) | Reported where | Notes |
|---|---|---|---|---|---|---|---|
| A<nn> | <Q-id \| none> | <`confirmatory` \| `exploratory`> | <plan-<slug>-v1:P<n> \| none> | scripts/<file> | <estimate, uncertainty, n \| null: estimate, uncertainty, n \| failed: reason> | <methods \| results \| methods+results \| none> | <DV-id; reason when reported where is none> |
| EXAMPLE A02 | Q1 | `confirmatory` | plan-marsh-v1:P1 | scripts/a02-richness-glmm.R | rate ratio 1.12 (95% CI 1.03–1.22), n = 48 | methods+results | none |
| EXAMPLE A04 | none | `exploratory` | none | scripts/a04-richness-gam.R | failed: did not converge; no estimate | none | abandoned model; kept in analysis-log.md and listed under Part B "Not mapped" |
| EXAMPLE A06 | Q2 | `exploratory` | none | scripts/a06-calls-cover.R | null: slope 0.02 (95% CI −0.10 to 0.14), n = 48 | results | DV1: site random effect dropped (singular fit) |

## Copy rules
- Log row, label, plan-id, script and result are copied from analysis-log.md and results/*.md. They are never edited here.
- If a label is wrong, append an inbox.md line that targets analysis-log.md. A `confirmatory` row whose plan-id is not in the tagged plan blocks the gate until it is fixed upstream.
- Question is the single Q-id the analysis answers, or `none`. An analysis is never split across two questions; when it seems to serve two, pick one and say why in Notes.
- `none` under "Reported where" needs a reason in Notes. The row still appears in the archived analysis log and in the disclosure "all analyses reported" statement.

## Completeness rule
One row per analysis-log row, in log order. Nulls, failed fits, abandoned models and reruns all get rows, and two log rows are never merged [C5, C19, F31].
Count check, run in papers/<slug>/. It assumes row IDs are `A` followed by digits; adapt the pattern if yours differ. EXAMPLE rows do not match it, and the sed range keeps Part B rows out of the count.
```
grep -c '^| A[0-9]' analysis-log.md
sed -n '/^## Part A/,/^## Part B/p' question-map.md | grep -c '^| A[0-9]'
diff <(grep -o '^| A[0-9][0-9]*' analysis-log.md | sort -u) <(sed -n '/^## Part A/,/^## Part B/p' question-map.md | grep -o '^| A[0-9][0-9]*' | sort -u)
```
The two counts must be equal and the diff must be empty, or the stage 06 gate fails.

Outcome-independence check, for every `confirmatory` row:
```
git tag -l 'plan-<slug>-*'
git log -1 --format=%cs plan-<slug>-v1
```
The plan tag must exist, and its date must be earlier than the date of the first outcome-model row in analysis-log.md [C7, C25].

## Orphan rules [C2, F1, F31]
- Analysis with no question: set Question to `none`. List the row under Part B "Not mapped"; never delete it.
- Question with no analysis: it gets no row here. List it under Part B "Not mapped" with the reason, because a dropped hypothesis must be disclosed.
- Planned analysis that never ran (a plan-id with no log row): list it under Part B "Not mapped" and add an inbox line that targets deviations.md.
- Orphan claim (a result in methods.md, results.md or a draft with no log row behind it): flag it in inbox.md. The claim is cut unless stage 05 adds the log row.
