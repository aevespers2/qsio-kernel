# ADR 0002: A.L.I.S.T.A.I.R.E. kernel role and authority boundary

- **Status:** Proposed
- **Date:** 2026-07-20
- **Decision owners:** A.L.I.S.T.A.I.R.E. architecture and repository governance

## Context

`qsio-kernel` implements a compact executable model for QSO state, QSI requests, QSIO outcomes, content hashing, replay, and Quietus. The wider A.L.I.S.T.A.I.R.E. portfolio also contains repositories concerned with QSO runtime semantics, genomes, coordination, evidence review, external verification, and autonomous development.

Without an explicit ownership decision, similar concepts may evolve independently, creating incompatible schemas, duplicated runtimes, unclear release authority, and unsupported claims that a local prototype is the portfolio control plane.

## Proposed decision

Until a portfolio-level decision supersedes this ADR:

1. treat `qsio-kernel` as an **experimental local semantic-kernel candidate**;
2. use it to test deterministic records, transitions, lifecycle controls, and replay semantics;
3. do not assign it autonomous task planning, repository access, credentials, merging, release, deployment, or incident authority;
4. do not claim its witnesses, permission records, or in-memory ledger provide independent attestation, comprehensive authorization, or durable consensus; and
5. require explicit reconciliation with `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC` before adopting its contracts as canonical portfolio interfaces.

## Options requiring approval

The architecture authority should choose one durable role:

### Option A — Canonical semantic kernel

`qsio-kernel` owns the lowest-level QSO/QSI/QSIO runtime contract. Other repositories integrate through versioned schemas and adapters.

**Consequences:** requires formal contract ownership, compatibility policy, persistence design, independent authorization, and production-grade verification.

### Option B — Reference conformance implementation

Another repository owns the canonical contract, while `qsio-kernel` remains a small executable oracle for fixtures, deterministic replay, and interoperability tests.

**Consequences:** minimizes runtime scope but requires a clearly identified upstream schema and conformance process.

### Option C — Migration source

Accepted concepts and tests move into `QuantumStateObjects` or another canonical runtime, after which this repository becomes archived provenance.

**Consequences:** reduces duplication but requires a mapped migration, preserved history, compatibility notes, and closure criteria.

### Option D — Independent research prototype

The repository continues separately for semantic experiments and does not define portfolio contracts.

**Consequences:** permits exploration but requires prominent separation from production and canonical architecture claims.

## Invariants under every option

- Runtime state changes remain explicit and evidence linked.
- Proposed and accepted transitions remain distinguishable.
- Pre-state hashes are checked before accepted mutation.
- Rejected interactions remain auditable.
- Quietus cannot be bypassed by ordinary transition paths.
- Hash and replay semantics are versioned before incompatible change.
- External authority is never inferred from an internal record type.
- Consequential portfolio actions retain independently assigned authorization and rollback.

## Consequences of the interim boundary

### Positive

- Prevents a documentation change from silently expanding implementation scope.
- Gives the portfolio a testable semantic artifact while ownership is resolved.
- Preserves room for consolidation without prematurely declaring a canonical runtime.
- Makes autonomous-development integration dependent on explicit capabilities and evidence.

### Negative

- Some portfolio diagrams and contracts remain provisional.
- Integration work is blocked until ownership and schema direction are chosen.
- Similar concepts may require temporary cross-repository mapping.

## Acceptance criteria

This ADR may move to **Accepted** only when the portfolio records:

- the selected option;
- canonical repository and package identity;
- contract and schema owners;
- compatibility and migration policy;
- capability and authorization owners;
- release, incident, emergency-stop, and rollback authority; and
- the relationship to A.L.I.S.T.A.I.R.E.'s autonomous-development control plane.

## Supersession

A later ADR may supersede this proposal, but it must preserve provenance and explain migration or archival treatment for existing QSIO records and public documentation.