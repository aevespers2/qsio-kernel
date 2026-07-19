from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Nexis:
    nexis_id: str
    participants: tuple[str, ...]
    relation_type: str
    permissions: dict[str, tuple[str, ...]]
    covenant_hash: str | None
    created_by_qsio: str
    status: str
