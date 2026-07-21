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
- Portfolio obstruction and gluing analysis with 18 material incompatibilities, eight pairwise contract edges, and eight required triple-overlap witness groups.
- Release and integration punch list converting architecture, compatibility, authority, privacy, security, recovery, and publication gaps into bounded P0–P5 work.
- ADR 0002 proposing the interim portfolio role and identifying canonical-runtime options.
- Repository task chain and expanded release-readiness plan.
- Exact-head strict documentation workflow with source-identity assertion, generated-site boundary checks, SHA-256 evidence, and retained rendered-site artifacts.

### Clarified

- Version `0.1.0` is an in-memory experimental reference kernel, not a production agent platform, autonomous-development control plane, portable device-security system, or hosted service.
- `qsio-kernel` is a candidate canonical semantic kernel, reference conformance implementation, migration source, or independent research prototype until the portfolio chooses one durable role.
- The lowest-overlap candidate is a small conformance implementation, but no role has been approved.
- Repository `0` local proposal state is non-authoritative; execution begins only after Repository `1` or another approved authority admits a task and issues a narrow capability.
- Local `PermissionSet` data, canon values, witness records, successful transitions, and QSIO hashes do not grant external authority.
- Local execution outcome, evidence verification, policy evaluation, canonical disposition, and later correction or revocation are separate states.
- QSO-GENOMES declarative identity does not create operational admission.
- QSO-FABRIC experiment aggregation does not create canonical state or redefine kernel hashes and lifecycle semantics.
- Bridge transport and QSO-STUDIO/AionUi interaction do not create authority by transport or display alone.
- Forbidden transition keys are semantic validation controls rather than an operating-system sandbox.
- Witnesses are generated in process and are not independent attestations or signatures.
- Permission types exist, but comprehensive capability issuance, revocation, and enforcement are not implemented in the main execution path.
- Deterministic timestamps provide prototype logical ordering and are not externally verified wall time, freshness, or expiry evidence.
- Quietus is a local lifecycle control distinct from portfolio freeze, capability revocation, quarantine, emergency stop, and recovery.
- Persistence, networking, external execution, federation, autonomous spawning, repository modification, and production authority remain outside current scope.
- A documentation artifact proves renderability of the reviewed source, not runtime correctness, accessibility, compatibility, conformance, or production readiness.

### Changed

- Expanded the Pages information architecture to include obstruction and gluing analysis alongside ontology, terminology, lifecycle, operations, threat model, integration guidance, and architecture decisions.
- Reconciled `README.md`, `docs/index.md`, `docs/alistaire-integration.md`, `taskchain.md`, `punchlist.md`, `release.md`, `mkdocs.yml`, and this changelog around current portfolio contracts and unresolved ownership.
- Added release gates for machine-readable schemas, canonical bytes, reason codes, clock domains, pairwise gluing profiles, triple-overlap witnesses, correction, revocation, privacy, retention, emergency stop, and recovery.
- No runtime behavior, schema, package interface, adapter, credential, capability, persistence, network route, canonical-state authority, publication, release, or deployment changed in this documentation milestone.

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
