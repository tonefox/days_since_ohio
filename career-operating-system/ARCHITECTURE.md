# Architecture

How the Career Operating System is layered, why, and how work flows through it.

---

## 1. Layered Model

```
┌─────────────────────────────────────────────────────────────┐
│  CONSTITUTION  (steadfast — mission, vetoes, standards)       │  read-only to skills
├─────────────────────────────────────────────────────────────┤
│  GOVERNANCE  (precedence, change classes, amendment process)  │
├─────────────────────────────────────────────────────────────┤
│  LEARNING & EVIDENCE LAYER                                    │
│    state/LEARNING_LEDGER.md   (observations, pattern maturity)│  ← skills WRITE here
│    state/EXPERIMENT_REGISTER  (tests of hypotheses)           │     not to Constitution
│    state/AMENDMENT_QUEUE      (proposed constitutional change) │
├─────────────────────────────────────────────────────────────┤
│  CURRENT STATE  (what is happening now — active work)         │  ← read first, updated often
│    state/CURRENT_STATE.md, state/DECISION_REGISTER.md         │
├─────────────────────────────────────────────────────────────┤
│  ORCHESTRATION                                                │
│    executive-career-orchestrator (parent)                     │
│      ├─ executive-job-search-orchestrator                     │
│      └─ consulting-practice-orchestrator                      │
├─────────────────────────────────────────────────────────────┤
│  SPECIALIST SKILLS  (one mandate each, contract-bound)        │
├─────────────────────────────────────────────────────────────┤
│  CONTRACTS  (SKILL_CONTRACT, EVIDENCE_STANDARD, QUALITY_CHECK)│
└─────────────────────────────────────────────────────────────┘
```

The defining principle of v2: **durable constitutional principles are separated from operational learning.** Skills learn by writing to the Learning & Evidence Layer. They cannot rewrite the Constitution. Change flows *upward* only through governance.

---

## 2. Orchestrator Map

```
                     executive-career-orchestrator
                     (intake, routing, precedence,
                      cross-path conflict resolution)
                        /                        \
                       /                          \
   executive-job-search-orchestrator     consulting-practice-orchestrator
   ─ market-intelligence                 ─ market-intelligence (shared)
   ─ role-discovery                      ─ consulting-practice-architect
   ─ company-diligence                   ─ pov-thought-leadership
   ─ role-fit-evaluation                 ─ company-diligence (buyer mode)
   ─ executive-narrative (shared)        ─ executive-narrative (shared)
   ─ application-materials               ─ networking-and-sponsorship (shared)
   ─ networking-and-sponsorship          ─ compensation-and-offer-analysis (pricing mode)
   ─ interview-intelligence
   ─ compensation-and-offer-analysis

   tech-executive-career-architect = strategic synthesis across BOTH (judgment layer)
```

Both child orchestrators read the same Constitution, Current State, Learning Ledger, and Decision Register. They stay separate so an **employment role** and a **consulting prospect** are never scored or managed as if they were the same kind of opportunity.

---

## 3. Default Operating Flow

```
Constitution
    ↓
Current State + Learning Ledger
    ↓
Career Architect (frame + route)
    ↓
Relevant Orchestrator
    ↓
Required Specialist Skill(s)   ← load only what the task needs
    ↓
Quality Check (only when threshold crossed)
    ↓
Decision or Artifact
    ↓
Learning / Decision / Experiment Record
```

### Normal role flow
```
Discover → Verify → Company diligence → Evaluate fit + vetoes →
Decide pursue/monitor/reject → Map approved narrative →
Create outreach/materials → Quality Check → Submit →
Measure response → Record learning
```

Not every skill runs for every task. Low-risk admin updates skip the Quality Check.

---

## 4. The Two-Pass Quality Model

High-impact outputs use a lightweight two-pass model, **not** a dedicated evaluator persona per skill:

1. The specialist skill produces the work.
2. The relevant orchestrator runs the **Quality Check** (a reusable contract, `contracts/QUALITY_CHECK.md`) before finalization.

The producing skill may revise after review but **may not approve its own failed review**. See `contracts/QUALITY_CHECK.md` for the trigger threshold and the five questions.

---

## 5. Gap Analysis Resolutions (v1 → v2)

The v2 design closes these material gaps identified in v1 (a single-persona skill):

| Gap (v1) | Resolution (v2) |
|---|---|
| No separation of durable principle vs. learning | Constitution + Learning & Evidence Layer with upward-only governance |
| No persistent state; context drift between sessions | `CURRENT_STATE.md` read first every session |
| No controlled change process; risk of mission drift | Three change classes + Amendment Queue + precedence order |
| Self-review only; no honesty backstop | Two-pass Quality Check; no self-approval of failed reviews |
| Employment and consulting conflated | Two child orchestrators, distinct scoring |
| No way to measure if the system improves outcomes | Experiment Register + outcome metrics in Weekly Rhythm |
| Duplicate work across sessions | Decision Register + Current State + de-dup rules in Role Discovery |
| Stale data risk | Freshness rules in Evidence Standard + Market Intelligence |
| Sensitive info handling undefined | Privacy rules in Evidence Standard + Governance |
| No failure recovery path | `workflows/FAILURE_AND_ESCALATION.md` |

Full narrative is in `README.md` §"Gap analysis".
