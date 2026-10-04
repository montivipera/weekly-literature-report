# STATE: <slug>
Template: copy to papers/<slug>/STATE.md at stage 00. Overwritten every burst (never appended); history lives in git; keep ≤60 lines.

```yaml
slug: <slug>
title: <working title>
entry_mode: <a-data-only | b-analysis-done | c-half-draft | d-finished-manuscript | e-under-revision>
prior_exposure: <none | descriptive | outcome-looked | analysed | published>   # highest level reached before the plan tag
mode: work                # work | propagate (propagate only after the user types "propagate inbox")
current_stage: 00-intake  # stages/<NN-name>.md
live_file: intake.md      # relative to papers/<slug>/; trailing "/" = directory; several: comma-separated
plan_tag: <none | plan-<slug>-v1>
scan_commit: <none | short commit of search-log.md at the time of the plan tag>
stale: []                 # downstream files flagged by an upstream change, e.g. [methods.md]
```

## Gates
Status is one of PASSED, RETRO-AUDIT, NOT-PASSABLE, OPEN. Evidence is a file path or a commit. Only status, evidence and date change.

| gate | status | evidence | date |
|---|---|---|---|
| S00 intake | OPEN | <file or commit> | <YYYY-MM-DD> |
| S01 data-inventory | OPEN | <file or commit> | <YYYY-MM-DD> |
| S02 pre-question-scan | OPEN | <file or commit> | <YYYY-MM-DD> |
| S03 question-framing | OPEN | <file or commit> | <YYYY-MM-DD> |
| S04 method-and-plan-freeze | OPEN | <tag plan-<slug>-v1 or "no plan"> | <YYYY-MM-DD> |
| S05 analysis | OPEN | <file or commit> | <YYYY-MM-DD> |
| S06 question-map | OPEN | <file or commit> | <YYYY-MM-DD> |
| S07 methods-results | OPEN | <file or commit> | <YYYY-MM-DD> |
| S08 literature-extraction | OPEN | <file or commit> | <YYYY-MM-DD> |
| S09 citation-verification | OPEN | <file or commit> | <YYYY-MM-DD> |
| S10 discussion-critique-submission | OPEN | <file or commit> | <YYYY-MM-DD> |

## Prior exposure statement
<Who saw which outcome-level results, when and how (source: intake.md, data-access log). Write "none" only if a dated artefact shows it.>

## Disclosure queue
One line per NOT-PASSABLE gate or post hoc item; consumed at stages 07 and 10.
- <Q1> | <gate SNN> | <text the paper must state> | queued <YYYY-MM-DD>

## Decisions (last 5)
Newest first; older ones are in `git log -p STATE.md`.
- <YYYY-MM-DD> | <decision> | <why, pointer file@commit>

## Open inbox items
count: <n> · IDs: <I03, I07> (full text in inbox.md)

## Next step
<one sentence: stage, live file, first action>

## After /clear or compaction
1. Re-read this file first, before any other file or action.
2. Then read CLAUDE.md and stages/<current_stage>.md only; open other files on demand.
3. Edit only live_file, this file and inbox.md; append every other idea to inbox.md.
