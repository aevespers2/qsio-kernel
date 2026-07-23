# ADR 0004 — Kernel-to-runtime crosswalk options

- **Status:** Proposed; no option selected
- **Decision class:** Portfolio compatibility and migration boundary
- **Authority effect:** None
- **Supersedes:** Nothing
- **Related:** ADR 0002, ADR 0003, Runtime Conformance Boundary Profile

## Context

`qsio-kernel` and candidate portfolio runtimes use related QSO/QSI/QSIO terminology, but matching names do not prove matching identity, canonical bytes, lifecycle, outcome, time, authority, witness, correction, or recovery semantics. The portfolio needs a bounded decision structure that permits exact compatibility, explicit projection, deliberate non-integration, or preservation-safe migration without allowing an undocumented adapter to create authority.

## Options under review

1. **Exact semantic profile** — both implementations conform to a separately governed neutral contract and immutable fixture package.
2. **Explicit projection profile** — a versioned mapper produces a narrower projection and records every omission or transformation.
3. **Unsupported route** — no mapping is accepted and kernel records remain local research evidence.
4. **Migration-source profile** — selected concepts and fixtures migrate to the approved runtime while this repository becomes historical or test-only.

## Proposed decision rule

No architectural option is selected here. The route remains **unsupported by default** until an authorized review packet proves all requirements of another option.

Every field and semantic class must be dispositioned as `EXACT`, `TRANSFORM`, `PROJECT`, `UNSUPPORTED`, `UNKNOWN`, or `LOSSY_REJECTED`. Missing, ambiguous, or lossy mappings fail closed. Local permissions, witnesses, outcomes, lifecycle values, hashes, passing tests, and fixtures do not grant external authority.

## Consequences

### Positive

- Prevents name-based equivalence and accidental authority expansion.
- Gives reviewers a clear no-integration option rather than pressuring them to accept a weak adapter.
- Preserves the kernel as useful evidence even when no runtime mapping is safe.
- Makes migration, deprecation, correction, withdrawal, and rollback reviewable.
- Provides a stable vocabulary for pairwise and triple-overlap fixtures.

### Costs

- Compatibility claims require more explicit ownership and independent evidence.
- Some apparently similar records will remain unsupported.
- Parallel contract generations may require temporary projection receipts and stale-claim handling.
- Migration cannot be declared complete until provenance and restored-state evidence are retained.

## Acceptance gates

A future approving ADR must identify:

- the selected option and exact profile version;
- neutral contract, namespace, registry, fixture, and mapping owners;
- the canonical runtime and exact source/configuration;
- field-level dispositions and unsupported routes;
- canonical bytes or reversible transformation rules;
- identity, state, authority, temporal, correction, stop/recovery, and consumer-continuity witnesses;
- privacy, retention, redaction, and disclosure treatment;
- compatibility reviewer, claim expiry, correction, withdrawal, support, and incident owners;
- migration and rollback evidence; and
- resulting exact-head validation.

## Rejection and rollback

Reject or withdraw a profile when it accepts an unsupported or lossy route, collapses local metadata into external authority, changes a bound source without revalidation, diverges under replay, fails to propagate correction or revocation, or cannot restore the previous independently verified state.

Rollback restores the prior accepted profile or the unsupported route, preserves failed evidence, invalidates downstream claims and caches, and requires a new review generation rather than rewriting history.

## Scope

This ADR is documentation-only. It does not select a canonical runtime, approve a mapper, change runtime code, establish a registry, publish a compatibility claim, or authorize persistence, networking, credentials, repository writes, release, deployment, Pages publication, or canonical-state mutation.
