# Contributing a Skill

Add your skill in the category that fits best:

```text
skills/bioinformatics/<your-skill>/SKILL.md
skills/productivity/<your-skill>/SKILL.md
skills/webdev/<your-skill>/SKILL.md
skills/writing/<your-skill>/SKILL.md
```

Use a lowercase, hyphenated folder name, such as `literature-review`.

Each skill must have a `SKILL.md` file. If your skill has supporting files, keep them inside the same skill folder.

Then add your skill name to the matching group in `skills.sh.json`. If that group does not exist yet, add it.

For example, if you add:

```text
skills/bioinformatics/literature-review/SKILL.md
```

also add `literature-review` to the Bioinformatics group in `skills.sh.json`.

Open a pull request when you are done. CI checks skill frontmatter and naming,
unique names, local file references, and discovery with the installed Skills CLI.

Run the same check locally with Node.js and [uv](https://docs.astral.sh/uv/):

```bash
npm ci
uv run scripts/validate-skills.py
```

The script uses the specification's recommended
[skills-ref validator](https://agentskills.io/specification#validation) and a
Markdown parser. It checks local Markdown links and images in each skill's
Markdown files, plus inline-code paths under `references/`, `scripts/`, and
`assets/`. It checks file existence, not URL availability or heading anchors.
Unique names and complete CLI discovery are repository checks; grouping policy
in `skills.sh.json` is separate from this validator.

You can also verify your skill with:

```bash
npx skills add ./skills --list
```

Only include groups in `skills.sh.json` after they have at least one skill.
