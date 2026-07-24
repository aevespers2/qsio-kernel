# Developer onboarding

## Prerequisites

- Python 3.12 or later
- Git
- A virtual environment tool (`venv` is sufficient)

The runtime has no required third-party package dependencies. The test extra installs `pytest`.

## Local setup

```bash
git clone https://github.com/aevespers2/qsio-kernel.git
cd qsio-kernel
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
```

On Windows PowerShell, activate with:

```powershell
.venv\Scripts\Activate.ps1
```

## Validate the baseline

```bash
pytest
python -m qsio.demo
```

The test suite currently checks the most important prototype guarantees:

- canon-forbidden external-operation requests are rejected;
- Quietus blocks ordinary interaction until explicit resume;
- resumed QSIO records verify; and
- ledger replay reproduces the final state hashes of the four-QSO demonstration.

## Repository layout

```text
.
├── docs/                  # Pages-ready project and developer documentation
├── src/qsio/              # Kernel records, execution logic, runtime, replay
│   └── runtime/           # Sanctum context, permissions, runtime limits
├── tests/                 # Executable behavioral checks
├── pyproject.toml         # Packaging, Python version, pytest, and mypy settings
├── taskchain.md           # Ordered delivery plan and scope gates
├── release.md             # Release evidence and blocking criteria
└── changelog.md           # User-visible repository history
```

## Development workflow

1. Start from the current default branch.
2. Create a focused branch for one bounded change.
3. Read `taskchain.md` and `release.md` before changing behavior.
4. Add or update tests before claiming a new invariant.
5. Update architecture/design documentation when semantics change.
6. Add a changelog entry under `Unreleased`.
7. Run the complete test suite and the demo.
8. Open a pull request that distinguishes implementation evidence from proposed behavior.

## Scope-sensitive changes

The following require an explicit design decision before implementation:

- durable persistence or schema migration;
- cryptographic signing or identity authority;
- external witnesses;
- network, model, filesystem, or subprocess access;
- concurrency or distributed execution;
- autonomous QSO creation;
- changes to canonical serialization or hash domains;
- new lifecycle states or changed Quietus semantics; and
- compatibility promises for external consumers.

Do not infer authorization for these capabilities from existing class names or conceptual documents.

## Adding an interaction type

A bounded interaction type should include:

- a clear QSI payload contract;
- validation rules;
- deterministic transition construction;
- precondition and postcondition hashes;
- witness behavior;
- rejection and exception behavior;
- replay coverage;
- tests for accepted and rejected paths; and
- documentation of compatibility impact.

## Adding a state field

State fields participate in content hashing. A field addition therefore requires a versioned schema or hash-domain decision. Never add or reinterpret a hashed state field without fixtures that demonstrate deterministic serialization and explain how older records are handled.

## Documentation preview

The repository includes `mkdocs.yml` but does not add MkDocs to the runtime package dependencies. To preview the site in a documentation-only environment:

```bash
python -m pip install mkdocs
mkdocs serve
```

Publishing GitHub Pages remains an administrative action and should occur only after link, rendering, accessibility, and release checks are recorded.

## Debugging guidance

When a transition behaves unexpectedly, inspect in this order:

1. QSI initiator, participants, interaction type, and logical time;
2. validation reason codes or raised lifecycle exception;
3. recorded `pre_state_hashes`;
4. transition patch and `postcondition_hash`;
5. witness metadata;
6. QSIO `parent_qsio_hashes` and `content_hash`; and
7. replayed state through the affected QSIO.

This order preserves the evidence chain and avoids debugging solely from mutable current state.
