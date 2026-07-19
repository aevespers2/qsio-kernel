from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .errors import CanonViolationError, QSIOValidationError
from .qsi import QSI
from .serialization import hash_payload
from .transition import StateTransition, build_transition
from .types import Hash, Timestamp
from .validation import ValidationReport, VerificationReport
from .witness import WitnessRecord, build_witness


@dataclass(frozen=True)
class QSIO:
    qsio_id: str
    qsi: QSI
    pre_state_hashes: dict[str, Hash]
    proposed_transitions: tuple[StateTransition, ...]
    accepted_transitions: tuple[StateTransition, ...]
    witnesses: tuple[WitnessRecord, ...]
    outcome: Literal["accepted", "rejected", "partial", "quarantined"]
    reason_codes: tuple[str, ...]
    parent_qsio_hashes: tuple[Hash, ...]
    created_at: Timestamp
    content_hash: Hash


def _apply_patch(state: "QSOState", patch: tuple[dict[str, object], ...]) -> "QSOState":
    values = {
        "state_version": state.state_version,
        "lifecycle": state.lifecycle,
        "lumen": dict(state.lumen),
        "umbra_commitment": state.umbra_commitment,
        "telion_hash": state.telion_hash,
        "memora_root": state.memora_root,
        "logical_time": state.logical_time,
    }
    for item in patch:
        field = str(item["field"])
        values[field] = item["value"]
    from .types import QSOState

    return QSOState(
        state_version=int(values["state_version"]),
        lifecycle=str(values["lifecycle"]),  # type: ignore[arg-type]
        lumen=dict(values["lumen"]),  # type: ignore[arg-type]
        umbra_commitment=values["umbra_commitment"],  # type: ignore[arg-type]
        telion_hash=str(values["telion_hash"]),
        memora_root=str(values["memora_root"]),
        logical_time=int(values["logical_time"]),
        content_hash=hash_payload("qso.state.v1", {
            "state_version": int(values["state_version"]),
            "lifecycle": values["lifecycle"],
            "lumen": values["lumen"],
            "umbra_commitment": values["umbra_commitment"],
            "telion_hash": values["telion_hash"],
            "memora_root": values["memora_root"],
            "logical_time": int(values["logical_time"]),
        }),
    )


def _qsio_payload(
    qsio_id: str,
    qsi: QSI,
    pre_state_hashes: dict[str, Hash],
    proposed_transitions: tuple[StateTransition, ...],
    accepted_transitions: tuple[StateTransition, ...],
    witnesses: tuple[WitnessRecord, ...],
    outcome: str,
    reason_codes: tuple[str, ...],
    parent_qsio_hashes: tuple[Hash, ...],
    created_at: Timestamp,
) -> dict[str, object]:
    return {
        "qsio_id": qsio_id,
        "qsi": qsi,
        "pre_state_hashes": pre_state_hashes,
        "proposed_transitions": proposed_transitions,
        "accepted_transitions": accepted_transitions,
        "witnesses": witnesses,
        "outcome": outcome,
        "reason_codes": reason_codes,
        "parent_qsio_hashes": parent_qsio_hashes,
        "created_at": created_at,
    }


def validate_qsi(qsi: QSI, context: "RuntimeContext") -> ValidationReport:
    forbidden_keys = {"external_io", "spawn", "subprocess", "network"}
    if forbidden_keys.intersection(qsi.requested_transition):
        return ValidationReport(False, ("canon_violation",))
    if qsi.interaction_type == "genesis":
        if not context.genesis_authorized:
            return ValidationReport(False, ("unauthorized_genesis",))
        return ValidationReport(True, ())
    if qsi.initiator not in context.qso_registry:
        return ValidationReport(False, ("unknown_initiator",))
    missing = [participant for participant in qsi.participants if participant not in context.qso_registry]
    if missing:
        return ValidationReport(False, ("unknown_participant",), {"missing": ",".join(missing)})
    for qso_id in qsi.participants:
        context.ensure_not_quietus(qso_id)
    return ValidationReport(True, ())


def verify_qsio(qsio: QSIO) -> VerificationReport:
    expected = hash_payload("qsio.v1", _qsio_payload(
        qsio.qsio_id,
        qsio.qsi,
        qsio.pre_state_hashes,
        qsio.proposed_transitions,
        qsio.accepted_transitions,
        qsio.witnesses,
        qsio.outcome,
        qsio.reason_codes,
        qsio.parent_qsio_hashes,
        qsio.created_at,
    ))
    if expected != qsio.content_hash:
        return VerificationReport(False, ("hash_mismatch",), {"expected": expected, "actual": qsio.content_hash})
    if qsio.qsi.interaction_type != "genesis":
        for transition in qsio.accepted_transitions:
            expected_pre = qsio.pre_state_hashes.get(transition.qso_id)
            if expected_pre is None or expected_pre != transition.precondition_hash:
                return VerificationReport(False, ("stale_pre_state",))
    else:
        for transition in qsio.accepted_transitions:
            if transition.precondition_hash != "sha256:0":
                return VerificationReport(False, ("stale_pre_state",))
    if any(not witness.verified for witness in qsio.witnesses) and qsio.outcome == "accepted":
        return VerificationReport(False, ("unverified_witness",))
    return VerificationReport(True, ())


def execute_qsi(qsi: QSI, context: "RuntimeContext") -> QSIO:
    validation = validate_qsi(qsi, context)
    if not validation.valid:
        qsio = QSIO(
            qsio_id=f"qsio_{hash_payload('qsio.id.v1', qsi)}",
            qsi=qsi,
            pre_state_hashes={},
            proposed_transitions=(),
            accepted_transitions=(),
            witnesses=(),
            outcome="rejected",
            reason_codes=validation.reason_codes,
            parent_qsio_hashes=tuple(record.content_hash for record in context.ledger.records[-1:]),
            created_at=context.timestamp(),
            content_hash="",
        )
        object.__setattr__(qsio, "content_hash", hash_payload("qsio.v1", _qsio_payload(
            qsio.qsio_id,
            qsio.qsi,
            qsio.pre_state_hashes,
            qsio.proposed_transitions,
            qsio.accepted_transitions,
            qsio.witnesses,
            qsio.outcome,
            qsio.reason_codes,
            qsio.parent_qsio_hashes,
            qsio.created_at,
        )))
        context.ledger.append(qsio)
        return qsio
    if qsi.interaction_type == "genesis":
        payload = qsi.requested_transition
        qso_id = str(payload["qso_id"])
        state_hash = str(payload["state_hash"])
        if qso_id in context.qso_registry:
            raise QSIOValidationError(f"QSO already exists: {qso_id}")
        if not context.genesis_authorized:
            raise CanonViolationError("Genesis not authorized")
        from .qso import QSO, QSOState, create_qso

        state = QSOState(
            state_version=int(payload["state_version"]),
            lifecycle="active",
            lumen=dict(payload["lumen"]),
            umbra_commitment=payload.get("umbra_commitment"),
            telion_hash=str(payload["telion_hash"]),
            memora_root=str(payload["memora_root"]),
            logical_time=int(payload["logical_time"]),
            content_hash=state_hash,
        )
        qso = create_qso(
            qso_id=qso_id,
            genome_version=str(payload["genome_version"]),
            canon_constraints=tuple(payload["canon_constraints"]),
            state=state,
            permissions=context.permissions,
            created_at=context.timestamp(),
        )
        context.register_qso(qso)
        transition = build_transition(
            qso_id=qso_id,
            operation="genesis",
            precondition_hash="sha256:0",
            patch=(
                {"field": "lifecycle", "value": "active"},
                {"field": "lumen", "value": payload["lumen"]},
            ),
            postcondition_hash=state.content_hash,
            confidence=1.0,
            evidence_refs=tuple(qsi.input_refs),
        )
        witness = build_witness(
            witness_id=f"wit_{qso_id}",
            verifier="genesis-witness",
            verified=True,
            evidence_refs=tuple(qsi.input_refs),
            observed_at=context.timestamp(),
            notes="Genesis verified",
        )
        qsio = QSIO(
            qsio_id=f"qsio_{qso_id}_{qsi.logical_time}",
            qsi=qsi,
            pre_state_hashes={},
            proposed_transitions=(transition,),
            accepted_transitions=(transition,),
            witnesses=(witness,),
            outcome="accepted",
            reason_codes=(),
            parent_qsio_hashes=tuple(record.content_hash for record in context.ledger.records[-1:]),
            created_at=context.timestamp(),
            content_hash="",
        )
        object.__setattr__(qsio, "content_hash", hash_payload("qsio.v1", _qsio_payload(
            qsio.qsio_id,
            qsio.qsi,
            qsio.pre_state_hashes,
            qsio.proposed_transitions,
            qsio.accepted_transitions,
            qsio.witnesses,
            qsio.outcome,
            qsio.reason_codes,
            qsio.parent_qsio_hashes,
            qsio.created_at,
        )))
        context.ledger.append(qsio)
        return qsio
    pre_state_hashes = {
        qso_id: context.current_state(qso_id).content_hash for qso_id in qsi.participants
    }
    if qsi.interaction_type == "quietus":
        qso_id = qsi.participants[0]
        qso = context.qso_registry[qso_id]
        transition = build_transition(
            qso_id=qso_id,
            operation="quietus",
            precondition_hash=pre_state_hashes[qso_id],
            patch=(
                {"field": "state_version", "value": qso.state.state_version + 1},
                {"field": "lifecycle", "value": "quietus"},
                {"field": "logical_time", "value": qso.state.logical_time + 1},
            ),
            postcondition_hash=hash_payload("qso.state.v1", {
                "state_version": qso.state.state_version + 1,
                "lifecycle": "quietus",
                "lumen": qso.state.lumen,
                "umbra_commitment": qso.state.umbra_commitment,
                "telion_hash": qso.state.telion_hash,
                "memora_root": qso.state.memora_root,
                "logical_time": qso.state.logical_time + 1,
            }),
            confidence=1.0,
            evidence_refs=tuple(qsi.input_refs),
        )
        witness = build_witness(
            witness_id=f"wit_{qso_id}_{qsi.logical_time}",
            verifier="quietus-witness",
            verified=True,
            evidence_refs=tuple(qsi.input_refs),
            observed_at=context.timestamp(),
            notes="Quietus entered",
        )
        qso = context.qso_registry[qso_id]
        new_state = _apply_patch(qso.state, transition.patch)
        context.record_state(qso_id, new_state)
        qsio = QSIO(
            qsio_id=f"qsio_{qso_id}_{qsi.logical_time}",
            qsi=qsi,
            pre_state_hashes=pre_state_hashes,
            proposed_transitions=(transition,),
            accepted_transitions=(transition,),
            witnesses=(witness,),
            outcome="accepted",
            reason_codes=(),
            parent_qsio_hashes=tuple(record.content_hash for record in context.ledger.records[-1:]),
            created_at=context.timestamp(),
            content_hash="",
        )
        object.__setattr__(qsio, "content_hash", hash_payload("qsio.v1", _qsio_payload(
            qsio.qsio_id,
            qsio.qsi,
            qsio.pre_state_hashes,
            qsio.proposed_transitions,
            qsio.accepted_transitions,
            qsio.witnesses,
            qsio.outcome,
            qsio.reason_codes,
            qsio.parent_qsio_hashes,
            qsio.created_at,
        )))
        context.ledger.append(qsio)
        return qsio
    qso_id = qsi.participants[0]
    qso = context.qso_registry[qso_id]
    requested = qsi.requested_transition
    new_lumen = dict(qso.state.lumen)
    if "lumen" in requested:
        new_lumen.update(dict(requested["lumen"]))  # type: ignore[arg-type]
    if "assertion" in requested:
        new_lumen["assertion"] = requested["assertion"]
    if "kind" in requested and requested["kind"] == "synthesis":
        new_lumen["synthesis"] = requested.get("synthesis", {})
    if qso.state.lifecycle == "quietus":
        raise QSIOValidationError("Cannot mutate quietus state")
    transition = build_transition(
        qso_id=qso_id,
        operation=qsi.interaction_type,
        precondition_hash=pre_state_hashes[qso_id],
        patch=(
            {"field": "state_version", "value": qso.state.state_version + 1},
            {"field": "lumen", "value": new_lumen},
            {"field": "logical_time", "value": qso.state.logical_time + 1},
        ),
        postcondition_hash=hash_payload("qso.state.v1", {
            "state_version": qso.state.state_version + 1,
            "lifecycle": qso.state.lifecycle,
            "lumen": new_lumen,
            "umbra_commitment": qso.state.umbra_commitment,
            "telion_hash": qso.state.telion_hash,
            "memora_root": qso.state.memora_root,
            "logical_time": qso.state.logical_time + 1,
        }),
        confidence=float(requested.get("confidence", 0.9)) if isinstance(requested.get("confidence", 0.9), (int, float)) else 0.9,
        evidence_refs=tuple(qsi.input_refs),
    )
    witness = build_witness(
        witness_id=f"wit_{qso_id}_{qsi.logical_time}",
        verifier=qsi.interaction_type,
        verified=True,
        evidence_refs=tuple(qsi.input_refs),
        observed_at=context.timestamp(),
        notes=f"{qsi.interaction_type} accepted",
    )
    new_state = _apply_patch(qso.state, transition.patch)
    context.record_state(qso_id, new_state)
    qsio = QSIO(
        qsio_id=f"qsio_{qso_id}_{qsi.logical_time}",
        qsi=qsi,
        pre_state_hashes=pre_state_hashes,
        proposed_transitions=(transition,),
        accepted_transitions=(transition,),
        witnesses=(witness,),
        outcome="accepted",
        reason_codes=(),
        parent_qsio_hashes=tuple(record.content_hash for record in context.ledger.records[-1:]),
        created_at=context.timestamp(),
        content_hash="",
    )
    object.__setattr__(qsio, "content_hash", hash_payload("qsio.v1", _qsio_payload(
        qsio.qsio_id,
        qsio.qsi,
        qsio.pre_state_hashes,
        qsio.proposed_transitions,
        qsio.accepted_transitions,
        qsio.witnesses,
        qsio.outcome,
        qsio.reason_codes,
        qsio.parent_qsio_hashes,
        qsio.created_at,
    )))
    context.ledger.append(qsio)
    return qsio


def submit_qsi(qsi: QSI, context: "RuntimeContext") -> QSIO:
    return execute_qsi(qsi, context)


def enter_quietus(qso_id: str, reason: str, context: "RuntimeContext") -> QSIO:
    context.quietus_registry[qso_id] = reason
    qsi = QSI(
        interaction_type="quietus",
        initiator=qso_id,
        participants=(qso_id,),
        input_refs=(),
        requested_transition={"reason": reason},
        logical_time=context.current_state(qso_id).logical_time + 1,
    )
    return execute_qsi(qsi, context)


def resume_from_quietus(qso_id: str, context: "RuntimeContext") -> QSIO:
    if qso_id not in context.quietus_registry:
        raise QSIOValidationError(f"QSO {qso_id} is not in Quietus")
    qso = context.qso_registry[qso_id]
    if qso.state.lifecycle != "quietus":
        raise QSIOValidationError(f"QSO {qso_id} is not in Quietus")
    pre_state_hash = qso.state.content_hash
    transition = build_transition(
        qso_id=qso_id,
        operation="resume",
        precondition_hash=pre_state_hash,
        patch=(
            {"field": "state_version", "value": qso.state.state_version + 1},
            {"field": "lifecycle", "value": "active"},
            {"field": "logical_time", "value": qso.state.logical_time + 1},
        ),
        postcondition_hash=hash_payload("qso.state.v1", {
            "state_version": qso.state.state_version + 1,
            "lifecycle": "active",
            "lumen": qso.state.lumen,
            "umbra_commitment": qso.state.umbra_commitment,
            "telion_hash": qso.state.telion_hash,
            "memora_root": qso.state.memora_root,
            "logical_time": qso.state.logical_time + 1,
        }),
        confidence=1.0,
        evidence_refs=(),
    )
    witness = build_witness(
        witness_id=f"wit_resume_{qso_id}_{qso.state.logical_time + 1}",
        verifier="resume-witness",
        verified=True,
        evidence_refs=(),
        observed_at=context.timestamp(),
        notes="Quietus resumed",
    )
    new_state = _apply_patch(qso.state, transition.patch)
    context.record_state(qso_id, new_state)
    qsio = QSIO(
        qsio_id=f"qsio_{qso_id}_resume_{new_state.logical_time}",
        qsi=QSI(
            interaction_type="resume",
            initiator=qso_id,
            participants=(qso_id,),
            input_refs=(),
            requested_transition={"reason": context.quietus_registry[qso_id]},
            logical_time=new_state.logical_time,
        ),
        pre_state_hashes={qso_id: pre_state_hash},
        proposed_transitions=(transition,),
        accepted_transitions=(transition,),
        witnesses=(witness,),
        outcome="accepted",
        reason_codes=(),
        parent_qsio_hashes=tuple(record.content_hash for record in context.ledger.records[-1:]),
        created_at=context.timestamp(),
        content_hash="",
    )
    object.__setattr__(qsio, "content_hash", hash_payload("qsio.v1", _qsio_payload(
        qsio.qsio_id,
        qsio.qsi,
        qsio.pre_state_hashes,
        qsio.proposed_transitions,
        qsio.accepted_transitions,
        qsio.witnesses,
        qsio.outcome,
        qsio.reason_codes,
        qsio.parent_qsio_hashes,
        qsio.created_at,
    )))
    context.ledger.append(qsio)
    del context.quietus_registry[qso_id]
    return qsio


from .runtime.sanctum import RuntimeContext  # noqa: E402
from .types import QSOState  # noqa: E402
