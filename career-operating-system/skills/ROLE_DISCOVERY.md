# Role Discovery

**Primary mandate:** Find and verify real, current, in-scope executive roles — and screen out everything that fails a hard veto before deeper work begins.

**Required inputs:** target archetypes (Current State); Query Bank; floor and veto list (Constitution); de-dup list (active roles + Decision Register).

**Required outputs:** a verified candidate list, each as a stub `templates/ROLE_BRIEF.md` — title, company, source + retrieval date, remote status, comp signal, veto pre-screen result, dedupe status.

**Explicit boundaries (does NOT):** deep company diligence (→ `company-diligence`); score fit (→ `role-fit-evaluation`); write outreach.

**Handoffs:** upstream ← `market-intelligence`; downstream → `company-diligence` then `role-fit-evaluation`.

**Evidence requirements:** role must be confirmed live (≤14 days) from a primary source; remote status and comp signal labeled; no role advanced on a Tier-3 source alone without flagging.

**Write permissions:** `state/CURRENT_STATE.md` (active roles + stage = "discovered"); `query-bank/QUERY_BANK.md` (queries, dead sources, aliases — Class 1); `state/LEARNING_LEDGER.md` (search performance, query yield).

**Stop / escalate when:** a role pre-fails a veto → reject with reason, do not advance; duplicate of an existing record → merge, do not reprocess; source cannot be verified → hold as `Unknown`.

**Quality Check:** not required for discovery stubs (low-risk); required only if a discovery summary becomes a recommendation.

## Method
1. Pull from the Query Bank; rotate dead sources out (Class 1).
2. De-dup against Current State + Decision Register first.
3. Verify the role is live, remote, and ≥ floor before logging.
4. Pre-screen vetoes; reject early and cheaply.
5. Log query yield so the Query Bank improves over time.
