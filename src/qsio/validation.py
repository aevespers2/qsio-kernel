from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ValidationReport:
    valid: bool
    reason_codes: tuple[str, ...]
    details: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class VerificationReport:
    verified: bool
    reason_codes: tuple[str, ...]
    details: dict[str, str] = field(default_factory=dict)
