# Task chain

This task chain defines the approved order of work for `qsio-kernel`. It distinguishes the implemented `0.1.0` reference kernel from proposed hardening and prevents conceptual QSO language from silently expanding runtime authority.

## Status legend

- **Complete** — implemented and represented by repository evidence.
- **In progress** — bounded work is underway but release evidence is incomplete.
- **Blocked** — requires an architectural decision or prerequisite.
- **Proposed** — not authorized for implementation by this document alone.

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
- Tests for canon rejection, Quietus/resume, and replay.

P0 does not establish production readiness.

## P1 — Documentation and contract foundation

**Status: In progress**

Required outcomes:

- [x] Project overview and scope boundaries.
- [x] Pages-ready documentation structure.
- [x] Architecture and trust-boundary diagrams.
- [x] Design and invariant reference.
- [x] Public API guide.
- [x] Developer onboarding.
- [x] Security posture and limitations.
- [x] Task-chain, release, and changelog alignment.
- [ ] Automated documentation link/render check.
- [ ] Formal schema fixtures for all public records.
- [ ] Compatibility statement for `0.x` consumers.

## P2 — Verification hardening

**Status: Proposed**

Bounded objectives:

- expand malformed-input and rejection-path coverage;
- test every public record's canonical serialization and hash fixture;
- test replay through intermediate QSIO boundaries;
- test corrupted hashes, stale preconditions, and unverified witnesses;
- define whether lifecycle errors return rejected records or remain exceptions;
- prove deterministic results across supported Python environments; and
- add static typing, packaging, and dependency checks to CI.

P2 must not add persistence, network access, or external authority.

## P3 — Local persistence design

**Status: Blocked pending architecture approval**

Questions requiring decisions before implementation:

- What is the canonical durable ledger format?
- Is storage append-only, event-sourced, snapshot-based, or layered?
- What is the migration and corruption-recovery policy?
- How are timestamps represented without breaking deterministic replay?
- What constitutes an authoritative ledger root?
- What data may be redacted, compacted, or retained?

Any persistence work must remain local unless networking is separately approved.

## P4 — Authorization and independent verification

**Status: Blocked pending authority and threat-model approval**

Potential work includes capability enforcement, signer identity, independent witnesses, revocation, expiry, key rotation, and verification policy. Existing `PermissionSet` and witness records are data structures, not authorization to claim production access control or independent attestation.

## P5 — External integration or federation

**Status: Not authorized**

The following are outside current scope:

- network services;
- external model or tool execution;
- filesystem or subprocess authority;
- autonomous QSO spawning;
- distributed consensus;
- payment or credential operations;
- cross-repository canonical authority; and
- self-modifying or continuously running agents.

A future proposal must define users, operators, data classes, authority, inputs, outputs, failure containment, privacy, observability, rollback, and repository boundaries before implementation begins.

## Change-control rule

A pull request that changes runtime semantics must:

1. identify the task-chain phase it advances;
2. update tests and fixtures;
3. update relevant design and API documentation;
4. update `release.md` without prematurely passing gates;
5. add an `Unreleased` changelog entry; and
6. state any compatibility or migration impact.
