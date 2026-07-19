from __future__ import annotations

from qsio.demo import build_demo_context
from qsio.memora import build_memora_entry
from qsio.qsi import QSI
from qsio.qso import build_qso_state
from qsio.qsio import execute_qsi
from qsio.telion import build_telion
from qsio.types import EpistemicValue


def test_umbra_never_appears_in_lumen_serialization() -> None:
    ctx = build_demo_context()
    telion = build_telion("t", 1, ("purpose",), {"purpose": 1.0}, None)
    memora = build_memora_entry(
        "m",
        None,
        EpistemicValue(
            value={"seed": True},
            status="observed",
            confidence=1.0,
            evidence_refs=(),
            method="bootstrap",
            observed_at="2026-07-19T00:00:00Z",
        ),
        (),
    )
    state = build_qso_state(
        state_version=1,
        lifecycle="active",
        lumen={"public": True},
        umbra_commitment="sha256:secret",
        telion_hash=telion.content_hash,
        memora_root=memora.content_hash,
        logical_time=1,
    )
    qsio = execute_qsi(
        QSI(
            interaction_type="genesis",
            initiator="system",
            participants=("A",),
            input_refs=(),
            requested_transition={
                "qso_id": "A",
                "description": "alpha",
                "genome_version": "qsio.genome.v1",
                "canon_constraints": ("identity stable",),
                "state_version": 1,
                "lumen": state.lumen,
                "umbra_commitment": state.umbra_commitment,
                "telion_hash": telion.content_hash,
                "memora_root": memora.content_hash,
                "logical_time": 1,
                "state_hash": state.content_hash,
            },
            logical_time=1,
        ),
        ctx,
    )
    assert "sha256:secret" not in qsio.qsi.requested_transition["lumen"]
