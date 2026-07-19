from __future__ import annotations

from dataclasses import dataclass, field

from ..types import Timestamp


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
            capability.resource == resource and operation in capability.operations
            for capability in self.capabilities
        )

    def with_capability(self, capability: Capability) -> "PermissionSet":
        return PermissionSet(capabilities=self.capabilities + (capability,))
