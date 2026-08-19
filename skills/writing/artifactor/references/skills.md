# Skills

Read this with Artifactor when creating or revising a skill.

## Package

A skill folder contains `SKILL.md` and may contain disclosed resources:

```text
skill-name/
|-- SKILL.md
|-- references/
|-- scripts/
`-- assets/
```

Keep normal-path behavior in `SKILL.md`. Put optional detail, rare branches, long examples, and domain notes in `references/`. Put deterministic repeated work in `scripts/`. Put reusable templates, fixtures, and source material in `assets/`.

Index every bundled resource in `SKILL.md`. Each pointer must give its path, contents, and exact condition for reading or using it. Treat an unindexed resource as invisible. Use relative paths from the skill root and keep references one level deep.

## Frontmatter and discovery

Use portable Agent Skills frontmatter:

```yaml
---
name: lowercase-hyphenated-name
description: Use when creating or revising concrete artifact names and user-visible trigger phrases.
---
```

The folder name and `name` must match. The Agent Skills specification requires `name` and `description`; consult the host's documentation before adding non-standard fields. Treat the description as the skill's always-loaded router. Front-load words users will say, name each distinct trigger branch, and add a near-miss exclusion when false invocation is likely. Do not summarize the body there.

Create another skill only when it needs independent discovery. Otherwise keep the branch as a referenced file. Prefer one skill that routes to bundled references over several skills whose descriptions compete for the same requests.

If behavior should run only after an explicit user request, use the host's manual command or workflow mechanism when one exists. Do not depend on non-standard frontmatter in a skill intended for multiple agents.

Before accepting the discovery choice and description, test:

- one obvious prompt that should invoke the skill
- one casual prompt that should invoke it
- one adjacent prompt that should not invoke it

## Build or revise

For a new skill:

1. Define the changed behavior, trigger branches, action boundary, and success signal.
2. Remove temporary details from the current task.
3. Choose what stays in `SKILL.md` and what is disclosed.
4. Draft the smallest complete workflow and resource index.
5. Add examples only when they teach a boundary, format, or recurring failure.
6. Probe realistic prompts, name each failure, and revise the smallest responsible part.

For an existing skill, begin with an observed failure. Classify it before editing:

- trigger miss or false trigger
- ambiguous process or completion bound
- instruction that changes no behavior
- hidden normal-path material or invisible resource
- duplication, excessive length, or stale material
- temporary task context captured as durable guidance
- missing boundary between discussion and file modification
- revision overfit to one example

Retest the failing prompt and one adjacent prompt after the edit. Stop when the observed failure is resolved without weakening nearby behavior.

## Scripts, assets, and evals

Add a script when the work is deterministic, correctness matters, or agents repeatedly reinvent the same transformation. Add an asset when the skill needs a reusable template, fixture, example, or source file. Point to each from `SKILL.md` instead of copying its contents there.

Prefer a few qualitative probes. Build formal evals only when success is objectively checkable, such as a fixed format, extraction, or deterministic transformation.

## Completion bound

The skill is ready when it follows the Agent Skills specification, trigger tests pass, normal-path behavior is inline, every resource has a precise pointer, every workflow step has a completion criterion, and each remaining line changes behavior.
