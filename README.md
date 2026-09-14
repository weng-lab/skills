# Weng Lab Agent Skills

[![skills.sh](https://skills.sh/b/weng-lab/skills)](https://skills.sh/weng-lab/skills)
[![Validate skills](https://github.com/weng-lab/skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/weng-lab/skills/actions/workflows/validate-skills.yml)

Reusable agent skills for Weng Lab's development and writing workflows. Browse the skills below, choose the ones that fit your work, and install them into your coding agent.

[Browse on skills.sh](https://skills.sh/weng-lab/skills) · [Contribute a skill](CONTRIBUTING.md) · [Maintainer guide](docs/maintaining.md)

## Quick start

Run this from the project where you want to use the skills, then select skills and agents interactively:

```bash
npx skills@latest add weng-lab/skills
```

Preview the available skills without installing:

```bash
npx skills@latest add weng-lab/skills --list
```

Requires Node.js 22.20 or newer. The CLI supports Claude Code, Cursor, Codex, OpenCode, Gemini CLI, and [other agents](https://github.com/vercel-labs/skills#supported-agents).

## Web Development

| Skill | When to choose it |
| --- | --- |
| [react-best-practices](skills/webdev/react-best-practices/SKILL.md) | Weng Lab's general React/TypeScript guidance: state, effects, component design, composition, and React/Next.js performance. Start here for everyday React work. |
| [react-doctor](skills/webdev/react-doctor/SKILL.md) | Run React Doctor and interpret its diagnostics, scan scope, and configuration. Requires React Doctor installed in the target project. |
| [vercel-react-best-practices](skills/webdev/vercel-react-best-practices/SKILL.md) | The bundled Vercel performance rulebook for React and Next.js. Choose this for its detailed optimization references; it overlaps with the general React skill. |

```bash
npx skills@latest add weng-lab/skills --skill react-best-practices
```

## Productivity

| Skill | When to choose it |
| --- | --- |
| [commit](skills/productivity/commit/SKILL.md) | Inspect and commit changes when you explicitly ask the agent to create a Git commit. |

```bash
npx skills@latest add weng-lab/skills --skill commit
```

## Writing

| Skill | When to choose it |
| --- | --- |
| [unslop](skills/writing/unslop/SKILL.md) | Write and revise documentation, messages, PR descriptions, and other prose with a natural voice. |

```bash
npx skills@latest add weng-lab/skills --skill unslop
```

## Installation options

Install multiple skills for a specific agent:

```bash
npx skills@latest add weng-lab/skills --skill commit unslop --agent claude-code
```

Add `--global` to make a skill available across projects:

```bash
npx skills@latest add weng-lab/skills --skill commit --global
```

## Manage installed skills

```bash
npx skills@latest list
npx skills@latest update --project
npx skills@latest update --global
npx skills@latest update commit
npx skills@latest remove commit
```

`update` refreshes the skills installed in your agent. `@latest` selects the latest CLI; the repository's pinned development CLI is upgraded separately.

## Try a skill without installing

Generate a prompt to use with your agent:

```bash
npx skills@latest use weng-lab/skills --skill commit
```

This prints a prompt and stages the skill in a temporary directory. To launch a supported agent with it, add an agent option, for example `--agent claude-code`.

## Repository layout

Source skills live in `skills/<category>/<skill-name>/`. Each skill includes its own `SKILL.md` and supporting resources. The catalog above lists all current skills; bioinformatics is a reserved category with no published skills yet.

[skills.sh.json](skills.sh.json) defines the sections on our skills.sh page. The directory structure controls source organization; valid `SKILL.md` files make skills discoverable. CI checks skill format, references, CLI discovery, and complete grouping coverage.

See the [maintainer guide](docs/maintaining.md) for listing refreshes, retired skills, CLI upgrades, and attribution follow-ups.

## License

Original contributions are licensed under the [MIT License](LICENSE). Third-party material retains its existing licenses and attribution; see the [provenance notes](docs/maintaining.md#attribution-and-licensing).
