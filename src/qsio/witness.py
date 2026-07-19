from __future__ import annotations

from dataclasses import dataclass

from .serialization import hash_payload
from .types import Hash, Timestamp


@dataclass(frozen=True)
class WitnessRecord:
    witness_id: str
    verifier: str
    verified: bool
    summary_hash: Hash
    evidence_refs: tuple[Hash, ...]
    observed_at: Timestamp
    notes: str


def build_witness(
    witness_id: str,
    verifier: str,
    verified: bool,
    evidence_refs: tuple[Hash, ...],
    observed_at: Timestamp,
    notes: str,
) -> WitnessRecord:
    payload = {
        "witness_id": witness_id,
        "verifier": verifier,
        "verified": verified,
        "evidence_refs": list(evidence_refs),
        "observed_at": observed_at,
        "notes": notes,
    }
    return WitnessRecord(
        witness_id=witness_id,
        verifier=verifier,
        verified=verified,
        summary_hash=hash_payload("witness.v1", payload),
        evidence_refs=evidence_refs,
        observed_at=observed_at,
        notes=notes,
    )
