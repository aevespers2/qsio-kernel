from __future__ import annotations

import pytest

from qsio.demo import build_demo_context, run_demo
from qsio.memora import build_memora_entry
from qsio.qsi import QSI
from qsio.qso import build_qso_state
from qsio.qsio import execute_qsi, verify_qsio
from qsio.telion import build_telion
from qsio.types import EpistemicValue


def _seed_context():
    ctx = build_demo_context()
    telion = build_telion("telion", 1, ("purpose",), {"purpose": 1.0}, None)
    memora = build_memora_entry(
        "memora",
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
    return ctx, telion, memora


def test_identical_inputs_generate_identical_qsio_hashes() -> None:
    ctx1, telion1, memora1 = _seed_context()
    ctx2, telion2, memora2 = _seed_context()
    state1 = build_qso_state(
        state_version=1,
        lifecycle="active",
        lumen={"name": "A"},
        umbra_commitment=None,
        telion_hash=telion1.content_hash,
        memora_root=memora1.content_hash,
        logical_time=1,
    )
    state2 = build_qso_state(
        state_version=1,
        lifecycle="active",
        lumen={"name": "A"},
        umbra_commitment=None,
        telion_hash=telion2.content_hash,
        memora_root=memora2.content_hash,
        logical_time=1,
    )
    qsi1 = QSI(
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
            "lumen": state1.lumen,
            "umbra_commitment": None,
            "telion_hash": telion1.content_hash,
            "memora_root": memora1.content_hash,
            "logical_time": 1,
            "state_hash": state1.content_hash,
        },
        logical_time=1,
    )
    qsi2 = QSI(
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
            "lumen": state2.lumen,
            "umbra_commitment": None,
            "telion_hash": telion2.content_hash,
            "memora_root": memora2.content_hash,
            "logical_time": 1,
            "state_hash": state2.content_hash,
        },
        logical_time=1,
    )
    qsio1 = execute_qsi(qsi1, ctx1)
    qsio2 = execute_qsi(qsi2, ctx2)
    assert qsio1.content_hash == qsio2.content_hash


def test_tampered_qsio_fails_verification() -> None:
    ctx, telion, memora = _seed_context()
    state = build_qso_state(
        state_version=1,
        lifecycle="active",
        lumen={"name": "A"},
        umbra_commitment=None,
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
                "umbra_commitment": None,
                "telion_hash": telion.content_hash,
                "memora_root": memora.content_hash,
                "logical_time": 1,
                "state_hash": state.content_hash,
            },
            logical_time=1,
        ),
        ctx,
    )
    object.__setattr__(qsio, "content_hash", "sha256:deadbeef")
    assert not verify_qsio(qsio).verified
