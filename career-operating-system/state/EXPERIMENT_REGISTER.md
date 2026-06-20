# Experiment Register

> Where hypotheses are tested **before** they become strategy or constitution. This is how the system measures whether it is actually improving outcomes rather than just generating activity. Class 2 hypotheses should be tested here before any Class 3 proposal.

## When to log an experiment
- A Class 2 strategic hypothesis (new archetype, buyer, positioning, scoring tweak)
- An outreach/message/POV/pricing test
- A query or sourcing change worth measuring
- Any change whose value is claimed but unproven

## Entry schema
```
ID:            EX-YYYYMMDD-NN
Date opened:
Hypothesis:    (falsifiable statement)
Linked to:     (LL id / amendment id / Current State item)
Class:         (1 / 2 / 3-candidate)
Metric:        (what will be measured)
Success criteria: (pre-registered threshold)
Sample / window: (how much data, how long)
Result:        (pending / supported / not supported / inconclusive)
Decision:      (adopt / drop / iterate / propose amendment)
Reversal plan:
Status:        (running / closed)
```

## Outcome metrics the system tracks (system-improvement KPIs)
- Discovery yield: in-scope verified roles per search hour
- False-positive rate: roles advanced then vetoed late
- Response rate: outreach/application → reply
- Interview conversion and recurring-objection count
- Scoring calibration: predicted fit vs. realized outcome
- Consulting: discovery→qualified→proposal→won; pricing realized vs. modeled
- Governance health: amendments proposed/tested/ratified/reverted

## Register
_(append-only; newest at top)_

```
ID:            EX-20260620-01
Date opened:   2026-06-20
Hypothesis:    Parallel job-search + consulting for 90 days yields a higher-quality primary path choice than committing now.
Linked to:     DR-20260620-01
Class:         2
Metric:        # qualified employment opportunities vs. # qualified consulting prospects at day 90
Success criteria: ≥1 qualified opportunity in each path, with a clear evidence-based primacy signal
Sample / window: 90 days
Result:        pending
Decision:      pending
Reversal plan: collapse to single path if one shows no qualified opportunity by day 45
Status:        running
```
