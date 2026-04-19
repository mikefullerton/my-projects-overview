# My Projects Overview

A central index of all active projects, providing structured overviews and a browsable HTML site for Claude to reference.

## Purpose

This project keeps track of all the projects being worked on across `~/projects/active/` and provides a comprehensive index for Claude Code to reference. It auto-generates detailed overview files (tech stack, directory structure, git history, build commands) for each project and publishes them as a static HTML site.

It solves the problem of Claude needing context about the broader project ecosystem — which repos exist, what they do, how they relate, and what state they're in.

## Key Features

- Deterministic project scanner (`scripts/scan_projects.py`) that gathers tech stack, git info, docs, and directory structure
- Per-project `overview.md` files with structured, machine-readable content
- Static HTML site generation under `site/` for browsable project index
- Categorized index (`index.md`) grouping projects by domain (macOS apps, web apps, tools, etc.)
- Draft-generation script (`scripts/generate_description_drafts.py`) for standardizing project descriptions

## Tech Stack

- **Language:** Python 3.9+
- **Build/Test:** pytest
- **Site:** Static HTML generated from markdown

## Status

Active development — index and overviews are regenerated regularly as projects evolve.

## Related Projects

- All projects in `~/projects/active/` are tracked by this project
- [My Projects](../../myprojects/docs/project/description.md) — a separate web dashboard for project management
