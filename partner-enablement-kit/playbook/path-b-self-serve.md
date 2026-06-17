# Path B — Self-Serve Catalog

> **Instantiation layer.** A lean run-guide for organizations without a dedicated L&D function.
> Adapt activities, owners, and timelines to your context.

**When this path applies:** the routing logic in `assessment/scoring-and-routing.md` recommends
Path B when the organization lacks a dedicated L&D or enablement function and cannot rely on a
train-the-trainer population. Enablement must reach the field directly.

**The core idea:** make the organization self-sufficient. Instead of depending on trainers, the
kit equips the field — and whoever owns enablement locally — to **self-identify gaps, assemble a
path from a modular catalog, build assessments from templates, and roll out directly**. The
constitution and competency maps supply the standard; the catalog and templates supply the means.

```
 Competency maps  ─┐
 (the standard)    ├─►  Self-identify gaps  ─►  Assemble path from catalog  ─►  Build assessment  ─►  Roll out to field
 Modular catalog  ─┘                                                              (templates)
```

## Roles

- **Sponsor** — leadership owner who ratified the Articles and owns the outcome signals.
- **Local owner** — whoever holds enablement responsibility (often a line manager or a senior
  individual contributor), even if part-time.
- **Field** — the sellers and technical staff enabling themselves through the catalog.

## How to run it

### B1. Self-identify gaps against the competency maps
- Each individual (or their manager) assesses themselves against the relevant competency map —
  `competency-maps/sales-competencies.md` or `competency-maps/technical-competencies.md` — to
  identify which competencies are not yet demonstrated at the required tier.
- This produces a personal gap list, which is the seed of the adaptive path (Article IV) without
  requiring a central pathing function.

### B2. Assemble a path from the modular catalog
- Treat the competencies in scope as a **catalog** of modular units. Each individual assembles a
  path from the units that close their gaps — nothing more, nothing less.
- Sequence Foundational before Practitioner; reserve Advisor for those who will later seed a
  trainer population (the bridge to Path A).

### B3. Build the assessment
- Use `templates/assessment-builder-template.md` to build a demonstration for each competency in
  scope. The template is designed so a non-specialist can produce a credible, scenario-based
  assessment (Article V) without instructional-design expertise.
- Keep assessments demonstration-based even in self-serve mode — completion is not competency.

### B4. Roll out directly to the field
- Publish the catalog, paths, and assessments to the field. Individuals progress through their
  own paths and submit demonstrations for evaluation.
- Where maturity allows, AI assists both the individual (assembling and tailoring their path) and
  the evaluation of demonstrations — this is how Path B scales without a trainer population.

### B5. Certify by demonstration and record it
- Record demonstrated competency per individual per competency and tier. Even without central
  L&D, this record is what keeps paths adaptive and prevents re-teaching.

### B6. Report against outcomes
- The local owner rolls up results against the ratified outcome signals (Article VIII). Keep this
  lightweight but real — a single outcome signal tracked honestly beats a dashboard of vanity
  metrics.

## Where AI raises the ceiling

Path B is where AI leverage matters *most*, because there is no trainer population to absorb the
work. As the organization climbs the maturity model:

- **L1–L2:** AI assembles each individual's path from the catalog and tailors examples to their
  role and vertical — replacing the pathing work a central L&D function would otherwise do.
- **L3:** AI administers and scores demonstrations, which is what makes demonstration-based
  certification feasible without dedicated assessors.
- **L4–L5:** the catalog and assessments stay current automatically, and the system learns which
  units correlate with outcomes.

In effect, AI is the substitute for the L&D function the organization does not have. This is the
clearest expression of asymmetric scaling in the kit.

## Common failure modes

- **Reverting to completion.** Without trainers watching, the path of least resistance is to mark
  modules complete. Keep certification demonstration-based.
- **Over-scoping personal paths.** Self-identified paths can balloon. Constrain each path to the
  demonstrated gaps, nothing more (Article IV).
- **No owner.** "Self-serve" still needs a named local owner for outcomes; fully ownerless
  rollouts decay.

## Graduating to Path A

Path B is often a stepping stone. As individuals reach the **Advisor** tier, they become the seed
of a trainer population — at which point the organization can adopt **Path A**
(`playbook/path-a-trainer-cascade.md`) and gain multiplicative reach.
