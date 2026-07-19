from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal, TypeAlias

JSONValue: TypeAlias = (
    str
    | int
    | float
    | bool
    | None
    | list["JSONValue"]
    | dict[str, "JSONValue"]
)

SchemaVersion = str
Hash = str
Timestamp = str


@dataclass(frozen=True)
class EpistemicValue:
    value: JSONValue
    status: Literal["observed", "derived", "inferred", "hypothesized", "unknown"]
    confidence: float
    evidence_refs: tuple[Hash, ...]
    method: str
    observed_at: Timestamp | None


@dataclass(frozen=True)
class Canon:
    version: str
    constraints: tuple[str, ...]
    content_hash: Hash


@dataclass(frozen=True)
class Telion:
    telion_id: str
    version: int
    purposes: tuple[str, ...]
    priorities: dict[str, float]
    parent_hash: Hash | None
    content_hash: Hash


@dataclass(frozen=True)
class MemoraEntry:
    entry_id: str
    parent_hash: Hash | None
    epistemic: EpistemicValue
    provenance_refs: tuple[Hash, ...]
    content_hash: Hash


@dataclass(frozen=True)
class QSOState:
    state_version: int
    lifecycle: Literal["genesis", "active", "quietus", "quarantined", "retired"]
    lumen: dict[str, JSONValue]
    umbra_commitment: Hash | None
    telion_hash: Hash
    memora_root: Hash
    logical_time: int
    content_hash: Hash


@dataclass(frozen=True)
class Capability:
    name: str
    resource: str
    operations: tuple[str, ...]
    expires_at: Timestamp | None
    granted_by: str


@dataclass(frozen=True)
class PermissionSet:
    capabilities: tuple[Capability, ...] = field(default_factory=tuple)

    def allows(self, resource: str, operation: str) -> bool:
        return any(
            cap.resource == resource and operation in cap.operations for cap in self.capabilities
        )


@dataclass(frozen=True)
class WitnessRecord:
    witness_id: str
    verifier: str
    verified: bool
    summary_hash: Hash
    evidence_refs: tuple[Hash, ...]
    observed_at: Timestamp
    notes: str
