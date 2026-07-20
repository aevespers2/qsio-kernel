# ADR 0001: Kernel boundaries

- **Status:** Accepted for the `0.1.0` experimental baseline
- **Date:** 2026-07-19
- **Scope:** Local semantic-kernel prototype

## Context

The first executable QSIO kernel needed to make a small set of QSO concepts testable without prematurely introducing persistence, networking, external models, distributed execution, credentials, or autonomous authority.

A narrow boundary was necessary so that state changes could be inspected, hashed, replayed, and tested before broader system integration.

## Decision

The `0.1.0` kernel will:

1. run in one local Python process;
2. keep QSO registry, state history, ledger, and lifecycle controls in memory;
3. represent interaction intent as an explicit QSI;
4. represent outcomes as content-hashed QSIO records;
5. keep proposed and accepted transitions distinguishable;
6. bind accepted non-genesis transitions to pre-state hashes;
7. attach evidence references and in-process witness metadata;
8. preserve deterministic replay semantics;
9. provide Quietus and explicit resume as lifecycle controls; and
10. reject selected requested-transition keys for external I/O, networking, subprocesses, and spawning.

## Boundary

The kernel does not include:

- durable storage;
- network protocols or services;
- external model or tool execution;
- filesystem or subprocess adapters;
- distributed consensus or federation;
- cryptographic identity or independent attestation;
- comprehensive capability issuance and revocation;
- production scheduling or resource isolation;
- repository, release, deployment, payment, or credential authority; or
- self-directed spawning or self-modification.

The absence of these capabilities is intentional, not an incomplete promise that they are silently available.

## Invariants

- State mutation is represented by an accepted transition in a QSIO.
- Rejected validation does not mutate QSO state.
- Accepted non-genesis transitions use the current state hash as precondition.
- Record hashing uses explicit domain separators.
- Quietus blocks ordinary mutation.
- Resume is explicit and represented in evidence.
- Replay reconstructs state from ordered accepted transitions.
- Semantic controls are not described as operating-system isolation.
- Internal records do not create external authority.

## Consequences

### Positive

- The implementation remains small enough to review and test.
- Semantic records and invariants are executable rather than purely conceptual.
- Replay and integrity defects can be studied before durable integration.
- External authority remains separated from internal QSO representation.

### Negative

- State and ledger evidence disappear when the process ends.
- Witnesses and permissions have limited trust strength.
- The prototype cannot support hosted, concurrent, distributed, or credentialed use.
- Some lifecycle values and semantic records lack complete operational behavior.

## Alternatives considered

### Build a networked service immediately

Rejected because identity, authorization, persistence, privacy, incident response, and operational ownership were not defined.

### Use a database as the initial ledger

Deferred because durable format, migration, corruption recovery, retention, and authoritative-root policy require architecture approval.

### Allow arbitrary tool execution behind permission records

Rejected because the current permission representation lacks comprehensive issuance, revocation, isolation, and audit semantics.

### Combine planning, execution, and governance in one kernel

Rejected because self-authorized consequential action would collapse critical trust boundaries and make evidence less meaningful.

## Verification

Repository evidence for this decision includes:

- QSO, QSI, QSIO, transition, witness, ledger, replay, and runtime-context code;
- tests for canon rejection, lifecycle behavior, replay, provenance, and default security boundaries; and
- the deterministic four-QSO demo.

Passing these tests supports the prototype boundary only. It does not approve external integration or production release.

## Follow-up decisions

Separate ADRs are required for:

- canonical A.L.I.S.T.A.I.R.E. runtime ownership;
- durable ledger and migration design;
- independent identity, signatures, and witnesses;
- capability enforcement and revocation;
- external adapters and isolation;
- autonomous-development control-plane integration; and
- hosted-service operations.

[ADR 0002](0002-alistaire-kernel-role.md) proposes the interim portfolio role and records the unresolved canonical-runtime decision.

## Supersession rule

Any change that expands this boundary must state which invariant changes, what new trust assumptions are introduced, how failure is contained, and which release gates and rollback procedures apply.