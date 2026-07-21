# Release and integration punch list

This punch list turns the repository task chain, release gates, and obstruction analysis into reviewable work. Checked boxes require repository evidence; documentation alone must not mark runtime, authority, security, or release work complete.

## P0 — Preserve the current reference baseline

- [x] Keep the Python `0.1.0` runtime local and in memory.
- [x] Preserve explicit QSI request, accepted/rejected QSIO outcome, state-hash, parent-link, witness-metadata, and replay concepts.
- [x] Preserve Quietus and explicit resume behavior.
- [x] Keep network, subprocess, filesystem, model, payment, repository, and deployment operations outside the semantic execution path.
- [ ] Record a fresh clean-environment test run against the intended release commit.
- [ ] Record canonical hash fixtures for every public record type.
- [ ] Add intermediate replay, malformed-input, corrupted-hash, parent-divergence, and stale-precondition fixtures.
- [ ] Verify deterministic fixtures across every supported Python environment.

## P0A — Decide the portfolio role

- [ ] Accept, revise, or supersede ADR 0002.
- [ ] Select one durable role: canonical kernel, conformance implementation, migration source, or independent research prototype.
- [ ] Name the canonical repository and package identity.
- [ ] Record the relationship to `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC`.
- [ ] Define deprecation, migration, archive, and provenance treatment for the unselected paths.
- [ ] Assign release, compatibility, incident, emergency-stop, rollback, and withdrawal owners.

## P1 — Complete the documentation foundation

- [x] Publish a polished repository overview and explicit non-capabilities.
- [x] Add Pages-ready architecture, ontology, terminology, lifecycle, API, onboarding, operations, security, threat-model, governance, and ADR documentation.
- [x] Add A.L.I.S.T.A.I.R.E. portfolio-boundary guidance.
- [x] Add an obstruction and gluing analysis.
- [x] Add this coordinated punch list.
- [x] Align `README.md`, `taskchain.md`, `release.md`, `changelog.md`, and MkDocs navigation.
- [x] Implement exact-head strict documentation validation and retained evidence.
- [ ] Confirm a new passing documentation run for the final immutable head after all coordination updates.
- [ ] Review diagrams for semantic accuracy and readable fallback text.
- [ ] Record keyboard, heading, contrast, table, and screen-reader review.
- [ ] Record Pages publication authority, deployment source, provenance, and rollback if publication is enabled.

## P1A — Freeze contract vocabulary

- [ ] Name owners for QSO, QSI, QSIO, transition, witness, reason-code, lifecycle, and replay contracts.
- [ ] Publish machine-readable schema fixtures with canonical byte and digest vectors.
- [ ] Define required, optional, omitted, null, unknown, partial, rejected, revoked, corrected, and superseded semantics.
- [ ] Define unsupported-version and downgrade behavior.
- [ ] Define package namespace and registry ownership.
- [ ] Approve `0.x` compatibility, migration, and deprecation policy.
- [ ] Prove fixture equivalence with the selected canonical runtime or explicitly document non-equivalence.

## P1B — Glue QSO-GENOMES to the kernel

- [ ] Define immutable genome identity, version, lineage, digest, and resolution rules.
- [ ] Keep declarative genome validity distinct from operational admission.
- [ ] Define canon and policy projection into local validation.
- [ ] Add accepted, malformed, unsupported, revoked, superseded, lineage-conflict, and downgrade fixtures.
- [ ] Record who can admit a genome for execution and who can revoke admission.
- [ ] Prove Genome → kernel → Fabric triple-overlap fixtures.

## P1C — Glue Repositories `0` and `1` to the kernel

- [ ] Preserve `0:proposal` as non-authoritative local staging.
- [ ] Define the versioned Repository `0` proposal envelope admitted into Repository `1` quarantine.
- [ ] Define the Repository `1` execution-admission and capability profile.
- [ ] Bind task, actor, environment, runtime, schema, genome, inputs, limits, expiry, expected pre-state, replay domain, and idempotency.
- [ ] Name issuer, requester, executor, verifier, approver, revoker, incident owner, and recovery owner.
- [ ] Add accepted, rejected, stale, replayed, expired, wrong-environment, wrong-runtime, expected-head mismatch, unsupported-version, and revoked-capability fixtures.
- [ ] Prove Repository `0` → Repository `1` → kernel triple-overlap fixtures.

## P1D — Glue evidence references to the kernel

- [ ] Designate source acquisition, temporal interpretation, domain interpretation, and transport owners.
- [ ] Version an evidence-reference profile containing subject, integrity, provenance, transformation, freshness, privacy class, correction, revocation, retention, and license fields.
- [ ] Prohibit silent retrieval or reinterpretation by the kernel.
- [ ] Add stale, replayed, wrong-subject, revoked, corrected, private, unlicensed, malformed, and unsupported-profile fixtures.
- [ ] Prove Seeker → temporal interpretation → kernel triple-overlap fixtures.

## P1E — Glue the kernel to QSO-FABRIC

- [ ] Decide whether Fabric receives full QSIO records, projections, checkpoints, contradiction annotations, or experiment events.
- [ ] Prevent Fabric from redefining canonical transition hashes or lifecycle semantics.
- [ ] Define branch, conflict, merge, abandonment, and partial-experiment behavior.
- [ ] Keep experiment aggregation distinct from Repository `1` canonical disposition.
- [ ] Add multi-QSO, branch-conflict, partial, abandoned, revoked, and rollback fixtures.
- [ ] Prove kernel → Fabric → Repository `1` triple-overlap fixtures.

## P1F — Glue review and transport surfaces

- [ ] Define Bridge profile ownership and keep transport distinct from semantic authority.
- [ ] Define QSO-STUDIO/AionUi projection identity and stale-view behavior.
- [ ] Preserve proposed versus accepted transitions, reason codes, `UNKNOWN`, partial, correction, supersession, and revocation status.
- [ ] Represent annotation, recommendation, approval, and canonical disposition as separate acts.
- [ ] Require authenticated approval receipts rather than inferring authority from interface interaction.
- [ ] Add redaction, mapping, stale-view, correction, revocation, inaccessible-view, and rollback fixtures.
- [ ] Prove kernel → Bridge → review-interface triple-overlap fixtures.

## P2 — Verification hardening

- [ ] Add static typing and enforce declared strictness.
- [ ] Build and inspect wheel and source distributions.
- [ ] Verify installed package contents and console entry point from built artifacts.
- [ ] Add dependency, license, secret, and supply-chain checks.
- [ ] Test every public exception path and rejected outcome.
- [ ] Define whether lifecycle validation failures are records, exceptions, or profile-dependent.
- [ ] Add property-based or generated malformed-record tests with bounded resources.
- [ ] Map every documented invariant to a named test and release gate.
- [ ] Retain exact-head runtime evidence with commands, environment, artifacts, and hashes.

## P2A — Authorization and witness semantics

- [ ] Keep `PermissionSet` explicitly non-authoritative until an adapter profile is approved.
- [ ] Define independent capability issuance, expiry, replay prevention, narrowing, and revocation.
- [ ] Define witness classes, verifier identity, signature scope, trust strength, and downgrade rules.
- [ ] Add forged, missing, unverified, wrong-signer, expired, revoked, and unsupported-witness fixtures.
- [ ] Ensure a successful local QSIO cannot authorize external execution, merge, release, payment, or deployment.

## P2B — Clock, reason-code, and correction semantics

- [ ] Assign logical-clock and temporal-profile ownership.
- [ ] Define clock domains, causal ordering, wall-time provenance, expiry, and skew rules.
- [ ] Publish a shared outcome and reason-code mapping that preserves unknown and partial states.
- [ ] Define append-only correction, supersession, revocation, and cache invalidation.
- [ ] Distinguish historical execution replay from current authorized-state reconstruction.
- [ ] Prove Correction → canonical disposition → replay triple-overlap fixtures.

## P3 — Persistence and recovery design

- [ ] Select append-only, event-sourced, snapshot, or layered storage semantics.
- [ ] Define atomic state-and-ledger commit behavior.
- [ ] Define idempotency, retry, crash recovery, partial failure, and explicit `UNKNOWN` outcomes.
- [ ] Define authoritative roots, checkpoint identity, corruption detection, and migration.
- [ ] Define schema evolution and unsupported-record handling.
- [ ] Define privacy, retention, deletion, redaction, compaction, and hash-disclosure policy.
- [ ] Add restart, interrupted-write, corrupted-store, stale-checkpoint, rollback, and migration fixtures.
- [ ] Keep persistence local unless network architecture is separately approved.

## P3A — Quietus, freeze, revocation, and recovery

- [ ] Publish a lifecycle crosswalk for active, Quietus, frozen, revoked, quarantined, retired, and recovering states.
- [ ] Define queued and in-flight work behavior after stop or revocation.
- [ ] Ensure stop authority does not depend on the component being stopped.
- [ ] Preserve evidence and volatile-state capture during incident handling.
- [ ] Prohibit automatic unlock.
- [ ] Require approved checkpoint identity and least-authority restart order.
- [ ] Prove Quietus → revocation → recovery triple-overlap fixtures.

## P4 — Security, privacy, and operations

- [ ] Assign security contact, privacy owner, incident commander, emergency-stop owner, and recovery owner.
- [ ] Classify QSO state, evidence references, genome fields, witnesses, logs, and artifacts.
- [ ] Define prohibited sensitive fields and reference-only handling.
- [ ] Review canonical hashes for disclosure and correlation risk.
- [ ] Define log, artifact, fixture, and Pages retention.
- [ ] Perform hostile-input, denial-of-service, replay, confusion, downgrade, and resource-limit testing.
- [ ] Perform a tabletop incident, freeze, evidence-preservation, rollback, and bounded-restart exercise.
- [ ] Record residual risks and unsupported platform assumptions.

## P5 — Release and publication

- [ ] Select the release class: experimental source, conformance fixture package, documentation publication, or another approved class.
- [ ] Record immutable source, package, schema, fixture, dependency, test, and documentation identities.
- [ ] Record exact build and verification commands.
- [ ] Identify previous known-good package and documentation artifacts.
- [ ] Exercise withdrawal and restoration procedures.
- [ ] Approve public privacy, licensing, support, and vulnerability-reporting routes.
- [ ] Finalize changelog, migration notes, compatibility statement, and limitations.
- [ ] Obtain explicit release and publication approval.

## Explicitly not authorized

Until the applicable gates are approved and evidenced, this punch list does not authorize:

- network, filesystem, subprocess, browser, external-model, payment, or device-control adapters;
- durable or distributed runtime services;
- autonomous QSO spawning or self-modification;
- credential, signing-key, or capability issuance;
- repository mutation, merge, release, publication, deployment, or infrastructure changes;
- canonical-state ownership; or
- production-readiness claims.
