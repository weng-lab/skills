---
name: artifactor
description: Use when creating or revising agent-facing instructions, including skills, SKILL.md, AGENTS.md, CLAUDE.md, agent definitions, subagent prompts, reusable prompts, and agent-facing reference docs. Does not govern ordinary human-facing prose.
---

# Artifactor

Write instructions that produce a predictable process across runs. Stable behavior matters; identical output does not.

## Route the artifact

Read each reference whose condition matches before drafting or editing:

- `references/skills.md`: Skill packaging, discovery, routing, resources, and iteration. Read when creating or revising a skill, `SKILL.md`, skill reference, skill script, skill asset, or trigger description.
- `references/instruction-files.md`: Scoped repository instructions. Read when editing `AGENTS.md`, `CLAUDE.md`, or another inherited instruction file.
- `references/subagent-prompts.md`: Bounded assignments. Read when writing an agent definition, subagent prompt, reviewer prompt, or reusable task prompt.

Use this file alone when no specialized branch applies.

## Process

1. Define the contract.
   Name the primary reader, the behavior the artifact must change, the branches that should reach it, and the observable completion signal. Separate durable instructions from facts that belong only to the current task.
   Done when every proposed instruction supports the same reader and behavioral purpose.

2. Map branches and pointers.
   A context pointer names out-of-context material and states the branch that should load it. Give each distinct branch one trigger and collapse synonyms for the same branch. Inline material every branch needs. Put branch-specific material behind a pointer.
   Done when every branch reaches all the material it needs without loading unrelated material.

3. Build the information hierarchy.
   Put ordered actions in steps. Keep reference needed on every run in the main file. Disclose optional reference in a separate file. Co-locate each concept's definition, rules, and caveats.
   Done when the normal path is visible in one pass and no step is buried under unrelated reference.

4. Bound the work.
   End each step with a condition that distinguishes done from not done. Demand the necessary legwork, such as accounting for every modified file instead of merely producing a change list. Split a sequence only when visible later steps repeatedly cause premature completion and the current bound cannot be made clearer.
   Done when every step has a checkable criterion and the artifact has an exhaustive final criterion.

5. Prune.
   Keep each meaning in one authoritative place. Remove copies of config, directory layout, scripts, or command help that the agent can inspect cheaply. Delete stale material, generic advice, decorative examples, and instructions that do not change behavior. State the desired behavior directly. Keep prohibitions for hard guardrails and pair them with the safe action. Use a leading word only when it replaces repeated explanation without adding ambiguity.
   Done when removing any remaining line would change discovery, execution, output, resource use, or safety.

6. Probe the artifact.
   Test one obvious invocation, one casual invocation, and one adjacent case that should stay outside scope. Walk one normal branch and each materially different exceptional branch. Name the failure before making the smallest responsible correction.
   Done when the right material loads for every tested branch and the near-miss stays outside scope.

## The two loads

- Context load is always-visible text. Keep pointers and inherited instructions tight because they spend attention on every turn.
- Cognitive load is what a person must remember exists and choose to invoke. Spend it where human judgment matters. Use reliable routing for the rest.

Progressive disclosure trades a small pointer for lower context load and a clearer hierarchy. It works only when the pointer states the branch precisely enough to retrieve the hidden material.
