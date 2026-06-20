# Career Operating System — v2

An evidence-based, drift-resistant system that helps Tony build a durable executive position across **two paths** — an executive employment role and an independent consulting practice — under one set of durable principles.

The defining idea of v2: **separate durable constitutional principles from operational learning.** Skills don't rewrite the mission. They record observations in a Learning Ledger; change reaches the Constitution only through a controlled, human-approved amendment process.

---

## Gap analysis (what v2 fixes)

v1 was a single coaching persona — strong judgment, but no memory, no governance, and no honesty backstop. Material gaps closed in v2:

1. **Governance / drift** — no way to stop one search result or AI suggestion from rewriting strategy. → Constitution + three change classes + precedence order.
2. **State management / context drift** — nothing persisted between sessions. → `state/CURRENT_STATE.md` read first, every time.
3. **Evidence quality / honesty** — self-review only. → Evidence Standard (truth labels, source tiers, freshness) + two-pass Quality Check that can't self-approve a failed review.
4. **Workflow handoffs / duplicate work** — undefined boundaries, repeated effort. → Skill Contract (explicit handoffs) + Decision Register + dedupe rules.
5. **Job search vs. consulting conflation** — one rubric for two different things. → Two child orchestrators with distinct scoring.
6. **Measuring improvement** — activity ≠ progress. → Experiment Register + system-improvement KPIs in the Weekly Rhythm.
7. **Failure recovery** — no escalation path. → `workflows/FAILURE_AND_ESCALATION.md`: stop-and-escalate over fabricate.
8. **Data freshness** — stale comp/remote/role facts. → freshness windows; stale facts downgraded to `Unknown`.
9. **Privacy** — sensitive data handling undefined. → sensitivity tiers; Quality Check blocks Confidential leaks.
10. **Archiving / version control** — no record of change. → Changelog + git; Amendment Queue history.

What v2 deliberately **avoids**: an evaluator persona per skill, mandatory full-pipeline runs, Quality Checks on trivial updates, and numerical scores that manufacture false certainty or override a veto.

---

## Repository map

```
CONSTITUTION.md      Steadfast mission, vetoes, standards (Class-3-change only)
GOVERNANCE.md        Precedence order, 3 change classes, amendment lifecycle
ARCHITECTURE.md      Layers, orchestrator map, flows, gap resolutions
CHANGELOG.md         Approved structural/constitutional changes

contracts/           SKILL_CONTRACT · EVIDENCE_STANDARD · QUALITY_CHECK
orchestrators/       EXECUTIVE_CAREER (parent) · JOB_SEARCH · CONSULTING_PRACTICE
skills/              12 contract-bound specialists
state/               CURRENT_STATE · LEARNING_LEDGER · DECISION_REGISTER ·
                     EXPERIMENT_REGISTER · AMENDMENT_QUEUE
workflows/           WEEKLY_OPERATING_RHYTHM · SELF_CORRECTION_LOOP · FAILURE_AND_ESCALATION
query-bank/          QUERY_BANK (Class-1 calibration)
templates/           ROLE_BRIEF · COMPANY_DILIGENCE_BRIEF · DECISION_MEMO ·
                     CONSTITUTIONAL_AMENDMENT · CONSULTING_OPPORTUNITY_BRIEF
prompts/             CODEX_CLAUDE_CODE_SYSTEM_PROMPT
```

## Architecture at a glance

```
Constitution → Current State + Learning Ledger → Career Architect →
Relevant Orchestrator → Required Specialist Skill(s) →
Quality Check (when required) → Decision or Artifact →
Learning / Decision / Experiment Record
```

Change only ever flows **upward** through governance. A Learning Ledger note can become a calibration, then a tested hypothesis, then — with Tony's approval — a constitutional amendment. It can never silently override the Constitution.

---

## How to initialize and use

**Initialize (once):**
1. Open `state/CURRENT_STATE.md`. Set the strategic priority, sprint theme, and any user overrides.
2. Confirm the Constitution reflects your real constraints (floor, remote, vetoes). Anything you want to change is a Class 3 amendment — propose it via `templates/CONSTITUTIONAL_AMENDMENT.md`.
3. Seed `query-bank/QUERY_BANK.md` with starting queries.

**Each working session:**
1. Read Constitution → Governance → Current State (the agent does this automatically via `prompts/CODEX_CLAUDE_CODE_SYSTEM_PROMPT.md`).
2. State your task. The parent orchestrator routes it to job search, consulting, or the architect.
3. Only the needed skills load. High-impact outputs get a Quality Check.
4. Observations land in the Learning Ledger; decisions in the Decision Register; tests in the Experiment Register.

**Weekly:** run `workflows/WEEKLY_OPERATING_RHYTHM.md` — plan Monday, execute midweek, review/measure Friday.

**To change the mission:** you can't do it casually — that's the point. Draft an amendment, attach evidence and a test, and approve it explicitly. The system records it in the Changelog.

---

## Design guarantee

Strong enough to improve itself through evidence; constrained enough that it cannot casually rewrite its mission, standards, or priorities.
