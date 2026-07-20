# qsio-kernel

`qsio-kernel` is the first executable, bounded semantic kernel for Quantum State Objects (QSOs) and Quantum State Interaction Objects (QSIOs). It provides an in-memory Python reference runtime for deterministic state transitions, content-addressed interaction records, witness metadata, ledger replay, and the Quietus lifecycle control.

Within the wider A.L.I.S.T.A.I.R.E. endeavor, this repository is presently a **candidate low-level semantic-kernel component**. It can model bounded execution and produce reviewable evidence, but it does not own autonomous planning, repository access, credentials, merging, release, deployment, or portfolio governance.

## Project status

The repository is an **experimental reference implementation**, not a production agent platform, autonomous network, or control plane. Version `0.1.0` demonstrates a deterministic local runtime with no external I/O, subprocess execution, network access, or uncontrolled object spawning.

The current implementation:

- creates QSOs through an authorized genesis interaction;
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

- **QSO** — an identified object with a genome version, canon, state, permissions, and creation time.
- **QSI** — a requested interaction describing an initiator, participants, referenced inputs, requested transition, and logical time.
- **QSIO** — the auditable result envelope containing pre-state hashes, transitions, witnesses, outcome, reason codes, parent hashes, and a content hash.
- **Quietus** — a lifecycle state that blocks ordinary mutation until an explicit resume operation.

## A.L.I.S.T.A.I.R.E. boundary

The kernel may eventually serve as a deterministic execution-and-evidence substrate beneath an independently authorized development control plane. That integration remains provisional until the portfolio decides whether this repository is the canonical runtime, a conformance implementation, a migration source, or a separate research prototype.

See [A.L.I.S.T.A.I.R.E. integration](docs/alistaire-integration.md) and [ADR 0002](docs/adr/0002-alistaire-kernel-role.md).

## Documentation

- [Project site](docs/index.md)
- [Architecture](docs/architecture.md)
- [A.L.I.S.T.A.I.R.E. integration](docs/alistaire-integration.md)
- [Design and invariants](docs/design.md)
- [Public API](docs/api.md)
- [Developer onboarding](docs/onboarding.md)
- [Operations and recovery](docs/operations.md)
- [Security and trust boundaries](docs/security.md)
- [Task chain](taskchain.md)
- [Release gates](release.md)
- [Changelog](changelog.md)

A Pages-ready MkDocs configuration is included in `mkdocs.yml`. Pull requests that change documentation are validated by an exact-head strict site build and produce a retained rendered-site evidence artifact. Publishing the site remains a repository administration decision and is not performed by the documentation workflow.

## Scope discipline

Documentation in this repository describes behavior that exists in the current code or clearly labels future work. New persistence, networking, autonomous spawning, external execution, federation, production authority, or cross-repository orchestration requires an approved task-chain change, architecture decision, and corresponding verification evidence.

## License

MIT. See [LICENSE](LICENSE).