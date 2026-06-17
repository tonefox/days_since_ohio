# Technical Competency Map

> **Instantiation layer.** This map expresses the constitution's principles as demonstrable
> outcomes for partner **technical** roles (solution engineers, architects, implementation and
> support staff). The competencies are durable; examples and product references should be adapted
> via `brand.yaml`.

This map is the technical counterpart to the sales competency map. It instantiates the **same
constitution** for a different role (Article VII — same principles, different instantiation).
Every competency is a demonstrable outcome (Article I), written against customer requirements
rather than product features (Article II), and certified by demonstration (Article V). "AI
fluency in the role" is standing, not elective (Article VI).

## How to read this map

- **Competency** — what the technical practitioner must be able to do.
- **Demonstration** — how it is proven, under realistic conditions.
- **Outcome signal** — the result it should move (Article VIII).

Proficiency tiers — **Foundational → Practitioner → Advisor** — are defined at the end and mirror
the sales map.

---

## Domain 1 — Discovery and Design

### T1. Elicit technical requirements and constraints
- **Demonstration:** given a customer scenario, elicit functional and non-functional requirements
  (reliability, security, scale, integration constraints) and separate true requirements from
  assumptions.
- **Outcome signal:** rework rate later in the implementation; design-stage rejections.

### T2. Design a fit-for-purpose solution architecture
- **Demonstration:** produce an architecture that meets the elicited requirements, justify the
  trade-offs, and articulate why it fits *this* customer rather than presenting a generic
  reference design.
- **Outcome signal:** proof-of-concept success rate; architecture acceptance.

### T3. Map the solution to business outcomes
- **Demonstration:** connect technical design decisions back to the customer's business outcomes,
  in language a non-technical stakeholder can act on — the technical complement to sales value
  articulation.
- **Outcome signal:** technical-win-to-business-win conversion.

## Domain 2 — Demonstration and Proof

### T4. Deliver a credible demonstration or proof of concept
- **Demonstration:** scope, build, and run a demo or POC against the customer's success criteria,
  and handle objections and live failure gracefully.
- **Outcome signal:** POC-to-commit conversion; POC cycle time.

### T5. Integrate within a realistic environment
- **Demonstration:** design and validate an integration against representative systems and
  constraints, anticipating failure modes and operational requirements.
- **Outcome signal:** implementation success rate; post-go-live incident rate.

## Domain 3 — AI Fluency in the Technical Role (Article VI)

### T6. Use AI to accelerate solution design and prototyping
- **Demonstration:** use AI tools to accelerate architecture drafting, configuration, and
  prototyping, and critically review the output for correctness, security, and fit before
  relying on it.
- **Outcome signal:** design and prototyping cycle time.

### T7. Design AI-enabled solutions for customers
- **Demonstration:** where relevant, incorporate AI capabilities into the customer solution
  appropriately — identifying suitable use cases, data and integration implications, and
  limitations.
- **Outcome signal:** adoption and value realization of delivered AI use cases.

### T8. Apply AI responsibly and within guardrails
- **Demonstration:** recognize data-handling, security, and reliability risks of AI tools and
  AI-enabled solutions, and follow the organization's responsible-use and security guardrails.
- **Outcome signal:** security/compliance exceptions (trending down).

## Domain 4 — Implementation and Enablement of Others

### T9. Lead a successful implementation
- **Demonstration:** plan and govern an implementation to the customer's success criteria,
  managing risk, scope, and operational handover.
- **Outcome signal:** time-to-value; customer retention and expansion.

### T10. Troubleshoot under realistic pressure
- **Demonstration:** diagnose and resolve a realistic failure scenario methodically, and document
  the resolution so it strengthens the shared knowledge base.
- **Outcome signal:** mean time to resolution; recurrence rate.

---

## Proficiency tiers

| Tier | Definition |
| --- | --- |
| **Foundational** | Can perform the competency in a structured scenario with guidance. |
| **Practitioner** | Performs independently in realistic conditions with sound judgment. |
| **Advisor** | Performs under high complexity and ambiguity, and can coach others — the train-the-trainer tier for Path A. |

## Using this map

- **Assessment:** each demonstration maps to a scenario, lab, or artifact built from
  `templates/assessment-builder-template.md`.
- **Pathing:** a practitioner's adaptive path (Article IV) is the set of competencies not yet
  demonstrated at the required tier.
- **Train-the-trainer (Path A):** the **Advisor** tier defines who can cascade technical
  enablement to the wider field.
- **Accountability:** programs report against the **outcome signals** above, not against
  completion.
