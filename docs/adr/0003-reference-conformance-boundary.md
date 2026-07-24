# ADR 0003 — Reference-Conformance Boundary

- **Status:** Proposed
- **Date:** 2026-07-21
- **Decision owner:** Unassigned portfolio architecture authority
- **Scope:** `qsio-kernel`, QuantumStateObjects, QSO-GENOMES, QSO-FABRIC, Repositories `0` and `1`, and neutral contract ownership

## Context

`qsio-kernel` contains a compact executable model of QSO/QSI/QSIO records, deterministic local transitions, content hashing, witness metadata, Quietus, an in-memory ledger, and replay. QuantumStateObjects is being documented as the broader candidate runtime-admission and bounded-execution layer. QSO-GENOMES owns declarative identity and policy references, while QSO-FABRIC coordinates multi-QSO experiments.

Without an explicit boundary, the portfolio can accidentally treat two implementations as simultaneously canonical, infer authority from local records, or allow similarly named fields to hide incompatible semantics.

## Decision candidate

Adopt `qsio-kernel` as a **small reference-conformance implementation** rather than the broad canonical runtime.

Under this candidate:

- a neutral, separately governed package owns schemas, canonical or explicitly mapped bytes, digests, namespaces, profile registry, fixtures, and compatibility rules;
- QuantumStateObjects or another explicitly approved runtime owns admission and bounded operational execution for the accepted profile;
- `qsio-kernel` executes immutable conformance fixtures locally and emits deterministic comparison evidence;
- Repository `1` or a successor remains the capability, revocation, canonical-disposition, and recovery authority;
- Repository `0` remains a proposal and orchestration layer;
- QSO-GENOMES remains the declarative genome and policy-reference owner;
- QSO-FABRIC remains an experiment coordinator and evidence aggregator;
- Bridge and review interfaces transport or display evidence without creating approval.

A passing reference result is evidence of agreement for the tested contract and fixture. It is not operational admission, authority, independent attestation, canonical state, or production readiness.

## Reasons

This option has the lowest ownership overlap because it:

- preserves the kernel's deterministic fixtures, hashes, replay, and lifecycle research value;
- avoids duplicating broad runtime admission and execution responsibility;
- creates a practical oracle for compatibility testing;
- exposes semantic mismatches before adapters or deployments are introduced;
- allows migration or retirement later without losing provenance;
- keeps local `PermissionSet`, witness, ledger, and Quietus concepts from silently acquiring external authority.

## Alternatives considered

### Canonical low-level semantic kernel

Potentially coherent, but it would require moving or subordinating broad runtime semantics elsewhere and resolving substantial ownership overlap with QuantumStateObjects and QSO-FABRIC.

### Migration source

Accepted concepts and fixtures could move into another repository. This may eventually be appropriate, but immediate migration risks provenance loss before mappings and compatibility fixtures exist.

### Independent research prototype

Safest from an authority perspective, but it leaves useful deterministic conformance value disconnected from the portfolio.

### Dual canonical runtimes

Rejected as the default. Two independently evolving canonical implementations without a neutral contract and reproduced fixtures create semantic forks rather than redundancy.

## Consequences

### Positive

- clear separation between semantic reference and operational runtime;
- testable compatibility claims at immutable versions;
- preserved research and provenance;
- reduced pressure to add networking, persistence, credentials, or production operations to the kernel;
- explicit owner required for shared contracts rather than implementation-by-accident.

### Costs

- a neutral contract and fixture owner must be established;
- field mappings and lifecycle crosswalks require formal work;
- compatibility evidence must be regenerated whenever contracts, mappings, fixtures, kernel source, or canonical runtime change;
- disagreements must remain visible rather than being normalized away.

### Risks

- consumers may still mistake a passing fixture for runtime security or authority;
- the reference implementation can drift from the neutral contract;
- private or sensitive state may leak through canonical vectors or hashes;
- an unowned compatibility registry can become stale or misleading;
- the candidate canonical runtime may itself remain unresolved.

## Required safeguards

- distinct identifiers for contract, fixture, conformance run, QSI, QSIO, runtime admission, capability, execution, receipt, and canonical disposition;
- fail-closed unsupported-version and mapping behavior;
- positive, negative, malformed, stale, replayed, revoked, corrected, superseded, partial, and unknown fixtures;
- no network, credential, repository, device, payment, release, or deployment authority in the conformance path;
- privacy and disclosure review for fixture content and hashes;
- independent review of compatibility claims;
- explicit claim expiry, withdrawal, correction, and migration procedures;
- required pairwise and triple-overlap witnesses.

## Acceptance conditions

This ADR may be accepted only when:

1. the human architecture authority approves the role;
2. the neutral contract/package/registry owner is named;
3. the canonical runtime and supported profile are named;
4. machine-readable schemas, mappings, fixtures, and digest vectors exist at immutable commits;
5. QSO-GENOMES and QSO-FABRIC boundaries are approved;
6. Repository `1` capability and canonical-disposition boundaries are approved;
7. all required gluing witnesses pass;
8. compatibility, privacy, release, incident, recovery, rollback, support, and withdrawal owners are assigned.

## Non-decisions

This ADR does not:

- approve QuantumStateObjects as canonical runtime;
- approve a neutral schema package or registry;
- change current kernel code or public interfaces;
- authorize persistence, networking, external tools, credentials, signing, or deployment;
- approve a conformance claim or release;
- resolve migration or archive policy.

## Rollback or supersession

If the portfolio selects another durable role, preserve this ADR and all conformance evidence, mark the decision superseded, document the replacement ownership map, and provide fixture and provenance migration. No accepted public version or evidence record should be silently rewritten.
