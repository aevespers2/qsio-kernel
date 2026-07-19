from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .canon import Canon, build_canon
from .serialization import hash_payload
from .types import QSOState, Timestamp
from .runtime.permissions import PermissionSet


@dataclass
class QSO:
    qso_id: str
    genome_version: str
    canon: Canon
    state: QSOState
    permissions: PermissionSet
    created_at: Timestamp


def build_qso_state(
    *,
    state_version: int,
    lifecycle: Literal["genesis", "active", "quietus", "quarantined", "retired"],
    lumen: dict[str, object],
    umbra_commitment: str | None,
    telion_hash: str,
    memora_root: str,
    logical_time: int,
) -> QSOState:
    payload = {
        "state_version": state_version,
        "lifecycle": lifecycle,
        "lumen": lumen,
        "umbra_commitment": umbra_commitment,
        "telion_hash": telion_hash,
        "memora_root": memora_root,
        "logical_time": logical_time,
    }
    return QSOState(
        state_version=state_version,
        lifecycle=lifecycle,
        lumen=dict(lumen),
        umbra_commitment=umbra_commitment,
        telion_hash=telion_hash,
        memora_root=memora_root,
        logical_time=logical_time,
        content_hash=hash_payload("qso.state.v1", payload),
    )


def create_qso(
    *,
    qso_id: str,
    genome_version: str,
    canon_constraints: tuple[str, ...],
    state: QSOState,
    permissions: PermissionSet,
    created_at: Timestamp,
) -> QSO:
    canon = build_canon("canon.v1", canon_constraints)
    return QSO(
        qso_id=qso_id,
        genome_version=genome_version,
        canon=canon,
        state=state,
        permissions=permissions,
        created_at=created_at,
    )
