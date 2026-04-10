# my-projects-overview

This repo follows `worktree-workflow-rule` from `~/.claude/CLAUDE.md`.

All code changes go through a worktree branch and PR — never commit directly
to `main`. Start with `EnterWorktree`, commit and push as you go (draft PR on
first push), finish with `ExitWorktree` + `gh pr ready` + `gh pr merge`.

## Project-specific rules

See `.claude/rules/` for rules that also apply in this repo:

- `always-commit-and-push.md` — commit and push after every file change (on
  your branch, not main)
- `atomic-site-updates.md` — overview.md changes must be accompanied by
  regenerated site output in the same commit
