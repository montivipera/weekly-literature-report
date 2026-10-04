# Stage 04 — Method justification and plan freeze
Goal: justify every candidate model against a named protocol, then freeze a structured analysis plan with a git tag before any outcome model runs.

## Entry modes
- `a-data-only`: normal, provided the prior-exposure level in STATE.md is below `outcome-looked`. Design and sample size were fixed before the plan and are `NOT-PASSABLE` (the freeze covers analysis only): queue "collection and freeze dates; any prior looks; when the inclusion rules were fixed". If an outcome-level look already happened, treat the stage as in modes b–e.
- `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`: S04 is `NOT-PASSABLE`, because a plan written after outcomes cannot show that decisions were prespecified [F16]. Queue the disclosure items "no plan; not preregistered; every analysis exploratory; every analysis reported in order; post hoc subsection; robustness section" [F1, F31]. The paper never uses "registered" in a way that implies equivalence. Exception: in `d-finished-manuscript` a dated prior plan found at intake gives `PASSED` with that artefact as evidence.
- What still runs in modes b–e (recorded as audit, not freeze): steps 1–3 audit the as-run methods against the protocols, and step 4 writes the robustness rule (multiverse or specification curve, second analyst from raw data, sensitivity checks, hold-out) into analysis-plan.md, tagged before any robustness run.
- Confirmatory rule (every mode): a plan-id may be labelled `confirmatory` only with a plan-id from a pre-outcome tag AND (mode a with no outcome-level look, or a declared, never-explored hold-out / new data). Declared = a data-access.md row naming the dataset, committed at stage 00 or 01 before any analysis in this workflow, with no `outcome-level? yes` row for it since. Every other plan-id is `exploratory` [F10–F12, F35].

## Inputs · Live file(s) · Outputs
- **Inputs:** questions.md, data-inventory.md, scan-notes.md (key rows), data-access.md, `prior_exposure:` and `scan_commit:` in STATE.md. Markdown only.
- **Live files:** `method-rationale.md, critique.md` (steps 1–3), then `analysis-plan.md` (steps 4–9). Before the tag every write to analysis-plan.md prompts the user (`ask` rule); after the tag guard.sh denies it, because CLAUDE.md text alone is not enforced [B23].
- **Outputs:**
  - `method-rationale.md` (≤150 lines + advisor section): header `derives-from: questions.md@<c>, data-inventory.md@<c>`; per RQ: candidate models and why (structure, dependence, response distribution); assumptions and how each is checked; candidate set and selection rule; sensitivity checks; the protocol cited for each choice (Zuur & Ieno 2016 [C33], Zuur et al. 2010 [C32], Bolker et al. 2009 [C35], Harrison et al. 2018 [C36]). Then `## Advisor` (comments → inbox IDs).
  - `critique.md`: `## Stage 04`, written by the critic (it creates the file with line 1 `derives-from: method-rationale.md@<c>`); one row per finding, whose status the main session sets to `resolved: <commit>` or `logged: <reason>`. Stage 10 appends `## Stage 10`.
  - `analysis-plan.md`: header `derives-from: questions.md@<c>, method-rationale.md@<c>`; eight sections:
    1. data status: dataset pre-existed; prior-exposure statement copied verbatim from STATE.md; data-access.md pointer (commit) and every declared hold-out or new dataset;
    2. hypotheses `H# | RQ-ID | statement and direction | origin: literature|data|advisor`;
    3. variables: responses, predictors, random effects, units, transformations;
    4. exclusions and data-handling rules;
    5. planned analyses `plan-id (plan-<slug>-v1:P#) | H# | label (confirmatory|exploratory, by the rule above) | dataset | model | candidate set + selection rule | decision rule incl. how a null is reported`;
    6. sensitivity and robustness rule [C37];
    7. deviation policy: every change after the tag = one deviations.md row with reason and effect on the label [C27];
    8. everything not listed above is `exploratory`.

## Model and agent
- `agents/methods-advisor.md` (claude-opus-5-5, effort high; reads md only ≤50k tokens; output ≤150 lines): writes method-rationale.md directly with the Write tool and returns only its ≤10-line message.
- `agents/critic.md` (claude-opus-5-5, effort high, fresh context; output ≤120 lines): must find errors in the committed method-rationale.md; writes `## Stage 04` in critique.md and never edits the rationale.
- `agents/analyst.md` (claude-sonnet-5-5, effort medium) in template-fill mode, allowed only while no `plan-<slug>-*` tag exists: fills analysis-plan.md from questions.md and method-rationale.md and adds nothing new (judgement call, no direct evidence).
- Main session (Opus 5.5, effort medium): commits the rationale before the critic runs, records dispositions with the user, checks the plan, prepares the advisor export. It never reads data/. Claude commits working files; only the user creates the tag.

## Procedure
1. Set `live_file: method-rationale.md, critique.md`; methods-advisor reads questions.md and data-inventory.md and writes the per-RQ rationale to method-rationale.md.
2. Main session commits method-rationale.md (`rationale: <slug>`); then the critic, in a fresh context, attacks that commit and writes `## Stage 04` in critique.md.
3. With the user, main session sets each finding's status (`resolved: <commit>` after fixing the rationale, or `logged: <reason>`) and commits both files; a model-written justification is not trusted without this pass [A20, A25].
4. Set `live_file: analysis-plan.md`; analyst fills the eight sections from questions.md and method-rationale.md, including the robustness rule (section 6) and a label per plan-id by the confirmatory rule.
5. Main session checks that every chosen RQ maps to at least one H# and one plan-id, that the prior-exposure statement matches STATE.md word for word, and that every `confirmatory` plan-id outside `a-data-only` names a declared dataset.
6. Commit analysis-plan.md and export both files for the advisor (touchpoint below); advisor comments become inbox.md items, applied through the propagate step before the tag.
7. The advisor's sign-off (name, date, commit of the exported files) is written into the S04 evidence pointer in STATE.md.
8. Confirm that no outcome model has run (`a-data-only`: results/ absent or empty, no analysis-log.md; modes b–e: no robustness or hold-out run yet).
9. The user runs `git tag -a plan-<slug>-v1 -m "plan freeze"` on the commit that holds both files; Claude never creates or moves the tag.
10. After the tag, any change to the plan is a deviations.md row at stage 05; set `live_file: scripts/, results/, analysis-log.md, deviations.md` for stage 05.

## Gate (pass/fail)
Run gate commands from paper-workflow/ (the project root for Claude Code).
- [ ] method-rationale.md covers every chosen RQ with candidate models and reasons, assumptions and their checks, candidate set and selection rule, sensitivity checks, and a named protocol per choice.
- [ ] critique.md has `## Stage 04` from a fresh critic run; its `derives-from: method-rationale.md@<c>` names a commit (`git cat-file -e <c>` succeeds); it lists at least one finding, each `resolved: <commit>` or `logged: <reason>`.
- [ ] analysis-plan.md has all eight sections; every hypothesis has an origin tag; every plan-id maps to an H# and an RQ-ID and carries a label.
- [ ] Advisor sign-off (name, date, export commit) is recorded in STATE.md.
- [ ] `git tag -l 'plan-<slug>-v1'` returns the tag, and `git cat-file -t plan-<slug>-v1` returns `tag` (annotated, so it carries a date).
- [ ] The scan predates the tag: `git merge-base --is-ancestor <scan_commit> plan-<slug>-v1` succeeds.
- [ ] `a-data-only`: no result predates the tag: `git log --oneline plan-<slug>-v1 -- papers/<slug>/results/` is empty, and no file in results/ is older than the tag date (`git for-each-ref --format='%(taggerdate:iso)' refs/tags/plan-<slug>-v1`). Any hit fails the gate.
- [ ] Hold-out (modes b–e, or `a-data-only` after an outcome-level look): each `confirmatory` plan-id names a dataset declared in data-access.md, and the declaring commit (`git log --reverse --format=%h -S '<dataset path>' -- papers/<slug>/data-access.md | head -1`) is an ancestor of the first results/ commit (`git log --reverse --format=%h -- papers/<slug>/results/ | head -1`; none yet also passes). Otherwise every plan-id is `exploratory`.
- [ ] The guard works: one test Edit on analysis-plan.md after the tag is denied by guard.sh.
- [ ] Modes b–e (and `a-data-only` after an outcome-level look): S04 is `NOT-PASSABLE` with its disclosure items queued, and no robustness result predates the tag.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is method-rationale.md, analysis-plan.md or an upstream file. Write the change list in plan mode and wait for user approval. Before the tag: set `mode: propagate`, edit upstream files first (questions.md, then method-rationale.md, then analysis-plan.md) and mark downstream files `stale:` in STATE.md. After the tag: no edit to analysis-plan.md is possible or proposed; each item becomes a deviations.md row at stage 05 instead. Close each item by appending its row with status `CLOSED -> <file>@<commit>`, then set `mode: work`.

## Advisor touchpoint (entry 1 of 3; the only outcome-independent one [C31])
- Export, from papers/<slug>/: `pandoc method-rationale.md analysis-plan.md -o <slug>-plan-review.docx` (or `.pdf`), saved outside the repo and not committed; note the commit it was built from.
- Ask exactly: "Is any analysis missing, mis-specified, or already influenced by outcomes?"
- No sign-off, no tag: the gate stays `OPEN` until sign-off is recorded. The recommendation to involve an advisor or statistician is a judgement call, not a retrieved requirement [C37].

## Evidence
- [C7] A: only analyses specified before seeing the data count as confirmatory.
- [F10] A: disclose prior knowledge of a dataset; use hold-out subsamples. [F11] A: a data checkout log shows plans predate access. [F12] A: Explore-and-Confirm on secondary data. [F35] A: a fresh dataset resolves the conflict between local evidence and global error rates.
- [C23] A: preregistering analyses of pre-existing data is useful, and a template exists.
- [C27] A: deviations from a plan are reported transparently and justified.
- [C33] A, [C35] A, [C36] A: named protocols (Zuur & Ieno 10 steps; Bolker GLMMs; Harrison mixed-model best practice, where multimodel inference is hard without training).
- [C37] A: report multiple models, preprocessing sensitivity, multiple analysts; multiverse analysis.
- [F16] A: retrospective registration cannot show decisions were prespecified.
- [A20] B: agents miss subtle details and are weak on scientific judgement; [A25] B: supplied records are accepted uncritically (hence a fresh critic and the disposition pass).
- [B23] A: CLAUDE.md is context, not enforced configuration; blocking needs a PreToolUse hook.
