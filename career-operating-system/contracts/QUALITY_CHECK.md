# Quality Check

A lightweight, reusable review contract — **not** a permanent persona and **not** a per-skill evaluator. The relevant orchestrator runs it before an output is finalized. It exists to protect honesty and decision quality without adding bureaucracy.

---

## 1. When a Quality Check is REQUIRED

Run it when an output:

- Produces a **final recommendation**
- Will be **sent to another person** (outreach, application, proposal, public POV)
- **Changes career positioning**
- Contains **claims about Tony's experience**
- Contains **compensation or financial analysis**
- Affects a **major career or consulting decision**
- **Proposes a constitutional amendment**

## 2. When it is NOT required

Routine operational updates: query tuning, formatting, logging an observation, updating a status field, de-duping a role, internal working notes. Do not gate low-risk admin work.

---

## 3. The Five Questions

1. **Is the output factually supported?** Every material claim carries a truth label of `Corroborated`/`Verified` where the decision depends on it; time-sensitive facts are fresh (`EVIDENCE_STANDARD.md` §3).
2. **Does it comply with the Constitution?** No veto crossed; floor respected; standards honored; precedence intact.
3. **Does it overstate Tony's experience, authority, or fit?** No inflated ownership, scope, titles, or technical depth. Influence ≠ ownership.
4. **Are important risks, counterarguments, or unknowns missing?** The strongest counterargument and key unknowns are present.
5. **Is the recommended action clear?** A reader knows what to do next and what would change the recommendation.

---

## 4. Outcome

- **Pass** → finalize; stamp the output header `Quality Check: passed`.
- **Fail** → return to the producing skill with specific defects. The skill **revises** and resubmits. **The producing skill may not approve its own failed review** — the orchestrator (or Tony) re-runs the check.
- **Escalate** → if a failure reflects a constitutional tension or a judgment call, hand to `tech-executive-career-architect`; if it implies a constitutional change, route to the Amendment Queue.

Record material Quality Check failures and their resolution as observations in `state/LEARNING_LEDGER.md` so recurring defects can mature into calibration or amendments.

---

## 5. Reusable contract block (paste into the orchestrator step)

```
QUALITY CHECK — <artifact name>
[ ] 1 Factually supported (labels + freshness verified)
[ ] 2 Constitution-compliant (no veto crossed)
[ ] 3 No overstatement of Tony's experience/authority/fit
[ ] 4 Risks / counterargument / unknowns present
[ ] 5 Recommended action is clear
Result: PASS / FAIL → <defects> / ESCALATE → <where>
Reviewer: <orchestrator>  Date: <date>
```
