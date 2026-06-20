# Decision Register

> Material decisions, recorded so the system doesn't re-litigate settled questions or duplicate work. Orchestrators write entries; Tony confirms material decisions. Higher precedence than Skill defaults (rank 6), lower than the Constitution.

## When to record
- Pursue / monitor / reject an employment role
- Pursue / price / continue / pivot / stop a consulting prospect or the practice
- Accept / decline / counter an offer
- Any strategic fork resolved by `tech-executive-career-architect`

## Entry schema
```
ID:           DR-YYYYMMDD-NN
Date:
Decision:
Type:         (role / consulting / offer / strategy)
Context:      (links to ROLE_BRIEF / diligence / fit eval / decision memo)
Recommendation source:
Tony confirmed: (yes/no/n-a)
Rationale (1-3 lines):
Reversible?   (yes/no) · Reversal condition:
What would change it:
Status:       (active / superseded / closed)
```

## Register
_(append-only; newest at top)_

```
ID:           DR-20260620-01
Date:         2026-06-20
Decision:     Adopt Career Operating System v2 (this repository).
Type:         strategy
Context:      Revision request; ARCHITECTURE.md; GOVERNANCE.md
Recommendation source: revision spec
Tony confirmed: pending
Rationale:    Separate durable principles from operational learning; add controlled governance.
Reversible?   yes · Reversal condition: revert to v1 single-skill if v2 proves too heavy to operate
What would change it: evidence the system adds friction without improving decisions
Status:       active
```
