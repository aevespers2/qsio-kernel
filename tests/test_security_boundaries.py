from __future__ import annotations

import pytest

from qsio.demo import build_demo_context
from qsio.runtime.scheduler import Scheduler


def test_network_and_subprocess_denied_by_default() -> None:
    ctx = build_demo_context()
    with pytest.raises(Exception):
        ctx.ensure_capability("network", "connect")
    with pytest.raises(Exception):
        ctx.ensure_capability("subprocess", "spawn")


def test_scheduler_enforces_spawn_limit() -> None:
    ctx = build_demo_context()
    scheduler = Scheduler(ctx.limits)
    with pytest.raises(Exception):
        scheduler.enforce(steps=1, interactions=1, memory_growth=1, duration=1, spawned=1)
