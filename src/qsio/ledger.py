from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class AppendOnlyLedger:
    records: list["QSIO"] = field(default_factory=list)

    def append(self, qsio: "QSIO") -> None:
        self.records.append(qsio)

    def through(self, qsio_id: str | None) -> list["QSIO"]:
        if qsio_id is None:
            return list(self.records)
        selected: list["QSIO"] = []
        for record in self.records:
            selected.append(record)
            if record.qsio_id == qsio_id:
                break
        return selected


from .qsio import QSIO  # noqa: E402
