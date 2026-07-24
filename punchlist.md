# Release and integration punch list

This punch list turns the repository task chain, release gates, and obstruction analysis into reviewable work. Checked boxes require repository evidence; documentation alone must not mark runtime, authority, security, compatibility, accessibility certification, publication, or release work complete.

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
- [ ] Accept, revise, or supersede ADR 0003.
- [ ] Accept, revise, or supersede ADR 0004.
- [ ] Select one durable role: canonical kernel, conformance implementation, migration source, or independent research prototype.
- [ ] Select an exact semantic, explicit projection, unsupported-route, or migration-source crosswalk disposition for every claimed runtime profile.
- [ ] Name the canonical repository and package identity.
- [ ] Name the neutral contract, namespace, registry, fixture, and compatibility owner.
- [ ] Name the canonical operational runtime for each supported profile.
- [ ] Record the relationship to `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC`.
- [ ] Define deprecation, migration, archive, and provenance treatment for the unselected paths.
- [ ] Assign compatibility-claim, release, support, incident, emergency-stop, rollback, withdrawal, and recovery owners.

## P1 — Complete the documentation foundation

- [x] Publish a polished repository overview and explicit non-capabilities.
- [x] Add Pages-ready architecture, ontology, terminology, lifecycle, API, onboarding, operations, security, threat-model, governance, and ADR documentation.
- [x] Add A.L.I.S.T.A.I.R.E. portfolio-boundary guidance.
- [x] Add a runtime conformance boundary profile.
- [x] Add a kernel-to-runtime crosswalk options guide and machine-readable profile.
- [x] Add ADR 0003 recording the candidate reference-conformance role.
- [x] Add ADR 0004 recording the crosswalk options and unsupported safe default.
- [x] Add an obstruction and gluing analysis.
- [x] Add an accessibility review and exact-head evidence protocol.
- [x] Add a machine-readable accessibility review profile with explicit authority denials.
- [x] Add this coordinated punch list.
- [x] Align `README.md`, `taskchain.md`, `release.md`, `changelog.md`, and MkDocs navigation.
- [x] Implement exact-head strict documentation validation and retained evidence.
- [x] Add structural checks for heading order, table headers, diagram–prose markers, JSON integrity, and meaningful link text.
- [ ] Confirm a new passing documentation run for the final immutable head after all conformance, coordination, and accessibility updates.
- [ ] Record the rendered-site artifact, digest, manifest, tooling, and source identity for that head.
- [ ] Perform keyboard, focus, heading, table, screen-reader, zoom/reflow, contrast, and cognitive-access review on the exact rendered artifact.
- [ ] Record reviewer or vacancy, environment, findings, untested conditions, residual risk, correction, and supersession state.
- [ ] Record Pages publication authority, deployment source, provenance, withdrawal, rollback, and restored-state verification if publication is enabled.

## P1A — Freeze contract vocabulary

- [ ] Name owners for QSO, QSI, QSIO, transition, witness, reason-code, lifecycle, replay, mapping, and compatibility contracts.
- [ ] Publish machine-readable schema fixtures with canonical or explicitly mapped byte and digest vectors.
- [x] Document the crosswalk disposition vocabulary: `EXACT`, `TRANSFORM`, `PROJECT`, `UNSUPPORTED`, `UNKNOWN`, and `LOSSY_REJECTED`.
- [ ] Define required, optional, omitted, null, unknown, partial, rejected, revoked, corrected, and superseded semantics.
- [ ] Define unsupported-version, unsupported-mapping, and downgrade behavior.
- [ ] Define package namespace and registry ownership.
- [ ] Approve `0.x` compatibility, migration, claim-expiry, deprecation, withdrawal, and support policy.
- [ ] Prove fixture equivalence with the selected canonical runtime or explicitly document non-equivalence.

## P1B — Glue QSO-GENOMES to the neutral contract and kernel

- [ ] Define immutable genome identity, version, lineage, digest, and resolution rules.
- [ ] Keep declarative genome validity distinct from operational admission.
- [ ] Define canon and policy projection into neutral fixtures and local validation.
- [ ] Add accepted, malformed, unsupported, revoked, superseded, lineage-conflict, mapping-conflict, and downgrade fixtures.
- [ ] Record who can admit a genome for canonical execution and who can revoke admission.
- [ ] Prove QSO-GENOMES → neutral contract → kernel triple-overlap fixtures.

## P1C — Glue Repositories `0` and `1` to the canonical runtime

- [ ] Preserve `0:proposal` as non-authoritative local staging.
- [ ] Define the versioned Repository `0` proposal envelope admitted into Repository `1` quarantine.
- [ ] Define the Repository `1` execution-admission and capability profile.
- [ ] Bind task, actor, device, workspace, environment, runtime, schema, genome, inputs, limits, expiry, expected pre-state, replay domain, and idempotency.
- [ ] Name issuer, requester, executor, verifier, approver, revoker, incident owner, and recovery owner.
- [ ] Add accepted, rejected, stale, replayed, expired, wrong-device, wrong-workspace, wrong-runtime, expected-head mismatch, unsupported-version, and revoked-capability fixtures.
- [ ] Prove Repository `0` → Repository `1` → canonical runtime triple-overlap fixtures.

## P1D — Glue evidence references to the canonical runtime and conformance kernel

- [ ] Designate source acquisition, temporal interpretation, domain interpretation, and transport owners.
- [ ] Version an evidence-reference profile containing subject, integrity, provenance, transformation, freshness, privacy class, correction, revocation, retention, and license fields.
- [ ] Prohibit silent retrieval or reinterpretation by `qsio-kernel`.
- [ ] Define how the canonical runtime projects admitted evidence into immutable conformance fixtures.
- [ ] Add stale, replayed, wrong-subject, revoked, corrected, private, unlicensed, malformed, unsupported-profile, and lossy-mapping fixtures.
- [ ] Prove Seeker/temporal/Digitalis → canonical runtime → kernel triple-overlap fixtures.

## P1E — Prove kernel-to-runtime conformance

- [x] Document exact semantic, explicit projection, unsupported-route, and migration-source options without selecting one.
- [x] Publish a machine-readable documentation-only options profile with authority denials and fail-closed conditions.
- [x] Establish `UNSUPPORTED` as the safe default when evidence for another route is absent.
- [ ] Select the canonical runtime for the profile under test.
- [ ] Bind `contract_profile_id`, `fixture_set_id`, kernel source, runtime source, configuration, and mapping version.
- [ ] Classify every mapped field as `EXACT`, `TRANSFORM`, `PROJECT`, `UNSUPPORTED`, `UNKNOWN`, or `LOSSY_REJECTED`.
- [ ] Keep conformance runs separate from runtime admissions, capabilities, executions, receipts, and canonical dispositions.
- [ ] Compare expected and observed bytes, digests, outcomes, reasons, lifecycle, replay, correction, and revocation semantics.
- [ ] Add positive, malformed, wrong-subject, wrong-head, stale, replayed, revoked, corrected, superseded, partial, unknown, and mapping-mismatch vectors.
- [ ] Require independent compatibility review, claim expiry, correction, withdrawal, and migration.
- [ ] Prove neutral contract → kernel → canonical runtime triple-overlap fixtures.

## P1F — Glue the canonical runtime to QSO-FABRIC

- [ ] Decide whether Fabric receives full execution records, QSIO projections, checkpoints, contradiction annotations, or experiment events.
- [ ] Prevent Fabric from redefining canonical transition hashes or lifecycle semantics.
- [ ] Define branch, conflict, merge, abandonment, and partial-experiment behavior.
- [ ] Keep experiment aggregation distinct from Repository `1` canonical disposition.
- [ ] Add multi-QSO, branch-conflict, partial, abandoned, revoked, mapping-mismatch, and rollback fixtures.
- [ ] Prove kernel → canonical runtime → Fabric triple-overlap fixtures.

## P1G — Glue review and transport surfaces

- [ ] Define Bridge profile ownership and keep transport distinct from semantic authority.
- [ ] Define QSO-STUDIO/AionUi projection identity and stale-view behavior.
- [ ] Preserve conformance run, runtime admission, execution, receipt, disposition, reason code, `UNKNOWN`, partial, correction, supersession, and revocation status.
- [ ] Represent annotation, recommendation, approval, compatibility claim, and canonical disposition as separate acts.
- [ ] Require authenticated approval or compatibility receipts rather than inferring authority from interface interaction.
- [ ] Add redaction, mapping, stale-view, correction, revocation, inaccessible-view, claim-withdrawal, and rollback fixtures.
- [ ] Prove kernel → Bridge → review-interface triple-overlap fixtures.

## P1H — Complete exact-head documentation accessibility evidence

- [x] Define safe review states from `NOT_REVIEWED` through `WITHDRAWN` and `UNKNOWN`.
- [x] Separate automated checks, manual review, certification, publication, and restoration.
- [x] Require diagram–prose equivalence and table interpretation.
- [x] Define finding severity and new-generation closure requirements.
- [x] Preserve historical review packets rather than silently editing them.
- [ ] Run automated checks against the final exact documentation head.
- [ ] Review the same retained artifact manually.
- [ ] Correct every blocking finding and rebuild from a new immutable source.
- [ ] Assign a human publication approver and rollback owner before Pages publication.
- [ ] Independently verify any restored public site after rollback.

## P2 — Verification hardening

- [ ] Add static typing and enforce declared strictness.
- [ ] Build and inspect wheel and source distributions.
- [ ] Verify installed package contents and console entry point from built artifacts.
- [ ] Add dependency, license, secret, and supply-chain checks.
- [ ] Test every public exception path and rejected outcome.
- [ ] Define whether lifecycle validation failures are records, exceptions, or profile-dependent.
- [ ] Add property-based or generated malformed-record tests with bounded resources.
- [ ] Map every documented invariant to a named test and release gate.
- [ ] Retain exact-head runtime and conformance evidence with commands, environment, artifacts, and hashes.

## P2A — Authorization and witness semantics

- [ ] Keep `PermissionSet` explicitly non-authoritative until an adapter profile is approved.
- [ ] Define independent capability issuance, expiry, replay prevention, narrowing, and revocation outside the kernel.
- [ ] Define witness classes, verifier identity, signature scope, trust strength, and downgrade rules.
- [ ] Keep local witness metadata distinct from independent conformance review and attestation.
- [ ] Add forged, missing, unverified, wrong-signer, expired, revoked, and unsupported-witness fixtures.
- [ ] Ensure a successful local QSIO or conformance run cannot authorize external execution, merge, release, payment, or deployment.

## P2B — Clock, reason-code, and correction semantics

- [ ] Assign logical-clock and temporal-profile ownership.
- [ ] Define clock domains, causal ordering, wall-time provenance, expiry, and skew rules.
- [ ] Publish a shared outcome and reason-code mapping that preserves unknown and partial states.
- [ ] Define append-only correction, supersession, revocation, claim withdrawal, and cache invalidation.
- [ ] Distinguish historical semantic replay from current authorized-state reconstruction.
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
- [ ] Expire incompatible compatibility claims after contract or mapping incidents.
- [ ] Prove Quietus → revocation → recovery triple-overlap fixtures.

## P4 — Security, privacy, and operations

- [ ] Assign security contact, privacy owner, incident commander, emergency-stop owner, recovery owner, compatibility reviewer, claim-withdrawal owner, publication approver, accessibility reviewer, and rollback owner.
- [ ] Classify QSO state, evidence references, genome fields, witnesses, fixtures, mappings, logs, artifacts, and accessibility review records.
- [ ] Define prohibited sensitive fields and reference-only handling.
- [ ] Review canonical hashes and fixture vectors for disclosure and correlation risk.
- [ ] Define log, artifact, fixture, mapping, accessibility packet, and Pages retention.
- [ ] Perform hostile-input, denial-of-service, replay, confusion, downgrade, mapping, and resource-limit testing.
- [ ] Perform a tabletop incident, freeze, evidence-preservation, claim-withdrawal, rollback, bounded-restart, and site-restoration exercise.
- [ ] Record residual risks and unsupported platform assumptions.

## P5 — Release and publication

- [ ] Select the release class: experimental source, conformance fixture package, documentation publication, or another approved class.
- [ ] Record immutable source, canonical runtime, contract, mapping, package, schema, fixture, dependency, test, documentation, and accessibility-review identities.
- [ ] Record exact build and verification commands.
- [ ] Identify previous known-good package, compatibility claim, fixture set, and documentation artifacts.
- [ ] Exercise withdrawal and restoration procedures.
- [ ] Approve public privacy, licensing, accessibility, support, and vulnerability-reporting routes.
- [ ] Finalize changelog, migration notes, compatibility statement, limitations, and claim-expiry rules.
- [ ] Obtain explicit release, compatibility-claim, and publication approval.

## Explicitly not authorized

Until the applicable gates are approved and evidenced, this punch list does not authorize:

- network, filesystem, subprocess, browser, external-model, payment, or device-control adapters;
- durable or distributed runtime services;
- autonomous QSO spawning or self-modification;
- credential, signing-key, or capability issuance;
- repository mutation, merge, release, publication, deployment, or infrastructure changes;
- canonical-state or canonical-runtime ownership;
- accessibility certification, legal-compliance conclusions, or unreviewed publication claims;
- unreviewed compatibility or conformance claims; or
- production-readiness claims.
