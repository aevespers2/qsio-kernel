from __future__ import annotations

from dataclasses import dataclass

from ..errors import QSIOValidationError
from .sanctum import RuntimeLimits


@dataclass
class Scheduler:
    limits: RuntimeLimits

    def enforce(self, *, steps: int, interactions: int, memory_growth: int, duration: int, spawned: int) -> None:
        if steps > self.limits.maximum_steps:
            raise QSIOValidationError("maximum steps exceeded")
        if interactions > self.limits.maximum_interactions:
            raise QSIOValidationError("maximum interactions exceeded")
        if memory_growth > self.limits.maximum_memory_growth:
            raise QSIOValidationError("maximum memory growth exceeded")
        if duration > self.limits.maximum_duration_seconds:
            raise QSIOValidationError("maximum duration exceeded")
        if spawned > self.limits.maximum_spawned_objects:
            raise QSIOValidationError("spawned object limit exceeded")
