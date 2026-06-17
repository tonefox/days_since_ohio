# Constitution — The Amendment Process

> **Constitutional layer.** This document defines how the durable core itself changes. It is the
> mechanism that keeps the framework current without letting it drift.

The constitution is durable, not frozen. The amendment process is how it evolves as the ecosystem
learns — and how the framework reconciles a single shared standard with the local sovereignty of
every organization that adopts it (Article VII).

## What is amendable, and what is not

| Element | Stability | How it changes |
| --- | --- | --- |
| The eight Articles | Highest | Formal amendment only (this process) |
| The maturity model | High | Formal amendment only |
| Competency maps | Medium | Versioned revisions, reviewed against the Articles |
| Assessment items, playbook tactics, templates | Lower | Routine updates in the instantiation layer |
| Brand, language, examples, product references | Continuous | Local customization via `brand.yaml` — never an amendment |

Local customization is **not** amendment. An organization changing its brand, voice, vertical
examples, or product references is exercising federated sovereignty and requires no upstream
process. Amendment is reserved for changes to the shared durable core.

## The two directions of change

Because the kit is designed for "build for both" distribution (standalone use *and*
fork-and-amend), change flows in two directions:

**Downstream (upstream → fork).** When the accelerating partner publishes a new version of the
constitution, downstream organizations choose when to adopt it. The kit's separation of the
constitutional core from local customization (`brand.yaml`, local examples) is what makes this a
clean merge rather than a manual reconciliation. Versioning is tracked in `CHANGELOG.md`.

**Upstream (fork → upstream).** When a downstream organization discovers an improvement — a
sharper Article phrasing, a missing competency, a maturity-model refinement validated by outcome
data — it proposes that change back to the core via the contribution process in
`CONTRIBUTING.md`. This is how the flywheel (L5) operates at the *ecosystem* level, not just
within a single organization.

## The amendment standard

A proposed amendment to the Articles or the maturity model should be evaluated against four
tests. An amendment should pass all four:

1. **Durability.** Does the change remain true across technologies, vendors, and product cycles?
   If it only holds for the current product or AI capability, it belongs in the instantiation
   layer, not the constitution.

2. **Outcome evidence.** Is the change supported by outcome signals (Article VIII) — observed
   correlation with qualified pipeline, win rates, successful implementations, or retention —
   rather than opinion or preference alone?

3. **Non-contradiction.** Does the change cohere with the remaining Articles, or does it
   undermine one of them? The Articles are designed to be mutually reinforcing; an amendment must
   preserve that.

4. **Portability.** Can the change be expressed without reference to a specific organization's
   brand, vertical, or product? If not, it is a local statute, not a constitutional amendment.

## Procedure

1. **Propose.** Open a proposal describing the change, the Article(s) affected, and the outcome
   evidence supporting it (see `CONTRIBUTING.md` for the mechanics in a forked setup).
2. **Test.** Evaluate the proposal against the four-part amendment standard above.
3. **Review.** The maintainers of the constitutional core review the proposal. Federated input
   from adopting organizations is solicited for changes to the Articles or maturity model.
4. **Ratify and version.** Accepted amendments are merged into the core, the version is
   incremented, and the change is recorded in `CHANGELOG.md` with its rationale and evidence.
5. **Propagate.** Downstream organizations adopt the new version on their own cadence, re-running
   `customize.py` to re-apply local branding on top of the updated core.

## Cadence

The Articles and maturity model should be reviewed on a deliberate, infrequent cadence — annually
is typical — plus on demand when strong outcome evidence warrants it. Instantiation-layer
elements (assessment items, playbook tactics, templates) are expected to change far more often
and do not require this process. Resisting the temptation to amend the durable core frequently is
itself a discipline: the value of the constitution is precisely that it does not move with every
product release.
