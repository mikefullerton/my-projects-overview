#!/usr/bin/env python3
"""Tests for scan_projects.py."""

import json
import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from scan_projects import (
    _parse_existing_categories,
    _parse_package_json,
    _parse_pyproject_toml,
    build_tree,
    detect_tech,
    diff_projects,
    discover_projects,
    gather_claude_config,
    gather_docs,
    gather_git,
    generate_template,
    read_file_safe,
    regenerate_index,
    scan_all,
    scan_project,
)


@pytest.fixture
def tmp_project(tmp_path):
    """Create a minimal project directory with git repo."""
    project = tmp_path / "test-project"
    project.mkdir()
    subprocess.run(["git", "init", str(project)], capture_output=True)
    subprocess.run(
        ["git", "-C", str(project), "config", "user.email", "test@test.com"],
        capture_output=True,
    )
    subprocess.run(
        ["git", "-C", str(project), "config", "user.name", "Test"],
        capture_output=True,
    )
    (project / "README.md").write_text("# Test Project\nA test.")
    subprocess.run(
        ["git", "-C", str(project), "add", "."], capture_output=True,
    )
    subprocess.run(
        ["git", "-C", str(project), "commit", "-m", "initial"],
        capture_output=True,
    )
    return project


@pytest.fixture
def tmp_projects_dir(tmp_path):
    """Create a projects directory with several project dirs."""
    projects = tmp_path / "projects"
    projects.mkdir()
    (projects / "alpha").mkdir()
    (projects / "bravo").mkdir()
    (projects / "charlie-tests").mkdir()
    (projects / "my-projects-overview").mkdir()
    (projects / ".hidden").mkdir()
    return projects


# --- discover_projects ---


class TestDiscoverProjects:
    def test_basic_discovery(self, tmp_projects_dir):
        result = discover_projects(tmp_projects_dir)
        assert "alpha" in result
        assert "bravo" in result

    def test_skips_tests_suffix(self, tmp_projects_dir):
        result = discover_projects(tmp_projects_dir)
        assert "charlie-tests" not in result

    def test_skips_overview_repo(self, tmp_projects_dir):
        result = discover_projects(tmp_projects_dir)
        assert "my-projects-overview" not in result

    def test_skips_hidden(self, tmp_projects_dir):
        result = discover_projects(tmp_projects_dir)
        assert ".hidden" not in result

    def test_sorted(self, tmp_projects_dir):
        result = discover_projects(tmp_projects_dir)
        assert result == sorted(result)

    def test_nonexistent_dir(self, tmp_path):
        result = discover_projects(tmp_path / "nonexistent")
        assert result == []

    def test_skips_files(self, tmp_projects_dir):
        (tmp_projects_dir / "not-a-dir.txt").write_text("hi")
        result = discover_projects(tmp_projects_dir)
        assert "not-a-dir.txt" not in result


# --- diff_projects ---


class TestDiffProjects:
    def test_all_new(self, tmp_path):
        existing = tmp_path / "existing"
        existing.mkdir()
        new, removed, updated = diff_projects(["a", "b"], existing)
        assert new == ["a", "b"]
        assert removed == []
        assert updated == []

    def test_all_existing(self, tmp_path):
        existing = tmp_path / "existing"
        existing.mkdir()
        (existing / "a").mkdir()
        (existing / "b").mkdir()
        new, removed, updated = diff_projects(["a", "b"], existing)
        assert new == []
        assert removed == []
        assert updated == ["a", "b"]

    def test_mixed(self, tmp_path):
        existing = tmp_path / "existing"
        existing.mkdir()
        (existing / "a").mkdir()
        (existing / "old").mkdir()
        new, removed, updated = diff_projects(["a", "b"], existing)
        assert new == ["b"]
        assert removed == ["old"]
        assert updated == ["a"]

    def test_nonexistent_existing_dir(self, tmp_path):
        new, removed, updated = diff_projects(
            ["a"], tmp_path / "nope",
        )
        assert new == ["a"]


# --- gather_git ---


class TestGatherGit:
    def test_with_git_repo(self, tmp_project):
        result = gather_git(tmp_project)
        assert result["branch"] == "main" or result["branch"] == "master"
        assert result["clean"] is True
        assert len(result["recent_commits"]) >= 1
        assert result["recent_commits"][0]["message"] == "initial"

    def test_dirty_repo(self, tmp_project):
        (tmp_project / "new_file.txt").write_text("dirty")
        result = gather_git(tmp_project)
        assert result["clean"] is False
        assert len(result["dirty_files"]) > 0

    def test_no_git(self, tmp_path):
        project = tmp_path / "no-git"
        project.mkdir()
        result = gather_git(project)
        assert result["remote_url"] is None
        assert result["branch"] is None
        assert result["clean"] is None

    def test_org_parsing(self, tmp_project):
        subprocess.run(
            ["git", "-C", str(tmp_project), "remote", "add", "origin",
             "git@github.com:testorg/testrepo.git"],
            capture_output=True,
        )
        result = gather_git(tmp_project)
        assert result["org"] == "testorg"
        assert result["remote_url"] == "git@github.com:testorg/testrepo.git"


# --- detect_tech ---


class TestDetectTech:
    def test_node_project(self, tmp_path):
        project = tmp_path / "node-proj"
        project.mkdir()
        pkg = {
            "dependencies": {"react": "^19.2.4", "vite": "^8.0.0"},
            "devDependencies": {"typescript": "^5.0.0"},
            "scripts": {"build": "vite build", "dev": "vite"},
        }
        (project / "package.json").write_text(json.dumps(pkg))
        result = detect_tech(project)
        assert result["type"] == "node"
        assert result["language"] == "TypeScript"
        assert "React 19" in result["frameworks"]
        assert "Vite" in result["frameworks"]
        assert result["scripts"]["build"] == "vite build"

    def test_python_project(self, tmp_path):
        project = tmp_path / "py-proj"
        project.mkdir()
        (project / "pyproject.toml").write_text(
            '[project]\nname = "foo"\n\n[project.dependencies]\nflask = ">=3.0"\nclick = ">=8.0"\n'
        )
        result = detect_tech(project)
        assert result["type"] == "python"
        assert result["language"] == "Python"

    def test_swift_project(self, tmp_path):
        project = tmp_path / "swift-proj"
        project.mkdir()
        (project / "Package.swift").write_text("// swift-tools-version: 5.9")
        result = detect_tech(project)
        assert result["type"] == "swift"
        assert result["language"] == "Swift"

    def test_unknown_project(self, tmp_path):
        project = tmp_path / "mystery"
        project.mkdir()
        result = detect_tech(project)
        assert result["type"] == "unknown"

    def test_deployment_detection(self, tmp_path):
        project = tmp_path / "cf-proj"
        project.mkdir()
        (project / "package.json").write_text('{"dependencies":{}}')
        (project / "wrangler.jsonc").write_text("{}")
        result = detect_tech(project)
        assert result["deployment"] == "Cloudflare Workers"

    def test_node_js_detection(self, tmp_path):
        project = tmp_path / "js-proj"
        project.mkdir()
        (project / "package.json").write_text('{"dependencies":{"express":"^4.0"}}')
        result = detect_tech(project)
        assert result["language"] == "JavaScript"
        assert "Express" in result["frameworks"]

    def test_typescript_via_tsconfig(self, tmp_path):
        project = tmp_path / "ts-proj"
        project.mkdir()
        (project / "package.json").write_text('{"dependencies":{}}')
        (project / "tsconfig.json").write_text("{}")
        result = detect_tech(project)
        assert result["language"] == "TypeScript"


# --- build_tree ---


class TestBuildTree:
    def test_basic_tree(self, tmp_path):
        project = tmp_path / "proj"
        project.mkdir()
        (project / "src").mkdir()
        (project / "src" / "main.py").write_text("")
        (project / "README.md").write_text("")
        tree = build_tree(project)
        assert "src/" in tree
        assert "main.py" in tree
        assert "README.md" in tree

    def test_excludes_node_modules(self, tmp_path):
        project = tmp_path / "proj"
        project.mkdir()
        (project / "node_modules").mkdir()
        (project / "node_modules" / "foo").mkdir()
        tree = build_tree(project)
        assert "node_modules" not in tree

    def test_depth_limit(self, tmp_path):
        project = tmp_path / "proj"
        d = project
        for name in ["a", "b", "c", "d", "e"]:
            d = d / name
            d.mkdir(parents=True)
            (d / "file.txt").write_text("")
        tree = build_tree(project, max_depth=2)
        # Should show a/ and a/b/ but not deeper files
        assert "a/" in tree
        assert "b/" in tree


# --- gather_docs ---


class TestGatherDocs:
    def test_root_docs(self, tmp_path):
        project = tmp_path / "proj"
        project.mkdir()
        (project / "README.md").write_text("# Hello")
        (project / "CLAUDE.md").write_text("# Rules")
        docs, planning = gather_docs(project)
        assert docs["README.md"] == "# Hello"
        assert docs["CLAUDE.md"] == "# Rules"
        assert planning == {}

    def test_missing_docs(self, tmp_path):
        project = tmp_path / "proj"
        project.mkdir()
        docs, planning = gather_docs(project)
        assert docs["README.md"] is None
        assert docs["CLAUDE.md"] is None

    def test_planning_docs(self, tmp_path):
        project = tmp_path / "proj"
        project.mkdir()
        (project / "docs").mkdir()
        (project / "docs" / "plan.md").write_text("# Plan")
        docs, planning = gather_docs(project)
        assert "docs/plan.md" in planning
        assert planning["docs/plan.md"] == "# Plan"


# --- gather_claude_config ---


class TestGatherClaudeConfig:
    def test_no_claude_dir(self, tmp_path):
        project = tmp_path / "proj"
        project.mkdir()
        result = gather_claude_config(project)
        assert result["rules"] == []
        assert result["skills"] == []

    def test_with_rules(self, tmp_path):
        project = tmp_path / "proj"
        rules_dir = project / ".claude" / "rules"
        rules_dir.mkdir(parents=True)
        (rules_dir / "always-test.md").write_text("Always test")
        result = gather_claude_config(project)
        assert len(result["rules"]) == 1
        assert result["rules"][0]["content"] == "Always test"

    def test_with_skills(self, tmp_path):
        project = tmp_path / "proj"
        skill_dir = project / ".claude" / "skills" / "my-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text("# My Skill")
        result = gather_claude_config(project)
        assert len(result["skills"]) == 1

    def test_with_settings(self, tmp_path):
        project = tmp_path / "proj"
        claude_dir = project / ".claude"
        claude_dir.mkdir(parents=True)
        (claude_dir / "settings.json").write_text('{"key": "value"}')
        result = gather_claude_config(project)
        assert result["settings"]["settings.json"] == {"key": "value"}


# --- generate_template ---


class TestGenerateTemplate:
    def test_basic_template(self):
        git = {
            "remote_url": "git@github.com:org/repo.git",
            "branch": "main", "clean": True,
            "last_commit_date": "2026-04-07",
            "recent_commits": [
                {"hash": "abc1234", "date": "2026-04-07", "message": "feat: init"},
            ],
        }
        tech = {
            "type": "node", "language": "TypeScript",
            "frameworks": ["React 19"], "dependencies": {"react": "^19.0"},
            "scripts": {"build": "vite build"}, "deployment": None,
        }
        template = generate_template(
            "my-app", git, tech, "├── src/\n└── package.json",
            {"README.md": "# My App", "CLAUDE.md": None},
            {}, {"rules": [], "skills": [], "settings": {}, "commands": []},
        )
        assert "# my-app" in template
        assert "<!-- LLM:" in template
        assert "React 19" in template
        assert "git@github.com:org/repo.git" in template
        assert "abc1234" in template
        assert "vite build" in template

    def test_template_no_scripts(self):
        git = {
            "remote_url": None, "branch": None, "clean": None,
            "last_commit_date": None, "recent_commits": [],
        }
        tech = {
            "type": "unknown", "language": None,
            "frameworks": [], "dependencies": {},
            "scripts": {}, "deployment": None,
        }
        template = generate_template(
            "empty", git, tech, "", {}, {},
            {"rules": [], "skills": [], "settings": {}, "commands": []},
        )
        assert "No build scripts detected." in template
        assert "None configured." in template


# --- read_file_safe ---


class TestReadFileSafe:
    def test_read_normal(self, tmp_path):
        f = tmp_path / "test.txt"
        f.write_text("hello\nworld\n")
        assert read_file_safe(f) == "hello\nworld\n"

    def test_read_max_lines(self, tmp_path):
        f = tmp_path / "test.txt"
        f.write_text("a\nb\nc\nd\ne\n")
        result = read_file_safe(f, max_lines=2)
        assert result == "a\nb\n"

    def test_read_nonexistent(self, tmp_path):
        assert read_file_safe(tmp_path / "nope.txt") is None


# --- _parse_existing_categories ---


class TestParseExistingCategories:
    def test_parses_categories(self, tmp_path):
        index = tmp_path / "index.md"
        index.write_text(
            "## macOS Native Apps\n\n"
            "| [Foo](projects/foo/overview.md) | A foo | Swift |\n"
            "| [Bar](projects/bar/overview.md) | A bar | Swift |\n\n"
            "## Web Apps\n\n"
            "| [Baz](projects/baz/overview.md) | A baz | React |\n"
        )
        result = _parse_existing_categories(index)
        assert result["macOS Native Apps"] == ["foo", "bar"]
        assert result["Web Apps"] == ["baz"]

    def test_nonexistent_file(self, tmp_path):
        result = _parse_existing_categories(tmp_path / "nope.md")
        assert result == {}

    def test_skips_quick_reference(self, tmp_path):
        index = tmp_path / "index.md"
        index.write_text(
            "## Apps\n\n"
            "| [A](projects/a/overview.md) | ... |\n\n"
            "## Quick Reference\n\n"
            "stuff\n"
        )
        result = _parse_existing_categories(index)
        assert "Quick Reference" not in result
        assert "Apps" in result


# --- scan_project ---


class TestScanProject:
    def test_scan_basic(self, tmp_project):
        result = scan_project("test-project", tmp_project)
        assert "git" in result
        assert "tech" in result
        assert "template_md" in result
        assert "# test-project" in result["template_md"]

    def test_scan_with_package_json(self, tmp_path):
        project = tmp_path / "node-proj"
        project.mkdir()
        subprocess.run(["git", "init", str(project)], capture_output=True)
        (project / "package.json").write_text(
            '{"dependencies":{"react":"^19.0"},"scripts":{"build":"vite build"}}'
        )
        result = scan_project("node-proj", project)
        assert result["tech"]["type"] == "node"
        assert "React 19" in result["tech"]["frameworks"]


# --- scan_all ---


class TestScanAll:
    def test_scan_single_project(self, tmp_project):
        projects_dir = tmp_project.parent
        subdir = projects_dir / "overviews"
        subdir.mkdir()
        result = scan_all(projects_dir, subdir, single_project="test-project")
        assert "test-project" in result["projects"]
        assert result["new"] == ["test-project"]

    def test_scan_single_not_found(self, tmp_path):
        result = scan_all(tmp_path, tmp_path / "sub", single_project="nonexistent")
        assert "error" in result

    def test_scan_all_projects(self, tmp_path):
        projects_dir = tmp_path / "projects"
        projects_dir.mkdir()
        (projects_dir / "alpha").mkdir()
        (projects_dir / "bravo").mkdir()
        subdir = tmp_path / "overviews"
        subdir.mkdir()
        (subdir / "alpha").mkdir()
        result = scan_all(projects_dir, subdir)
        assert "alpha" in result["projects"]
        assert "bravo" in result["projects"]
        assert result["existing"] == ["alpha"]
        assert result["new"] == ["bravo"]


# --- regenerate_index ---


class TestRegenerateIndex:
    def test_generates_index(self, tmp_path):
        projects_subdir = tmp_path / "projects"
        (projects_subdir / "foo").mkdir(parents=True)
        (projects_subdir / "foo" / "overview.md").write_text(
            "# Foo App\n\n## Project Summary\nA foo application.\n\n"
            "## Type & Tech Stack\n- **Language:** Python\n- **Frameworks:** Flask\n\n"
            "## GitHub URL\n`git@github.com:testorg/foo.git`\n"
        )
        index_file = tmp_path / "index.md"
        regenerate_index(projects_subdir, index_file)
        content = index_file.read_text()
        assert "Foo App" in content
        assert "A foo application." in content
        assert "testorg" in content

    def test_preserves_categories(self, tmp_path):
        projects_subdir = tmp_path / "projects"
        (projects_subdir / "foo").mkdir(parents=True)
        (projects_subdir / "foo" / "overview.md").write_text(
            "# Foo\n\n## Project Summary\nFoo thing.\n\n"
            "## Type & Tech Stack\n- **Language:** Python\n\n"
            "## GitHub URL\n`git@github.com:org/foo.git`\n"
        )
        index_file = tmp_path / "index.md"
        index_file.write_text(
            "## My Category\n\n"
            "| [Foo](projects/foo/overview.md) | Old summary | Python |\n"
        )
        regenerate_index(projects_subdir, index_file)
        content = index_file.read_text()
        assert "## My Category" in content

    def test_new_project_uncategorized(self, tmp_path):
        projects_subdir = tmp_path / "projects"
        (projects_subdir / "bar").mkdir(parents=True)
        (projects_subdir / "bar" / "overview.md").write_text(
            "# Bar\n\n## Project Summary\nBar thing.\n\n"
            "## Type & Tech Stack\n- **Language:** Rust\n\n"
            "## GitHub URL\n`git@github.com:org/bar.git`\n"
        )
        index_file = tmp_path / "index.md"
        # No existing index
        regenerate_index(projects_subdir, index_file)
        content = index_file.read_text()
        assert "## Uncategorized" in content
        assert "Bar" in content


# --- CLI integration ---


class TestCLI:
    def test_help(self):
        result = subprocess.run(
            ["python3", str(Path(__file__).parent / "scan_projects.py"), "--help"],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        assert "scan" in result.stdout.lower() or "project" in result.stdout.lower()

    def test_scan_with_override(self, tmp_path):
        projects_dir = tmp_path / "projects"
        projects_dir.mkdir()
        (projects_dir / "demo").mkdir()
        overview_repo = tmp_path / "repo"
        overview_repo.mkdir()
        (overview_repo / "projects").mkdir()

        result = subprocess.run(
            [
                "python3", str(Path(__file__).parent / "scan_projects.py"),
                "--projects-dir", str(projects_dir),
                "--overview-repo", str(overview_repo),
            ],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert "demo" in data["projects"]
        assert data["new"] == ["demo"]

    def test_regenerate_index_cli(self, tmp_path):
        overview_repo = tmp_path / "repo"
        projects_subdir = overview_repo / "projects" / "foo"
        projects_subdir.mkdir(parents=True)
        (projects_subdir / "overview.md").write_text(
            "# Foo\n\n## Project Summary\nA foo.\n\n"
            "## Type & Tech Stack\n- **Language:** Go\n\n"
            "## GitHub URL\n`git@github.com:org/foo.git`\n"
        )

        result = subprocess.run(
            [
                "python3", str(Path(__file__).parent / "scan_projects.py"),
                "--regenerate-index",
                "--overview-repo", str(overview_repo),
            ],
            capture_output=True, text=True,
        )
        assert result.returncode == 0
        index_content = (overview_repo / "index.md").read_text()
        assert "Foo" in index_content
