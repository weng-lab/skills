# Weng Lab Agent Skills

[![skills.sh](https://skills.sh/b/weng-lab/skills)](https://skills.sh/weng-lab/skills)

Reusable AI agent skills for Weng Lab bioinformatics, web development, writing, productivity, and lab workflows.

This repository is a shared library of agent instructions that lab members can install into tools like OpenCode, Claude Code, Cursor, Codex, Gemini, and other agents supported by the [`skills` CLI](https://www.skills.sh/docs).

## Install

List available skills:

```bash
npx skills add weng-lab/skills --list
```

Install interactively:

```bash
npx skills add weng-lab/skills
```

Install a specific skill:

```bash
npx skills add weng-lab/skills --skill commit
```

Install globally for your user account:

```bash
npx skills add weng-lab/skills --global
```

Install for a specific agent:

```bash
npx skills add weng-lab/skills --agent opencode
```

## Use Without Installing

Run one skill ad hoc:

```bash
npx skills use weng-lab/skills --skill commit
```

## Update Installed Skills

Update one installed skill:

```bash
npx skills update commit
```

Update all installed skills:

```bash
npx skills update
```

## Repository Layout

Skills are organized by category under `skills/`:

```text
skills/
  bioinformatics/
    workflow-review/
      SKILL.md
      references/
      scripts/
      assets/
  productivity/
    commit/
      SKILL.md
  webdev/
    nextjs-review/
      SKILL.md
  writing/
    manuscript-review/
      SKILL.md
```

Each skill lives in its own folder and must include a `SKILL.md`. Category folders are only containers. Do not put a `SKILL.md` directly in `skills/bioinformatics/`, `skills/productivity/`, `skills/webdev/`, `skills/writing/`, or another category folder, because shallow skills can shadow nested ones during discovery.

A minimal skill looks like this:

```markdown
---
name: manuscript-review
description: Use when drafting, revising, or reviewing scientific manuscript sections for clarity, structure, and audience fit.
---

# Manuscript Review

Instructions for how the agent should help with manuscript review.
```

## Add A Skill

See [CONTRIBUTING.md](CONTRIBUTING.md) for the short checklist. In brief: add your skill under the best category, keep its files together, and add the skill name to `skills.sh.json`.

## Skill Quality

Good skills are:

- **Specific**: one clear workflow, not a grab bag.
- **Triggerable**: the description says when the skill should be used.
- **Lean**: include only instructions the agent needs.
- **Safe**: no secrets, credentials, private data, or hidden network actions.
- **Reusable**: useful to more than one person or project.

Prefer this:

```yaml
description: Use when drafting, revising, or reviewing scientific manuscript sections for clarity, structure, and audience fit.
```

Avoid this:

```yaml
description: Helps with writing.
```

## Experimental Skills

Work-in-progress skills should go under:

```text
skills/.experimental/
```

or be marked internal:

```yaml
metadata:
  internal: true
```

Internal skills are hidden from normal discovery unless installed with:

```bash
INSTALL_INTERNAL_SKILLS=1 npx skills add weng-lab/skills --list
```

## Contributing

Open a pull request with your new or updated skill folder. CI will check formatting and skills CLI compatibility.

`skills.sh.json` controls how the repository page is grouped on skills.sh. It does not make skills installable; installability comes from valid `SKILL.md` files under `skills/`. Only add a group to `skills.sh.json` after it has at least one real skill.

## Related Links

- [skills.sh documentation](https://www.skills.sh/docs)
- [skills CLI](https://github.com/vercel-labs/skills)
- [Agent Skills specification](https://agentskills.io)
