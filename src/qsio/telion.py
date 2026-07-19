from __future__ import annotations

from dataclasses import dataclass

from .serialization import hash_payload
from .types import Hash


@dataclass(frozen=True)
class Telion:
    telion_id: str
    version: int
    purposes: tuple[str, ...]
    priorities: dict[str, float]
    parent_hash: Hash | None
    content_hash: Hash


def build_telion(
    telion_id: str,
    version: int,
    purposes: tuple[str, ...],
    priorities: dict[str, float],
    parent_hash: Hash | None,
) -> Telion:
    payload = {
        "telion_id": telion_id,
        "version": version,
        "purposes": list(purposes),
        "priorities": priorities,
        "parent_hash": parent_hash,
    }
    return Telion(
        telion_id=telion_id,
        version=version,
        purposes=purposes,
        priorities=dict(priorities),
        parent_hash=parent_hash,
        content_hash=hash_payload("telion.v1", payload),
    )
