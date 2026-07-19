from __future__ import annotations

from dataclasses import dataclass

from .serialization import hash_payload
from .types import Hash, JSONValue


@dataclass(frozen=True)
class StateTransition:
    qso_id: str
    operation: str
    precondition_hash: Hash
    patch: tuple[dict[str, JSONValue], ...]
    postcondition_hash: Hash
    confidence: float
    evidence_refs: tuple[Hash, ...]


def build_transition(
    qso_id: str,
    operation: str,
    precondition_hash: Hash,
    patch: tuple[dict[str, JSONValue], ...],
    postcondition_hash: Hash,
    confidence: float,
    evidence_refs: tuple[Hash, ...],
) -> StateTransition:
    payload = {
        "qso_id": qso_id,
        "operation": operation,
        "precondition_hash": precondition_hash,
        "patch": list(patch),
        "postcondition_hash": postcondition_hash,
        "confidence": confidence,
        "evidence_refs": list(evidence_refs),
    }
    return StateTransition(
        qso_id=qso_id,
        operation=operation,
        precondition_hash=precondition_hash,
        patch=patch,
        postcondition_hash=postcondition_hash,
        confidence=confidence,
        evidence_refs=evidence_refs,
    )
