# Engagement Lifecycle

> **Instantiation layer.** This is the operating procedure for an engagement. The six stages are
> stable; the specific activities, owners, and timelines should be adapted to your organization.

The engagement lifecycle is how the framework is applied in practice. It is the procedure an
accelerating partner — or an organization enabling itself — follows to move up the maturity model
(`constitution/02-maturity-model.md`) under the discipline of the Articles.

The lifecycle is a loop, not a project plan. Its six stages mirror the constitutional layers:

```
   ┌──────────────────────────────────────────────────────────────────┐
   │                                                                    │
   ▼                                                                    │
ASSESS ──► RATIFY ──► INSTANTIATE ──► OPERATE ──► ENFORCE ──► AMEND ────┘
(diagnose) (agree on  (derive the     (deliver   (verify     (feed
           principles) org-specific    adaptive   demonstrated learning
                       programs)        paths)     competency)  back)
```

---

## 1. Assess — *locate the organization*

**Purpose:** establish where the organization is and where this engagement will take it.

- Run the **maturity self-assessment** (`assessment/maturity-self-assessment.md`).
- Apply **scoring and routing** (`assessment/scoring-and-routing.md`) to produce three outputs:
  current placement, target placement (typically +1 to +2 levels), and recommended path (A or B).
- Identify the binding constraint from the section diagnostics (foundations, AI leverage, or
  governance).

**Exit criterion:** current placement, target placement, and recommended path are documented and
agreed.

## 2. Ratify — *agree on the constitution*

**Purpose:** secure leadership agreement to the Articles as the organization's enablement
standard. This is the step that makes everything downstream legitimate.

- Walk leadership through the **Articles** (`constitution/01-articles.md`) and the **executive
  one-pager** (`playbook/executive-one-pager.md`).
- Confirm which Articles need local interpretation and capture any **local statutes** the
  organization wishes to add (permitted as long as they do not contradict an Article — Article
  VII).
- Agree the **outcome signals** by which success will be judged (Article VIII).

**Exit criterion:** leadership has ratified the Articles and named the outcome signals.

## 3. Instantiate — *derive the organization-specific program*

**Purpose:** turn the durable principles into a concrete, branded, organization-specific program.

- Customize the kit: complete `brand.yaml` and run `customize.py` to produce a branded copy
  (`dist/`). This applies the organization's language, examples, and product references.
- Select the relevant competencies from the **sales** and **technical** maps for the roles in
  scope, and set the required proficiency tier per role.
- This is where AI leverage is introduced or deepened, in line with the target maturity level —
  using AI to author, assemble, and tailor the program rather than hand-building it.

**Exit criterion:** a branded, role-specific program exists, traceable to the competency maps.

## 4. Operate — *deliver adaptive paths*

**Purpose:** deliver enablement to the field via the recommended path.

- **Path A — Trainer Cascade** (`playbook/path-a-trainer-cascade.md`): enable the
  train-the-trainer population (Advisor tier), who cascade to the wider field.
- **Path B — Self-Serve Catalog** (`playbook/path-b-self-serve.md`): the field self-identifies
  gaps, assembles paths from the catalog, and proceeds directly.
- In both paths, partners receive **adaptive paths** (Article IV) — only the competencies they
  have not yet demonstrated at the required tier.

**Exit criterion:** the field is progressing through paths aligned to the competency maps.

## 5. Enforce — *verify demonstrated competency*

**Purpose:** certify capability by demonstration, not completion.

- Administer demonstrations built from `templates/assessment-builder-template.md` (Article V).
- Record demonstrated competency per partner per competency and tier, so future paths can adapt
  (Article IV depends on this record existing).
- Where the target maturity level supports it, AI administers and scores demonstrations at scale
  (Article VI / maturity L3+).

**Exit criterion:** competency is recorded against demonstrations, and certification reflects
demonstrated ability.

## 6. Amend — *feed learning back*

**Purpose:** close the loop and improve both the local program and the shared core.

- Compare results against the ratified **outcome signals** (Article VIII). Where the data is
  clear, adjust the instantiation (content, paths, assessments).
- Where an improvement is durable and portable, propose it back to the constitutional core via
  the **amendment process** (`constitution/03-amendment-process.md`) and `CONTRIBUTING.md`.
- Re-enter **Assess**: the organization has moved, and the next target can be set.

**Exit criterion:** outcome data has been acted upon locally, and any durable improvement has
been proposed upstream.

---

## Running the loop well

- **Movement, not perfection.** Each pass targets one or two levels of progress, not an
  end-state. The loop is meant to be run repeatedly.
- **The Articles are the guardrails.** Every stage decision should trace to an Article. AI applied
  without that discipline accelerates the wrong work (see the maturity model).
- **Path is not destiny.** An organization on Path B can use the loop to build a trainer
  population and graduate to Path A.
