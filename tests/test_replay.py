from __future__ import annotations

from qsio.demo import run_demo
from qsio.replay import replay


def test_ledger_replay_reproduces_final_hashes() -> None:
    result = run_demo()
    ctx = result.context
    for qso_id in ("EXPLORER", "ARCHIVIST", "SKEPTIC", "SYNTHESIST"):
        assert replay(qso_id, context=ctx).content_hash == ctx.current_state(qso_id).content_hash
