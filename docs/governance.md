# Scope and release governance

The repository uses three root documents to keep implementation, evidence, and public claims aligned.

## Task chain

[`taskchain.md`](../taskchain.md) defines the approved order of work.

Current posture:

- the executable semantic baseline is complete for the prototype;
- documentation and contract hardening are in progress;
- verification hardening is proposed;
- persistence and independent authorization require architectural approval; and
- external integration, federation, and autonomous spawning are not authorized.

A runtime change must identify the task-chain phase it advances and may not infer approval from a conceptual name or future-facing design note.

## Release plan

[`release.md`](../release.md) defines evidence required before a release claim.

The current `0.1.0` code is an experimental source baseline. A new release remains blocked until applicable build, packaging, verification, security, documentation, provenance, and rollback gates have recorded evidence. Production or hosted-service release is not authorized by the current architecture.

## Changelog

[`changelog.md`](../changelog.md) records user-visible changes and clarifications. Runtime changes, schema changes, compatibility impacts, security-relevant behavior, and documentation milestones belong under `Unreleased` until a version is approved.

## Pull-request alignment checklist

Every behavior-changing pull request should answer:

1. What repository goal does this advance?
2. Which task-chain phase authorizes it?
3. What tests or fixtures prove the claim?
4. Does architecture, API, security, or onboarding documentation need revision?
5. Which release gates gain evidence, and which remain blocked?
6. What changelog entry describes the user-visible effect?
7. Is there a compatibility, migration, privacy, or rollback impact?

## Documentation-only changes

Documentation may clarify present behavior, expose limitations, improve navigation, or define approval criteria. It must not present a proposed capability as implemented or pass a release gate without evidence.
