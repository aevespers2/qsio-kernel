from __future__ import annotations

from .errors import QSIOValidationError
from .qso import QSOState
from .serialization import hash_payload
from .runtime.sanctum import RuntimeContext
from .qsio import QSIO, _apply_patch


def replay(qso_id: str, through: str | None = None, context: RuntimeContext | None = None) -> QSOState:
    if context is None:
        raise QSIOValidationError("replay requires an explicit RuntimeContext")
    state: QSOState | None = None
    for record in context.ledger.through(through):
        if record.outcome != "accepted":
            continue
        for transition in record.accepted_transitions:
            if transition.qso_id != qso_id:
                continue
            current = context.qso_history[qso_id][0] if state is None else state
            state = _apply_patch(current, transition.patch)
    if state is None:
        return context.current_state(qso_id)
    return state
