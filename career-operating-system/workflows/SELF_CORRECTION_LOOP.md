# Self-Correction Loop

How the system improves itself **without** rewriting its mission. This is the engine that turns observations into calibrated change through governance — never around it.

```
        ┌──────────────────────────────────────────────────────┐
        │ 1. OBSERVE                                            │
        │   Skill logs an observation → Learning Ledger        │
        │   (labeled, maturity = Isolated by default)          │
        └───────────────┬──────────────────────────────────────┘
                        ↓
        ┌──────────────────────────────────────────────────────┐
        │ 2. CLASSIFY (pattern-maturity ladder)                │
        │   Noise / Isolated / Emerging / Repeated / Verified  │
        └───────────────┬──────────────────────────────────────┘
                        ↓
        ┌──────────────────────────────────────────────────────┐
        │ 3. ROUTE BY CLASS                                     │
        │   Emerging  → Class 1 calibration (apply directly)   │
        │   Repeated  → Class 2 hypothesis → Experiment Register│
        │   Verified+consequential → Class 3 → Amendment Queue │
        └───────────────┬──────────────────────────────────────┘
                        ↓
        ┌──────────────────────────────────────────────────────┐
        │ 4. TEST (Class 2/3)                                   │
        │   Pre-register metric + success criteria; run; read  │
        └───────────────┬──────────────────────────────────────┘
                        ↓
        ┌──────────────────────────────────────────────────────┐
        │ 5. DECIDE                                             │
        │   Class 1: keep/revert · Class 2: adopt as working   │
        │   hypothesis · Class 3: Tony approves → edit          │
        │   Constitution → Changelog                            │
        └───────────────┬──────────────────────────────────────┘
                        ↓
        ┌──────────────────────────────────────────────────────┐
        │ 6. REVERSE IF NEEDED                                  │
        │   Underperforms its test → revert via same process,  │
        │   log reversal in Changelog                           │
        └──────────────────────────────────────────────────────┘
```

## Invariants
- A single observation never changes the Constitution.
- Every Class 2/3 change carries a pre-registered test and a reversal plan.
- The producing skill cannot approve its own failed Quality Check.
- Calibration that touches durable strategy, standards, or priorities is **always** Class 3.

## Contradiction handling
When new evidence contradicts a prior decision or a constitutional assumption, log it as a `contradiction` in the Ledger, raise maturity only with corroboration, and route through the ladder — do not silently flip the decision.
