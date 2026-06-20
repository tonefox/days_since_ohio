# Governance

How the Career Operating System changes itself without drifting. This file defines source-of-truth precedence, the three change classes, the amendment lifecycle, and write permissions.

---

## 1. Source-of-Truth Precedence

When two instructions conflict, the higher-ranked source wins. A lower source **never silently overrides** a higher one; it may only *propose* a change through the amendment process.

1. Tony's explicit instruction in the current session
2. `CONSTITUTION.md`
3. Approved constitutional amendments + `CHANGELOG.md`
4. Governance rules (this file)
5. `state/CURRENT_STATE.md`
6. Approved `state/DECISION_REGISTER.md` entries
7. Specialist Skill definitions (`skills/*`)
8. Orchestrator defaults (`orchestrators/*`)
9. `state/LEARNING_LEDGER.md` observations
10. Generated artifacts

**Rule of drift resistance:** A Learning Ledger observation (rank 9) must never override the Constitution (rank 2). It can only mature into a proposed amendment and be ratified upward.

---

## 2. Write Permissions Matrix

| Target file | Who may write | Approval needed |
|---|---|---|
| `CONSTITUTION.md` | Tony only (via ratified amendment) | Class 3 |
| `CHANGELOG.md` | Orchestrators, after approval | Records approved changes only |
| `state/CURRENT_STATE.md` | Orchestrators + skills (scoped fields) | None for routine; Class 2/3 fields gated |
| `state/LEARNING_LEDGER.md` | Any skill or orchestrator | None (append-only observations) |
| `state/DECISION_REGISTER.md` | Orchestrators (on material decisions) | Tony confirms material decisions |
| `state/EXPERIMENT_REGISTER.md` | Orchestrators + skills | None to log; Class 2 to act on results |
| `state/AMENDMENT_QUEUE.md` | Any skill or orchestrator (propose) | Tony approves/rejects |
| `query-bank/QUERY_BANK.md` | Skills (Class 1 calibration) | None |
| `skills/*`, `orchestrators/*`, `contracts/*` | Coding agent via PR | Tony reviews structural change |

Skills **never** write directly to `CONSTITUTION.md`. Full stop.

---

## 3. Three Classes of Change

### Class 1 — Operational Calibration (no constitutional approval)
Does not alter durable strategy. Apply directly; note in the relevant file's changelog section if material.
- Query improvements, dead-source removal, ATS/search-pattern tuning
- Formatting changes, duplicate aliases, minor workflow improvements

### Class 2 — Strategic Hypothesis Update (propose + test, do not ratify immediately)
A candidate truth that must earn its way up. Logged as a hypothesis and ideally tested via `state/EXPERIMENT_REGISTER.md` before any Class 3 proposal.
- New role archetype, new company category, new capability gap
- New consulting buyer, recommended scoring adjustment, new positioning hypothesis

A Class 2 item lives in `CURRENT_STATE.md` (as an active hypothesis/experiment) and the Learning Ledger. It may **inform** recommendations only if labeled as a working hypothesis with confidence stated. It becomes constitutional only by being promoted to a Class 3 amendment with evidence.

### Class 3 — Constitutional Change (Tony's explicit approval required)
Alters mission, standards, or priorities.
- Lowering the compensation floor; changing location requirements
- Adding direct-sales roles; removing exclusions
- Changing the primary career thesis; changing scoring weights
- Changing truth/evidence standards; changing family/lifestyle priorities
- Making consulting the primary path

---

## 4. Amendment Lifecycle

```
observe → pattern matures in Learning Ledger → draft amendment (templates/CONSTITUTIONAL_AMENDMENT.md)
   → enqueue in state/AMENDMENT_QUEUE.md → (Class 2: test via Experiment Register)
   → Tony reviews → approve / reject / defer → if approved: edit CONSTITUTION.md
   → record in CHANGELOG.md → close queue item
```

Every amendment proposal (see `templates/CONSTITUTIONAL_AMENDMENT.md`) must include:
- The current rule
- The proposed change
- The reason
- Supporting evidence (with truth labels)
- Risks and unintended consequences
- A test before adoption when possible
- A reversal plan
- The affected constitutional section
- Approval status
- Final decision
- Changelog entry reference

A Quality Check (`contracts/QUALITY_CHECK.md`) is **required** on every amendment proposal before it reaches Tony.

---

## 5. Pattern Maturity Ladder (from the Learning & Evidence Layer)

The Learning Ledger classifies every observation so that only durable, consequential signal can drive change:

`Noise → Isolated observation → Emerging pattern → Repeated pattern → Highly consequential verified fact`

- **Noise / Isolated:** recorded, not actionable.
- **Emerging pattern:** may inform a Class 1 calibration.
- **Repeated pattern:** may justify a Class 2 hypothesis + experiment.
- **Highly consequential verified fact:** may justify a Class 3 amendment proposal.

Maturity is never assumed from a single data point. Promotion up the ladder requires corroboration recorded in the Ledger.

---

## 6. Reversibility

Every Class 2 and Class 3 change carries a reversal plan. If a ratified change underperforms against its stated test, it is reverted via the same process and the reversal is logged in `CHANGELOG.md`.
