# Contributing a skill

## Choose a location

Add a skill under `skills/<category>/<skill-name>/SKILL.md`. Current categories are `webdev`, `productivity`, and `writing`; `bioinformatics` is reserved for future skills. Choose a new category only when an existing one does not fit.

Use a lowercase, hyphenated directory name that matches the skill's unique `name`.

## Write the skill

Start with valid YAML frontmatter:

```markdown
---
name: literature-review
description: Find and synthesize research papers on a defined question. Use when the user requests a literature review or comparison of published evidence.
---

# Literature Review

Describe the workflow, required inputs, expected output, and how to verify it.
```

Follow the [Agent Skills specification](https://agentskills.io/specification):

- `name`: at most 64 characters; lowercase letters, numbers, and single hyphens, matching the containing directory.
- `description`: 1–1024 characters explaining what the skill does and when it should activate.
- Keep `SKILL.md` under 500 lines; move detailed material into supporting files.
- Keep resources inside the skill directory and reference them with relative paths.
- Use `compatibility` when specific tools or environment access are required.
- Preserve attribution and required license notices for adapted material. Record the upstream URL and revision; see [maintenance notes](docs/maintaining.md#attribution-and-licensing).

Make the scope distinct from existing skills. Include enough guidance to verify the result and explain important constraints without imposing unrelated workflows.

## Add it to the catalog

1. Add a linked entry with a clear use case to the matching README section.
2. Add the exact skill name to one group in `skills.sh.json`.
3. Create a group only when it has a real source skill. Every current source skill must appear exactly once; remove entries when retiring skills.

These coverage rules are repository policy. skills.sh itself permits ungrouped skills and uses the first matching group for duplicates.

## Validate

Use Node.js 22.20+ and [uv](https://docs.astral.sh/uv/):

```bash
npm ci
npm run validate
```

CI uses the same command. Validation checks specification frontmatter and naming, unique names, local resource references, discovery with the pinned CLI, and the grouping configuration's structure and coverage.

Local-reference checks cover Markdown links and images plus inline-code paths under `references/`, `scripts/`, and `assets/`. They check file existence, not remote URLs or heading anchors. The discovery command uses `--list` with telemetry disabled and installs nothing.

For a manual discovery preview:

```bash
npx skills add ./skills --list
```

Try the skill on a representative task and describe that result in your pull request. For content-only edits, a brief before/after example is sufficient. Publishing to skills.sh also requires the [listing refresh procedure](docs/maintaining.md#publish-and-refresh-the-skillssh-page) after merge.
