# Public API guide

The package re-exports its primary records and runtime operations from `qsio`. Helper constructors that are not listed in `qsio.__all__` must be imported from their defining modules. The API is intentionally small and should be treated as experimental until a compatibility policy is approved.

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

Represents the current semantic and lifecycle state. The helper constructor is not re-exported from the package root; use `qsio.qso.build_qso_state(...)` to construct a content-hashed state for genesis or test fixtures.

```python
from qsio.qso import build_qso_state
```

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

Returns a `ValidationReport` for top-level forbidden transition keys, genesis authorization, and known initiators and participants. When a participant is already in Quietus, validation calls the lifecycle guard and raises `QuietusError` rather than returning an invalid report. Callers using validation as a preflight API must handle both the report and that exception path.

### `execute_qsi(qsi, context)`

Validates and executes a request, updates runtime state when accepted, creates a QSIO result, and appends that result to the context ledger. Some lifecycle violations raise an exception rather than returning a rejected record.

### `submit_qsi(qsi, context)`

Alias for `execute_qsi(...)`.

### `verify_qsio(qsio)`

Recomputes the QSIO content hash, validates transition preconditions represented in the envelope, and rejects an accepted record when any witness that is present is unverified.

Verification does not require an accepted record to contain a witness, so an accepted QSIO with `witnesses=()` can still pass the current structural verifier. Verification is local and structural; it is not signature verification or independent attestation.

## Lifecycle operations

### `enter_quietus(qso_id, reason, context)`

Records a Quietus reason in the context registry and executes a lifecycle transition that changes the QSO state to `quietus`. Use this helper for a resumable Quietus transition.

Submitting a raw `QSI(interaction_type="quietus", ...)` directly to `execute_qsi(...)` changes the lifecycle state but does not populate the Quietus registry. A record entered that way cannot be resumed by `resume_from_quietus(...)` without separate registry repair.

### `resume_from_quietus(qso_id, context)`

Creates and records an explicit resume transition, returns the QSO to `active`, and removes it from the Quietus registry. It requires both a `quietus` lifecycle state and a matching registry entry.

## Replay

### `replay(qso_id, through=None, context=...)`

Reconstructs the state of one QSO by applying accepted transitions from the ledger, optionally stopping at the QSIO identifier supplied through `through`. A complete replay should reproduce the same final state hash as the runtime context.

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
