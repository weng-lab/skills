# Inherited instruction files

Read this with Artifactor when editing `AGENTS.md`, `CLAUDE.md`, or another file loaded by directory scope.

## Write for inheritance

Inherited instructions spend context on every turn in their scope. Keep only rules that apply throughout that scope. Move branch-specific detail to a referenced document with a precise reading condition. Keep task-specific facts in the task, not in inherited instructions.

Place an instruction at the narrowest directory scope that covers every file it governs. A root instruction should not carry rules for one package when that package can own them.

## Prefer facts the environment cannot reveal

Record unwritten conventions, ownership boundaries, reasons behind surprising choices, mandatory workflows, and traps that inspection will not expose. Point to authoritative config or documentation instead of copying dependency versions, directory listings, schema details, or commands the agent can inspect directly.

State precedence when local instructions refine or replace parent instructions. A more specific example does not replace the parent rule.

## Write actionable rules

Name the condition and required behavior together. Prefer "Read `.devserve/err.log` when diagnosing server failures" to a detached list of files. Put hard guardrails beside the action they constrain and state the safe behavior positively.

Avoid mission statements and generic engineering advice. If a competent agent would behave the same without the line, delete it.

## Completion bound

The file is ready when every line applies throughout its scope, every branch-specific rule has a reachable pointer, no cheap environment lookup is copied, and local precedence is unambiguous.
