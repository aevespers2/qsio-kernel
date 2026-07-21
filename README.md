# qsio-kernel

`qsio-kernel` is a compact, executable reference implementation for bounded Quantum State Objects (QSOs) and Quantum State Interaction Objects (QSIOs). It provides an in-memory Python runtime for deterministic state transitions, content-addressed interaction records, witness metadata, lifecycle controls, ledger replay, and conformance-oriented fixtures.

Within A.L.I.S.T.A.I.R.E., this repository is presently a **candidate reference-conformance implementation** for low-level QSO/QSI/QSIO semantics. It can evaluate immutable fixtures and produce reviewable comparison evidence, but it does not own broad runtime admission, autonomous planning, device control, repository access, credentials, capability issuance, canonical state, merging, release, publication, deployment, or portfolio governance.

## Project status

The repository is an **experimental reference implementation**, not a production agent platform, autonomous network, device-management service, or control plane. Version `0.1.0` demonstrates deterministic local behavior with no external I/O, subprocess execution, network access, durable storage, or uncontrolled object spawning.

The current implementation:

- creates QSOs through an authorized local genesis interaction;
- records proposed and accepted state transitions in QSIO envelopes;
- hashes QSO states, transitions, witnesses, and ledger records;
- rejects transition payloads requesting forbidden external capabilities;
- supports Quietus and explicit resumption;
- replays the in-memory ledger to reproduce final QSO state hashes; and
- includes a four-QSO demonstration: Explorer, Archivist, Skeptic, and Synthesist.

It does **not** currently provide durable storage, distributed consensus, cryptographic signatures, independent witnesses, external model access, network federation, concurrent execution, comprehensive authorization enforcement, or production operations.

## Quick start

Requires Python 3.12 or later.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
pytest
python -m qsio.demo
```

The demo creates four bounded QSOs, executes a deterministic interaction chain, verifies the resulting QSIO records, replays final state, and places every QSO into Quietus.

## Conceptual model

```mermaid
flowchart LR
    QSI[QSI request] --> V[Validate request]
    V -->|rejected| R[Rejected QSIO record]
    V -->|accepted| T[Build state transition]
    T --> W[Attach witness metadata]
    W --> S[Apply state update]
    S --> L[Append content-hashed QSIO]
    L --> P[Replay and verify]
```

- **QSO** — an identified object with a genome version, canon, state, permission metadata, and creation time.
- **QSI** — a requested interaction describing initiator, participants, referenced inputs, requested transition, and logical time.
- **QSIO** — the auditable local outcome containing pre-state hashes, transitions, witness metadata, outcome, reason codes, parent hashes, and a content hash.
- **Quietus** — a local lifecycle state that blocks ordinary mutation until an explicit resume operation.

## A.L.I.S.T.A.I.R.E. working boundary

The current portfolio model places Repository `0` upstream as proposal and orchestration support, Repository `1` or an approved successor as capability and canonical-disposition authority, QSO-GENOMES as declarative identity and policy authority, QuantumStateObjects as the candidate broad runtime-admission and bounded-execution layer, QSO-FABRIC as coordination and experiment evidence, and QSO-STUDIO/AionUi as review surfaces.

Under the lowest-overlap candidate, `qsio-kernel` evaluates pinned semantic fixtures and compares observed QSIO/replay results with a separately governed neutral contract. It does not accept a Repository `0` proposal or Repository `1` capability as self-interpreting authority, and it does not replace the canonical runtime's device, workspace, admission, privacy, resource, rollback, or execution checks.

A passing conformance vector proves agreement only for the tested contract, mapping, fixture, kernel source, and canonical-runtime source. A local canon value, `PermissionSet`, witness record, successful transition, conformance witness, or QSIO hash cannot grant permission to use a device, network, repository, credential, payment method, release channel, or deployment environment.

The unresolved architectural choice remains whether this repository becomes:

1. the canonical low-level semantic kernel;
2. a small reference conformance implementation for QuantumStateObjects or another runtime;
3. a migration source whose accepted concepts move elsewhere; or
4. an independent research prototype.

The documentation now develops option 2 as the lowest-overlap candidate in [Runtime Conformance Boundary Profile](docs/runtime-conformance-boundary-profile.md) and [ADR 0003](docs/adr/0003-reference-conformance-boundary.md). This is a proposal, not an approved role or compatibility claim.

## Material integration obstructions

The portfolio must still resolve:

- neutral ownership for QSO/QSI/QSIO schemas, package, format, canonical bytes, hashes, namespaces, fixtures, and compatibility registry;
- overlap with QuantumStateObjects and QSO-FABRIC;
- genome validity versus operational admission;
- local `PermissionSet` metadata versus Repository `1` capabilities;
- local witness metadata versus independent attestation;
- in-memory ledger state versus canonical portfolio disposition;
- logical time versus observation time, freshness, expiry, and replay domains;
- evidence-reference, reason-code, correction, privacy, retention, and redaction contracts;
- Quietus versus freeze, revocation, emergency stop, and recovery;
- compatibility-claim issuance, expiry, withdrawal, support, and migration; and
- release, incident, rollback, publication, and withdrawal authority.

No adapter or conformance claim should be added until machine-readable pairwise and triple-overlap fixtures prove these contracts glue consistently.

## Documentation

- [Project site](docs/index.md)
- [Architecture](docs/architecture.md)
- [A.L.I.S.T.A.I.R.E. integration](docs/alistaire-integration.md)
- [Runtime conformance boundary](docs/runtime-conformance-boundary-profile.md)
- [Obstruction and gluing analysis](docs/obstruction-and-gluing.md)
- [Design and invariants](docs/design.md)
- [Public API](docs/api.md)
- [Developer onboarding](docs/onboarding.md)
- [Operations and recovery](docs/operations.md)
- [Security and trust boundaries](docs/security.md)
- [ADR 0003 — Reference conformance boundary](docs/adr/0003-reference-conformance-boundary.md)
- [Task chain](taskchain.md)
- [Release and integration punch list](punchlist.md)
- [Release gates](release.md)
- [Changelog](changelog.md)

A Pages-ready MkDocs configuration is included in `mkdocs.yml`. Pull requests that change documentation are validated by an exact-head strict site build and produce a retained rendered-site evidence artifact. Publishing the site remains a repository-administration decision and is not performed by the documentation workflow.

## Scope discipline

Documentation in this repository describes behavior supported by repository evidence or clearly labels future work. New persistence, signatures, networking, autonomous spawning, external execution, federation, production authority, cross-repository orchestration, or canonical-state ownership requires an approved task-chain change, architecture decision, implementation evidence, security review, and rollback plan.

## License

MIT. See [LICENSE](LICENSE).
