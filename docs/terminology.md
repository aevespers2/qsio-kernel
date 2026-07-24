# Terminology

This glossary describes terms as they are used by the current `0.1.0` implementation. It does not assign metaphysical, legal, organizational, or external-system authority to these names.

## Core records

### Quantum State Object (QSO)

A bounded stateful entity represented by `QSO`. A QSO binds:

- a stable `qso_id` within the runtime;
- a `genome_version` reference;
- a `Canon` containing declared constraints;
- the current `QSOState`;
- a `PermissionSet`; and
- a creation timestamp.

A QSO is not an operating-system process, model instance, legal person, autonomous account, or network identity.

### QSO state

The content-hashed mutable state associated with a QSO. It contains:

- state version;
- lifecycle;
- visible `lumen` data;
- optional `umbra_commitment`;
- Telion and Memora references;
- logical time; and
- content hash.

State changes are expected to be represented by accepted transitions recorded in QSIOs.

### Quantum State Interaction (QSI)

An immutable request describing an intended interaction. A QSI contains:

- interaction type;
- initiator;
- participants;
- input references;
- requested transition data; and
- logical time.

A QSI expresses intent. It does not prove authorization and does not mutate state by itself.

### Quantum State Interaction Object (QSIO)

The persistent-form result envelope produced for an interaction, although the current repository stores it only in memory. A QSIO records:

- the originating QSI;
- participant pre-state hashes;
- proposed and accepted transitions;
- witness metadata;
- outcome and reason codes;
- parent QSIO hashes;
- creation time; and
- its own content hash.

A rejected QSIO is still useful evidence because it records why a request was not accepted.

## Semantic structures

### Canon

A content-hashed set of declared constraints associated with a QSO. The current validator also rejects a small set of forbidden requested-transition keys. Canon data and semantic validation do not constitute an operating-system sandbox or complete policy engine.

### Lumen

The visible dictionary-like portion of QSO state. The prototype uses `lumen` for explicit assertions and synthesis data. It should be treated as application data, not unrestricted memory.

### Umbra commitment

An optional commitment string stored in QSO state. The current implementation does not reveal, verify, encrypt, or independently resolve hidden Umbra content.

### Telion

A record or hash reference intended to represent purpose or directed objective. In this kernel, Telion is semantic data; it does not independently authorize execution.

### Memora

Memory-related records and a state root reference. The prototype uses content-addressed semantics but does not provide durable memory storage, retention policy, search, or privacy enforcement.

### Nexis

A semantic relation or connection record among entities or evidence. It is not a live network connection.

### State transition

A content-hashed record describing:

- target QSO;
- operation;
- precondition hash;
- field patch;
- postcondition hash;
- confidence; and
- evidence references.

A proposed transition becomes state-changing only when the runtime accepts and applies it.

### Witness record

Metadata describing an in-process verification observation. Current witness records are not cryptographic signatures, independent third-party attestations, trusted timestamps, or durable audit proofs.

## Runtime terms

### RuntimeContext

The in-memory execution boundary, also described as the prototype Sanctum. It owns the clock, limits, permissions, ledger, QSO registry, state history, Quietus registry, and genesis-authorization flag.

### Sanctum

A conceptual name for the bounded runtime context. It should not be interpreted as hardware isolation, a secure enclave, a container, or an operating-system sandbox.

### Ledger

The ordered in-memory sequence of QSIO records. Parent hashes and content hashes support integrity checks, but the current ledger is not durable, replicated, independently witnessed, or consensus backed.

### Replay

Reconstruction of QSO state by consuming accepted transitions from ordered QSIO records. Replay is used to compare reconstructed and runtime state hashes.

### Logical time

An integer ordering mechanism supplied by the prototype runtime. It is not verified wall-clock time and does not establish cross-system chronology.

## Lifecycle terms

### Genesis

The authorized in-process creation of a QSO and its initial accepted QSIO record.

### Active

A lifecycle state in which ordinary accepted transitions may update the QSO.

### Quietus

A lifecycle state that blocks ordinary mutation. Entry and resume are expected to be represented explicitly in QSIO records.

### Resume

An explicit operation returning a QSO from Quietus to active operation under the current prototype rules.

### Quarantined

A lifecycle value available in the state type for isolating a QSO. Comprehensive quarantine operations and incident policy are not yet implemented.

### Retired

A lifecycle value indicating terminal or withdrawn status. Complete retirement semantics, archival policy, and migration behavior are not yet defined.

## Portfolio terms

### A.L.I.S.T.A.I.R.E.

The canonical system objective across the wider repository portfolio. In this documentation, the name identifies the larger architecture and mission; it does not imply that `qsio-kernel` is already its authoritative runtime or autonomous-development control plane.

### Autonomous-development control plane

The not-yet-designated component responsible for bounded task authorization, capability grants, evidence review, repository actions, release and deployment decisions, emergency stop, and rollback. `qsio-kernel` does not currently perform these functions.

### Canonical runtime

The repository and package formally designated to own the portfolio's runtime contracts and compatibility policy. The canonical runtime for the overlapping QSO repositories has not yet been approved.

## Naming rule

New terminology must include an executable or contract-level definition, ownership boundary, non-capabilities, and compatibility impact. Conceptual names may not be used to bypass security, release, or governance requirements.