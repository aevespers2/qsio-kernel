# Task chain

This task chain defines the approved order of work for `qsio-kernel`. It distinguishes the implemented `0.1.0` reference kernel from proposed hardening and prevents conceptual QSO or A.L.I.S.T.A.I.R.E. language from silently expanding runtime authority.

## Status legend

- **Complete** — implemented and represented by repository evidence.
- **In progress** — bounded work is underway but final evidence is incomplete.
- **Blocked** — requires an architectural decision or prerequisite.
- **Proposed** — not authorized for implementation by this document alone.
- **Not authorized** — expressly outside present scope.

## P0 — Executable semantic baseline

**Status: Complete for the prototype baseline**

Evidence in the repository:

- Python 3.12 package structure and console entry point.
- QSO, QSOState, QSI, QSIO, transition, witness, canon, Telion, Memora, Nexis, and epistemic-value records.
- Domain-separated canonical content hashing.
- Authorized local genesis flow.
- Ordinary state transitions over visible `lumen` state.
- Rejected QSIO records for core validation failures.
- Quietus and explicit resume lifecycle operations.
- In-memory ledger and state history.
- Replay of final state hashes.
- Four-QSO deterministic demonstration.
- Tests for canon rejection, Quietus/resume, replay, provenance, and default security boundaries.

P0 does not establish production readiness, durable evidence, comprehensive authorization, independent attestation, external authority, or portfolio canonical state.

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
- [x] Portfolio obstruction and gluing analysis.
- [x] Release and integration punch list.
- [x] Task-chain, punch-list, release, and changelog alignment.
- [x] Exact-head strict documentation workflow implemented.

Evidence still required before P1 is complete:

- [ ] A new exact-head documentation run passes after the final gluing and coordination changes.
- [ ] The retained artifact and digest are recorded for the current immutable pull-request head.
- [ ] Formal machine-readable schema fixtures exist for all public records.
- [ ] Compatibility statement for `0.x` consumers is approved.
- [ ] Diagrams receive semantic and fallback-text review.
- [ ] Published Pages URL, deployment source, publication authority, and rollback owner are recorded if Pages is enabled.
- [ ] Accessibility review is recorded for the published site.

A successful documentation run is valid only for the exact source SHA recorded by that run. Any later source change requires a new passing run.

## P1A — Canonical portfolio role

**Status: Blocked pending architecture clarification**

The portfolio must select one durable role:

1. canonical low-level semantic kernel;
2. reference conformance implementation for another canonical runtime;
3. migration source whose accepted concepts move into `QuantumStateObjects` or another repository; or
4. independent research prototype.

The lowest-overlap candidate is a small conformance implementation, because it preserves deterministic fixture value without duplicating broad runtime ownership. This is a recommendation only.

The decision must designate:

- canonical repository and package identity;
- QSO/QSI/QSIO schema, format, hashing, registry, and compatibility owner;
- relationship to `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC`;
- migration, deprecation, archive, and provenance policy;
- capability issuer and revoker;
- release, incident, emergency-stop, recovery, rollback, and withdrawal authority; and
- boundary with Repositories `0` and `1`.

No documentation in this repository resolves those ownership questions by itself.

## P1B — Cross-repository gluing contracts

**Status: Proposed and blocked on owners**

The obstruction analysis identifies eight pairwise profiles:

1. QSO-GENOMES → `qsio-kernel` genome consumption;
2. Repository `0` → Repository `1` proposal admission;
3. Repository `1` → `qsio-kernel` execution admission;
4. evidence pipeline → `qsio-kernel` reference consumption;
5. `qsio-kernel` → QSO-FABRIC experiment evidence;
6. `qsio-kernel` → Repository `1` result reconciliation;
7. `qsio-kernel` → QSO-STUDIO/AionUi review projection; and
8. `qsio-kernel` → persistence and recovery.

Before integration, the portfolio must also pass eight triple-overlap witness groups:

- genome → kernel → Fabric;
- Repository `0` → Repository `1` → kernel;
- Seeker → temporal interpretation → kernel;
- kernel → Fabric → Repository `1`;
- kernel → Bridge → review interface;
- Quietus → revocation → recovery;
- format registry → canonical runtime → conformance kernel; and
- correction → canonical disposition → replay.

Pairwise adapters alone cannot complete P1B.

## P1C — Contract vocabulary and compatibility

**Status: Proposed**

Required bounded outcomes:

- machine-readable schemas and canonical byte fixtures for every public record;
- supported, unsupported, malformed, stale, replayed, revoked, corrected, superseded, partial, and unknown semantics;
- canonical format and digest rules;
- reason-code and outcome mappings;
- lifecycle crosswalk across active, Quietus, frozen, revoked, quarantined, and recovering states;
- clock domains, temporal provenance, freshness, expiry, and replay rules;
- privacy, retention, redaction, correction, and hash-disclosure policy; and
- `0.x` compatibility, migration, deprecation, and withdrawal rules.

Implementation changes remain blocked until owners and fixtures are approved.

## P2 — Verification hardening

**Status: Proposed**

Bounded objectives:

- expand malformed-input and rejection-path coverage;
- test every public record's canonical serialization and hash fixture;
- test replay through intermediate QSIO boundaries;
- test corrupted hashes, stale preconditions, parent-link divergence, revoked references, and unverified witnesses;
- define whether lifecycle errors return rejected records or remain exceptions;
- prove deterministic results across supported Python environments;
- add static typing, packaging, dependency, license, and supply-chain checks to CI;
- add bounded hostile-input and resource-limit tests; and
- map every implemented invariant to a named test and release gate.

P2 must not add persistence, network access, external authority, device control, or autonomous repository behavior.

## P2A — Authorization and independent verification

**Status: Blocked pending authority and threat-model approval**

Existing `PermissionSet` and witness records are data structures, not comprehensive authorization or independent attestation.

Potential work includes:

- independently issued capabilities;
- expiry, replay prevention, narrowing, and revocation;
- signer and verifier identity;
- witness classes and trust strength;
- reason-code and result reconciliation; and
- evidence classification and verification policy.

P2A requires named external owners for identity, capability issuance, revocation, key custody, witness policy, audit retention, privacy, incident response, emergency stop, recovery, and rollback.

## P3 — Local persistence and recovery design

**Status: Blocked pending architecture approval**

Questions requiring decisions before implementation:

- What is the canonical durable ledger format?
- Is storage append-only, event-sourced, snapshot-based, or layered?
- What is the atomic state-and-ledger commit boundary?
- What is the migration and corruption-recovery policy?
- How are timestamps represented without breaking deterministic replay?
- What constitutes an authoritative checkpoint or ledger root?
- What data may be redacted, compacted, corrected, revoked, or retained?
- How are schema versions and unsupported records handled?
- Which repository owns storage adapters and operational recovery?
- How are partial failure, idempotency, retry, and explicit `UNKNOWN` states represented?

Any persistence work must remain local unless networking is separately approved.

## P3A — Quietus, freeze, revocation, and recovery

**Status: Proposed and blocked on portfolio authority**

The portfolio must define and test:

- local Quietus behavior;
- external admission freeze and capability revocation;
- queued and in-flight work disposition;
- evidence and volatile-state preservation;
- correction and cache-invalidation propagation;
- prohibition on automatic unlock;
- approved checkpoint identity; and
- least-authority bounded restart with old capabilities invalid.

## P4 — External integration or federation

**Status: Not authorized**

The following are outside current scope:

- network services;
- external model or tool execution;
- filesystem or subprocess authority;
- device-management or remediation commands;
- autonomous QSO spawning;
- distributed consensus;
- payment or credential operations;
- cross-repository canonical authority;
- continuous self-modification; and
- self-authorized repository, merge, release, publication, or deployment actions.

A future proposal must define users, operators, data classes, authority, inputs, outputs, failure containment, privacy, observability, rollback, and repository boundaries before implementation begins.

## Change-control rule

A pull request that changes runtime semantics must:

1. identify the task-chain phase it advances;
2. update tests and machine-readable fixtures;
3. update relevant design, API, security, operations, obstruction, and integration documentation;
4. update `punchlist.md` and `release.md` without prematurely passing gates;
5. add an `Unreleased` changelog entry;
6. state compatibility, migration, privacy, authority, incident, and rollback impact;
7. identify every cross-repository contract change; and
8. add or update an ADR when ownership or an architectural boundary changes.

A documentation-only pull request must build strictly from its immutable submitted head and may not mark non-documentation gates complete without corresponding evidence.
