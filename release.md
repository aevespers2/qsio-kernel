# Release plan

## Current release posture

The repository contains a functional `0.1.0` experimental kernel, but no new release is approved by this document. The present documentation work is release-neutral: it clarifies behavior, portfolio fit, operational limits, and evidence requirements without changing runtime scope.

## Release classes

### Experimental source release

A source release may expose the current local reference kernel when every applicable gate below is satisfied and its limitations remain prominent.

### Documentation publication

A GitHub Pages publication may expose rendered documentation after exact-head build evidence, generated-site review, publication authority, accessibility review, and rollback ownership are recorded. The documentation workflow builds an artifact; it does not deploy Pages.

### Production or hosted-service release

Not authorized. The current architecture lacks durable storage, independent attestation, complete authorization enforcement, network isolation, operational monitoring, service ownership, incident response, and an approved trust model.

## Required gates

### Scope and governance

- [x] Repository purpose and non-goals documented.
- [x] Task chain distinguishes implemented, proposed, blocked, and unauthorized work.
- [x] A.L.I.S.T.A.I.R.E. integration boundary documented.
- [x] Proposed portfolio-role ADR exists.
- [x] MIT license present.
- [ ] Canonical role relative to `QuantumStateObjects`, `QSO-GENOMES`, and `QSO-FABRIC` approved.
- [ ] Release owner and approval record identified.
- [ ] Compatibility policy approved.
- [ ] Incident, emergency-stop, and rollback authorities designated.

### Build and packaging

- [x] `pyproject.toml` declares package metadata and Python requirement.
- [x] Editable local installation path documented.
- [ ] Clean build from a fresh environment recorded.
- [ ] Wheel and source distribution built and inspected.
- [ ] Package installation from built artifacts verified.
- [ ] Exported package contents and console entry point verified.

### Verification

- [x] Core pytest suite exists.
- [x] Demo exercises genesis, interactions, verification, replay, and Quietus.
- [ ] Full test output captured for the release commit.
- [ ] Canonical hash fixtures recorded.
- [ ] Malformed-input and corruption tests completed.
- [ ] Parent-link and intermediate replay tests completed.
- [ ] Supported-environment replay comparison completed.
- [ ] Static type check completed with the declared strict settings.

### Security and privacy

- [x] Current trust boundaries and limitations documented.
- [x] Local operations and failure response documented.
- [x] External I/O, network, subprocess, and spawn requests are forbidden in the semantic validation path.
- [ ] Capability enforcement architecture approved.
- [ ] Independent identity, witness, revocation, and expiry policies approved.
- [ ] Dependency and supply-chain review recorded.
- [ ] Secret scan recorded for the release source and artifacts.
- [ ] Adversarial test evidence recorded.
- [ ] Privacy review confirms no sensitive fixtures or generated artifacts.
- [ ] Security contact or reporting route approved.

### Documentation and accessibility

- [x] Project overview, architecture, design, API, onboarding, operations, security, governance, and portfolio-integration guides exist in the candidate.
- [x] Pages-ready navigation exists.
- [x] Exact-head strict documentation workflow is implemented.
- [ ] Documentation workflow passes on the final submitted commit.
- [ ] Rendered-site artifact and digest are recorded.
- [ ] Internal links and generated-site boundary checks pass.
- [ ] Mermaid source diagrams are reviewed for correctness and fallback readability.
- [ ] Keyboard, contrast, heading, table, and screen-reader review recorded for the published site.
- [ ] Published Pages URL, deployment source, and deployment provenance recorded, if Pages is enabled.

### Provenance and reproducibility

- [ ] Release commit SHA recorded.
- [ ] Runtime build and test environment recorded.
- [ ] Documentation source SHA and workflow run recorded.
- [ ] Artifact hashes recorded.
- [ ] Build commands recorded.
- [ ] Changelog finalized for the release version.
- [ ] Tag is signed or release-signing limitation is explicitly accepted.

### Operations and rollback

For an experimental source release:

- [x] Local failure triage and recovery guidance documented.
- [ ] Previous known-good tag identified.
- [ ] Artifact withdrawal procedure exercised or reviewed.
- [ ] Breaking hash/schema changes explicitly prohibited or migrated.
- [ ] Release withdrawal authority assigned.

For documentation publication:

- [ ] Pages publication owner identified.
- [ ] Previous known-good site artifact identified.
- [ ] Site withdrawal and restoration procedure reviewed.
- [ ] Public artifact retention and privacy policy approved.

For any future hosted runtime, deployment, health-check, data backup, incident-response, credential-revocation, emergency-stop, and rollback gates are mandatory and require separate architecture approval.

## Release decision

**Blocked** until all gates applicable to the intended release class have evidence. Existing code, a passing demo, or a successful documentation build must not be described as production-ready.

The unresolved canonical portfolio role is a release-significant architecture decision. No release should imply that `qsio-kernel` is A.L.I.S.T.A.I.R.E.'s authoritative runtime until that ownership is explicitly approved.

## Rollback criteria

Withdraw or supersede a release when any of the following is discovered:

- canonical serialization or hash instability;
- replay divergence for a supported record sequence;
- accepted transition with an invalid precondition;
- broken parent linkage;
- Quietus bypass;
- forbidden external-capability request accepted by the semantic path;
- packaging that installs different code than the reviewed commit;
- documentation artifact built from a source other than the submitted immutable head;
- undocumented capability or authority expansion;
- sensitive information in source, tests, artifacts, or Pages;
- misleading canonical-runtime or production claims; or
- a material license or provenance defect.

Rollback for the current package means marking the affected release as withdrawn, returning source and documentation to the last verified behavior, and issuing a corrected version rather than rewriting an existing public tag.

## Evidence template

A release or documentation-publication record should include:

```text
Release class:
Version or publication label:
Repository:
Source commit:
Approver:
Canonical role decision:
Python environments:
Build commands:
Test command and result:
Type-check command and result:
Documentation workflow run:
Documentation artifact and digest:
Security and privacy checks:
Artifacts and SHA-256 values:
Known limitations:
Previous known-good release or site:
Rollback trigger and procedure:
Incident and withdrawal authority:
```
