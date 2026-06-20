# Company Diligence

**Primary mandate:** Assess a specific company (employer) or buyer organization (consulting) — trajectory, leadership, funding, AI investment reality, sponsorship quality, and risk.

**Required inputs:** a `ROLE_BRIEF` stub or named buyer; the diligence questions that matter for the decision.

**Required outputs:** a `templates/COMPANY_DILIGENCE_BRIEF.md` — trajectory, leadership & likely sponsor, funding/financial health, remote reality, AI-investment substance vs. marketing, risks, unknowns, sources with dates.

**Explicit boundaries (does NOT):** score role fit (→ `role-fit-evaluation`); decide pursue/reject; design narrative or pricing.

**Handoffs:** upstream ← `role-discovery` (employer) or `consulting-practice-architect` (buyer); downstream → `role-fit-evaluation` or `consulting` pipeline.

**Evidence requirements:** "AI investment" must be backed by substance (hires, products, spend, customers) — never asserted from marketing; funding/leadership ≤60 days; remote policy ≤14 days; each risk labeled.

**Write permissions:** `state/CURRENT_STATE.md` (diligence status); `state/LEARNING_LEDGER.md` (company/sponsor signals, AI-washing patterns); `state/DECISION_REGISTER.md` only via orchestrator.

**Stop / escalate when:** diligence reveals a veto (e.g., remote rescinded) → flag immediately; sponsorship looks weak or "AI positioning without investment" → record as a key risk, escalate to evaluation.

**Quality Check:** required (the brief feeds a pursue/reject recommendation and may contain financial claims).

## Method
1. Establish trajectory and financial health from primary sources.
2. Identify the hiring executive / sponsor and assess alignment.
3. Test AI claims against real investment evidence.
4. Confirm remote reality independent of the posting.
5. Surface the strongest reasons *not* to proceed.
