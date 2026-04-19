import json
import subprocess
import sys
from pathlib import Path


def test_gather_single_project():
    """Script gathers info for a known project and outputs valid JSON."""
    result = subprocess.run(
        [sys.executable, "scripts/generate_description_drafts.py",
         "--project", "myprojectsoverview", "--json"],
        capture_output=True, text=True, cwd=str(Path(__file__).parent.parent),
    )
    assert result.returncode == 0, "stderr: %s" % result.stderr
    data = json.loads(result.stdout)
    assert data["name"] == "myprojectsoverview"
    assert "remote_url" in data
    assert "tech_stack" in data
    assert isinstance(data["tech_stack"], list)


def test_gather_all_projects():
    """Script gathers info for all projects."""
    result = subprocess.run(
        [sys.executable, "scripts/generate_description_drafts.py", "--json"],
        capture_output=True, text=True, cwd=str(Path(__file__).parent.parent),
    )
    assert result.returncode == 0, "stderr: %s" % result.stderr
    data = json.loads(result.stdout)
    assert isinstance(data, list)
    assert len(data) >= 20
    names = [p["name"] for p in data]
    assert "catherding" in names
