# Subagent and reusable prompts

Read this with Artifactor when defining an agent or delegating a bounded task.

## Bound the assignment

Give the agent a temporary role only when it changes how the task should be handled. State the exact task, relevant context and sources of truth, constraints, modification authority, expected result, and required verification.

Separate product decisions owned by the parent from execution decisions the subagent may resolve. Require an output the parent can use directly, such as paths, findings, exact check outcomes, uncertainty, or a focused patch.

For read-only work, request findings rather than edits. For implementation, grant modification authority and name the allowed scope. State whether the agent may delegate.

## Keep context bounded

Include facts the subagent cannot cheaply discover and point to local sources for the rest. Replace broad conversation history with the settled decisions that govern the task. Label hypotheses so the agent can disprove them.

Use a fresh agent when independence matters. Continue an existing session when the next task depends on context it already gathered.

## Match verification to risk

Name the checks that provide useful evidence and let the agent resolve ordinary details. Keep validation proportional to risk. Require exact outcomes rather than "tests pass" when the distinction matters.

## Completion bound

The prompt is ready when the agent can begin without asking about scope, authority, sources of truth, expected output, or how to establish completion.
