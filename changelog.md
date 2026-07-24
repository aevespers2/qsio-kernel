# Changelog

All notable repository changes should be recorded here. The format is based on Keep a Changelog, and the project uses semantic versioning as an intent rather than a compatibility guarantee during the `0.x` series.

## Unreleased

### Added

- GitHub Pages-ready documentation landing page and expanded navigation.
- Expanded project overview and explicit non-goals.
- Architecture, runtime-flow, component, lifecycle, trust-boundary, and A.L.I.S.T.A.I.R.E. portfolio diagrams.
- Design reference for QSO state, QSI requests, transitions, witnesses, hashing, validation, replay, determinism, and permissions.
- Public API guide for records, runtime operations, lifecycle controls, replay, and exceptions.
- Developer onboarding, local setup, test workflow, contribution rules, and debugging guidance.
- Local operations, evidence-capture, incident-triage, recovery, and rollback runbook.
- Security posture, threat model, limitations, safe-operation guidance, and future security gates.
- A.L.I.S.T.A.I.R.E. integration guide aligned with the current Repository `0` proposal/orchestration and Repository `1` capability/canonical-disposition model.
- Runtime Conformance Boundary Profile defining the candidate neutral-contract → reference-kernel → canonical-runtime split, identity separation, explicit mappings, fixture classes, and triple-overlap witnesses.
- Kernel-to-runtime crosswalk decision packet with exact semantic, explicit projection, unsupported-route, and migration-source options.
- Machine-readable `qsio.kernel-runtime-crosswalk-options.v1` profile defining field dispositions, fail-closed conditions, authority denials, acceptance gates, and FYSA-120 mapping.
- Accessibility review and exact-head evidence protocol covering structural checks, manual keyboard and assistive-technology review, diagram–prose equivalence, zoom/reflow, contrast, finding severity, correction, supersession, withdrawal, rollback, and independently verified restoration.
- Machine-readable `qsio.documentation-accessibility-review.v1` profile defining review states, exact-generation bindings, automated and manual review domains, publication gates, authority denials, and FYSA-120 mapping.
- Reusable strict accessibility-documentation validator for profile integrity, heading order, table headers, diagram–prose equivalence, meaningful link text, and lifecycle status consistency.
- ADR 0003 proposing `qsio-kernel` as a small deterministic reference-conformance implementation rather than the broad canonical runtime.
- ADR 0004 preserving the unsupported route as the safe default until an independently reviewed crosswalk is approved.
- Portfolio obstruction and gluing analysis with material incompatibilities, pairwise contract edges, and required triple-overlap witness groups.
- Release and integration punch list converting architecture, compatibility, authority, privacy, security, accessibility, recovery, conformance, support, and publication gaps into bounded P0–P5 work.
- Repository task chain and expanded release-readiness plan.
- Exact-head strict documentation workflow with source-identity assertion, generated-site boundary checks, SHA-256 evidence, retained rendered-site artifacts, and structural accessibility validation.

### Clarified

- Version `0.1.0` is an in-memory experimental reference kernel, not a production agent platform, autonomous-development control plane, portable device-security system, or hosted service.
- The lowest-overlap candidate role is a small reference-conformance implementation beneath a separately governed neutral contract and an explicitly approved canonical runtime.
- The conformance candidate does not approve QuantumStateObjects or another repository as the canonical runtime; that decision remains external and blocked.
- A passing fixture demonstrates agreement only for the exact contract, mapping, fixture set, kernel source, runtime source, and configuration under test.
- Contract profile, fixture set, genome projection, runtime admission, capability, conformance run, QSI, QSIO, runtime execution, receipt, canonical disposition, correction, revocation, and recovery checkpoint identities must remain distinct.
- Similarly named QSO/QSI/QSIO fields across repositories are not equivalent without an approved mapping and shared fixtures.
- Every crosswalk field must be classified as `EXACT`, `TRANSFORM`, `PROJECT`, `UNSUPPORTED`, `UNKNOWN`, or `LOSSY_REJECTED`; missing, ambiguous, and lossy mappings fail closed.
- The unsupported route is an affirmative safe disposition, not a documentation failure or temporary warning.
- Repository `0` local proposal state is non-authoritative; execution begins only after Repository `1` or another approved authority admits a task and issues a narrow capability to a canonical runtime.
- Local `PermissionSet` data, canon values, witness records, successful transitions, conformance witnesses, and QSIO hashes do not grant external authority.
- Local execution outcome, conformance result, evidence verification, policy evaluation, canonical disposition, and later correction or revocation are separate states.
- QSO-GENOMES declarative identity does not create operational admission.
- QSO-FABRIC experiment aggregation does not create canonical state or redefine kernel hashes and lifecycle semantics.
- Bridge transport and QSO-STUDIO/AionUi interaction do not create authority by transport or display alone.
- Forbidden transition keys are semantic validation controls rather than an operating-system sandbox.
- Witnesses are generated in process and are not independent attestations or signatures.
- Permission types exist, but comprehensive capability issuance, revocation, and enforcement are not implemented in the main execution path.
- Deterministic timestamps provide prototype logical ordering and are not externally verified wall time, freshness, or expiry evidence.
- Quietus is a local lifecycle control distinct from portfolio freeze, capability revocation, quarantine, compatibility-claim withdrawal, emergency stop, and recovery.
- Persistence, networking, external execution, federation, autonomous spawning, repository modification, and production authority remain outside current scope.
- A documentation artifact proves renderability of the reviewed source, not runtime correctness, accessibility, compatibility, conformance, or production readiness.
- Automated accessibility checks do not replace manual review, establish certification, determine legal compliance, or authorize publication.
- Accessibility evidence is current only for the exact source and rendered artifact recorded by its packet; a later source change makes the prior result historical.
- `REVIEWED_NO_KNOWN_BLOCKERS` means no blocking finding was identified under the recorded conditions, not that every environment or user need was tested.

### Changed

- Expanded the Pages information architecture to include the runtime conformance boundary, kernel-to-runtime crosswalk options, exact-head accessibility review evidence, and ADRs 0003–0004 alongside obstruction and gluing analysis, ontology, terminology, lifecycle, operations, threat model, integration guidance, and architecture decisions.
- Reconciled `README.md`, `taskchain.md`, `punchlist.md`, `release.md`, `mkdocs.yml`, and this changelog around the candidate reference-conformance role, explicit unsupported route, accessibility non-certification boundary, and unresolved neutral-contract/canonical-runtime ownership.
- Reframed gluing witnesses around QSO-GENOMES → neutral contract → kernel, neutral contract → kernel → canonical runtime, Repository `0` → Repository `1` → canonical runtime, kernel → canonical runtime → Fabric, evidence interpretation → runtime → kernel, transport/review, stop/recovery, and correction/replay triples.
- Added release gates for field-level mapping dispositions, unsupported and lossy routes, canonical runtime identity, neutral mappings, compatibility claims, claim expiry and withdrawal, independent compatibility review, fixture-vector privacy, mapping-confusion tests, exact-artifact accessibility review, finding preservation, site withdrawal, rollback, and restored-state verification.
- Extended the established Documentation workflow to execute the accessibility validator, retain both profiles and the automated result, write generated state outside the checkout, assert tracked-source cleanliness, and include the accessibility outcome in the terminal fail-closed gate.
- No runtime behavior, schema, package interface, adapter, credential, capability, persistence, network route, canonical-state authority, compatibility claim, accessibility certification, Pages publication, release, or deployment changed in this documentation milestone.

## 0.1.0 — 2026-07-19

### Added

- First executable QSO/QSIO semantic kernel.
- Python package and `qsio-demo` entry point.
- QSO and QSO state records.
- QSI request and QSIO result envelopes.
- Canon, Telion, Memora, Nexis, transition, witness, validation, and epistemic-value records.
- Domain-separated content hashing and canonical serialization.
- Authorized genesis and ordinary transition execution.
- Quietus and resume lifecycle operations.
- In-memory ledger, state history, verification, and replay.
- Four-QSO Explorer, Archivist, Skeptic, and Synthesist demonstration.
- Tests for forbidden canon requests, Quietus/resume behavior, QSIO verification, provenance, default security boundaries, and replayed final-state hashes.
