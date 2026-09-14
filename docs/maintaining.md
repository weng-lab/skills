# Maintaining the catalog

## Publish and refresh the skills.sh page

The root `skills.sh.json` groups our listing into Web Development, Productivity, and Writing. Use exact skill names, keep descriptions brief, and add categories only when they contain a source skill.

1. Merge skill and grouping changes into the repository's default branch (`main`).
2. Install the skills you need from the public repository with the current CLI:

   ```bash
   npx skills@latest add weng-lab/skills
   ```

3. Telemetry must be enabled for that install to refresh the stored page configuration. `DISABLE_TELEMETRY` and `DO_NOT_TRACK` disable it; respect users' preferences. A local-path install or `--list` is not the refresh procedure.
4. Allow processing and page caching to complete, then inspect [the listing](https://skills.sh/weng-lab/skills).

Visiting the page alone does not fetch the config. No approval or allowlist is needed. These behaviors are documented in [Customize repo pages](https://www.skills.sh/docs/customize).

The directory is based on observed installs, so it may retain retired names or omit skills that have not yet been installed. Ungrouped entries appear under **Other skills** with our current configuration. Grouping does not delete historical entries. Do not add retired names to the current catalog just to make them appear supported, or repeatedly install skills to inflate counts.

## Upgrade the development CLI

Use npm for repository tooling; CI installs `package-lock.json` with `npm ci`.

```bash
npm view skills version
npm install skills@latest --save-exact --ignore-scripts
npx skills --version
npm run validate
```

Commit `package.json` and `package-lock.json` together. The exact version makes local and CI discovery reproducible. `npx skills update` updates installed skills, not this dependency. Avoid introducing a second package-manager lockfile.

## Attribution and licensing

Original contributions are covered by the root [MIT License](../LICENSE). Third-party material retains its existing licenses and attribution. The root license does not replace upstream terms or resolve missing provenance; preserve upstream copyright and license notices with imported material.

Current attribution to review when changing or refreshing these skills:

| Skill | Recorded provenance |
| --- | --- |
| `react-best-practices` | Its Attribution section identifies rewritten Vercel composition and performance guidance and records the imported MIT declarations. |
| `vercel-react-best-practices` | Frontmatter identifies Vercel, MIT, and version 1.0.0. This is a bundled copy, not an automatic upstream update. |
| `react-doctor` | Frontmatter says it was adapted from the original React Doctor skill; the exact upstream revision and license are not recorded. |
| `unslop` | No upstream attribution or license is recorded in its frontmatter. Confirm provenance before assigning licensing terms. |

For future imports, record the upstream repository, revision, license, and local changes alongside the skill. Keep required notices in the installed skill directory so they travel with it.

## GitHub presentation

Keep the repository description specific to the current catalog, link the homepage to the skills.sh listing, and use relevant topics such as `agent-skills`, `react`, and `developer-tools`. Add bioinformatics to the catalog and description when a usable skill is published.
