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
- A.L.I.S.T.A.I.R.E. integration guide defining the candidate semantic-kernel role, input/output boundaries, autonomous-development relationship, and acceptance gates.
- ADR 0002 proposing the interim portfolio role and identifying canonical-runtime options.
- Repository task chain and release-readiness plan.
- Exact-head strict documentation workflow with source-identity assertion, generated-site boundary checks, SHA-256 evidence, and retained rendered-site artifacts.

### Clarified

- Version `0.1.0` is an in-memory experimental reference kernel, not a production agent platform, autonomous-development control plane, or hosted service.
- `qsio-kernel` is a candidate A.L.I.S.T.A.I.R.E. semantic component until the portfolio chooses a canonical runtime role.
- The relationship to `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC` requires an explicit architecture decision.
- Forbidden transition keys are semantic validation controls rather than an operating-system sandbox.
- Witnesses are generated in process and are not independent attestations or signatures.
- Permission types exist, but comprehensive capability issuance, revocation, and enforcement are not implemented in the main execution path.
- Deterministic timestamps provide prototype ordering and are not externally verified wall time.
- Persistence, networking, external execution, federation, autonomous spawning, repository modification, and production authority remain outside current scope.
- A documentation artifact proves renderability of the reviewed source, not runtime correctness, accessibility, or production readiness.

### Changed

- Expanded the Pages information architecture to include ontology, terminology, lifecycle, operations, threat model, integration guidance, and architecture decisions.
- Reconciled `taskchain.md`, `release.md`, and documentation governance around exact-head evidence and unresolved portfolio ownership.
- No runtime behavior, schema, package interface, or external authority changed in this documentation milestone.

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
