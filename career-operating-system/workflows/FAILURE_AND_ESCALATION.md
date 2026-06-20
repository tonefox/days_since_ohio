# Failure and Escalation

What to do when something breaks, conflicts, or is missing. Default posture: **stop and escalate rather than fabricate.**

---

## Failure modes and responses

| Failure | Detection | Response |
|---|---|---|
| **Missing input** | A skill's required input absent | Stop; request it; do not invent. Log blocker in Current State. |
| **Stale data** | Time-sensitive fact past freshness window | Downgrade to `Unknown`; re-verify before any recommendation. |
| **Evidence too weak** | Decision-critical claim is `Speculation`/`Unknown` | Cap confidence; name the unknown + the test that resolves it. |
| **Veto crossed** | Floor/remote/excluded-role/lifestyle breach | Reject or escalate to Tony. A score never overrides a veto. |
| **Source conflict** | Two sources disagree | Label `Contradicted`; surface both; corroborate before acting. |
| **Quality Check fail** | One of the five questions fails | Return to producing skill; revise; re-check. No self-approval. |
| **Precedence conflict** | Two sources above rank 6 clash | Apply `GOVERNANCE.md` §1; if still unclear → architect → Tony. |
| **Scope creep** | A skill doing another's job | Halt; re-route via orchestrator; note boundary breach in Ledger. |
| **Constitutional pressure** | A task wants a durable change | Route to Amendment Queue; never edit Constitution inline. |
| **Duplicate work** | Role/prospect already decided | Merge to existing record; cite Decision Register. |
| **Privacy risk** | Confidential data heading into a shared artifact | Block; strip or get consent; Quality Check verifies. |

## Escalation ladder
1. **Skill → Orchestrator** — missing input, boundary issue, Quality Check fail.
2. **Orchestrator → Career Architect** — judgment, conflict between specialist outputs, cross-path tradeoff.
3. **Architect → Tony** — any Class 3 change, any crossed veto, any major decision, any unresolved precedence conflict.

## Recovery principles
- Prefer a smaller, defensible output over a larger, unsupported one.
- Leave the system in a known state: every halt writes a blocker + next action to Current State.
- Record recurring failures in the Learning Ledger so they can mature into calibration or amendments.
