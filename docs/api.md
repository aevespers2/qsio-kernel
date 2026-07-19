# Public API guide

The package re-exports its primary records and operations from `qsio`. The API is intentionally small and should be treated as experimental until a compatibility policy is approved.

## Core records

### `QSO`

Represents a registered object with:

- `qso_id`
- `genome_version`
- `canon`
- current `state`
- `permissions`
- `created_at`

Use `create_qso(...)` when constructing a QSO directly. In ordinary kernel flow, genesis through `execute_qsi(...)` creates and registers it.

### `QSOState`

Represents the current semantic and lifecycle state. Use `build_qso_state(...)` to construct a content-hashed state for genesis or test fixtures.

### `QSI`

```python
from qsio import QSI

request = QSI(
    interaction_type="hypothesis",
    initiator="EXPLORER",
    participants=("EXPLORER",),
    input_refs=(),
    requested_transition={
        "assertion": {
            "kind": "hypothesis",
            "text": "Novel structure exists",
        }
    },
    logical_time=2,
)
```

A QSI is a request and contains no outcome fields.

### `QSIO`

Returned by execution. Inspect:

- `outcome`
- `reason_codes`
- `pre_state_hashes`
- `proposed_transitions`
- `accepted_transitions`
- `witnesses`
- `parent_qsio_hashes`
- `content_hash`

## Runtime

### `RuntimeContext`

```python
from qsio import RuntimeContext

context = RuntimeContext()
```

The context owns the current logical clock, limits, permissions, ledger, QSO registry, state history, and Quietus registry. It is mutable, in-memory, and not thread-safe by contract.

### `PermissionSet` and `Capability`

These types model resource/operation grants. The current kernel exposes capability evaluation through the runtime context, but interaction execution does not yet enforce a complete authorization policy.

## Execution operations

### `validate_qsi(qsi, context)`

Returns a `ValidationReport` containing a validity flag, reason codes, and optional details. Validation currently checks forbidden transition keys, genesis authorization, known initiators and participants, and Quietus state.

### `execute_qsi(qsi, context)`

Validates and executes a request, updates runtime state when accepted, creates a QSIO result, and appends that result to the context ledger. Some lifecycle violations raise an exception rather than returning a rejected record.

### `submit_qsi(qsi, context)`

Alias for `execute_qsi(...)`.

### `verify_qsio(qsio)`

Recomputes the QSIO content hash, validates transition preconditions represented in the envelope, and rejects accepted records containing unverified witnesses.

Verification is structural and local; it is not signature verification.

## Lifecycle operations

### `enter_quietus(qso_id, reason, context)`

Records a Quietus reason and executes a lifecycle transition that changes the QSO state to `quietus`.

### `resume_from_quietus(qso_id, context)`

Creates and records an explicit resume transition, returns the QSO to `active`, and removes it from the Quietus registry.

## Replay

### `replay(qso_id, through_qsio_id=None, context=...)`

Reconstructs the state of one QSO by applying accepted transitions from the ledger, optionally stopping at a selected QSIO record. A complete replay should reproduce the same final state hash as the runtime context.

## Semantic record types

The public surface also exports:

- `Canon`
- `Telion`
- `MemoraEntry`
- `Nexis`
- `StateTransition`
- `WitnessRecord`
- `EpistemicValue`
- `ValidationReport`
- `VerificationReport`

These records support content-addressed identity, purpose, memory/provenance, relationships, transition evidence, and validation results.

## Exceptions

- `CanonViolationError`
- `PermissionDeniedError`
- `QuietusError`
- `QSIOValidationError`

Callers should currently handle both result-based rejection and raised exceptions.

## Stability warning

The package is `0.1.0`. Field names, validation paths, exception behavior, and hash-compatible schemas should not be considered stable until compatibility fixtures and a formal versioning policy are added.
