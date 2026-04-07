# mysetup Project Overview

## Project Summary

**mysetup** is a comprehensive macOS and Windows 11 (WSL) development environment setup automation project. It provides declarative machine configuration (via `setup.md`), 20+ utility scripts, shell configuration, and Claude Code plugin orchestration to streamline developer workflows.

**Type**: Development Infrastructure / Automation Tool Suite  
**Status**: Active (last update: April 6, 2026)

---

## Type & Tech Stack

### Project Type
- **Infrastructure Automation**: Shell scripts, Python utilities, and declarative configuration management
- **macOS/WSL Installer**: Cross-platform setup with platform detection
- **CLI Utility Collection**: 20+ executable scripts for git, file operations, development tasks
- **Claude Code Integration**: Setup skill for configuring Claude Code plugins

### Technology Stack
- **Shell**: Bash, Zsh (oh-my-zsh configuration)
- **Languages**: Bash/Shell scripting, Python 3
- **Build/Config**: Homebrew (taps, packages, casks), npm, pip, git, gh (GitHub CLI)
- **Key Dependencies**:
  - Node.js (installed via Homebrew)
  - Python 3 + uv (package manager)
  - Java (openjdk@17, openjdk@21)
  - Gradle
  - GitHub CLI (`gh`)
  - VS Code
  - Docker/Android Studio (via Homebrew casks)
  - Xcode/xcodegen (macOS)

### Project Types Handled
The setup script manages three categories of projects:
1. **Active Projects**: Regular repos in `~/projects/` (mikefullerton.com, mikeisdrumming, code-review-pipeline-test, workflows)
2. **Worktree Projects**: Bare repos with worktree directories (QualityTime, temporal)
3. **Config Repos**: Repos that have their own `install.sh` (dotfiles)

---

## GitHub URL

```
https://github.com/mikefullerton/mysetup
SSH: git@github.com:mikefullerton/mysetup.git
```

---

## Directory Structure

```
mysetup/
├── .claude/                           # Claude Code configuration
│   ├── CLAUDE.md                      # Project rules (branches, worktrees, PRs)
│   ├── settings.local.json            # Permissions (git, chmod, gh pr commands)
│   ├── Features/                      # Feature tracking directories (empty)
│   │   ├── Active-Roadmaps/
│   │   ├── Completed-Features/
│   │   ├── Completed-Roadmaps/
│   │   └── FeatureDefinitions/
│   └── worktrees/                     # Git worktrees for feature branches
├── .vscode/                           # VS Code workspace configuration
│   └── templates/
├── bin/                               # 20+ executable utility scripts
│   ├── lib/                           # Python library modules (11 files)
│   │   ├── check_installed_software.py
│   │   ├── git_branch.py, git_branch_manager.py
│   │   ├── git_commands.py, git_checkout_history.py
│   │   ├── shell_command.py
│   │   ├── menu.py, logger.py, text_color.py
│   │   ├── files.py, script_manager.py, prefs.py
│   │   └── script_collection.py
│   ├── utils/                         # Shell utility functions
│   │   ├── colors.sh
│   │   ├── dispatcher.sh
│   │   ├── cd-wrapper.sh
│   │   └── set-prompt.sh
│   ├── catherine                      # Complex script (referenced in permissions)
│   ├── git-branches                   # List branches by commit date
│   ├── git-mypush, git-mypull         # Custom git push/pull wrappers
│   ├── git-myfpush                    # Safe force-push wrapper
│   ├── git-force-update               # Interactive rebase helper
│   ├── git-import-directory-from-another-repo
│   ├── git-set-to-github-repo         # Git config for GitHub repos
│   ├── split-out-links                # HTML/webloc link extraction (with Playwright)
│   ├── split-out-links-python-only    # Link extraction (Python only)
│   ├── open_workspace                 # Opens .xcworkspace/.xcodeproj/.code-workspace
│   ├── change-type                    # Batch file extension rename
│   ├── copy-folder                    # Rsync wrapper with exclusions
│   ├── delete-orig-files              # Recursive .orig file removal
│   ├── list-to-json                   # Convert text list to JSON
│   ├── mytop                          # Top processes by CPU (5s refresh)
│   ├── st                             # Open in SourceTree
│   ├── mysetup                        # List all available scripts
│   ├── snag.py                        # iOS app image cache exporter
│   └── clone_impal.py                 # Copy impal from mounted volumes
├── setup_files/                       # Config files & resources
│   ├── mikefullerton.zsh-theme        # Custom oh-my-zsh theme
│   ├── tab-title-hook.zsh             # Shell tab title configuration
│   ├── silence.aiff                   # Audio file
│   ├── teddy.png                      # Image resource
│   ├── License files                  # Kaleidoscope, Sublime Text, Alfred
│   └── Other config files
├── manifests/                         # Declarative state files
│   ├── Brewfile                       # Homebrew dependencies
│   ├── npm-globals.txt                # npm global packages
│   ├── pip-globals.txt                # pip global packages
│   ├── vscode-extensions.txt          # VS Code extension list
│   └── software.md                    # Inventory of installed software
├── skills/                            # Claude Code skills
│   └── setup/                         # Main setup skill
│       ├── SKILL.md                   # Setup skill definition
│       └── references/                # Reference implementations
├── deprecated/                        # 100+ archived scripts/utilities
│   ├── bin/                           # Old script directory
│   ├── commapps/                      # Legacy application scripts
│   ├── bats_bin/                      # Old build system
│   └── Various legacy tools
├── install.sh                         # Main setup script (1243 lines, v29)
├── uninstall.sh                       # Removes shell config without uninstalling software
├── setup.md                           # Declarative manifest (version 28)
├── README.md                          # User-facing documentation
├── mysetup.code-workspace             # VS Code workspace file
├── .gitignore                         # Excludes .worktrees/, .DS_Store
├── .gitattributes                     # Git attributes
├── .DS_Store                          # macOS folder metadata (ignored)
└── .git/                              # Git repository metadata
```

---

## Key Files & Components

### Core Scripts

| File | Description | Lines | Language |
|------|-------------|-------|----------|
| **install.sh** | Main setup automation | 1243 | Bash |
| **uninstall.sh** | Remove shell config | 3938 | Bash |
| **setup.md** | Declarative manifest (version 28) | 130 | YAML/Markdown |
| **README.md** | User documentation | 150 | Markdown |

### Git-Related Scripts
- `git-branches`: List branches by commit date with metadata
- `git-mypush` / `git-mypull` / `git-myfpush`: Custom wrappers with branch safety
- `git-force-update`: Blocks force-push to `main`; allows to other branches after rebase
- `git-import-directory-from-another-repo`: Preserve subdirectory history across repos
- `git-set-to-github-repo`: Configure git email and disable GPG signing

### Python Libraries (bin/lib/)
- `shell_command.py` (20KB): Wrapper for running bash commands from Python
- `git_branch.py` (11KB): Git branch inspection utilities
- `git_branch_manager.py` (10KB): Branch creation, switching, deletion
- `git_commands.py` (8KB): High-level git operations
- `check_installed_software.py`: Verify tool installation
- `menu.py`, `logger.py`, `text_color.py`: UI/logging utilities
- `files.py`, `script_manager.py`, `prefs.py`: File and script management

### Setup Skill (Claude Code Integration)
- **File**: `skills/setup/SKILL.md` (100+ lines)
- **Invocation**: `/setup`, `/setup --check`, `/setup --section <name>`
- **Features**:
  - Declarative state management from `setup.md`
  - Dry-run mode with `--check`
  - Section-specific execution
  - Platform detection (macOS/WSL/Linux)
  - Multi-phase processing: Shell → Homebrew → npm/pip → Extensions → Git → Repos → Project Scripts

### Manifests
- **Brewfile**: Taps (koekeishiya, steipete, felixkratz, asmvik, antoniorodr), packages, casks
- **npm-globals.txt**: openclaw, wrangler
- **pip-globals.txt**: pillow, Pygments, fonttools, fpdf2, pytest
- **vscode-extensions.txt**: GitHub Actions, Python, Pylance, envs
- **software.md**: Inventory of 50+ tools (developer + personal categories)

---

## Claude Configuration

### CLAUDE.md (Project Rules)
```
- Always use branches and PRs (no direct main commits)
- Always use worktrees for feature/fix branches
- Worktree directory: .claude/worktrees/
- Use: git worktree add .claude/worktrees/<name> to isolate work
```

### settings.local.json (Permissions)
Allowed operations for Claude agents:
- `Bash(git add:*)` — Stage changes
- `Bash(git commit:*)` — Create commits
- `Bash(git push)` — Push to remote
- `Bash(git checkout:*)` — Switch branches
- `Bash(git push:*)` — Force push (with safeguards)
- `Bash(chmod:*)` — Change file permissions
- `Bash(/Volumes/Data/myscripts/bin/catherine:*)` — Run catherine script
- `Bash(gh pr:*)` — GitHub PR operations

### Features Directory
- **Active-Roadmaps/**: Currently planned work (empty)
- **Completed-Features/**: Finished work history (empty)
- **Completed-Roadmaps/**: Finished roadmaps (empty)
- **FeatureDefinitions/**: Feature spec templates (empty)

---

## Planning & Research Documents

### setup.md (Version 28, Declarative Manifest)

**Key Sections:**
1. **Shell Configuration**
   - Default: zsh with oh-my-zsh
   - Theme: Custom `mikefullerton.zsh-theme`
   - PATH entries: `~/projects/active/mysetup/bin`, `~/.local/bin`
   - Aliases: git shortcuts (ga, gc, gs, gl, gpush, gpull, gfpush, co, gnb, gcb), claude-yolo/cy
   - Tab title hook from `setup_files/tab-title-hook.zsh`
   - Environment variables checked: CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID

2. **Homebrew Configuration**
   - Taps: antoniorodr/memo, asmvik/formulae (yabai), felixkratz/formulae (sketchybar), koekeishiya/formulae (skhd), steipete/tap
   - Core packages: node, gh, gradle, jq, openjdk@{17,21}, railway, socat, terminal-notifier, uv, xcodegen
   - Casks: Android Studio, visual-studio-code, Tailscale, darktable, digikam, Font packages
   - Tap packages: yabai, sketchybar, skhd, remindctl, memo

3. **Development Tools**
   - npm globals: openclaw, wrangler
   - pip globals: pillow, Pygments, fonttools, fpdf2, pytest
   - Node.js, Java (17/21), Gradle

4. **Projects**
   - **Active Projects**: mikefullerton.com, mikeisdrumming, code-review-pipeline-test, workflows
   - **Worktree Projects**: QualityTime, temporal
   - **Config Repos**: dotfiles (with install.sh)

5. **Repos Section** (from install.sh)
   - Active projects clone to `~/projects/` as regular repos
   - Worktree projects clone as bare repos with sibling `-wt/` directory
   - Bare repo usage: `git worktree add ../<name>-wt/<branch> -b <branch>`

6. **Claude Code Plugins** (from setup.md + README.md)
   - Core: playwright, figma, frontend-design, context7, semgrep
   - Workflow: superpowers, code-review, pr-review-toolkit, playground
   - Authoring: plugin-dev, agent-sdk-dev, hookify
   - Installation scope: user (via `claude plugin install <name> --scope user`)

### install.sh (v29, 1243 lines)

**Platform Detection:**
- Detects macOS, WSL, or Linux via `uname -s` and `/proc/version`
- Filters installation by platform markers (macOS), (WSL), (linux)

**Key Functions:**
- `detect_platform()`: Returns "macos", "wsl", or "linux"
- `is_macos()`, `is_wsl()`, `is_linux()`: Platform checks
- Batch tool scanning and installation with dependency ordering
- Deprecated tool cleanup (removes old tools)
- Project setup scripts execution (runs `install.sh` in cloned projects if present)

**Project Configuration:**
```bash
ACTIVE_PROJECTS=(
    "mikefullerton.com|git@github.com:mikefullerton/mikefullerton.com.git"
    "mikeisdrumming|git@github.com:mikefullerton/mikeisdrumming.git"
    "code-review-pipeline-test|git@github.com:Shared-Project-Helpers/code-review-pipeline-test.git"
    "workflows|git@github.com:Shared-Project-Helpers/workflows.git"
)

WORKTREE_PROJECTS=(
    "QualityTime|git@github.com:QualityTimeStudios/QualityTime.git"
    "temporal|git@github.com:temporal-company/temporal.git"
)
```

### Skills/Setup Skill (SKILL.md)

**Invocation:**
- `/setup` — Run all sections
- `/setup --check` — Dry-run, report what's installed vs. missing
- `/setup --section "Homebrew Packages"` — Run specific section

**Processing Order:**
1. Shell (zsh, oh-my-zsh, theme, PATH, aliases, env vars)
2. Homebrew Taps
3. Homebrew Packages
4. Homebrew Tap Packages
5. Homebrew Casks
6. Winget Packages (WSL only)
7. npm Global Packages
8. pip Global Packages
9. VS Code Extensions
10. Claude Code Plugins
11. Git Config
12. Repos (Active → Worktree → Config)
13. Project Setup Scripts

**Status Reporting:** OK, INSTALL, SKIP, FAIL, WARN prefixes with summary at end.

---

## Git History & Current State

### Recent Activity (Last 5 Commits)
```
2026-04-06 17:19:17 -0700  chore: update project paths to ~/projects/active/mysetup
2026-04-06 16:18:11 -0700  chore: standardize worktree directory to .claude/worktrees/
2026-03-31 10:53:23 -0700  remove extra stuff for now
2026-03-31 10:45:33 -0700  Merge pull request #24 from mikefullerton/remove-config-repos
2026-03-31 10:45:00 -0700  chore: remove claude-config and agentic-roadmaps from setup
```

### Historical Context (Last 30 Commits)
- **Recent refactorings**: Moving Claude Code install to claude-config, worktree directory standardization, removing deprecated plugins
- **Feature work**: Declarative setup.md manifest, /setup skill implementation (Phase 1), plugin prerequisites detection, enhanced plugin setup
- **Cleanup**: Removed custom hooks, removed Claude plugins installation from setup, standardized project paths

### Current State
- **Branch**: main
- **Status**: Clean (nothing to commit, working tree clean)
- **Remote**: Up to date with origin/main
- **Other branches**: remove-deprecated (appears to be cleaning up old code)

### Branch Structure
- **main**: Primary development branch (fully synced with remote)
- **remove-deprecated**: Cleanup branch (removing old scripts from `deprecated/` directory)
- **Remote**: origin/main, origin/remove-deprecated

---

## Build & Test Commands

### Installation
```bash
# Full setup (all sections)
./install.sh

# Check mode (dry-run, report missing)
/setup --check

# Specific section
/setup --section "Homebrew Packages"

# Uninstall (removes shell config without uninstalling software)
./uninstall.sh
```

### Available Scripts
```bash
# List all scripts
./bin/mysetup

# Git operations
git-branches              # List branches by commit date
git-mypush               # Push current branch
git-mypull               # Pull with rebase
git-myfpush              # Force push (non-main only)
git-force-update         # Interactive rebase helper

# File operations
change-type              # Batch rename by extension
copy-folder              # rsync with progress
delete-orig-files        # Remove .orig files
list-to-json             # Convert text to JSON

# Link extraction
split-out-links          # Extract from HTML/webloc (with Playwright)
split-out-links-python-only  # Extract (Python only)

# Utilities
open_workspace           # Open .xcworkspace / .code-workspace
mytop                    # Top processes (5s refresh)
st                       # Open in SourceTree
catherine                # Complex utility script
snag.py                  # Export iOS app image caches
clone_impal.py           # Copy impal from volumes
```

### No Traditional Build
This is not a compiled project. Installation is shell-script driven via `install.sh` and `setup.md` manifest processing.

### Testing
- **No test framework** visible (no test/ or specs/ directory)
- Manual testing via `./install.sh` or `/setup --check`
- Feature branches use worktrees to avoid main pollution

---

## Notes

### Architecture & Design Patterns

**Declarative Configuration:**
- `setup.md` is the source of truth (version 28)
- `/setup` skill converges machine state toward declared manifest
- Supports dry-run (`--check`) and section-specific execution
- Platform detection enables cross-platform automation (macOS/WSL/Linux)

**Modular Script Collection:**
- 20+ focused scripts in `bin/`, each with single responsibility
- Python library in `bin/lib/` provides reusable utilities (git, menus, logging, shell commands)
- Shell utilities in `bin/utils/` for colors, dispatcher, prompt configuration

**Project Management:**
- **Active Projects**: Regular clones in `~/projects/`
- **Worktree Projects**: Bare repos with sibling `-wt/` worktree directory (keeps main clean)
- **Config Repos**: Repos with their own `install.sh` (dotfiles example)
- Automatic repo fetching and worktree updates on each run

**Claude Code Integration:**
- Setup skill provides declarative `/setup` command
- Permissions in `settings.local.json` allow git, chmod, gh operations
- Project rules enforce branches + PRs + worktrees (never main commits)
- Feature tracking via `.claude/Features/` directories

### Known Issues & Cleanup
- **deprecated/** directory contains 100+ old scripts (remove-deprecated branch planned cleanup)
- Feature/roadmap directories in `.claude/Features/` are empty (infrastructure ready, not populated)
- `.DS_Store` tracked (macOS metadata) but rules should ignore

### Interesting Characteristics
- **Cross-platform installer**: Single `install.sh` handles macOS, WSL, and Linux with platform detection
- **Worktree strategy**: Bare repos prevent main branch pollution; worktree per feature branch
- **Declarative manifest**: `setup.md` decouples desired state from implementation; skill reads and converges
- **Rich git utilities**: Multiple custom git wrappers simplify branch management, force push safety, and rebase workflows
- **Software inventory**: Dual lists (Developer vs. Personal) track 50+ installed tools
- **Homebrew ecosystem**: Manages 5 custom taps (yabai, sketchybar, skhd, remindctl, memo) for specialized macOS tooling

### Project Goals (Inferred)
1. **Reproducible setup**: Run `./install.sh` on new Mac/WSL to get full environment
2. **Developer ergonomics**: Custom aliases, scripts, and utilities for daily workflows
3. **Clean branching model**: Worktrees + PRs prevent main pollution
4. **AI-assisted development**: Claude Code plugins (superpowers, code-review, etc.) integrated into workflow
5. **Modular, maintainable tooling**: Each script focused; library for shared logic

### Version History
- **setup.md**: v28 (as of Apr 6, 2026)
- **install.sh**: v29 (29 in SETUP_VERSION constant)
- **Skills**: v1 (setup skill)
- **Project**: 85 commits, active main branch

---

## Contact & License

**Author**: Mike Fullerton  
**Email**: mike@mikefullerton.com  
**Git User**: Mike Fullerton (configured in setup.md)

---

**Document Generated**: 2026-04-07  
**Project Last Updated**: 2026-04-06  
**Git Commit**: 2d68011 (chore: update project paths)
