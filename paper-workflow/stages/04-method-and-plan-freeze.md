# Stage 04 — Method justification and plan freeze
Goal: justify every candidate model against a named protocol, then freeze a structured analysis plan with a git tag before any outcome model runs.

## Entry modes
- `a-data-only`: normal, provided the prior-exposure level in STATE.md is below `outcome-looked`. Design and sample size were fixed before the plan and are `NOT-PASSABLE` (the freeze covers analysis only): queue "collection and freeze dates; any prior looks; when the inclusion rules were fixed". If an outcome-level look already happened, treat the stage as in modes b–e.
- `b-analysis-done`, `c-half-draft`, `d-finished-manuscript`, `e-under-revision`: S04 is `NOT-PASSABLE`, because a plan written after outcomes cannot show that decisions were prespecified [F16]. Queue the disclosure items "no plan; not preregistered; every analysis exploratory; every analysis reported in order; post hoc subsection; robustness section" [F1, F31]. The paper never uses "registered" in a way that implies equivalence. Exception: in `d-finished-manuscript` a dated prior plan found at intake gives `PASSED` with that artefact as evidence.
- What still runs in modes b–e (recorded as audit, not freeze): steps 1–2 audit the as-run methods against the protocols, and step 5 writes the robustness rule (multiverse or specification curve, second analyst from raw data, sensitivity checks, hold-out) into analysis-plan.md, tagged before any robustness run. `confirmatory` is allowed only for analyses on new data or on a hold-out the data-access log shows was never explored [F10–F12, F35].

## Inputs · Live file(s) · Outputs
- **Inputs:** questions.md, data-inventory.md, scan-notes.md (key rows), `prior_exposure:` and `scan_commit:` in STATE.md. Markdown only.
- **Live files:** `method-rationale.md` (steps 1–3), then `analysis-plan.md` (steps 4–9). Before the tag every write to analysis-plan.md prompts the user (`ask` rule); after the tag guard.sh denies it, because CLAUDE.md text alone is not enforced [B20].
- **Outputs:**
  - `method-rationale.md` (≤150 lines + critic section): header `derives-from: questions.md@<c>, data-inventory.md@<c>`; per RQ: candidate models and why (structure, dependence, response distribution); assumptions and how each is checked; candidate set and selection rule; sensitivity checks; the protocol cited for each choice (Zuur & Ieno 2016 [C33], Zuur et al. 2010 [C32], Bolker et al. 2009 [C35], Harrison et al. 2018 [C36]). Then `## Critic` (finding | disposition: fixed or rejected + reason) and `## Advisor` (comments → inbox IDs).
  - `analysis-plan.md`: header `derives-from: questions.md@<c>, method-rationale.md@<c>`; eight sections:
    1. data status: dataset pre-existed; prior-exposure statement copied verbatim from STATE.md; data-access log pointer;
    2. hypotheses `H# | RQ-ID | statement and direction | origin: literature|data|advisor`;
    3. variables: responses, predictors, random effects, units, transformations;
    4. exclusions and data-handling rules;
    5. planned analyses `plan-id (plan-<slug>-v1:P#) | H# | model | candidate set + selection rule | decision rule incl. how a null is reported`;
    6. sensitivity and robustness rule [C37];
    7. deviation policy: every change after the tag = one deviations.md row with reason and effect on the label [C27];
    8. everything not listed above is `exploratory`.

## Model and agent
- `agents/methods-advisor.md` (claude-opus-5-5, effort high; reads md only ≤50k tokens; output ≤150 lines): writes method-rationale.md directly with the Write tool and returns a ≤10-line summary.
- `agents/critic.md` (claude-opus-5-5, effort high, fresh context; output ≤120 lines): must find errors in method-rationale.md; it never edits.
- `agents/analyst.md` (claude-sonnet-5-5) in template-fill mode, with the task message setting effort low: fills analysis-plan.md from questions.md and method-rationale.md and adds nothing new (judgement call, no direct evidence).
- Main session (Opus 5.5, effort medium): records critic dispositions with the user, checks the plan, prepares the advisor export. It never reads data/. The user, not Claude, commits and tags.

## Procedure
1. Set `live_file: method-rationale.md`; methods-advisor reads questions.md and data-inventory.md and writes the per-RQ rationale to method-rationale.md.
2. critic attacks method-rationale.md in a fresh context, and the main session writes each finding with a user-approved disposition under `## Critic`.
3. Main session fixes the rationale for every finding marked `fixed`; a model-written justification is not trusted without this pass [A20, A25].
4. Main session sets `live_file: analysis-plan.md`, and analyst fills the plan template from questions.md and method-rationale.md.
5. Main session checks that every chosen RQ maps to at least one H# and one plan-id, and that the prior-exposure statement matches STATE.md word for word.
6. Commit both files and export them for the advisor (touchpoint below); advisor comments become inbox.md items, applied through the propagate step before the tag.
7. The advisor's sign-off (name, date, commit of the exported files) is written into the S04 evidence pointer in STATE.md.
8. Confirm that no outcome model has run (`a-data-only`: results/ absent or empty, no analysis-log.md; modes b–e: no robustness run yet).
9. The user commits both files and runs `git tag -a plan-<slug>-v1 -m "plan freeze"`; Claude never creates or moves the tag.
10. After the tag, any change to the plan is a deviations.md row at stage 05; set `live_file: scripts/` for stage 05.

## Gate (pass/fail)
- [ ] method-rationale.md covers every chosen RQ with candidate models and reasons, assumptions and their checks, candidate set and selection rule, sensitivity checks, and a named protocol per choice.
- [ ] `## Critic` lists at least one finding, each with a disposition.
- [ ] analysis-plan.md has all eight sections; every hypothesis has an origin tag; every plan-id maps to an H# and an RQ-ID.
- [ ] Advisor sign-off (name, date, export commit) is recorded in STATE.md.
- [ ] `git tag -l 'plan-<slug>-v1'` returns the tag, and `git cat-file -t plan-<slug>-v1` returns `tag` (annotated, so it carries a date).
- [ ] The scan predates the tag: `git merge-base --is-ancestor <scan_commit> plan-<slug>-v1` succeeds.
- [ ] `a-data-only`: no result predates the tag: `git log --oneline plan-<slug>-v1 -- papers/<slug>/results/` is empty, and no file in results/ is older than the tag date (`git for-each-ref --format='%(taggerdate:iso)' refs/tags/plan-<slug>-v1`). Any hit fails the gate.
- [ ] The guard works: one test Edit on analysis-plan.md after the tag is denied by guard.sh.
- [ ] Modes b–e (and `a-data-only` after an outcome-level look): S04 is `NOT-PASSABLE` with its disclosure items queued, and no robustness result predates the tag.
- [ ] STATE.md updated: gate status, live_file for next stage, stale flags, open inbox count.

## Propagate step
On the phrase "propagate inbox", or at this gate, read the OPEN inbox.md items whose target is method-rationale.md, analysis-plan.md or an upstream file. Write the change list in plan mode and wait for user approval. Before the tag: set `mode: propagate`, edit upstream files first (questions.md, then method-rationale.md, then analysis-plan.md) and mark downstream files `stale:` in STATE.md. After the tag: no edit to analysis-plan.md is possible or proposed; each item becomes a deviations.md row at stage 05 instead. Close each item by appending a CLOSED row with its pointer, then set `mode: work`.

## Advisor touchpoint (entry 1 of 3; the only outcome-independent one [C31])
- Export: `pandoc method-rationale.md analysis-plan.md -o <slug>-plan-review.docx` (or `.pdf`), saved outside the repo and not committed; note the commit it was built from.
- Ask exactly: "Is any analysis missing, mis-specified, or already influenced by outcomes?"
- No sign-off, no tag: the gate stays `OPEN` until sign-off is recorded. The recommendation to involve an advisor or statistician is a judgement call, not a retrieved requirement [C37].

## Evidence
- [C7] A: only analyses specified before seeing the data count as confirmatory.
- [C23] A: preregistering analyses of pre-existing data is useful, and a template exists.
- [C27] A: deviations from a plan are reported transparently and justified.
- [C33] A, [C35] A, [C36] A: named protocols (Zuur & Ieno 10 steps; Bolker GLMMs; Harrison mixed-model best practice, where multimodel inference is hard without training).
- [C37] A: report multiple models, preprocessing sensitivity, multiple analysts; multiverse analysis.
- [F16] A: retrospective registration cannot show decisions were prespecified.
