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
- [x] Reference-conformance boundary profile and ADR 0003 candidate.
- [x] Kernel-to-runtime crosswalk options, machine-readable profile, and ADR 0004 candidate.
- [x] Portfolio obstruction and gluing analysis.
- [x] Accessibility review protocol and machine-readable exact-generation evidence profile.
- [x] Release and integration punch list.
- [x] Task-chain, punch-list, release, and changelog alignment.
- [x] Exact-head strict documentation workflow implemented.
- [x] Automated structural accessibility invariants added to documentation validation.

Evidence still required before P1 is complete:

- [ ] A new exact-head documentation run passes after the final crosswalk, conformance, gluing, accessibility, and coordination changes.
- [ ] The retained artifact and digest are recorded for the current immutable pull-request head.
- [ ] Formal machine-readable schema fixtures exist for all public records.
- [ ] Compatibility statement for `0.x` consumers is approved.
- [ ] The exact rendered artifact receives manual keyboard, focus, heading, table, screen-reader, zoom/reflow, contrast, and cognitive-access review.
- [ ] The review packet records the exact artifact, digest, environment, reviewer or vacancy, findings, untested conditions, residual risk, and correction path.
- [ ] Published Pages URL, deployment source, publication authority, and rollback owner are recorded if Pages is enabled.

A successful documentation run is valid only for the exact source SHA recorded by that run. Any later source change requires a new passing run and makes prior accessibility evidence historical.

## P1A — Canonical portfolio role

**Status: Blocked pending architecture clarification**

The portfolio must select one durable role:

1. canonical low-level semantic kernel;
2. reference conformance implementation for another canonical runtime;
3. migration source whose accepted concepts move into `QuantumStateObjects` or another repository; or
4. independent research prototype.

The lowest-overlap candidate is developed in the Runtime Conformance Boundary Profile and ADR 0003: a small deterministic conformance implementation beneath a separately governed neutral contract and an explicitly approved canonical runtime. The Kernel-to-runtime crosswalk options guide and ADR 0004 add four explicit route dispositions: exact semantic profile, explicit projection, unsupported route, or preservation-safe migration. No route is selected; `UNSUPPORTED` remains the safe default when evidence is incomplete.

The decision must designate:

- canonical repository and package identity;
- QSO/QSI/QSIO schema, format, hashing, registry, fixture, mapping, and compatibility owner;
- canonical operational runtime for each accepted profile;
- relationship to `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC`;
- migration, deprecation, archive, and provenance policy;
- capability issuer and revoker;
- compatibility-claim issuer, reviewer, expiry, withdrawal, and support owner;
- release, incident, emergency-stop, recovery, rollback, and withdrawal authority; and
- boundary with Repositories `0` and `1`.

No documentation in this repository resolves those ownership questions by itself.

## P1B — Cross-repository gluing contracts

**Status: Proposed and blocked on owners**

The obstruction analysis identifies eight pairwise profiles:

1. QSO-GENOMES → `qsio-kernel` genome consumption;
2. Repository `0` → Repository `1` proposal admission;
3. Repository `1` → canonical runtime execution admission;
4. neutral contract and evidence pipeline → `qsio-kernel` reference consumption;
5. `qsio-kernel` ↔ canonical runtime conformance comparison;
6. canonical runtime → QSO-FABRIC experiment evidence;
7. conformance/runtime evidence → Repository `1` result reconciliation; and
8. conformance/runtime evidence → Bridge → QSO-STUDIO/AionUi review projection.

Before integration, the portfolio must also pass eight triple-overlap witness groups:

- QSO-GENOMES → neutral contract → kernel;
- neutral contract → kernel → canonical runtime;
- Repository `0` → Repository `1` → canonical runtime;
- kernel → canonical runtime → Fabric;
- Seeker/temporal/Digitalis → canonical runtime → kernel;
- kernel → Bridge → review interface;
- Quietus → revocation → recovery; and
- correction → canonical disposition → replay.

Pairwise adapters alone cannot complete P1B.

## P1C — Contract vocabulary and compatibility

**Status: Proposed**

Required bounded outcomes:

- machine-readable schemas and canonical or explicitly mapped byte fixtures for every public record;
- supported, unsupported, malformed, stale, replayed, revoked, corrected, superseded, partial, and unknown semantics;
- canonical format and digest rules;
- reason-code and outcome mappings;
- lifecycle crosswalk across active, Quietus, frozen, revoked, quarantined, and recovering states;
- clock domains, temporal provenance, freshness, expiry, and replay rules;
- privacy, retention, redaction, correction, and hash-disclosure policy; and
- `0.x` compatibility, migration, deprecation, claim-expiry, withdrawal, and support rules.

Every mapped field must use one explicit disposition: `EXACT`, `TRANSFORM`, `PROJECT`, `UNSUPPORTED`, `UNKNOWN`, or `LOSSY_REJECTED`. Missing or ambiguous dispositions fail closed. Implementation changes remain blocked until owners and fixtures are approved.

## P1D — Reference-conformance boundary

**Status: Proposed and documented**

The candidate profile requires:

- a neutral owner for schemas, canonical bytes, digests, namespaces, registry, fixtures, and compatibility policy;
- an explicitly named canonical runtime for each profile;
- distinct contract, fixture, genome projection, admission, capability, conformance-run, QSI, QSIO, execution, receipt, disposition, correction, revocation, and checkpoint identities;
- explicit mappings rather than name-based equivalence;
- fail-closed unsupported or lossy mappings;
- positive, negative, malformed, stale, replayed, revoked, corrected, superseded, partial, and unknown fixtures;
- independent compatibility review and claim withdrawal;
- no network, device, repository, credential, payment, release, or deployment authority in the conformance path.

P1D is complete only when ADR 0003 is accepted or superseded and the neutral contract, canonical runtime, fixtures, owners, and gluing witnesses are approved at immutable versions.

## P1E — Kernel-to-runtime crosswalk decision

**Status: Decision packet complete; architecture selection blocked**

Completed documentation work:

- [x] Four options defined: exact semantic profile, explicit projection, unsupported route, and migration source.
- [x] Field dispositions defined: `EXACT`, `TRANSFORM`, `PROJECT`, `UNSUPPORTED`, `UNKNOWN`, and `LOSSY_REJECTED`.
- [x] Machine-readable documentation profile records fail-closed conditions, authority denials, acceptance gates, and FYSA-120 mapping.
- [x] Identity, byte, state, authority, temporal, correction, stop/recovery, and consumer-continuity witness classes documented.
- [x] Unsupported route established as the safe default until another route is independently approved.

Blocked requirements:

- [ ] Select or reject a canonical runtime for a named profile.
- [ ] Assign neutral contract, registry, mapping, review, support, correction, and withdrawal owners.
- [ ] Bind exact contract, fixture, mapping, kernel, runtime, configuration, and consumer identities.
- [ ] Publish canonical bytes or a reversible transformation with hostile fixtures.
- [ ] Demonstrate pairwise and triple-overlap witnesses.
- [ ] Record independent review, claim expiry, correction, withdrawal, migration, rollback, and restored-state evidence.

No mapper or adapter implementation is authorized by P1E.

## P1F — Documentation accessibility evidence

**Status: Protocol complete; exact-head manual review not completed**

Completed documentation work:

- [x] Define review states without implying certification or publication authority.
- [x] Bind review evidence to exact source, workflow, artifact, digest, environment, reviewer or vacancy, findings, and correction history.
- [x] Define automated structural checks and manual keyboard, screen-reader, zoom/reflow, contrast, table, diagram, and cognitive-access review.
- [x] Define blocking, high, moderate, low, and unknown finding dispositions.
- [x] Define supersession, withdrawal, rollback, and independent restored-state evidence.
- [x] Map the protocol to FYSA-120 and propose `019-R` as a non-authoritative refinement.

Outstanding evidence:

- [ ] Review the exact rendered candidate artifact manually in the required environments.
- [ ] Record all open findings, untested conditions, and residual risk.
- [ ] Correct blocking findings on a new exact generation and repeat affected checks.
- [ ] Assign publication, withdrawal, rollback, and restored-state verification roles before any Pages deployment.

`REVIEWED_NO_KNOWN_BLOCKERS` would remain evidence only. It would not establish accessibility certification, legal compliance, publication approval, runtime approval, or portfolio authority.

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
- add bounded hostile-input and resource-limit tests;
- reproduce neutral-contract mappings against the selected canonical runtime; and
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
3. update relevant design, API, security, operations, obstruction, conformance, crosswalk, accessibility, and integration documentation;
4. update `punchlist.md` and `release.md` without prematurely passing gates;
5. add an `Unreleased` changelog entry;
6. state compatibility, migration, privacy, authority, incident, accessibility, and rollback impact;
7. identify every cross-repository contract change; and
8. add or update an ADR when ownership or an architectural boundary changes.

A documentation-only pull request must build strictly from its immutable submitted head and may not mark non-documentation gates complete without corresponding evidence.
