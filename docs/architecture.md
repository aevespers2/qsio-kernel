# Architecture

## Architectural intent

`qsio-kernel` is a single-process semantic reference runtime. Its architecture favors deterministic behavior, explicit records, and replayable state over throughput, distribution, or external integration.

## Component map

```mermaid
flowchart LR
    subgraph Public API
        A[QSO / QSOState]
        B[QSI]
        C[QSIO]
        D[Replay]
    end

    subgraph Semantic records
        E[Canon]
        F[Telion]
        G[MemoraEntry]
        H[StateTransition]
        I[WitnessRecord]
    end

    subgraph Runtime boundary
        J[RuntimeContext]
        K[PermissionSet]
        L[LogicalClock]
        M[Ledger]
        N[QSO registry and history]
        O[Quietus registry]
    end

    B --> C
    E --> A
    F --> A
    G --> A
    C --> H
    C --> I
    C --> J
    J --> K
    J --> L
    J --> M
    J --> N
    J --> O
    M --> D
    D --> A
```

## Runtime flow

```mermaid
sequenceDiagram
    participant Caller
    participant Kernel as execute_qsi
    participant Context as RuntimeContext
    participant Ledger

    Caller->>Kernel: QSI
    Kernel->>Context: validate initiator, participants, lifecycle
    alt invalid request
        Kernel->>Ledger: append rejected QSIO
        Kernel-->>Caller: rejected result + reason codes
    else genesis
        Kernel->>Context: register QSO and initial state
        Kernel->>Ledger: append accepted genesis QSIO
        Kernel-->>Caller: accepted QSIO
    else ordinary transition
        Kernel->>Context: read pre-state hash
        Kernel->>Kernel: build transition and witness
        Kernel->>Context: record updated state
        Kernel->>Ledger: append accepted QSIO
        Kernel-->>Caller: accepted QSIO
    end
```

## Major responsibilities

### QSO and state

A `QSO` binds identity and configuration to its current `QSOState`. The state includes lifecycle, visible `lumen` data, an optional `umbra_commitment`, references to Telion and Memora roots, logical time, and a content hash.

### QSI

A `QSI` is an immutable request. It does not itself mutate state. It identifies the interaction type, initiator, participants, input references, requested transition, and logical time.

### QSIO

A `QSIO` is the result envelope. It records the request, pre-state hashes, proposed and accepted transitions, witness records, outcome, reason codes, parent hashes, creation time, and its own content hash.

### RuntimeContext (Sanctum)

`RuntimeContext` is the current execution boundary. It owns the logical clock, limits, permission set, ledger, QSO registry, state history, Quietus registry, and genesis authorization flag. All of these structures are currently in memory.

### Replay

Replay consumes ledger records through an optional QSIO boundary and reconstructs state for a selected QSO. The demo and tests compare the replayed final content hash with the runtime's current state hash.

## Trust boundaries

```mermaid
flowchart TB
    U[Untrusted caller input] --> V[QSI validation boundary]
    V -->|forbidden key or invalid actor| R[Rejected record]
    V -->|accepted| E[In-process execution]
    E --> S[Mutable RuntimeContext]
    E --> H[Content hashing]
    H --> L[In-memory ledger]

    classDef boundary stroke-width:2px,stroke-dasharray: 5 5;
    class V,H boundary;
```

The current validation boundary is semantic rather than an operating-system sandbox. Rejecting keys such as `network`, `external_io`, `subprocess`, and `spawn` prevents those requests from being accepted by this kernel path, but it does not constitute process isolation.

## Deployment topology

There is currently one supported topology: a local Python process with an in-memory runtime. The package exposes a console entry point and module demo. No server, database, queue, remote API, browser client, or background service is part of version `0.1.0`.

## Architectural extension rule

Persistence, signatures, independent witness services, external models, concurrency, networking, federation, or autonomous object creation must be introduced as separate bounded changes with explicit schemas, migration behavior, threat analysis, and release evidence. They are not implied by the present abstractions.
