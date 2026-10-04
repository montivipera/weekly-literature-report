# Analysis-to-question table (template for Part A of question-map.md)
Stage 06 pastes the Table section below into papers/<slug>/question-map.md under "## Part A: Analysis-to-question table" and fills it before writing Part B. Its sources (analysis-log.md, questions.md and the plan tag) are named in the `derives-from:` header of question-map.md.
It is a lookup, not prose: no interpretation and no rewording of results. EXAMPLE rows show the format only. They are not results; delete them at first use.

Source columns, canonical in stages/05 (analysis-log.md): `ID | date | label | plan-id or "exploratory" | script | inputs | output file | result incl. null | notes`. Part A copies ID, label, plan-id or "exploratory", script, output file and result verbatim, and adds RQ and reported where.

## Table
| ID | RQ | label | plan-id or "exploratory" | script | output file | result incl. null | reported where | notes |
|---|---|---|---|---|---|---|---|---|
| A<nn> | <RQ-id \| none> | <`confirmatory` \| `exploratory`> | <plan-<slug>-v1:P<n> \| exploratory> | scripts/<file> | results/A<nn>.md | <estimate, uncertainty, n \| null: estimate, uncertainty, n \| failed: reason> | <methods \| results \| methods+results \| none> | <D-id; reason when reported where is none> |
| EXAMPLE A02 | RQ1 | `confirmatory` | plan-marsh-v1:P1 | scripts/A02_richness-glmm.R | results/A02.md | rate ratio 1.12 (95% CI 1.03–1.22), n = 48 | methods+results | none |
| EXAMPLE A04 | none | `exploratory` | exploratory | scripts/A04_richness-gam.R | results/A04.md | failed: did not converge; no estimate | none | abandoned model; kept in analysis-log.md and listed under Part B "Not mapped" |
| EXAMPLE A06 | RQ2 | `exploratory` | exploratory | scripts/A06_calls-cover.R | results/A06.md | null: slope 0.02 (95% CI −0.10 to 0.14), n = 48 | results | D01: site random effect dropped (singular fit) |

## Copy rules
- ID, label, plan-id, script, output file and result are copied from analysis-log.md and results/A<nn>.md. They are never edited here.
- If a label is wrong, append an inbox.md line that targets analysis-log.md. A `confirmatory` row whose plan-id is not in the tagged plan blocks the gate until it is fixed upstream.
- RQ is the single question the analysis answers, or `none`. An analysis is never split across two questions; when it seems to serve two, pick one and say why in notes.
- `none` under "reported where" needs a reason in notes. The row still appears in the archived analysis log and in the disclosure "all analyses reported" statement.

## Completeness rule
One row per analysis-log row, in log order. Nulls, failed fits, abandoned models and reruns all get rows, and two log rows are never merged [C5, C19, F31].
Count check. Run gate commands from paper-workflow/ (the project root for Claude Code). EXAMPLE rows do not match the pattern, and the sed range keeps Part B rows out of the count.
```
grep -c '^| A[0-9]' papers/<slug>/analysis-log.md
sed -n '/^## Part A/,/^## Part B/p' papers/<slug>/question-map.md | grep -c '^| A[0-9]'
diff <(grep -o '^| A[0-9][0-9]*' papers/<slug>/analysis-log.md | sort -u) <(sed -n '/^## Part A/,/^## Part B/p' papers/<slug>/question-map.md | grep -o '^| A[0-9][0-9]*' | sort -u)
```
The two counts must be equal and the diff must be empty, or the stage 06 gate fails.

Outcome-independence check, for every `confirmatory` row (a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data)):
```
git tag -l 'plan-<slug>-*'
git show plan-<slug>-v1:./papers/<slug>/analysis-plan.md | grep '<plan-id>'
first=$(git log --diff-filter=A --format=%h -- papers/<slug>/results/ | tail -1)
git merge-base --is-ancestor plan-<slug>-v1 "$first" && git log -1 --format=%cs "$first"
```
The plan tag must exist, contain the plan-id, and precede the first results/ commit [C7]. In modes b–e, or in a after an outcome-level look, the data-access.md row that declares the hold-out or new data must be dated before that commit date [C25]; otherwise the row is `exploratory`.

## Orphan rules [C2, F1, F31]
- Analysis with no question: set RQ to `none`. List the row under Part B "Not mapped"; never delete it.
- Question with no analysis: it gets no row here. List it under Part B "Not mapped" with the reason, because a dropped hypothesis must be disclosed.
- Planned analysis that never ran (a plan-id with no log row): list it under Part B "Not mapped" and add an inbox line that targets deviations.md.
- Orphan claim (a result in methods.md, results.md or a draft with no log row behind it): flag it in inbox.md and list it under Part B "Orphan claims". The claim is cut unless stage 05 adds the log row.
