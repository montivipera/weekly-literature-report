# STATE: <slug>
Template: copy to papers/<slug>/STATE.md at stage 00. Overwritten every burst (never appended); history lives in git; keep ≤60 lines.

```yaml
slug: <slug>
title: <working title>
entry_mode: <a-data-only | b-analysis-done | c-half-draft | d-finished-manuscript | e-under-revision>
prior_exposure: <none | descriptive | outcome-looked | analysed | published>   # highest level reached before the plan tag
mode: work                # work | propagate (propagate only after the user types "propagate inbox")
current_stage: 00-intake  # stages/<NN-name>.md
live_file: intake.md      # relative to papers/<slug>/; trailing "/" = directory; several: comma-separated; switch only where the stage file says
plan_tag: <none | plan-<slug>-v1>
baseline_tag: <none | submitted-<slug>-v<n>>   # mode e only
scan_commit: <none | short commit of search-log.md at the time of the plan tag>
holdout: <none | name of the hold-out or new data, declared in data-access.md on YYYY-MM-DD>
stale: []                 # downstream files flagged by an upstream change, e.g. [methods.md]
```

## Gates
Status is one of PASSED, RETRO-AUDIT, NOT-PASSABLE, OPEN; variant (normal|retro) says which checklist variant ran. Evidence is a file path or a commit. Only status, variant, evidence and date change. The user reviews `git diff papers/<slug>/STATE.md` at every gate.

| gate | status | variant | evidence | date |
|---|---|---|---|---|
| S00 intake | OPEN | normal | <file or commit> | <YYYY-MM-DD> |
| S01 data-inventory | OPEN | <normal or retro> | <file or commit> | <YYYY-MM-DD> |
| S02 pre-question-scan | OPEN | <normal or retro> | <file or commit> | <YYYY-MM-DD> |
| S03 question-framing | OPEN | <normal or retro> | <file or commit> | <YYYY-MM-DD> |
| S04 method-and-plan-freeze | OPEN | normal | <tag plan-<slug>-v1 or "no plan"> | <YYYY-MM-DD> |
| S05 analysis | OPEN | <normal or retro> | <file or commit> | <YYYY-MM-DD> |
| S06 question-map | OPEN | <normal or retro> | <file or commit> | <YYYY-MM-DD> |
| S07 methods-results | OPEN | <normal or retro> | <file or commit> | <YYYY-MM-DD> |
| S08 literature-extraction | OPEN | <normal or retro> | <file or commit> | <YYYY-MM-DD> |
| S09 citation-verification | OPEN | normal | <file or commit> | <YYYY-MM-DD> |
| S10 discussion-critique-submission | OPEN | <normal or retro> | <file or commit> | <YYYY-MM-DD> |

## Prior exposure statement
<Who saw which outcome-level results, when and how (source: intake.md, data-access.md). Write "none" only if a dated artefact shows it.>
Data access: every look at or run on the data is a row in data-access.md (append-only, always writable).

## Disclosure queue
One line per NOT-PASSABLE gate or post hoc item: ID (queuing stage + number, e.g. S04.1) and ≤6 words. The full text lives in disclosure.md under the same ID; consumed at stages 07 and 10.
- <S04.1> | <≤6 words> | queued <YYYY-MM-DD>

## Decisions (last 5)
Newest first; older ones are in `git log -p papers/<slug>/STATE.md`.
- <YYYY-MM-DD> | <decision> | <why, pointer file@commit>

## Open inbox items
count: <n> · IDs: <I03, I07> (full text in inbox.md)

## Next step
<one sentence: stage, live file, first action>

## After /clear or compaction
1. Re-read this file first (the SessionStart hook prints it), before any other file or action.
2. Then read CLAUDE.md and stages/<current_stage>.md only; open other files on demand.
3. Edit only live_file, this file, inbox.md and data-access.md; append every other idea to inbox.md.
