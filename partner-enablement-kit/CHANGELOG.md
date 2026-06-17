# Changelog

All notable changes to the **constitutional core** of this kit are recorded here. The version
applies to the durable core — the Articles, the maturity model, and the amendment process — and is
referenced by `customize.py` when stamping branded copies.

Versioning follows [Semantic Versioning](https://semver.org/):

- **MAJOR** — a breaking change to an Article or the maturity model.
- **MINOR** — an additive change (new competency, new path guidance, clarified Article).
- **PATCH** — editorial fixes that do not change meaning.

Local customization via `brand.yaml` is **not** a version change — see
`constitution/03-amendment-process.md`.

## [1.0.0] — Initial release

### Added
- **Constitution:** preamble, the eight Articles, the L0–L5 maturity model, and the amendment
  process.
- **Assessment:** maturity self-assessment and scoring/routing logic (routes to Path A or Path B).
- **Competency maps:** sales and technical, expressed as demonstrable outcomes across three
  proficiency tiers.
- **Playbook:** the Assess → Ratify → Instantiate → Operate → Enforce → Amend engagement
  lifecycle, the two delivery-path run-guides, and an executive one-pager.
- **Templates:** assessment builder and session plan.
- **Customization:** `brand.yaml` + `customize.py` for white-labeling, with `--check` validation.
- **Distribution:** standalone-usable and fork-and-amend ready, with `CONTRIBUTING.md`.
