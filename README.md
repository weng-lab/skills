# Weng Lab Agent Skills

[![skills.sh](https://skills.sh/b/weng-lab/skills)](https://skills.sh/weng-lab/skills)

Reusable AI agent skills for Weng Lab bioinformatics, web development, writing, productivity, and lab workflows.

These skills can be installed into supported AI coding agents with the [`skills` CLI](https://www.skills.sh/docs), including OpenCode, Claude Code, Cursor, Codex, Gemini, and others.

## Install Skills

List the skills available in this repo:

```bash
npx skills add weng-lab/skills --list
```

Install skills interactively:

```bash
npx skills add weng-lab/skills
```

Install one skill by name:

```bash
npx skills add weng-lab/skills --skill commit
```

Install skills globally for your user account:

```bash
npx skills add weng-lab/skills --global
```

Install skills for a specific agent:

```bash
npx skills add weng-lab/skills --agent opencode
```

## Update Installed Skills

Use `npx skills update` to update skills you previously downloaded with `npx skills add`.

The CLI can update skills installed in your current project, skills installed globally in your agent config folder, or both. It will guide you through those choices interactively.

```bash
npx skills update
```

You can also update one skill by name:

```bash
npx skills update commit
```

## Use a Skill Without Installing

Run a skill ad hoc:

```bash
npx skills use weng-lab/skills --skill commit
```

## Add a Skill

See [CONTRIBUTING.md](CONTRIBUTING.md) for the short checklist.

In brief: add your skill under the best category, keep its files together, and add the skill name to `skills.sh.json`.

## About `skills.sh.json`

`skills.sh.json` controls how this repo is grouped on [skills.sh](https://www.skills.sh/). It does not make skills installable; installable skills come from valid `SKILL.md` files under `skills/`.

Only include a group in `skills.sh.json` after it has at least one real skill.

## Links

- [skills.sh documentation](https://www.skills.sh/docs)
- [skills CLI](https://github.com/vercel-labs/skills)
- [Agent Skills specification](https://agentskills.io)
