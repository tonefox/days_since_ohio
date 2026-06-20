# Skill Contract

Every specialist skill in `skills/*` conforms to this contract. It is the reusable interface that keeps skills independent, composable, and operable by one person with AI assistance.

---

## Required sections (every skill file)

1. **Primary mandate** — one sentence. One job. If a skill needs two mandates, split it.
2. **Required inputs** — what must exist before the skill runs (files, briefs, prior outputs).
3. **Required outputs** — the concrete artifact(s) produced, in a named template where one exists.
4. **Explicit boundaries** — what this skill does **not** do (prevents overlap and scope creep).
5. **Handoff rules** — upstream source(s) and downstream consumer(s); what is passed and in what form.
6. **Evidence requirements** — minimum evidence tier per `contracts/EVIDENCE_STANDARD.md`; required truth labels.
7. **State / ledger write permissions** — exactly which files this skill may append to or update.
8. **Stop / escalate conditions** — when the skill must halt, ask Tony, or hand back to the orchestrator.
9. **Quality Check applicability** — which of this skill's outputs cross the review threshold.

---

## Operating rules

- **Load on demand.** An orchestrator loads a skill only when the task needs it. Skills do not auto-run.
- **One mandate.** A skill produces its named output and stops. It does not silently take over a neighbor's job.
- **Evidence in, evidence out.** Every material claim in an output carries a truth label. Unlabeled claims are treated as `Speculation`.
- **Write narrowly.** A skill writes only to the files listed in its write permissions. It never writes to `CONSTITUTION.md`.
- **Hand off explicitly.** Output names its downstream consumer and the decision it enables.
- **Escalate, don't guess.** On missing inputs, contradictions, or a crossed veto, the skill stops and escalates to its orchestrator rather than fabricating.

---

## Standard output header (prepend to every skill artifact)

```
Skill: <skill-name>
Task: <one line>
Inputs used: <files / briefs / sources, with dates>
Evidence tier: <highest claim tier present>
Quality Check: <required | not required>  ·  <pending | passed | failed→revised>
Downstream consumer: <orchestrator / skill / Tony>
```

---

## Minimal skill skeleton

```markdown
# <Skill Name>
**Primary mandate:** ...
**Required inputs:** ...
**Required outputs:** ...
**Explicit boundaries (does NOT):** ...
**Handoffs:** upstream ← ... ; downstream → ...
**Evidence requirements:** ...
**Write permissions:** ...
**Stop / escalate when:** ...
**Quality Check:** required for <which outputs>
## Method
...
```
