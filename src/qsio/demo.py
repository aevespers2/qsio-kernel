from __future__ import annotations

from dataclasses import dataclass

from .memora import build_memora_entry
from .qsi import QSI
from .qsio import execute_qsi, verify_qsio
from .qso import build_qso_state
from .replay import replay
from .runtime.permissions import PermissionSet
from .runtime.sanctum import RuntimeContext
from .serialization import canonical_json
from .telion import build_telion
from .types import EpistemicValue


@dataclass(frozen=True)
class DemoResult:
    context: RuntimeContext
    qsios: tuple["QSIO", ...]


def build_demo_context() -> RuntimeContext:
    return RuntimeContext()


def run_demo(context: RuntimeContext | None = None) -> DemoResult:
    ctx = context or build_demo_context()
    PermissionSet()
    explorer_telion = build_telion("telion_explorer", 1, ("seek novel patterns",), {"novelty": 1.0}, None)
    archivist_telion = build_telion("telion_archivist", 1, ("preserve provenance and context",), {"provenance": 1.0}, None)
    skeptic_telion = build_telion("telion_skeptic", 1, ("search for contradiction and unsupported claims",), {"scrutiny": 1.0}, None)
    synthesist_telion = build_telion("telion_synthesist", 1, ("combine compatible findings",), {"synthesis": 1.0}, None)
    memora_seed = build_memora_entry(
        "memora_seed",
        None,
        EpistemicValue(
            value={"kind": "seed"},
            status="observed",
            confidence=1.0,
            evidence_refs=(),
            method="bootstrap",
            observed_at="2026-07-19T00:00:00Z",
        ),
        (),
    )
    spec_items = (
        ("EXPLORER", "seeks novel patterns", explorer_telion),
        ("ARCHIVIST", "preserves provenance and context", archivist_telion),
        ("SKEPTIC", "searches for contradiction and unsupported claims", skeptic_telion),
        ("SYNTHESIST", "combines compatible findings", synthesist_telion),
    )
    qsios = []
    for logical_time, (qso_id, description, telion) in enumerate(spec_items, start=1):
        qso_state = build_qso_state(
            state_version=1,
            lifecycle="active",
            lumen={"name": qso_id, "role": description.split()[0].lower()},
            umbra_commitment=None,
            telion_hash=telion.content_hash,
            memora_root=memora_seed.content_hash,
            logical_time=logical_time,
        )
        qsi = QSI(
            interaction_type="genesis",
            initiator="system",
            participants=(qso_id,),
            input_refs=(),
            requested_transition={
                "qso_id": qso_id,
                "description": description,
                "genome_version": "qsio.genome.v1",
                "canon_constraints": ("identity stable", "no external io", "no uncontrolled spawn"),
                "state_version": 1,
                "lumen": qso_state.lumen,
                "umbra_commitment": None,
                "telion_hash": telion.content_hash,
                "memora_root": memora_seed.content_hash,
                "logical_time": logical_time,
                "state_hash": qso_state.content_hash,
            },
            logical_time=logical_time,
        )
        qsio = execute_qsi(qsi, ctx)
        assert verify_qsio(qsio).verified
        qsios.append(qsio)
    interactions = (
        QSI(
            interaction_type="hypothesis",
            initiator="EXPLORER",
            participants=("EXPLORER",),
            input_refs=(qsios[0].content_hash,),
            requested_transition={"assertion": {"kind": "hypothesis", "text": "Novel structure exists"}},
            logical_time=5,
        ),
        QSI(
            interaction_type="provenance",
            initiator="ARCHIVIST",
            participants=("ARCHIVIST",),
            input_refs=(qsios[1].content_hash, qsios[0].content_hash),
            requested_transition={"lumen": {"provenance": [qsios[0].content_hash, qsios[1].content_hash]}},
            logical_time=6,
        ),
        QSI(
            interaction_type="contradiction_check",
            initiator="SKEPTIC",
            participants=("SKEPTIC",),
            input_refs=(qsios[2].content_hash,),
            requested_transition={"lumen": {"contradictions": ["unsupported_claim"]}},
            logical_time=7,
        ),
        QSI(
            interaction_type="synthesis",
            initiator="SYNTHESIST",
            participants=("SYNTHESIST",),
            input_refs=(qsios[0].content_hash, qsios[1].content_hash, qsios[2].content_hash),
            requested_transition={"kind": "synthesis", "synthesis": {"qualified": True, "compatible": True}},
            logical_time=8,
        ),
    )
    for qsi in interactions:
        qsios.append(execute_qsi(qsi, ctx))
    for logical_time, qso_id in enumerate(("EXPLORER", "ARCHIVIST", "SKEPTIC", "SYNTHESIST"), start=9):
        qsios.append(
            execute_qsi(
                QSI(
                    interaction_type="quietus",
                    initiator=qso_id,
                    participants=(qso_id,),
                    input_refs=(qsios[-1].content_hash,),
                    requested_transition={"reason": "demo complete"},
                    logical_time=logical_time,
                ),
                ctx,
            )
        )
    for qso_id in ("EXPLORER", "ARCHIVIST", "SKEPTIC", "SYNTHESIST"):
        assert replay(qso_id, context=ctx).content_hash == ctx.current_state(qso_id).content_hash
    return DemoResult(context=ctx, qsios=tuple(qsios))


def main() -> None:
    result = run_demo()
    for qsio in result.qsios:
        print(canonical_json(qsio))


from .qsio import QSIO  # noqa: E402


if __name__ == "__main__":
    main()
