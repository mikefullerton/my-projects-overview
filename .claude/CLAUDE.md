# myprojectsoverview

## Project-specific rules

See `.claude/rules/` for rules that also apply in this repo:

- `always-commit-and-push.md` — commit and push after every file change (on
  your branch, not main)
- `atomic-site-updates.md` — overview.md changes must be accompanied by
  regenerated site output in the same commit

## graphify

This project has a graphify knowledge graph at graphify-out/.

Rules:
- Before answering architecture or codebase questions, read graphify-out/GRAPH_REPORT.md for god nodes and community structure
- If graphify-out/wiki/index.md exists, navigate it instead of reading raw files
- After modifying code files in this session, run `python3 -c "from graphify.watch import _rebuild_code; from pathlib import Path; _rebuild_code(Path('.'))"` to keep the graph current
