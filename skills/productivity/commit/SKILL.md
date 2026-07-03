---
name: commit
description: Use ONLY when the user explicitly asks to git commit, create a commit, or commit changes. Do not use for draft commit messages, diff review, or commit planning.
---

# Commit

1. Inspect `git status`, `git diff`, and `git log --oneline -10`.
2. Stage changes according to the user's stated scope; ask only before including changes that appear outside that scope.
3. Commit once, unless the user explicitly asked for multiple commits.
4. Match recent commit style; if no clear style exists, use a concise conventional message.
5. If there is nothing to commit, do not create an empty commit; say no commit was made.
