# cookbook-tests

## Project Summary

An external test harness for the Agentic Cookbook, using Vitest and TypeScript. Contains test specs for cookbook features (lint rules, optimization rules), test fixtures, a shared test runner/assertion library, and research findings (cc-plugin-eval evaluation). Separated from the cookbook repo to keep tests independent. Also includes research on the cc-plugin-eval framework and why it doesn't fit the cookbook's skill testing needs.

## Type & Tech Stack

- **Type**: Test harness (external, for agentic-cookbook/cookbook)
- **Language**: TypeScript (ES modules)
- **Test framework**: Vitest 3.2.1
- **Runtime**: Node.js
- **Build**: npm (package.json, private)

## GitHub URL

`git@github.com:agentic-cookbook/cookbook-tests.git`

## Directory Structure

```
cookbook-tests/
├── fixtures/
│   ├── lint-rule/                   # Lint rule test fixtures
│   └── optimize-rules/             # Optimization rule fixtures
├── lib/
│   ├── assertions.ts               # Shared test assertions
│   ├── fixtures.ts                 # Fixture loading utilities
│   └── runner.ts                   # Test runner helpers
├── research/
│   └── cc-plugin-eval-findings.md  # cc-plugin-eval evaluation
├── specs/
│   ├── lint-rule.test.ts           # Lint rule tests
│   └── optimize-rules.test.ts     # Optimization rule tests
├── node_modules/                    # Dependencies (untracked)
├── package.json                     # Project config (vitest dependency)
├── package-lock.json               # Lock file (untracked)
├── tsconfig.json                   # TypeScript config
├── vitest.config.ts                # Vitest configuration
└── .gitignore
```

## Key Files & Components

- `package.json` -- Name: "agentic-cookbook-test-harness", private, ES modules, Vitest 3.2.1, scripts: test, test:watch
- `specs/lint-rule.test.ts` -- Tests for cookbook lint rule functionality
- `specs/optimize-rules.test.ts` -- Tests for cookbook optimization rules
- `lib/runner.ts` -- Shared test runner for executing cookbook skills
- `lib/assertions.ts` -- Custom assertions for cookbook test validation
- `lib/fixtures.ts` -- Fixture loading and management utilities
- `fixtures/` -- Test fixture directories (lint-rule, optimize-rules)
- `research/cc-plugin-eval-findings.md` -- Evaluation of cc-plugin-eval framework for cookbook testing

## Claude Configuration

- No CLAUDE.md or `.claude/` directory
- No project-level Claude configuration

## Planning & Research Documents

- `research/cc-plugin-eval-findings.md` -- Evaluates the cc-plugin-eval framework (sjnims/cc-plugin-eval): a 4-stage evaluation framework for Claude Code marketplace plugins. Concludes it doesn't fit the cookbook's needs because it requires `.claude-plugin/plugin.json` manifest (cookbook uses project-local `.claude/skills/` instead) and only tests trigger activation, not functional correctness.

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "chore: add .gitignore"
- **Working tree**: 8 untracked items (fixtures/, lib/, node_modules/, package-lock.json, package.json, specs/, tsconfig.json, vitest.config.ts)
- **Total commits**: 2
- **Recent activity**: Initial research findings (Mar 2026), gitignore added (Apr 2026)
- **Note**: Most source files are untracked -- only research and gitignore are committed

## Build & Test Commands

```bash
# Install dependencies
npm install

# Run tests
npm test              # vitest run
npm run test:watch    # vitest (watch mode)
```

## Notes

- Owned by "agentic-cookbook" GitHub org
- Most source code is still untracked (only 2 commits: research findings and gitignore)
- The test harness is designed to run cookbook skills externally via a runner.ts wrapper
- cc-plugin-eval was evaluated and rejected because cookbook skills are project-local, not marketplace plugins
- Very early stage -- the test infrastructure exists locally but hasn't been fully committed
