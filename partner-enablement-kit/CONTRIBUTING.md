# Contributing & Federated Governance

This kit is designed for **"build for both"** distribution: it works as a clean standalone
download, and it is structured so downstream organizations can fork it, customize it locally, and
contribute improvements back upstream. This document explains how change flows in both directions.

It is the operational companion to `constitution/03-amendment-process.md`.

## The two layers you are working with

| Layer | Files | Who owns it | How it changes |
| --- | --- | --- | --- |
| **Constitutional core** | `constitution/`, the competency maps, the playbook, templates | Maintained upstream (the accelerator) | Amendment process + this guide |
| **Local customization** | `brand.yaml`, anything you add under `assets/`, local statutes | You (the adopting org) | Freely — exercise of federated sovereignty |

Keeping these separate is what makes upstream updates a clean merge. **Do not hand-edit the core
to inject branding** — put branding in `brand.yaml` and let `customize.py` apply it.

## Downstream: adopting upstream updates

When a new version of the constitution is published (see `CHANGELOG.md`):

1. Pull or merge the updated core into your fork.
2. Re-run `python3 customize.py` to re-apply your branding on top of the updated core.
3. Run `python3 customize.py --check` to confirm no tokens are left unresolved.
4. Review the `CHANGELOG.md` entry to understand what changed and whether it affects ratified
   local statutes.

Because your branding lives in `brand.yaml`, not in the core files, step 1 rarely produces
conflicts.

## Upstream: proposing an amendment

When you discover an improvement worth sharing across the ecosystem:

1. **Decide the layer.** If the change is specific to your brand, vertical, or product, it is a
   local statute — keep it local. If it is durable and portable, it is a candidate amendment.
2. **Check it against the amendment standard** in `constitution/03-amendment-process.md`:
   durability, outcome evidence, non-contradiction, portability. A proposal should pass all four.
3. **Open a proposal** describing:
   - the change and the file(s) affected;
   - which Article(s) it touches;
   - the **outcome evidence** supporting it (Article VIII) — what result improved, and how you
     know;
   - confirmation it does not contradict another Article.
4. **Engage review.** Maintainers review against the standard; for changes to the Articles or
   maturity model, federated input from adopting organizations is solicited.
5. **Ratify and version.** Accepted changes are merged, the version is incremented per
   `CHANGELOG.md`, and the rationale is recorded.

## Scope discipline

- **Amendments to the Articles and maturity model are rare by design.** Their value is stability.
  Most good ideas belong in the instantiation layer (assessment items, playbook tactics,
  templates), which changes freely without a formal amendment.
- **Local statutes may not contradict an Article** (Article VII). Add freely; contradict nothing.

## Practical conventions

- Keep prose professional and executive-credible; the kit is an enterprise artifact.
- Keep the constitutional core **technology-agnostic** — it must never name a specific product.
- Run `python3 customize.py --check` before proposing changes, so token integrity is preserved.
