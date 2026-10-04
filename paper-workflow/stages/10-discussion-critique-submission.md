# Stage 10 — Discussion, critique and submission
Goal: draft Introduction, Discussion and Abstract from verified ledger rows only, put them through an adversarial critique, and complete a disclosure that matches the target journal's live AI policy.

## Entry modes
- Runs normally in every mode once stage 09 is `PASSED`. The guard hook blocks draft/ until stage 09 sets `live_file: draft/`.
- `RETRO-AUDIT` in `c-half-draft` and `d-finished-manuscript`, and for the as-submitted text in `e-under-revision`. The existing Introduction and Discussion are committed into draft/ as the dated baseline and audited rather than drafted:
  - every citation must map to a `SUPPORT-CHECKED` row;
  - hypotheses first dated after a result are relabelled post hoc;
  - orphan claims are flagged [F1, F23, F28].
- Modes b–e: the Discussion gets a transparent post hoc subsection; the paper says "not preregistered" and never uses "registered" in a way that implies equivalence; exploratory findings are worded as preliminary [F1, F4 UNVERIFIED, F16].
- `e-under-revision`: changed citations get a retraction re-check at the audit. The response letter, which is the user's file outside the chain, must use the same labels as question-map.md [F23, F29].
- `NOT-PASSABLE` when neither Claude nor the user can read the target journal's live AI policy before submission. Queue this disclosure item: "The journal AI policy could not be read on <date>; the disclosure follows COPE/ICMJE defaults" [D31, D32].

## Inputs / Live files / Outputs
- **Inputs:**
  - STATE.md, for the disclosure queue;
  - intake.md, for the target journal;
  - doi-ledger.md: `SUPPORT-CHECKED` rows and the layer syntheses only;
  - question-map.md, methods.md, results.md and templates/section-skeleton.md;
  - in modes c–e, the existing text pointed to by intake.md.
- **Live files, one at a time:** first `live_file: draft/` (intro, discussion, abstract), then `critique.md`, then `disclosure.md`. Fix rounds switch back to the file being fixed.
- **Outputs:**
  - **draft/intro.md, draft/discussion.md, draft/abstract.md:** header `derives-from: doi-ledger.md@<short-commit>`. Skeleton bullets first, each with `[ledger: Rn, Rm]`, then prose. They cite only `SUPPORT-CHECKED` rows.
  - **critique.md:** items `C1…Cn`, each with location | error | evidence | severity | `resolved: <commit>` or `logged: <reason>`.
  - **disclosure.md:**
    - target journal, policy URL, date read and the quoted policy line;
    - the AI-use statement: tools with versions, purpose, human oversight, placement;
    - every queued disclosure item;
    - the references-checked declaration [D17];
    - a pointer to data and code availability.

## Model and agent
- **agents/drafter.md:** Opus 5.5 (`claude-opus-5-5`), one section per run, md only.
  - Effort: medium for Introduction and Abstract, high for the Discussion.
- **agents/critic.md:** Opus 5.5 at effort high, run as a fresh subagent that saw none of the drafting turns. It must find errors, and its output is ≤120 lines.
  - It writes critique.md itself with the Write tool and returns a ≤10-line summary; it never edits the drafts [A24, A25].
- **Main session (Opus 5.5):** sets the live files; runs the citation-map and number checks; re-reads the policy and writes disclosure.md.
  - It may call agents/source-rechecker.md (Sonnet 5.5, ≤20k tokens) when the critic disputes a passage.
- **Escalation to Fable 5.1:** prose polish only, and only if Opus output still fails acceptance after the critique round [A5].
  - The user must first check Fable's data-retention terms: 30-day retention is reported but UNVERIFIED [A19].
  - Fable never touches numbers, labels or citations, and its use is recorded in disclosure.md.

## Procedure
1. Read STATE.md and stop unless stage 09 is `PASSED` and `live_file: draft/`, committing the existing text into draft/ first as the baseline in modes c–e.
2. The drafter writes draft/intro.md (skeleton bullets with ledger IDs, then prose), keeping each hypothesis's `origin:` tag and never presenting literature consulted after results as its a priori basis [C2].
3. The drafter, at effort high, writes draft/discussion.md per question in question-map order, nulls included, with the post hoc subsection and the "not preregistered" wording in modes b–e.
4. The drafter writes draft/abstract.md last, taking every number from results.md and keeping each finding's label.
5. The main session maps every citation ID in draft/*.md, methods.md and results.md to a `SUPPORT-CHECKED` row and sends any newly needed source to inbox.md for stages 08–09, uncited until then.
6. Set `live_file: critique.md` and run the critic as a fresh subagent on all section files, question-map.md and the ledger, where it must report errors (overclaiming, unlabelled post hoc results, number mismatches, unverified citations, missing nulls, disclosure gaps).
7. Resolve each critique item in the live file it concerns, switching live_file or going through inbox and propagate, and mark it `resolved: <commit>` or `logged: <reason>` in critique.md.
8. Set `live_file: disclosure.md`, re-read the target journal's live AI policy (WebFetch, or a copy the user pastes), record URL, date and the quoted line, and complete disclosure.md, including every queued item from STATE.md [D27–D32].
9. In mode e, re-run the stage 09 retraction check on changed citations and compare the response letter's labels with question-map.md.
10. Export the full draft for the advisors, run the gate, write STATE.md, commit, run `/rename stage-10`, then `/clear`.

## Gate (pass/fail)
- [ ] The stage 09 gate commit precedes the first draft/ commit in git log.
- [ ] Every draft/*.md has a `derives-from:` header, and every skeleton bullet carries at least one ledger ID or `[own result]`.
- [ ] The citation map finds every cited ID `SUPPORT-CHECKED`, with 0 `NOT-CITABLE`, 0 `RETRACTED` and 0 unknown IDs.
- [ ] Every number in the Abstract and Discussion matches results.md.
- [ ] critique.md comes from a fresh critic subagent, has at least one item, and every item is `resolved:` or `logged:`.
- [ ] Modes b–e: the post hoc subsection is present, and "not preregistered" is present. A grep for "registered" finds no wording that implies equivalence with preregistration.
- [ ] disclosure.md has the policy URL, read date and quoted line, and every queued disclosure item, checked by count match.
- [ ] Its AI statement names every tool actually used (Claude models, NotebookLM, Fable if used) and sits where the policy requires.
- [ ] disclosure.md has the references-checked declaration.
- [ ] Mode e: the retraction re-check of changed citations is dated, and the response letter's labels match question-map.md.
- [ ] The advisor export path and date are recorded.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count. Next: `live_file: intake.md`, because the next entry is stage 00 in `e-under-revision` when reviews arrive.

## Propagate step
This runs at this gate, or when the user types "propagate inbox".
1. Read the OPEN inbox.md items that target draft/, critique.md, disclosure.md or upstream files.
2. Set `mode: propagate` and list the changes in plan mode.
3. Get user approval.
4. Edit upstream first: results.md before the Discussion. A new or changed citation re-runs stages 08–09 for that row.
5. Mark the affected draft files `stale:`.
6. Close each item with a commit pointer, plus its critique ID if it came from the critique. Then set `mode: work`.

## Advisor touchpoint (entry 3)
- **When:** after the critique round only, so that advisors see a draft that has already been attacked.
- **Export:** `pandoc draft/abstract.md draft/intro.md methods.md results.md draft/discussion.md disclosure.md -o draft-<date>.docx`, or `.pdf`. Attach question-map.md and the list of `logged:` critique items.
- **What the advisors are asked:**
  1. Does any sentence claim more than its question-map status, such as a null worded as a trend or an exploratory result worded as a test?
  2. Is every post hoc result in the post hoc subsection and worded as preliminary?
  3. Please spot-check two or three regional, national or local citations against their ledger quotes.
  4. Are the logged, unresolved critique items acceptable?
  5. Is the AI-use statement accurate for every author's use, and is the target journal right?
- Each reply point becomes one dated inbox.md line. Nothing is edited until the propagate step.

## Evidence
- [A24] A: LLMs fail at self-evaluation, hence a separate critic.
- [A25] B: supplied records are accepted uncritically, hence a fresh context and quotes that carry their sources.
- [A5] A: start with Opus 5.5; use Fable 5.1 only when Opus at higher effort still fails.
- [A19] C UNVERIFIED: Fable 5.1 reportedly requires 30-day data retention.
- [D27–D32] A (D29 and D32 are A UNVERIFIED; all snippet-based): where publishers and standards require AI use to be disclosed.
- [F1] A: report post hoc analyses transparently in a Discussion subsection.
- [F16] A: retrospective registration cannot show that decisions were prespecified.
- [F29] A: retracted papers keep being cited; check references before submission.
