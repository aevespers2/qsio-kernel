from __future__ import annotations

from dataclasses import dataclass, field

from ..clock import LogicalClock
from ..errors import PermissionDeniedError, QuietusError
from ..types import QSOState, Timestamp
from .permissions import Capability, PermissionSet


@dataclass(frozen=True)
class RuntimeLimits:
    maximum_steps: int = 10_000
    maximum_interactions: int = 1_000
    maximum_memory_growth: int = 1_000_000
    maximum_duration_seconds: int = 180
    maximum_spawned_objects: int = 0
    quarantine_threshold: int = 3


@dataclass
class Ledger:
    records: list["QSIO"] = field(default_factory=list)

    def append(self, qsio: "QSIO") -> None:
        self.records.append(qsio)

    def through(self, qsio_id: str | None) -> list["QSIO"]:
        if qsio_id is None:
            return list(self.records)
        filtered: list["QSIO"] = []
        for record in self.records:
            filtered.append(record)
            if record.qsio_id == qsio_id:
                break
        return filtered


@dataclass
class RuntimeContext:
    clock: LogicalClock = field(default_factory=LogicalClock)
    limits: RuntimeLimits = field(default_factory=RuntimeLimits)
    permissions: PermissionSet = field(default_factory=PermissionSet)
    ledger: Ledger = field(default_factory=Ledger)
    qso_registry: dict[str, "QSO"] = field(default_factory=dict)
    qso_history: dict[str, list[QSOState]] = field(default_factory=dict)
    quietus_registry: dict[str, str] = field(default_factory=dict)
    genesis_authorized: bool = True

    def timestamp(self) -> Timestamp:
        return f"2026-07-19T00:00:{self.clock.tick():02d}Z"

    def register_qso(self, qso: "QSO") -> None:
        self.qso_registry[qso.qso_id] = qso
        self.qso_history.setdefault(qso.qso_id, []).append(qso.state)

    def record_state(self, qso_id: str, state: QSOState) -> None:
        self.qso_history.setdefault(qso_id, []).append(state)
        qso = self.qso_registry[qso_id]
        qso.state = state

    def current_state(self, qso_id: str) -> QSOState:
        return self.qso_registry[qso_id].state

    def ensure_capability(self, resource: str, operation: str) -> None:
        if not self.permissions.allows(resource, operation):
            raise PermissionDeniedError(f"Capability denied for {resource}:{operation}")

    def ensure_not_quietus(self, qso_id: str) -> None:
        state = self.current_state(qso_id)
        if state.lifecycle == "quietus":
            raise QuietusError(f"QSO {qso_id} is in Quietus")


from ..qsio import QSIO  # noqa: E402
from ..qso import QSO  # noqa: E402
