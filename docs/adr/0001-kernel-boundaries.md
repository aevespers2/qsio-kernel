# ADR 0001: Kernel Boundaries

We keep QSO state mutations behind QSIO records, preserve explicit provenance,
and use a bounded sanctum with default-deny capabilities.
