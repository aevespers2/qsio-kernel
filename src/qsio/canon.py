from __future__ import annotations

from dataclasses import dataclass

from .serialization import hash_payload
from .types import Hash


@dataclass(frozen=True)
class Canon:
    version: str
    constraints: tuple[str, ...]
    content_hash: Hash


def build_canon(version: str, constraints: tuple[str, ...]) -> Canon:
    payload = {"version": version, "constraints": list(constraints)}
    return Canon(version=version, constraints=constraints, content_hash=hash_payload(version, payload))
