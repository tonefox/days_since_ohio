# Scoring and Routing

> **Instantiation layer.** The bands and thresholds below are sensible defaults. You may
> recalibrate them to your organization, provided the logic remains transparent and consistent.

This document turns a completed self-assessment into two outputs: a **maturity placement** on the
model, and a **recommended delivery path**.

## Step 1 — Place the organization on the maturity model

Use the statement subtotal (maximum 48) from `maturity-self-assessment.md`.

| Subtotal | Maturity placement | Interpretation |
| --- | --- | --- |
| 0–9 | **L0 — Static / Manual** | Enablement is artifact-and-event based; reach is capped by capacity. |
| 10–18 | **L1 — AI-Assisted Authoring** | AI helps create content; delivery and assessment remain manual. |
| 19–28 | **L2 — AI-Personalized Delivery** | Paths are adapted per partner; personalization is partly automated. |
| 29–37 | **L3 — AI-Assessed Competency** | Demonstrated competency is assessed at scale. |
| 38–44 | **L4 — Self-Updating Enablement** | Content regenerates continuously; staleness is managed. |
| 45–48 | **L5 — Ecosystem Flywheel** | The system learns from outcomes and improves itself. |

The placement is a *starting diagnosis*, not a grade. Its purpose is to identify the **next one
or two levels** to target — the engagement is about movement, not about the absolute number.

### Reading the sections diagnostically
Beyond the total, the four sections reveal *where* the constraint is:

- **Low Section A (1–3):** the problem is foundational — enablement is still content- and
  version-coupled. Address Articles I–III before investing heavily in AI tooling.
- **Low Section C (7–10):** AI leverage is the gap. This is the primary lever for asymmetric
  scaling; prioritize moving authoring, delivery, and assessment onto AI.
- **Low Section D (11–12):** the issue is governance and accountability — the work may be good but
  is not measured against outcomes or cannot be customized and improved repeatably.

A low total driven by Section C is the most encouraging case: the foundations exist and the
asymmetric-scaling upside is largely uncaptured.

## Step 2 — Recommend a delivery path

Routing depends on the organization's capacity to enable others, captured by routing questions R1
and R2. The path determines *how* enablement reaches the field, independent of maturity level.

| R1 (L&D function) | R2 (trainer population) | Recommended path |
| --- | --- | --- |
| Yes — established | Yes / Limited | **Path A — Trainer Cascade** |
| Partial | Yes | **Path A — Trainer Cascade** |
| Partial | Limited / No | **Path B — Self-Serve Catalog** (with a view to building toward A) |
| No | Any | **Path B — Self-Serve Catalog** |

- **Path A — Trainer Cascade** (`playbook/path-a-trainer-cascade.md`): the organization has, or
  can assemble, a train-the-trainer population. Enablement is delivered once to that population,
  which then cascades it to the wider field — a multiplicative reach model.

- **Path B — Self-Serve Catalog** (`playbook/path-b-self-serve.md`): the organization lacks a
  dedicated L&D function. The kit equips it to self-identify gaps, assemble a path from a modular
  catalog, build assessments from templates, and roll out directly to the field.

The two paths are not permanent assignments. A common trajectory is to begin on Path B, use it to
develop a credible trainer population, and graduate to Path A as the function matures.

## Step 3 — Record and act

Capture three things and carry them into the engagement lifecycle
(`playbook/engagement-lifecycle.md`):

1. **Current placement** (e.g., "L1, constrained by Section C — AI leverage").
2. **Target placement** for this engagement (typically current + 1 to 2 levels).
3. **Recommended path** (A or B) and the rationale from the routing table.

These three outputs are the inputs to the **Assess** stage of the engagement lifecycle.
