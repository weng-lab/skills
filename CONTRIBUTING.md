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

Open a pull request when you are done. CI will check the formatting and compatibility.

You can also verify your skill with:

```bash
npx skills add . --list
```

Only include groups in `skills.sh.json` after they have at least one skill.
