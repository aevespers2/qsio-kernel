from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from hashlib import sha256
from typing import Any

from .types import Hash


def _normalize(value: Any) -> Any:
    if is_dataclass(value):
        return _normalize(asdict(value))
    if isinstance(value, dict):
        return {str(key): _normalize(value[key]) for key in sorted(value)}
    if isinstance(value, tuple):
        return [_normalize(item) for item in value]
    if isinstance(value, list):
        return [_normalize(item) for item in value]
    if isinstance(value, float):
        if value != value or value in (float("inf"), float("-inf")):
            raise ValueError("NaN and Infinity are not allowed")
        return value
    return value


def canonical_json(value: Any) -> str:
    normalized = _normalize(value)
    return json.dumps(normalized, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def hash_payload(schema_version: str, payload: Any) -> Hash:
    data = f"QSIO:{schema_version}:{canonical_json(payload)}".encode("utf-8")
    return f"sha256:{sha256(data).hexdigest()}"
