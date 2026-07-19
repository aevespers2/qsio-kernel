from __future__ import annotations

from dataclasses import dataclass

from .serialization import hash_payload
from .types import EpistemicValue, Hash


@dataclass(frozen=True)
class MemoraEntry:
    entry_id: str
    parent_hash: Hash | None
    epistemic: EpistemicValue
    provenance_refs: tuple[Hash, ...]
    content_hash: Hash


def build_memora_entry(
    entry_id: str,
    parent_hash: Hash | None,
    epistemic: EpistemicValue,
    provenance_refs: tuple[Hash, ...],
) -> MemoraEntry:
    payload = {
        "entry_id": entry_id,
        "parent_hash": parent_hash,
        "epistemic": epistemic,
        "provenance_refs": list(provenance_refs),
    }
    return MemoraEntry(
        entry_id=entry_id,
        parent_hash=parent_hash,
        epistemic=epistemic,
        provenance_refs=provenance_refs,
        content_hash=hash_payload("memora.v1", payload),
    )
