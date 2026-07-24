# Operations and recovery

## Operating posture

`qsio-kernel` currently supports one operating mode: a local Python 3.12 process with in-memory state. There is no hosted service, durable database, queue, worker fleet, remote API, background daemon, or deployment target in version `0.1.0`.

This runbook therefore focuses on reproducible local execution, evidence capture, diagnosis, and safe withdrawal of experimental artifacts. It must not be used to imply production operations readiness.

## Local verification run

From a clean checkout:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[test]'
pytest -q
python -m qsio.demo
```

Record at minimum:

```text
Repository:
Commit SHA:
Python version:
Operating system:
Install command:
Test command and result:
Demo command and result:
Start time:
Completion time:
Operator:
Observed warnings or deviations:
```

A passing demo is evidence only for the bundled deterministic scenario. It is not evidence of persistence, concurrency, external authorization, independent attestation, or production safety.

## Expected demo behavior

The bundled demo should:

1. construct a bounded runtime context;
2. authorize genesis for four role-specific QSOs;
3. execute a deterministic interaction chain;
4. append QSIO records to the in-memory ledger;
5. verify record hashes and witness flags;
6. replay final state and compare hashes; and
7. place all QSOs into Quietus.

Unexpected network access, subprocess creation, filesystem writes outside ordinary Python tooling, uncontrolled QSO creation, or nondeterministic final hashes should be treated as a stop condition.

## Evidence package

For a documentation or experimental source candidate, preserve:

- exact commit SHA;
- clean-checkout status;
- Python and dependency versions;
- complete pytest output;
- demo output;
- documentation build output;
- generated-site artifact hash, when applicable;
- any expected and actual final state hashes;
- known warnings and limitations; and
- the reviewer or approver decision.

Evidence should be immutable or content addressed when practical. Do not store secrets, personal data, credentials, private prompts, or sensitive evidence in public workflow artifacts.

## Documentation build

The documentation workflow builds the site strictly from the submitted pull-request head. The equivalent local command is:

```bash
python -m pip install 'mkdocs==1.6.1'
mkdocs build --strict --site-dir site
```

After building, verify:

```bash
test -f site/index.html
find site -type f -maxdepth 5 | sort
```

The generated `site/` directory is disposable build output and should not be committed unless a separately approved Pages publication model requires it.

## Health indicators

Because there is no long-running service, health is evaluated per execution.

| Indicator | Healthy result | Failure meaning |
| --- | --- | --- |
| Installation | package installs from reviewed source | packaging or environment defect |
| Tests | all expected tests pass | behavior, fixture, dependency, or environment regression |
| Demo completion | deterministic chain completes | runtime or scenario defect |
| Record verification | every expected record verifies | content hash or witness inconsistency |
| Replay | reconstructed final hash matches runtime hash | ledger or transition divergence |
| Quietus | ordinary mutation is blocked after entry | lifecycle control failure |
| Documentation | strict MkDocs build succeeds | broken navigation, links, syntax, or configuration |

## Failure triage

### Installation failure

1. Confirm Python 3.12 or later.
2. Confirm the checkout SHA and clean working tree.
3. Recreate the virtual environment.
4. Capture the full installer error and dependency resolution.
5. Do not weaken package requirements merely to pass the run; record a compatibility proposal instead.

### Test failure

1. Identify the first failing test and exact commit.
2. Re-run that test in isolation with verbose output.
3. Determine whether the failure concerns serialization, hashing, lifecycle, replay, permissions, or environment assumptions.
4. Compare with the last known-good commit and fixture set.
5. Treat any Quietus bypass, stale-precondition acceptance, or replay divergence as release blocking.

### Hash mismatch

1. Preserve the input record and environment metadata.
2. Identify the domain separator and canonical payload used for hashing.
3. Compare serialized field order, value types, and omitted or default fields.
4. Check whether a schema or Python-version difference changed representation.
5. Do not rewrite existing records or tags to hide the mismatch.
6. Issue a compatibility or migration decision before accepting a new hash result.

### Replay divergence

1. Preserve the entire ordered QSIO sequence.
2. Verify every record content hash.
3. Verify parent links and transition preconditions.
4. Replay through intermediate boundaries to locate the first divergent state.
5. Quarantine the candidate release and record the smallest reproducible sequence.

### Quietus or resume failure

1. Stop further interactions for the affected QSO.
2. Preserve the lifecycle records and state history.
3. Confirm the transition precondition and witness metadata.
4. Determine whether the result was a rejected QSIO or an uncaught exception.
5. Block release until ordinary mutation cannot bypass Quietus and resume requires the intended witnessed operation.

### Forbidden-capability acceptance

A QSI requesting `network`, `external_io`, `subprocess`, or `spawn` should be rejected by the current semantic validation path.

If such a request is accepted:

1. stop the run;
2. preserve the request and QSIO result;
3. verify the exact execution path and validator version;
4. mark the candidate unsafe for release; and
5. add a regression test before repair acceptance.

Remember that successful rejection is not proof of operating-system isolation.

## Incident severity

| Severity | Example | Required response |
| --- | --- | --- |
| S0 — informational | documentation typo | correct through normal review |
| S1 — reproducibility | environment-specific test or build failure | record environment and block affected claim |
| S2 — integrity | hash mismatch or broken parent linkage | quarantine candidate and investigate |
| S3 — control failure | Quietus bypass, stale transition accepted, forbidden capability accepted | stop release, preserve evidence, require explicit repair review |
| S4 — external impact | unexpected credential, network, subprocess, or sensitive-data exposure | stop execution, revoke affected access externally, preserve audit evidence, invoke portfolio incident authority |

The repository has no autonomous incident authority. Portfolio operators must designate who may halt work, revoke capabilities, withdraw artifacts, and approve recovery.

## Recovery and rollback

The current repository has no durable runtime state to restore. Recovery means returning source and documentation to a verified commit and reproducing the local evidence package.

For an affected source release:

1. identify the last known-good tag or commit;
2. mark the defective candidate or release as withdrawn;
3. do not mutate an existing public tag;
4. prepare a corrected version with an explicit changelog entry;
5. rebuild and retest from a clean environment;
6. record artifact hashes and compatibility impact; and
7. retain the failed evidence for audit and diagnosis.

For documentation artifacts:

1. disable or supersede the affected Pages publication through the designated repository authority;
2. restore documentation from the last verified source commit;
3. rebuild the site from that immutable commit;
4. verify the generated artifact hash; and
5. document why the publication was withdrawn or replaced.

## Data handling

The demo and tests should use synthetic, non-sensitive fixtures. Before publishing workflow artifacts or Pages content, verify that they contain no:

- credentials or tokens;
- private repository information;
- personal or regulated data;
- proprietary prompts or model outputs;
- local filesystem paths that reveal sensitive details; or
- unreviewed evidence payloads.

The present in-memory ledger is not an approved evidence-retention system.

## Operational ownership still required

Before any hosted or continuously running use, the portfolio must designate:

- service and repository owner;
- on-call and incident authority;
- capability issuer and revoker;
- secret and credential custodian;
- evidence-retention and privacy owner;
- release approver;
- emergency-stop operator;
- rollback approver; and
- communication and disclosure owner.

Those roles are intentionally not assigned by this repository documentation.