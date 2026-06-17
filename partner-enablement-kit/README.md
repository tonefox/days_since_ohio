# Constitutional Enablement Kit

A portable, AI-era framework for **partner enablement** — packaged as a downloadable,
white-labelable kit an organization can adopt, brand, and run as its own.

The kit is built on a simple thesis: partner enablement should be **technology-agnostic in its
principles** but capable of **asymmetric (super-linear) scaling when AI is applied to the
enablement function itself**. It separates a small, durable *constitution* from an AI-operated
*instantiation*, so the standard travels intact across an ecosystem while each organization tailors
delivery to its own context.

> **Who this is for.** A partner enablement leader who wants a standard they can walk into any
> organization with — and hand *downstream* to partners who then run enablement themselves,
> acting as an accelerator across the ecosystem.

---

## The idea in one minute

- **Constitution, not curriculum.** Eight durable, technology-agnostic Articles define the
  standard. They are written against partner *outcomes*, not product features, so they survive
  product cycles. → `constitution/01-articles.md`
- **Asymmetric scaling.** A six-level maturity model (L0–L5) shows how applying AI to authoring,
  delivery, assessment, and currency drives the marginal cost of enabling each additional partner
  toward zero while quality rises. → `constitution/02-maturity-model.md`
- **Two delivery paths, chosen by a diagnostic.** A self-assessment routes each organization to
  **Trainer Cascade** (if it has L&D) or **Self-Serve Catalog** (if it does not). →
  `assessment/`
- **Demonstrable competency.** Sales and technical competency maps define enablement as what a
  partner can *do*, certified by demonstration, not recall. → `competency-maps/`
- **A repeatable engagement.** Assess → Ratify → Instantiate → Operate → Enforce → Amend. →
  `playbook/engagement-lifecycle.md`
- **White-labelable.** Edit one config file, run one script, get a branded copy. →
  `brand.yaml` + `customize.py`

## Quickstart

```bash
# 1. ASSESS — score the organization and find its delivery path
open assessment/maturity-self-assessment.md      # complete it, then:
open assessment/scoring-and-routing.md            # place on maturity model + route to Path A/B

# 2. BRAND — make the kit your own
$EDITOR brand.yaml                                # set org name, colors, logo, voice, terms
python3 customize.py                              # writes a branded copy to ./dist
python3 customize.py --check                      # verify no unresolved brand tokens remain

# 3. RUN — deliver via the routed path
open playbook/engagement-lifecycle.md             # the end-to-end loop
open playbook/path-a-trainer-cascade.md           # if routed to Path A
open playbook/path-b-self-serve.md                # if routed to Path B
```

`customize.py` requires only Python 3 (standard library — no `pip install`). It never modifies the
source files; it writes a branded copy to `dist/`, so you can keep pulling upstream updates and
re-run it. See `CONTRIBUTING.md`.

## What's in the kit

```
partner-enablement-kit/
├── README.md                  ← you are here
├── brand.yaml                 ← edit this to brand the kit
├── customize.py               ← run this to generate a branded ./dist copy
├── CHANGELOG.md               ← version history of the constitutional core
├── CONTRIBUTING.md            ← federated governance: how to fork, customize, and amend
├── constitution/              ← the durable core
│   ├── 00-preamble.md             why this exists; the asymmetric-scaling thesis
│   ├── 01-articles.md             the eight Articles (the standard)
│   ├── 02-maturity-model.md       L0–L5 and why scaling is asymmetric
│   └── 03-amendment-process.md    how the constitution evolves
├── assessment/                ← the diagnostic + routing
│   ├── maturity-self-assessment.md
│   └── scoring-and-routing.md
├── competency-maps/           ← demonstrable outcomes by role
│   ├── sales-competencies.md
│   └── technical-competencies.md
├── playbook/                  ← how to run an engagement
│   ├── engagement-lifecycle.md
│   ├── path-a-trainer-cascade.md  delivery for orgs WITH L&D
│   ├── path-b-self-serve.md       delivery for orgs WITHOUT L&D
│   └── executive-one-pager.md     leadership buy-in summary
└── templates/                 ← reusable skeletons
    ├── assessment-builder-template.md
    └── session-plan-template.md
```

## How to adopt it

The kit supports two adoption modes, and is built to do both:

- **Standalone download.** Clone or download, run the quickstart, own your copy. No upstream
  relationship required.
- **Fork-and-amend.** Fork it, keep your branding in `brand.yaml`, pull upstream constitution
  updates cleanly, and contribute durable improvements back. This is how the framework improves
  across the whole ecosystem. → `CONTRIBUTING.md`

## Where to start reading

1. `constitution/00-preamble.md` — the argument and the thesis.
2. `constitution/01-articles.md` — the eight principles you will speak to.
3. `playbook/executive-one-pager.md` — the summary you put in front of leadership.
4. `assessment/maturity-self-assessment.md` — the diagnostic you run first in any engagement.
