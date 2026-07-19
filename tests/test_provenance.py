from __future__ import annotations

from qsio.demo import run_demo


def test_demo_retains_provenance_and_epistemic_status() -> None:
    result = run_demo()
    ctx = result.context
    for qso_id in ("EXPLORER", "ARCHIVIST", "SKEPTIC", "SYNTHESIST"):
        state = ctx.current_state(qso_id)
        assert state.memora_root.startswith("sha256:")
        assert state.telion_hash.startswith("sha256:")
