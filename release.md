# Release plan

## Current release posture

The repository contains a functional `0.1.0` experimental kernel, but no new release is approved by this document. The present documentation work is release-neutral: it clarifies behavior, portfolio fit, gluing obstructions, operational limits, and evidence requirements without changing runtime scope.

## Release classes

### Experimental source release

A source release may expose the current local reference kernel when every applicable gate below is satisfied and its limitations remain prominent.

### Conformance-fixture release

If the portfolio selects `qsio-kernel` as a reference conformance implementation, a release may contain machine-readable fixtures, expected canonical bytes or declared mapping bytes, digests, accepted/rejected outcomes, lifecycle mappings, and replay expectations. This class requires an accepted canonical upstream contract.

### Documentation publication

A GitHub Pages publication may expose rendered documentation after exact-head build evidence, generated-site review, publication authority, accessibility review, privacy review, and rollback ownership are recorded. The documentation workflow builds an artifact; it does not deploy Pages.

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
- [x] MIT license present.
- [ ] Durable role relative to `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC` approved.
- [ ] Canonical repository, package, schema, format, hashing, and registry owners approved.
- [ ] Release owner and explicit approval record identified.
- [ ] Compatibility, migration, deprecation, archive, and withdrawal policies approved.
- [ ] Incident, emergency-stop, recovery, rollback, and withdrawal authorities designated.

### Cross-repository gluing

- [ ] QSO-GENOMES → kernel genome-consumption profile approved.
- [ ] Repository `0` → Repository `1` proposal-admission profile approved.
- [ ] Repository `1` → kernel execution-admission and capability profile approved.
- [ ] Evidence pipeline → kernel reference profile approved.
- [ ] Kernel → QSO-FABRIC experiment-evidence profile approved.
- [ ] Kernel → Repository `1` result and canonical-disposition profile approved.
- [ ] Kernel → Bridge → QSO-STUDIO/AionUi review profile approved.
- [ ] Kernel → persistence and recovery profile approved before durable storage work.
- [ ] All required pairwise positive and negative fixtures pass at immutable source identities.
- [ ] All required triple-overlap witnesses pass; pairwise adapters alone do not satisfy this gate.

### Contract and compatibility

- [ ] Machine-readable schemas exist for every public record.
- [ ] Canonical byte encoding, field omission, domain separation, and digest vectors are approved.
- [ ] Unsupported-version and downgrade behavior is fail closed.
- [ ] Accepted, rejected, unknown, partial, revoked, corrected, and superseded semantics are preserved.
- [ ] Outcome and reason-code mappings are versioned.
- [ ] Lifecycle crosswalk covers active, Quietus, frozen, revoked, quarantined, retired, and recovering states.
- [ ] Logical-time, observation-time, expiry, freshness, replay-domain, and skew semantics are assigned.
- [ ] `0.x` compatibility and migration statement is approved.
- [ ] If this is a conformance release, equivalence or explicit mapping with the canonical runtime is reproduced.

### Build and packaging

- [x] `pyproject.toml` declares package metadata and Python requirement.
- [x] Editable local installation path documented.
- [ ] Clean build from a fresh environment recorded.
- [ ] Wheel and source distribution built and inspected.
- [ ] Package installation from built artifacts verified.
- [ ] Exported package contents and console entry point verified.
- [ ] Built artifacts match the reviewed source and carry recorded SHA-256 values.

### Verification

- [x] Core pytest suite exists.
- [x] Demo exercises genesis, interactions, verification, replay, and Quietus.
- [ ] Full test output captured for the release commit.
- [ ] Canonical record and hash fixtures recorded.
- [ ] Malformed-input and corruption tests completed.
- [ ] Parent-link, intermediate replay, stale-precondition, and branch-divergence tests completed.
- [ ] Supported-environment replay comparison completed.
- [ ] Static type check completed with declared strict settings.
- [ ] Bounded hostile-input and resource-limit tests completed.
- [ ] Every documented invariant maps to a named test and release gate.

### Authorization and attestation

- [x] Documentation states that `PermissionSet` is not comprehensive capability enforcement.
- [x] Documentation states that current witnesses are not independent attestations.
- [ ] Capability issuer, requester, executor, verifier, approver, revoker, and incident owner are assigned.
- [ ] Capability scope, expiry, narrowing, replay prevention, expected pre-state, and revocation are tested.
- [ ] Witness classes, signer/verifier identity, signature scope, trust strength, and downgrade rules are approved.
- [ ] A successful local QSIO is proven unable to authorize external execution, merge, release, payment, publication, or deployment.

### Security, privacy, and retention

- [x] Current trust boundaries and limitations documented.
- [x] Local operations and failure response documented.
- [x] External I/O, network, subprocess, and spawn requests are forbidden in the semantic validation path.
- [ ] Dependency, license, and supply-chain review recorded.
- [ ] Secret scan recorded for release source and artifacts.
- [ ] Adversarial and confusion-boundary evidence recorded.
- [ ] Data classification covers QSO state, evidence references, genome fields, witnesses, logs, fixtures, and artifacts.
- [ ] Prohibited sensitive fields and reference-only handling are defined.
- [ ] Canonical-hash disclosure and correlation risks are reviewed.
- [ ] Privacy, retention, correction, redaction, deletion, cache invalidation, and public-artifact policy are approved.
- [ ] Security contact and vulnerability-reporting route approved.

### Lifecycle, emergency stop, and recovery

- [x] Quietus and explicit local resume are documented.
- [ ] Quietus is mapped distinctly from external freeze, capability revocation, quarantine, and emergency stop.
- [ ] Queued and in-flight work behavior after stop is defined.
- [ ] Evidence and volatile-state preservation are defined.
- [ ] Automatic unlock is prohibited.
- [ ] Approved checkpoint identity and least-authority restart order are defined.
- [ ] Old capabilities remain invalid after recovery.
- [ ] Quietus → revocation → recovery triple-overlap fixtures pass.
- [ ] A tabletop incident, freeze, rollback, and bounded-restart exercise is recorded.

### Documentation and accessibility

- [x] Project overview, architecture, design, API, onboarding, operations, security, governance, integration, obstruction, and ADR guides exist in the candidate.
- [x] Pages-ready navigation exists.
- [x] Exact-head strict documentation workflow is implemented.
- [ ] The final documentation candidate passes source-identity assertion and strict MkDocs build after all current changes.
- [ ] The rendered-site artifact and SHA-256 manifest are retained for the final immutable head.
- [ ] Internal-link validation and generated-site boundary checks pass for the final head.
- [ ] Mermaid source diagrams are reviewed for correctness and fallback readability.
- [ ] Keyboard, contrast, heading, table, and screen-reader review recorded.
- [ ] Published Pages URL, deployment source, deployment provenance, and rollback recorded if Pages is enabled.

Every source change invalidates prior exact-head documentation evidence and requires a new passing run.

### Provenance and reproducibility

- [ ] Runtime release commit SHA recorded.
- [ ] Runtime build and test environment recorded.
- [ ] Contract, schema, fixture, package, and canonical-runtime source identities recorded.
- [x] Documentation workflow records source SHA, workflow run, Python version, MkDocs version, and generation time.
- [x] Documentation artifact contains dependency, source-identity, site-file, and evidence SHA-256 manifests.
- [x] Documentation build commands are encoded in the reviewed workflow.
- [ ] Changelog finalized for the release version.
- [ ] Tag is signed or release-signing limitation is explicitly accepted.

### Operations and rollback

For an experimental or conformance source release:

- [x] Local failure triage and recovery guidance documented.
- [ ] Previous known-good tag identified.
- [ ] Artifact withdrawal procedure exercised or reviewed.
- [ ] Breaking hash/schema changes are prohibited or migrated.
- [ ] Correction and revocation do not rewrite accepted public history silently.
- [ ] Release withdrawal authority assigned.

For documentation publication:

- [ ] Pages publication owner identified.
- [ ] Previous known-good site artifact identified.
- [ ] Site withdrawal and restoration procedure reviewed.
- [ ] Public artifact retention and privacy policy approved.

For any future hosted runtime, deployment, health-check, backup, incident-response, credential-revocation, emergency-stop, and rollback gates are mandatory and require separate architecture approval.

## Release decision

**Blocked** until every gate applicable to the intended release class has evidence. Existing code, a passing demo, a successful local transition, or a successful documentation build must not be described as production-ready or canonically authoritative.

The unresolved portfolio role is release significant. No release should imply that `qsio-kernel` is A.L.I.S.T.A.I.R.E.'s authoritative runtime until ownership is explicitly approved. If another runtime is canonical, no conformance claim should be made until shared fixtures reproduce.

## Rollback criteria

Withdraw or supersede a release when any of the following is discovered:

- canonical serialization or hash instability;
- replay divergence for a supported record sequence;
- accepted transition with an invalid precondition;
- broken parent linkage or undeclared branch behavior;
- Quietus bypass or failed revocation propagation;
- forbidden external-capability request accepted by the semantic path;
- capability, witness, or interface data interpreted as stronger authority than supported;
- wrong-subject, stale, replayed, revoked, corrected, or private evidence accepted under an incompatible profile;
- packaging that installs different code than the reviewed commit;
- documentation artifact built from a source other than the submitted immutable head;
- undocumented capability, schema, or authority expansion;
- sensitive information in source, tests, artifacts, hashes, or Pages;
- misleading canonical-runtime, conformance, security, or production claims; or
- material license, provenance, compatibility, or migration defect.

Rollback means marking the affected release as withdrawn, preserving incident evidence, returning source and documentation to the last verified behavior, revoking affected capabilities, invalidating incompatible caches, and issuing a corrected version rather than rewriting an existing public tag.

## Evidence template

```text
Release class:
Version or publication label:
Repository and source commit:
Canonical role decision:
Canonical contract/package owner:
Schema and fixture identities:
Approver:
Capability and revocation owners:
Python environments:
Build commands:
Test and type-check results:
Pairwise gluing fixtures:
Triple-overlap witnesses:
Documentation workflow run:
Documentation artifact and digest:
Security, privacy, and retention checks:
Artifacts and SHA-256 values:
Known limitations:
Previous known-good release or site:
Rollback trigger and procedure:
Incident, emergency-stop, recovery, and withdrawal authorities:
```
