from __future__ import annotations

import pytest

from qsio.demo import build_demo_context
from qsio.memora import build_memora_entry
from qsio.qsi import QSI
from qsio.qso import build_qso_state
from qsio.qsio import enter_quietus, execute_qsi, resume_from_quietus, verify_qsio
from qsio.telion import build_telion
from qsio.types import EpistemicValue


def _bootstrap_context():
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
        lumen={"name": "A"},
        umbra_commitment=None,
        telion_hash=telion.content_hash,
        memora_root=memora.content_hash,
        logical_time=1,
    )
    qsi = QSI(
        interaction_type="genesis",
        initiator="system",
        participants=("A",),
        input_refs=(),
        requested_transition={
            "qso_id": "A",
            "description": "alpha",
            "genome_version": "qsio.genome.v1",
            "canon_constraints": ("identity stable", "no external io"),
            "state_version": 1,
            "lumen": state.lumen,
            "umbra_commitment": None,
            "telion_hash": telion.content_hash,
            "memora_root": memora.content_hash,
            "logical_time": 1,
            "state_hash": state.content_hash,
        },
        logical_time=1,
    )
    execute_qsi(qsi, ctx)
    return ctx


def test_canon_violations_cannot_be_accepted() -> None:
    ctx = _bootstrap_context()
    qsi = QSI(
        interaction_type="hypothesis",
        initiator="A",
        participants=("A",),
        input_refs=(),
        requested_transition={"external_io": True},
        logical_time=2,
    )
    qsio = execute_qsi(qsi, ctx)
    assert qsio.outcome == "rejected"
    assert "canon_violation" in qsio.reason_codes


def test_quietus_blocks_then_resume_allows_interactions() -> None:
    ctx = _bootstrap_context()
    enter_quietus("A", "demo pause", ctx)
    with pytest.raises(Exception):
        execute_qsi(
            QSI(
                interaction_type="hypothesis",
                initiator="A",
                participants=("A",),
                input_refs=(),
                requested_transition={"assertion": {"kind": "hypothesis"}},
                logical_time=3,
            ),
            ctx,
        )
    resume = resume_from_quietus("A", ctx)
    assert verify_qsio(resume).verified
    followup = execute_qsi(
        QSI(
            interaction_type="hypothesis",
            initiator="A",
            participants=("A",),
            input_refs=(resume.content_hash,),
            requested_transition={"assertion": {"kind": "hypothesis"}},
            logical_time=4,
        ),
        ctx,
    )
    assert followup.outcome == "accepted"
