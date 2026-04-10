# Dev Tools

## Project Summary

A collection of distributable Claude Code skills for project scaffolding, deployment, infrastructure management, and repo maintenance, bundled with supporting Python CLIs (`configurator`, `site-manager`, `webinator`) and a TypeScript/vitest harness for skill testing.

## Type & Tech Stack

**Type:** Claude Code skills repo + companion CLIs

**Tech Stack:**
- **Language:** Python 3.11+ (CLIs — stdlib only, zero external dependencies)
- **Python packaging:** `uv tool install -e` with `pyproject.toml` + `src/` layout (setuptools backend)
- **Skills:** Markdown `SKILL.md` files with YAML frontmatter, loaded via symlinks into `~/.claude/skills/`
- **Test harness:** TypeScript + vitest (`claude-skills-tester-cli/`)
- **Install:** Bash `install.sh` / `uninstall.sh` (symlinks skills, runs `uv tool install -e` for each bundled CLI)
- **Plugins enabled:** `superpowers@claude-plugins-official`

## GitHub URL

https://github.com/agentic-cookbook/dev-tools

## Directory Structure

```
.
├── .claude/
│   ├── CLAUDE.md              # Repo guidance (skills list + worktree workflow)
│   └── settings.json          # Enables superpowers plugin
├── .gitignore
├── README.md
├── install.sh                 # Symlinks skills -> ~/.claude/skills, uv-installs CLIs
├── uninstall.sh
├── skills/                    # 7 distributable skills
│   ├── configurator/          # SKILL.md v1.29.0 (~67KB), CHANGES.md, references/
│   │   ├── cli/               # site-manager CLI (pyproject -> site_manager)
│   │   │   └── src/site_manager/  (cli.py, deploy.py, verify_all.py, e2e.py, ...)
│   │   └── configurator-cli/  # configurator CLI (pyproject -> configurator)
│   │       └── src/configurator/  (cli.py, web.py, deploy.py, features/*)
│   ├── new-project/           # SKILL.md v1.0.0
│   ├── quick-ref/             # SKILL.md v1.0.0
│   ├── repo-cleaner/          # SKILL.md v5.0.0
│   ├── show-project-setup/    # SKILL.md v2.0.0
│   ├── web-view/              # SKILL.md v1.0.0 (render markdown as local HTML)
│   └── webinitor/             # SKILL.md v2.3.0
│       └── cli/               # webinator CLI (pyproject -> webinator)
│           └── src/webinator/ (cli.py, api.py, domains.py, dns.py, deploy.py, ...)
├── claude-skills-tester-cli/
│   ├── run.sh                 # Copies harness to sandbox, runs vitest
│   └── harness/
│       ├── package.json       # vitest ^3.2.1
│       ├── tsconfig.json
│       ├── vitest.config.ts
│       └── lib/               # assertions.ts, fixtures.ts, runner.ts
└── docs/
    ├── project/description.md
    ├── planning/planning.md
    ├── research/
    │   ├── claude-code-plugins.md
    │   └── cli-packaging.md
    └── superpowers/
        ├── plans/             # Dated implementation plans (2026-04-05..09)
        └── specs/             # Matching design specs
```

## Key Files & Components

**Skills (in `skills/`):**
- `configurator` (v1.29.0) — Deploy/manage a suite of up to 4 websites as a unified platform. Reads deployment specs from `~/.configurator/<name>.json`. Backend: Hono + Drizzle + PostgreSQL (Railway). Subcommands: `--configure`, `--deploy`, `add`, `update`, `verify`, `repair`, `status`, `manifest`, `seed-admin`, `go-live`. Largest skill in the repo (~67KB SKILL.md). Ships with two Python CLIs: `configurator` (interactive config web editor / spec builder) and `site-manager` (deployment executor).
- `new-project` (v1.0.0) — Creates a GitHub repo, clones it, scaffolds CLAUDE.md + docs. `<project-name> [in <org>]`.
- `quick-ref` (v1.0.0) — Generates a searchable dark-themed HTML reference page (defaults to Claude Code slash commands; accepts topics like `claude-flags`).
- `repo-cleaner` (v5.0.0) — Recursive repository cleanup; auto-fixes obvious issues, interactively resolves the rest. Flags: `--depth`, `--dry-run`.
- `show-project-setup` (v2.0.0) — HTML dashboard of all rules, skills, plugins, MCP servers, and dev tools installed locally/globally. `model: opus`, `disable-model-invocation: true`, `context: fork`.
- `web-view` (v1.0.0) — Render markdown as a styled local web page with in-page search. Newest skill (added in commit `7086c78`).
- `webinitor` (v2.3.0) — Website infrastructure management for Cloudflare (Wrangler), Railway, GoDaddy, and GitHub. Subcommands: `status`, `setup`, `configure`, `domains`, `dns`, `connect`, `deploy`. Backed by the `webinator` Python CLI.

**Bundled CLIs (`uv tool install -e`):**
- `configurator` — `skills/configurator/configurator-cli/` — interactive configurator with a large `features/` module (ab_testing, admin, analytics, api_view, auth, backend, credentials, dashboard, data_model, email, feature_flags, feedback, logging, login_tracking, pausing, project, sms, ...) and a `web.py` web editor (~32KB).
- `site-manager` — `skills/configurator/cli/` — 8-command deployment CLI (cli, deploy, verify, verify_all, e2e, dns_check, repair, status, test, manifest, check, claude).
- `webinator` — `skills/webinitor/cli/` — 11-command-group web infra CLI (api, config, configure, deploy, dns, domains, status).

**Test harness:** `claude-skills-tester-cli/` — copies `harness/` (package.json, vitest config, tsconfig, lib/assertions.ts, lib/fixtures.ts, lib/runner.ts), `fixtures/`, and `specs/` into a disposable sandbox at `../dev-tools-tests` (or `$TEST_SANDBOX`), runs `npm install` + `npx vitest run`, prints `cost-report.json` if present.

## Claude Configuration

- `.claude/CLAUDE.md` — Lists the skills and documents the git workflow: "All work must be done in worktree branches and merged back into main via PR. Use EnterWorktree to create feature branches. Never commit directly to main."
- `.claude/settings.json` — Enables `superpowers@claude-plugins-official` plugin.
- No local `rules/`, `hooks/`, or `agents/` directories under `.claude/`.
- Gitignored: `.claude/worktrees/`, `.claude/settings.local.json`, `.superpowers/`.

## Planning & Research Documents

**`docs/project/description.md`** — Standardized project description (per the my-projects-overview rollout). Confirms Python 3.11+, uv-based build, status: Active development.

**`docs/planning/planning.md`** — Placeholder (`(to be determined)`).

**`docs/research/`:**
- `claude-code-plugins.md` (2026-04-02) — Comprehensive reference on Claude Code plugin structure: `plugin.json`, SKILL.md frontmatter, the three loading methods (`--plugin-dir`, local marketplace, GitHub marketplace), plugin scopes (user/project/local), hooks, environment variables (`${CLAUDE_SKILL_DIR}`, `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`), and known gotchas.
- `cli-packaging.md` (2026-04-06, Status: Decided) — Rationale for `uv tool install -e` as the packaging approach. Covers why Python was kept over Swift/Go/Rust, and why `uv` beat shell wrappers, pip editable installs, and single-file scripts. Notes that site-manager (~620 lines) and webinator (~780 lines) are glue CLIs that mostly shell out to `railway`, `wrangler`, `claude`, `gh`, and hit GoDaddy/Cloudflare via stdlib `urllib`.

**`docs/superpowers/plans/` + `specs/`** — Dated (2026-04-05 through 2026-04-09) implementation plans and design specs:
- site-manager v1, smoke tests, add-and-deploy fix
- webinitor v2 (design + plan)
- init flow philosophy + existing-site-init (with a `init-flow.png` diagram)
- configurator web editor (2026-04-09)

## Git History & Current State

- **Remote:** `git@github.com:agentic-cookbook/dev-tools.git` (org: `agentic-cookbook`)
- **Current branch:** `main`
- **Working tree:** clean
- **Total commits:** 7 (new repo — scaffolded 2026-04-10)

Full log:
```
d3217f6 Update configurator to v1.29.0 from cat-herding branch
246f530 Remove build artifacts and add them to .gitignore
7086c78 Add web-view skill for rendering markdown as local web pages
4d457c8 fix: update stale cat-herding references in test runner
4857319 Move claude-skills-tester-cli and plugins research from cat-herding
8a71e7a Move 6 skills from cat-herding into dev-tools
05f7c92 Initial project scaffolding
```

The history shows `dev-tools` was carved out of `cat-herding` on 2026-04-10 — the initial 6 skills plus the test harness were migrated, then `web-view` was added and `configurator` was upgraded to v1.29.0.

## Build & Test Commands

**Install skills and CLIs:**
```bash
./install.sh
```
Creates symlinks in `~/.claude/skills/` for each directory in `skills/`, then runs `uv tool install -e <cli-dir>` for every `pyproject.toml` found at `skills/*/*/pyproject.toml` (installs: `configurator`, `site-manager`, `webinator`).

**Uninstall:**
```bash
./uninstall.sh
```
Removes the matching symlinks and runs `uv tool uninstall` for each managed CLI.

**Run skill tests (TypeScript/vitest harness):**
```bash
./claude-skills-tester-cli/run.sh [vitest-args]
# or
TEST_SANDBOX=/path/to/sandbox ./claude-skills-tester-cli/run.sh
```
Default sandbox is `../dev-tools-tests` (resolved via `git rev-parse --git-common-dir` so it works from worktrees). Harness cleans the sandbox (preserving `.git`, `node_modules`, `research`), copies `harness/` + `fixtures/` + `specs/`, runs `npm install`, then `npx vitest run`.

**Python CLI dev loop:** Edits under `skills/*/cli*/src/**` are live immediately (editable installs). Reinstall is only needed when `pyproject.toml` entry points or dependencies change, or when the repo moves on disk.

**Debug a CLI via module:**
```bash
PYTHONPATH=skills/webinitor/cli/src python3 -m webinator domains list
```

No linter, formatter, or CI config is committed in the repo.

## Notes

- The repo is the new home for skills and CLIs that previously lived in `cat-herding` — history of the migration is visible in the 7-commit log, and the research doc on CLI packaging (originally written for the old layout) still references `cli/site-manager/` and `cli/webinator/` rather than the current `skills/configurator/cli/` and `skills/webinitor/cli/` layout.
- Skill directory naming is slightly inconsistent with the SKILL.md `name:` fields: the directory is `webinitor` but the CLI and skill reference the name `webinator`; the directory is `configurator` and ships two CLIs (`configurator` for config authoring, `site-manager` for deployment execution).
- Both shipped shell scripts (`install.sh`, `uninstall.sh`) are the only bash in the repo — consistent with the global exception allowing install/uninstall scripts to remain shell.
- `configurator`'s `features/` module (20+ files) is the largest body of code in the repo and suggests the configurator CLI is the flagship component — the skill itself is ~67KB and at v1.29.0, dwarfing every other skill by size and version.
- The test harness under `claude-skills-tester-cli/harness/` is TypeScript, making it the only non-Python code in the repo. It is designed to run against a sibling sandbox directory and publishes a `cost-report.json` if the vitest suite produces one.
- `docs/planning/planning.md` is still a stub — no forward-looking roadmap is committed yet.
- The `.gitignore` excludes `.superpowers/`, `uv.lock`, `build/`, `*.egg-info/`, and `__pycache__/`, though some `__pycache__` and `*.egg-info/` directories are still present on disk under `skills/webinitor/cli/src/` (already-tracked artifacts from before they were ignored — see commit `246f530`).
