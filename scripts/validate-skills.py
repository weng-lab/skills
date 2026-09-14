# /// script
# requires-python = ">=3.11"
# dependencies = ["skills-ref==0.1.1", "markdown-it-py==3.0.0"]
# ///
"""Validate source skills and compare them with the installed Skills CLI's list."""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

from catalog import grouping_errors
from markdown_it import MarkdownIt
from skills_ref import read_properties, validate
from skills_ref.errors import SkillError

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = MarkdownIt()


def reference_errors(skill):
    errors = []
    for document in sorted(skill.rglob("*.md")):
        content = document.read_text()
        if content.startswith("---\n"):
            content = content.split("---", 2)[-1]
        for block in MARKDOWN.parse(content):
            for token in block.children or []:
                target = None
                if token.type == "link_open":
                    target = token.attrGet("href")
                elif token.type == "image":
                    target = token.attrGet("src")
                elif token.type == "code_inline" and re.fullmatch(
                    r"(?:references|scripts|assets)/[^\s`*<>]+", token.content
                ):
                    target = token.content
                if not target:
                    continue
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                # Markdown links are relative to their containing document;
                # resource paths in inline code are relative to the skill root.
                base = skill if token.type == "code_inline" else document.parent
                if not (base / unquote(url.path)).exists():
                    errors.append(f"{document.relative_to(ROOT)}: missing local reference {target}")
    return errors


def discovery_errors(names):
    result = subprocess.run(
        ["node", str(ROOT / "node_modules/skills/bin/cli.mjs"),
         "add", "./skills", "--list"],
        cwd=ROOT, capture_output=True, text=True, timeout=60,
        env={**os.environ, "DISABLE_TELEMETRY": "1", "NO_COLOR": "1"},
    )
    output = re.sub(r"\x1b\[[0-?]*[ -/]*[@-~]", "", result.stdout)
    if result.returncode:
        return [f"CLI discovery failed:\n{output}\n{result.stderr}"]
    # The CLI does not allow --json with --list. Read only the skill-name rows in its
    # Available Skills section, not descriptions that might mention a name.
    section = output.partition("Available Skills")[2].partition("Use --skill")[0]
    discovered = re.findall(r"^│    (\S+)\s*$", section, re.MULTILINE)
    if sorted(discovered) != sorted(names):
        return [f"CLI discovery mismatch: expected {sorted(names)}, got {sorted(discovered)}"]
    print(f"CLI discovers all {len(names)} source skills.")
    return []


def main():
    errors = []
    names = {}
    documents = sorted((ROOT / "skills").rglob("SKILL.md"))
    if not documents:
        errors.append("No source skills found under skills/.")
    for document in documents:
        skill = document.parent
        label = document.relative_to(ROOT)
        errors.extend(f"{label}: {error}" for error in validate(skill))
        try:
            name = read_properties(skill).name
        except SkillError as error:
            errors.append(f"{label}: {error}")
            continue
        if name in names:
            errors.append(f"{label}: duplicate skill name {name!r} (also {names[name]})")
        names[name] = label
        errors.extend(reference_errors(skill))
    try:
        config = json.loads((ROOT / "skills.sh.json").read_text())
        errors.extend(grouping_errors(config, names))
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"skills.sh.json: {error}")
    errors.extend(discovery_errors(list(names)))
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f"Validated {len(documents)} source skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
