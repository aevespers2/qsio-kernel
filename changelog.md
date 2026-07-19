# Changelog

All notable repository changes should be recorded here. The format is based on Keep a Changelog, and the project uses semantic versioning as an intent rather than a compatibility guarantee during the `0.x` series.

## Unreleased

### Added

- GitHub Pages-ready documentation landing page and navigation.
- Expanded project overview and explicit non-goals.
- Architecture, runtime-flow, component, lifecycle, and trust-boundary diagrams.
- Design reference for QSO state, QSI requests, transitions, witnesses, hashing, validation, replay, determinism, and permissions.
- Public API guide for records, runtime operations, lifecycle controls, replay, and exceptions.
- Developer onboarding, local setup, test workflow, contribution rules, and debugging guidance.
- Security posture, threat model, limitations, safe-operation guidance, and future security gates.
- Repository task chain and release-readiness plan.

### Clarified

- Version `0.1.0` is an in-memory experimental reference kernel, not a production agent platform.
- Forbidden transition keys are semantic validation controls rather than an operating-system sandbox.
- Witnesses are generated in-process and are not independent attestations or signatures.
- Permission types exist, but comprehensive capability enforcement is not yet implemented in the main execution path.
- Deterministic timestamps provide prototype ordering and are not externally verified wall time.
- Persistence, networking, external execution, federation, autonomous spawning, and production authority remain outside current scope.

### Changed

- No runtime behavior changed in this documentation milestone.

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
- Tests for forbidden canon requests, Quietus/resume behavior, QSIO verification, and replayed final-state hashes.
