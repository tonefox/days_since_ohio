# Constitution — The Maturity Model

> **Constitutional layer.** The six levels and the asymmetric-scaling thesis are durable. The
> illustrative examples may be adapted to your context via `brand.yaml`.

The maturity model describes how an enablement function progresses from static and manual to
AI-native, and explains why that progression decouples reach from cost. It is the lens the
self-assessment (`assessment/`) uses to locate an organization and route it to a delivery path.

## The six levels

| Level | Name | Defining characteristic | Marginal cost to enable one more partner |
| --- | --- | --- | --- |
| **L0** | Static / Manual | Fixed courseware and instructor-led events; content rebuilt per release | High and roughly constant |
| **L1** | AI-Assisted Authoring | AI accelerates content creation; delivery and assessment still manual | High, modestly reduced |
| **L2** | AI-Personalized Delivery | AI assembles and sequences adaptive paths per partner | Falling |
| **L3** | AI-Assessed Competency | AI administers and scores scenario-based demonstrations at scale | Low |
| **L4** | Self-Updating Enablement | Content regenerates continuously against the live product and market | Very low |
| **L5** | Ecosystem Flywheel | The system learns from partner and customer outcomes and improves itself | Approaching zero |

### L0 — Static / Manual
Enablement is a library of fixed artifacts delivered through scheduled events. Currency is
maintained by periodic rebuilds. Reach is bounded by trainer and content-production capacity.
This is the historical default and the baseline against which the asymmetry is measured.

### L1 — AI-Assisted Authoring
AI is used as a productivity tool for content creators — drafting, summarizing, translating, and
repurposing. Authoring gets faster and cheaper, but delivery and assessment remain human-bound,
so the binding constraint (reach) is only partially relieved. Most organizations beginning this
journey are here.

### L2 — AI-Personalized Delivery
The system assembles a path per partner from a pool of capabilities, sequencing against role,
maturity, vertical, and prior demonstrated competence (Article IV). Delivery cost stops scaling
linearly with the number of distinct partner profiles, because the personalization is automated.

### L3 — AI-Assessed Competency
Scenario-based demonstration (Article V) becomes affordable at scale because AI administers and
scores it. Rigorous certification — historically the most expensive part of enablement — is no
longer rationed. This is the level at which "capability over content" (Article I) becomes
operationally real rather than aspirational.

### L4 — Self-Updating Enablement
Content regenerates continuously against the current product and market state (Article III). The
organization invests in the regeneration *pipeline* rather than in artifacts. Staleness ceases to
be a recurring crisis and becomes a managed property of the system.

### L5 — Ecosystem Flywheel
Outcome signals (Article VIII) feed back into the system: what correlates with qualified
pipeline, win rates, and successful implementations is detected and reinforced; what does not is
retired. Enablement improves itself. The marginal cost of enabling an additional partner
approaches zero while currency and quality continue to rise.

## Why the scaling is asymmetric

In a traditional (L0) function, reach and cost rise together: doubling the number of enabled
partners roughly doubles the trainers, content, and coordination required. The curve is linear at
best.

As an organization climbs the model, the cost of each enablement activity — authoring (L1),
delivery (L2), assessment (L3), currency (L4), improvement (L5) — is progressively absorbed by
AI. The marginal cost of enabling one more partner falls at each level, while the *quality* and
*currency* of what they receive rises. Reach and cost **decouple**.

```
Enablement cost per partner

 high │■                         L0 — flat, high (reach is capped by capacity)
      │ ■■
      │   ■■■                    L1–L2 — falling as authoring & delivery automate
      │      ■■■■
      │          ■■■■■           L3–L4 — low, assessment & currency automate
      │               ■■■■■■
  low │                     ■■■■■■■■■■  L5 — approaching zero, system self-improves
      └───────────────────────────────────────────►
        L0    L1    L2    L3    L4    L5
                    AI applied to the enablement function
```

This is the asymmetry the framework exists to capture. Two corollaries follow:

- **Climbing the model is the strategy.** The objective of an engagement is not to produce better
  static courseware; it is to move the enablement function up the levels so that reach and cost
  decouple. Every recommendation in the playbook is, ultimately, a move up this model.

- **The Articles are the guardrails for the climb.** AI applied without the constitution produces
  faster production of the wrong thing — high-volume, low-currency, recall-based content. The
  Articles ensure that as AI is applied, it is applied to *capability, currency, personalization,
  demonstrated competency, and accountable outcomes* — the things that compound.

## How the model is used

- The **self-assessment** scores an organization across the dimensions implied by these levels
  and places it on the model.
- The **routing logic** uses that placement, together with whether the organization has a
  dedicated L&D function, to recommend **Path A (Trainer Cascade)** or **Path B (Self-Serve
  Catalog)** — see `assessment/scoring-and-routing.md`.
- The **engagement lifecycle** (`playbook/engagement-lifecycle.md`) is, in effect, the operating
  procedure for moving an organization one or more levels up this model.
