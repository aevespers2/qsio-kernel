from __future__ import annotations

from hashlib import sha256


def stable_id(prefix: str, *parts: str) -> str:
    digest = sha256()
    digest.update(prefix.encode("utf-8"))
    for part in parts:
        digest.update(b"\x1f")
        digest.update(part.encode("utf-8"))
    return f"{prefix}_{digest.hexdigest()[:24]}"
