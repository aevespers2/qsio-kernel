# Scope and release governance

The repository uses three root documents to keep implementation, evidence, and public claims aligned. Documentation may clarify these records, but it cannot grant authority beyond them.

## Task chain

[`taskchain.md`](https://github.com/aevespers2/qsio-kernel/blob/main/taskchain.md) defines the approved order of work.

Current posture:

- the executable semantic baseline is complete for the prototype;
- documentation and contract hardening are in progress;
- verification hardening is proposed;
- persistence and independent authorization require architectural approval; and
- external integration, federation, and autonomous spawning are not authorized.

A runtime change must identify the task-chain phase it advances and may not infer approval from a conceptual name, portfolio aspiration, or future-facing design note.

## Release plan

[`release.md`](https://github.com/aevespers2/qsio-kernel/blob/main/release.md) defines evidence required before a release claim.

The current `0.1.0` code is an experimental source baseline. A new release remains blocked until applicable build, packaging, verification, security, documentation, provenance, and rollback gates have recorded evidence. Production or hosted-service release is not authorized by the current architecture.

## Changelog

[`changelog.md`](https://github.com/aevespers2/qsio-kernel/blob/main/changelog.md) records user-visible changes and clarifications. Runtime changes, schema changes, compatibility impacts, security-relevant behavior, and documentation milestones belong under `Unreleased` until a version is approved.

## Portfolio authority boundary

A.L.I.S.T.A.I.R.E. is the canonical system objective, but this repository is not presently the portfolio control plane. The current kernel may produce deterministic state and interaction evidence; it may not independently:

- prioritize portfolio objectives;
- issue its own capabilities;
- access credentials or connected services;
- create or merge repository changes;
- approve releases or deployments;
- alter its own canon or enforcement boundary;
- suppress review evidence; or
- assume emergency-stop, incident, or rollback authority.

Those powers require designated ownership, independent authorization, revocation, audit, and recovery. See [A.L.I.S.T.A.I.R.E. integration](alistaire-integration.md) and [ADR 0002](adr/0002-alistaire-kernel-role.md).

## Pull-request alignment checklist

Every behavior-changing pull request should answer:

1. What repository goal does this advance?
2. Which task-chain phase authorizes it?
3. What tests or fixtures prove the claim?
4. Does architecture, API, security, onboarding, operations, or portfolio documentation need revision?
5. Which release gates gain evidence, and which remain blocked?
6. What changelog entry describes the user-visible effect?
7. Is there a compatibility, migration, privacy, authority, or rollback impact?
8. Does it change the boundary with another A.L.I.S.T.A.I.R.E. repository?
9. Does it require a new or updated architecture decision record?

## Documentation pull-request checklist

A documentation-only candidate should establish:

- the exact submitted source SHA;
- a strict site build from that immutable head;
- navigation and internal-link integrity;
- generated-site boundary and secret-pattern checks;
- retained rendered-site and evidence artifacts when practical;
- explicit separation of implemented, proposed, and blocked behavior; and
- alignment among overview, architecture, task chain, release plan, and changelog.

A passing documentation build proves renderability of the reviewed source. It does not prove runtime behavior, accessibility, security, or production readiness.

## Decision records

Architecture decisions belong under `docs/adr/` and should include status, context, decision or proposal, consequences, alternatives, acceptance criteria, and supersession behavior.

- [ADR 0001](adr/0001-kernel-boundaries.md) records the original kernel boundary.
- [ADR 0002](adr/0002-alistaire-kernel-role.md) proposes the interim portfolio role and identifies the unresolved canonical-runtime decision.

## Documentation-only changes

Documentation may clarify present behavior, expose limitations, improve navigation, define integration contracts, or establish approval criteria. It must not present a proposed capability as implemented, silently change runtime semantics, or mark a release gate complete without exact-source evidence.