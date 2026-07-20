# Task chain

This task chain defines the approved order of work for `qsio-kernel`. It distinguishes the implemented `0.1.0` reference kernel from proposed hardening and prevents conceptual QSO or A.L.I.S.T.A.I.R.E. language from silently expanding runtime authority.

## Status legend

- **Complete** — implemented and represented by repository evidence.
- **In progress** — bounded work is underway but release evidence is incomplete.
- **Blocked** — requires an architectural decision or prerequisite.
- **Proposed** — not authorized for implementation by this document alone.
- **Not authorized** — expressly outside present scope.

## P0 — Executable semantic baseline

**Status: Complete for the prototype baseline**

Evidence in the repository:

- Python 3.12 package structure and console entry point.
- QSO, QSOState, QSI, QSIO, transition, witness, canon, Telion, Memora, Nexis, and epistemic-value records.
- Domain-separated canonical content hashing.
- Authorized genesis flow.
- Ordinary state transitions over visible `lumen` state.
- Rejected QSIO records for core validation failures.
- Quietus and resume lifecycle operations.
- In-memory ledger and state history.
- Replay of final state hashes.
- Four-QSO deterministic demonstration.
- Tests for canon rejection, Quietus/resume, replay, provenance, and default security boundaries.

P0 does not establish production readiness, durable evidence, comprehensive authorization, independent attestation, or external authority.

## P1 — Documentation and contract foundation

**Status: In progress**

Completed in the documentation candidate:

- [x] Project overview and explicit non-capabilities.
- [x] Pages-ready documentation structure and navigation.
- [x] Architecture, runtime-flow, lifecycle, trust-boundary, and portfolio diagrams.
- [x] Design and invariant reference.
- [x] Public API guide.
- [x] Developer onboarding and debugging guidance.
- [x] Local operations, evidence, incident-triage, and rollback runbook.
- [x] Security posture and limitations.
- [x] A.L.I.S.T.A.I.R.E. integration role and authority boundary.
- [x] Architecture decision records for kernel boundaries and proposed portfolio role.
- [x] Task-chain, release, and changelog alignment.
- [x] Exact-head documentation workflow implemented.

Evidence still required before P1 is complete:

- [ ] Exact-head strict documentation build passes on the final submitted commit.
- [ ] Rendered-site and evidence artifacts are retained and identified.
- [ ] Internal links and generated-site boundary checks pass.
- [ ] Formal schema fixtures exist for all public records.
- [ ] Compatibility statement for `0.x` consumers is approved.
- [ ] Published Pages URL and publication authority are recorded, if Pages is enabled.
- [ ] Accessibility review is recorded for the published site.

## P1A — Canonical portfolio role

**Status: Blocked pending architecture clarification**

The A.L.I.S.T.A.I.R.E. portfolio must select one role for this repository:

1. canonical low-level semantic kernel;
2. conformance implementation for another canonical runtime;
3. migration source whose accepted concepts move into `QuantumStateObjects` or another repository; or
4. independent research prototype.

The decision must designate:

- canonical repository and package identity;
- QSO/QSI/QSIO schema and compatibility owner;
- relationship to `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC`;
- capability issuer and revoker;
- release, incident, emergency-stop, and rollback authority; and
- boundary with the autonomous-development control plane.

No documentation in this repository resolves those ownership questions by itself.

## P2 — Verification hardening

**Status: Proposed**

Bounded objectives:

- expand malformed-input and rejection-path coverage;
- test every public record's canonical serialization and hash fixture;
- test replay through intermediate QSIO boundaries;
- test corrupted hashes, stale preconditions, parent-link divergence, and unverified witnesses;
- define whether lifecycle errors return rejected records or remain exceptions;
- prove deterministic results across supported Python environments;
- add static typing, packaging, and dependency checks to CI; and
- map every implemented invariant to a named test and release gate.

P2 must not add persistence, network access, external authority, or autonomous repository behavior.

## P3 — Local persistence design

**Status: Blocked pending architecture approval**

Questions requiring decisions before implementation:

- What is the canonical durable ledger format?
- Is storage append-only, event-sourced, snapshot-based, or layered?
- What is the migration and corruption-recovery policy?
- How are timestamps represented without breaking deterministic replay?
- What constitutes an authoritative ledger root?
- What data may be redacted, compacted, or retained?
- How are schema versions and unsupported records handled?
- Which repository owns storage adapters and operational recovery?

Any persistence work must remain local unless networking is separately approved.

## P4 — Authorization and independent verification

**Status: Blocked pending authority and threat-model approval**

Potential work includes capability enforcement, signer identity, independent witnesses, revocation, expiry, key rotation, evidence classification, and verification policy. Existing `PermissionSet` and witness records are data structures, not authorization to claim production access control or independent attestation.

P4 requires named external owners for:

- identity and capability issuance;
- revocation and emergency stop;
- key and credential custody;
- witness independence and trust policy;
- audit retention and privacy; and
- incident response and rollback.

## P5 — External integration or federation

**Status: Not authorized**

The following are outside current scope:

- network services;
- external model or tool execution;
- filesystem or subprocess authority;
- autonomous QSO spawning;
- distributed consensus;
- payment or credential operations;
- cross-repository canonical authority;
- continuous self-modification; and
- self-authorized repository, merge, release, or deployment actions.

A future proposal must define users, operators, data classes, authority, inputs, outputs, failure containment, privacy, observability, rollback, and repository boundaries before implementation begins.

## Change-control rule

A pull request that changes runtime semantics must:

1. identify the task-chain phase it advances;
2. update tests and fixtures;
3. update relevant design, API, security, operations, and integration documentation;
4. update `release.md` without prematurely passing gates;
5. add an `Unreleased` changelog entry;
6. state compatibility, migration, privacy, authority, and rollback impact;
7. identify any cross-repository contract change; and
8. add or update an ADR when ownership or an architectural boundary changes.

A documentation-only pull request must build strictly from its immutable submitted head and may not mark non-documentation gates complete without corresponding evidence.