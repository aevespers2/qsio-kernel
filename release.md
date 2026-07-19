# Release plan

## Current release posture

The repository contains a functional `0.1.0` experimental kernel, but no new release is approved by this document. The present documentation work is release-neutral: it clarifies behavior and readiness without changing implementation scope.

## Release classes

### Experimental source release

A source release may expose the current local reference kernel when every required gate below is satisfied and its limitations remain prominent.

### Production or service release

Not authorized. The current architecture lacks durable storage, independent attestation, complete authorization enforcement, network isolation, operational monitoring, and an approved service trust model.

## Required gates

### Scope and governance

- [x] Repository purpose and non-goals documented.
- [x] Task chain distinguishes implemented and proposed work.
- [x] MIT license present.
- [ ] Release owner and approval record identified.
- [ ] Compatibility policy approved.

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
- [ ] Supported-environment replay comparison completed.
- [ ] Static type check completed with the declared strict settings.

### Security and privacy

- [x] Current trust boundaries and limitations documented.
- [x] External I/O, network, subprocess, and spawn requests are forbidden in the semantic validation path.
- [ ] Dependency and supply-chain review recorded.
- [ ] Secret scan recorded.
- [ ] Adversarial test evidence recorded.
- [ ] Privacy review confirms no sensitive fixtures or generated artifacts.
- [ ] Security contact or reporting route approved.

### Documentation and accessibility

- [x] Project overview, architecture, design, API, onboarding, and security guides exist.
- [x] Pages-ready navigation exists.
- [ ] Documentation build passes without warnings.
- [ ] Internal links and Mermaid rendering verified.
- [ ] Keyboard, contrast, heading, table, and screen-reader review recorded for the published site.
- [ ] Published Pages URL and deployment provenance recorded, if Pages is enabled.

### Provenance and reproducibility

- [ ] Release commit SHA recorded.
- [ ] Artifact hashes recorded.
- [ ] Build environment and commands recorded.
- [ ] Changelog finalized for the release version.
- [ ] Tag is signed or release-signing limitation is explicitly accepted.

### Operations and rollback

For a source-only experimental release:

- [ ] Previous known-good tag identified.
- [ ] Artifact withdrawal procedure documented.
- [ ] Breaking hash/schema changes explicitly prohibited or migrated.

For any future hosted runtime, additional deployment, health-check, data backup, incident-response, and rollback gates are mandatory and require a separate architecture approval.

## Release decision

**Blocked** until all gates applicable to the intended release class have evidence. Existing code and documentation must not be described as production-ready solely because the demo and current tests pass.

## Rollback criteria

Withdraw or supersede a release when any of the following is discovered:

- canonical serialization or hash instability;
- replay divergence for a supported record sequence;
- accepted transition with an invalid precondition;
- Quietus bypass;
- packaging that installs different code than the reviewed commit;
- undocumented capability expansion;
- sensitive information in source, tests, artifacts, or Pages; or
- a material license or provenance defect.

Rollback for the current package means marking the affected release as withdrawn, returning documentation to the last verified behavior, and issuing a corrected version rather than rewriting an existing public tag.

## Evidence template

A release record should include:

```text
Version:
Commit:
Approver:
Python environments:
Build commands:
Test command and result:
Type-check command and result:
Documentation build result:
Security checks:
Artifacts and SHA-256 values:
Known limitations:
Previous known-good release:
Rollback trigger and procedure:
```
