from __future__ import annotations

from dataclasses import dataclass

from .types import JSONValue


@dataclass(frozen=True)
class QSI:
    interaction_type: str
    initiator: str
    participants: tuple[str, ...]
    input_refs: tuple[str, ...]
    requested_transition: dict[str, JSONValue]
    logical_time: int
