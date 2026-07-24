# Release plan

## Current release posture

The repository contains a functional `0.1.0` experimental kernel, but no new release is approved by this document. The present documentation work is release-neutral: it clarifies behavior, portfolio fit, the candidate reference-conformance role, crosswalk options, gluing obstructions, operational limits, accessibility-review evidence, and release requirements without changing runtime scope.

The accessibility protocol status is `ACCESSIBILITY_REVIEW_PROTOCOL_DOCUMENTED_SITE_NOT_CERTIFIED`. It defines exact-generation review evidence but does not certify the current candidate, determine legal compliance, authorize Pages publication, or complete any release gate that requires human review.

## Release classes

### Experimental source release

A source release may expose the current local reference kernel when every applicable gate below is satisfied and its limitations remain prominent.

### Conformance-fixture release

If the portfolio selects `qsio-kernel` as a reference-conformance implementation, a release may contain machine-readable fixtures, expected canonical or explicitly mapped bytes, digests, accepted/rejected outcomes, lifecycle mappings, replay expectations, correction and revocation vectors, and compatibility evidence. This class requires an accepted neutral contract, an explicitly named canonical runtime, approved field-level dispositions, reproduced triple-overlap witnesses, and an independent compatibility decision.

### Documentation publication

A GitHub Pages publication may expose rendered documentation after exact-head build evidence, generated-site review, publication authority, manual accessibility review, privacy and licensing review, public-artifact retention, withdrawal, rollback ownership, and independently verified restoration are recorded. The documentation workflow builds an artifact; it does not deploy Pages.

### Production or hosted-service release

Not authorized. The current architecture lacks durable storage, independent attestation, complete authorization enforcement, network isolation, operational monitoring, service ownership, incident response, approved privacy and retention policy, and a production trust model.

## Required gates

### Scope and governance

- [x] Repository purpose and non-goals documented.
- [x] Task chain distinguishes implemented, proposed, blocked, and unauthorized work.
- [x] Release and integration punch list exists.
- [x] A.L.I.S.T.A.I.R.E. integration boundary documented.
- [x] Portfolio obstruction and gluing analysis exists.
- [x] Proposed portfolio-role ADR exists.
- [x] Runtime conformance boundary profile and ADR 0003 candidate exist.
- [x] Kernel-to-runtime crosswalk options, machine-readable profile, and ADR 0004 candidate exist.
- [x] Accessibility review protocol and machine-readable exact-generation profile exist.
- [x] MIT license present.
- [ ] Durable role relative to `QuantumStateObjects`, QSO-GENOMES, and QSO-FABRIC approved.
- [ ] Canonical repository and package identity approved.
- [ ] Neutral schema, format, hashing, namespace, registry, fixture, mapping, and compatibility owners approved.
- [ ] Canonical operational runtime named for each profile.
- [ ] Exact semantic, explicit projection, unsupported-route, or migration-source disposition approved for each claimed profile.
- [ ] Release owner and explicit approval record identified.
- [ ] Compatibility-claim issuer, reviewer, expiry, correction, withdrawal, and support owners identified.
- [ ] Migration, deprecation, archive, provenance, and withdrawal policies approved.
- [ ] Incident, emergency-stop, recovery, rollback, publication, accessibility-review, and release-withdrawal authorities designated.

### Cross-repository gluing

- [ ] QSO-GENOMES → neutral contract → kernel profile approved.
- [ ] Neutral contract → kernel → canonical runtime conformance profile approved.
- [ ] Repository `0` → Repository `1` → canonical runtime proposal/admission/capability profile approved.
- [ ] Evidence pipeline → canonical runtime → kernel reference profile approved.
- [ ] Kernel → canonical runtime → QSO-FABRIC experiment-evidence profile approved.
- [ ] Runtime/conformance evidence → Repository `1` reconciliation profile approved.
- [ ] Kernel/runtime evidence → Bridge → QSO-STUDIO/AionUi review profile approved.
- [ ] Quietus → revocation → recovery profile approved before operational reliance.
- [ ] All required pairwise positive and negative fixtures pass at immutable source identities.
- [ ] All required triple-overlap witnesses pass; pairwise adapters alone do not satisfy this gate.

### Crosswalk and compatibility

- [x] Crosswalk options and safe unsupported default are documented.
- [x] Machine-readable options profile denies adapter, runtime, capability, release, publication, deployment, and canonical-state authority.
- [ ] Every field and semantic class is dispositioned as `EXACT`, `TRANSFORM`, `PROJECT`, `UNSUPPORTED`, `UNKNOWN`, or `LOSSY_REJECTED`.
- [ ] Machine-readable schemas exist for every public record.
- [ ] Canonical or explicitly mapped byte encoding, field omission, domain separation, and digest vectors are approved.
- [ ] Contract, fixture, mapping, kernel, runtime, admission, capability, execution, receipt, disposition, correction, revocation, and checkpoint identities remain distinct.
- [ ] Unsupported-version, unsupported-mapping, ambiguity, and downgrade behavior fail closed.
- [ ] Accepted, rejected, unknown, partial, revoked, corrected, superseded, withdrawn, and privacy-restricted semantics are preserved.
- [ ] Outcome and reason-code mappings are versioned.
- [ ] Lifecycle crosswalk covers active, Quietus, frozen, revoked, quarantined, retired, and recovering states.
- [ ] Logical-time, observation-time, expiry, freshness, replay-domain, and skew semantics are assigned.
- [ ] `0.x` compatibility and migration statement is approved.
- [ ] If this is a conformance release, equivalence or explicit projection with the canonical runtime is independently reproduced.
- [ ] Compatibility claims carry scope, exact sources, profile, fixture set, expiry, correction, withdrawal, and support metadata.

### Build and packaging

- [x] `pyproject.toml` declares package metadata and Python requirement.
- [x] Editable local installation path documented.
- [ ] Clean build from a fresh environment recorded.
- [ ] Wheel and source distribution built and inspected.
- [ ] Package installation from built artifacts verified.
- [ ] Exported package contents and console entry point verified.
- [ ] Built artifacts match the reviewed source and carry recorded SHA-256 values.
- [ ] Any conformance-fixture package is separate from operational capability or credential material.

### Verification

- [x] Core pytest suite exists.
- [x] Demo exercises genesis, interactions, verification, replay, and Quietus.
- [ ] Full test output captured for the release commit.
- [ ] Canonical record, mapping, and hash fixtures recorded.
- [ ] Malformed-input, unsupported-profile, unsupported-mapping, ambiguity, and corruption tests completed.
- [ ] Parent-link, intermediate replay, stale-precondition, and branch-divergence tests completed.
- [ ] Supported-environment replay comparison completed.
- [ ] Canonical-runtime comparison completed against exact source and configuration.
- [ ] Exact, transformed, projected, unsupported, unknown, and lossy-rejected routes are tested.
- [ ] Static type check completed with declared strict settings.
- [ ] Bounded hostile-input and resource-limit tests completed.
- [ ] Every documented invariant maps to a named test and release gate.

### Authorization and attestation

- [x] Documentation states that `PermissionSet` is not comprehensive capability enforcement.
- [x] Documentation states that current witnesses are not independent attestations.
- [x] Documentation states that a passing conformance vector is not runtime admission, capability, execution, receipt, or canonical disposition.
- [x] Documentation states that projection and transport cannot strengthen authority.
- [ ] Capability issuer, requester, executor, verifier, approver, revoker, and incident owner are assigned outside the conformance kernel.
- [ ] Capability scope, expiry, narrowing, replay prevention, expected pre-state, and revocation are tested by the canonical runtime path.
- [ ] Witness classes, signer/verifier identity, signature scope, trust strength, and downgrade rules are approved.
- [ ] Independent compatibility reviewer and compatibility-claim receipt semantics are approved.
- [ ] A successful local QSIO, projection, or conformance run is proven unable to authorize external execution, merge, release, payment, publication, or deployment.

### Security, privacy, and retention

- [x] Current trust boundaries and limitations documented.
- [x] Local operations and failure response documented.
- [x] External I/O, network, subprocess, and spawn requests are forbidden in the semantic validation path.
- [ ] Dependency, license, and supply-chain review recorded.
- [ ] Secret scan recorded for release source and artifacts.
- [ ] Adversarial, mapping-confusion, projection-confusion, and authority-confusion evidence recorded.
- [ ] Data classification covers QSO state, evidence references, genome fields, witnesses, mappings, fixtures, logs, compatibility claims, accessibility packets, and artifacts.
- [ ] Prohibited sensitive fields and reference-only handling are defined.
- [ ] Canonical-hash and fixture-vector disclosure and correlation risks are reviewed.
- [ ] Privacy, retention, correction, redaction, deletion, cache invalidation, claim withdrawal, accessibility finding retention, and public-artifact policy are approved.
- [ ] Security contact and vulnerability-reporting route approved.

### Lifecycle, emergency stop, and recovery

- [x] Quietus and explicit local resume are documented.
- [x] Crosswalk documentation states that Quietus is not automatically freeze, revocation, quarantine, retirement, emergency stop, or recovery authority.
- [ ] Quietus is mapped distinctly from external freeze, capability revocation, quarantine, compatibility-claim withdrawal, and emergency stop.
- [ ] Queued and in-flight work behavior after stop is defined.
- [ ] Evidence and volatile-state preservation are defined.
- [ ] Automatic unlock is prohibited.
- [ ] Approved checkpoint identity and least-authority restart order are defined.
- [ ] Old capabilities and incompatible compatibility claims remain invalid after recovery.
- [ ] Quietus → revocation → recovery triple-overlap fixtures pass.
- [ ] A tabletop incident, freeze, claim-withdrawal, rollback, and bounded-restart exercise is recorded.

### Documentation and accessibility

- [x] Project overview, architecture, design, API, onboarding, operations, security, governance, integration, conformance, crosswalk, obstruction, accessibility-review, and ADR guides exist in the candidate.
- [x] Pages-ready navigation exists.
- [x] Exact-head strict documentation workflow is implemented.
- [x] Accessibility review states, exact-generation evidence fields, finding severity, correction, withdrawal, and rollback rules are documented.
- [x] Machine-readable accessibility profile denies certification, legal-compliance, publication, deployment, runtime, credential, and portfolio authority.
- [ ] The final documentation candidate passes source-identity assertion, crosswalk and accessibility-profile validation, local-link validation, structural accessibility checks, and strict MkDocs build after all current changes.
- [ ] The rendered-site artifact and SHA-256 manifest are retained for the final immutable head.
- [ ] Internal-link validation and generated-site boundary checks pass for the final head.
- [ ] Mermaid source diagrams are manually reviewed for correctness and fallback readability.
- [ ] Keyboard, focus, contrast, heading, table, screen-reader, 200%/400% zoom, reflow, and cognitive-access review is recorded against the exact retained artifact.
- [ ] Reviewer or vacancy, browser/OS, assistive technology, untested conditions, open findings, and residual risk are recorded.
- [ ] Blocking findings are corrected in a new immutable generation and the affected checks are repeated.
- [ ] Published Pages URL, deployment source, deployment provenance, withdrawal, rollback, and independently verified restoration are recorded if Pages is enabled.

Every source change invalidates prior exact-head documentation and accessibility evidence and requires a new passing run and review.

### Provenance and reproducibility

- [ ] Runtime release commit SHA recorded.
- [ ] Canonical runtime commit and configuration recorded for conformance claims.
- [ ] Runtime build and test environment recorded.
- [ ] Contract, mapping, schema, fixture, package, registry, and canonical-runtime source identities recorded.
- [x] Crosswalk profile records the exact parent generation from which the documentation decision packet was derived.
- [x] Accessibility profile defines exact source, artifact, environment, reviewer, finding, correction, and supersession bindings.
- [x] Documentation workflow records source SHA, workflow run, Python version, MkDocs version, and generation time.
- [x] Documentation artifact contains dependency, source-identity, site-file, and evidence SHA-256 manifests.
- [x] Documentation build commands are encoded in the reviewed workflow.
- [ ] Changelog finalized for the release version.
- [ ] Tag or claim receipt is signed, or signing limitations are explicitly accepted.

### Operations and rollback

For an experimental or conformance source release:

- [x] Local failure triage and recovery guidance documented.
- [x] Crosswalk withdrawal and safe fallback to the unsupported route are documented.
- [ ] Previous known-good tag and fixture set identified.
- [ ] Artifact and compatibility-claim withdrawal procedure exercised or reviewed.
- [ ] Breaking hash, schema, or mapping changes are prohibited or migrated.
- [ ] Correction and revocation do not rewrite accepted public history silently.
- [ ] Release and claim-withdrawal authority assigned.

For documentation publication:

- [x] Accessibility protocol defines finding preservation, correction on a new generation, and non-certification boundaries.
- [ ] Pages publication owner identified.
- [ ] Accessibility reviewer or accepted vacancy identified.
- [ ] Previous known-good site artifact identified.
- [ ] Site withdrawal and restoration procedure reviewed.
- [ ] Public artifact and accessibility-packet retention and privacy policy approved.
- [ ] Restored public state independently verified.

For any future hosted runtime, deployment, health-check, backup, incident-response, credential-revocation, emergency-stop, and rollback gates are mandatory and require separate architecture approval.

## Release decision

**Blocked** until every gate applicable to the intended release class has evidence. Existing code, a passing demo, a passing conformance vector, a successful local transition, a successful documentation build, or automated accessibility checks must not be described as production-ready, canonically authoritative, accessibility-certified, legally compliant, or publication-approved.

The unresolved portfolio role and crosswalk route are release significant. No release should imply that `qsio-kernel` is A.L.I.S.T.A.I.R.E.'s authoritative runtime until ownership is explicitly approved. If another runtime is canonical, no conformance claim should be made until neutral contracts, field dispositions, mappings, and shared fixtures reproduce under independent review. Until then, the route remains unsupported.

## Rollback criteria

Withdraw or supersede a release or compatibility claim when any of the following is discovered:

- canonical serialization, mapping, or hash instability;
- replay divergence for a supported record sequence;
- accepted transition with an invalid precondition;
- broken parent linkage or undeclared branch behavior;
- Quietus bypass or failed revocation propagation;
- forbidden external-capability request accepted by the semantic path;
- capability, witness, interface, projection, or conformance data interpreted as stronger authority than supported;
- wrong-subject, stale, replayed, revoked, corrected, private, or incompatible evidence accepted;
- canonical runtime and reference kernel disagree for a claimed profile;
- a missing, unsupported, ambiguous, or lossy mapping is treated as equivalent;
- packaging that installs different code than the reviewed commit;
- documentation artifact built from a source other than the submitted immutable head;
- inaccessible navigation, keyboard trap, missing critical prose equivalent, unusable critical table, hidden warning, or other blocking documentation-accessibility defect;
- an accessibility result is represented as current after its exact source or artifact changed;
- undocumented capability, schema, mapping, or authority expansion;
- sensitive information in source, tests, fixtures, artifacts, hashes, or Pages;
- misleading canonical-runtime, conformance, security, accessibility, legal-compliance, or production claims; or
- material license, provenance, compatibility, migration, support, or withdrawal defect.

Rollback means marking the affected release, compatibility claim, site, or accessibility result as withdrawn, preserving incident evidence, returning source and documentation to the last verified behavior or explicit unsupported route, revoking affected capabilities, invalidating incompatible caches and fixtures, and issuing a corrected version rather than rewriting an existing public tag or receipt.

A documentation rollback must not restore stale architecture claims, withdrawn compatibility claims, revoked authority, sensitive content, or a generation containing the same unresolved accessibility defect.

## Evidence template

```text
Release class:
Version or publication label:
Repository and source commit:
Canonical role decision:
Crosswalk option and profile version:
Canonical runtime and commit:
Neutral contract/package/registry owner:
Contract profile and fixture set:
Schema, field dispositions, mapping, and digest-vector identities:
Unsupported, unknown, projected, and lossy-rejected routes:
Approver:
Compatibility reviewer and claim receipt:
Capability and revocation owners:
Python environments:
Build commands:
Test, replay, mapping, and type-check results:
Pairwise gluing fixtures:
Triple-overlap witnesses:
Documentation workflow run:
Documentation artifact and digest:
Accessibility review state:
Accessibility reviewer or vacancy:
Browser, operating system, viewport, zoom, and assistive technology:
Keyboard, heading, table, diagram, contrast, reflow, and screen-reader results:
Accessibility findings, untested conditions, and residual risk:
Accessibility correction, supersession, or withdrawal record:
Security, privacy, licensing, and retention checks:
Artifacts and SHA-256 values:
Known limitations:
Claim expiry, correction, and withdrawal policy:
Previous known-good release, fixture set, claim, or site:
Rollback trigger and procedure:
Independent restored-state verification:
Incident, emergency-stop, recovery, support, publication, accessibility-review, and withdrawal authorities:
```
