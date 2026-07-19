# Threat Model

Default-deny applies to external I/O, subprocesses, network access, and uncontrolled spawning.
Validation must fail closed on stale pre-state hashes and canon violations.
