# Local Server Apps Layer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a second tier (`~/.local-server/apps/`) alongside `sites/` for permanent, curated applications whose source lives outside `~/.local-server`. Ship `my-projects-overview` as the first app to validate the mechanism end-to-end.

**Architecture:** Each app is declared by a single JSON manifest in `~/.local-server/apps/`. The manifest points at a built static directory anywhere on disk. On startup, `site_manager.py` loads every manifest, validates it, and registers a Caddy route via the Caddy admin API (`localhost:2019`) that serves the app's static root at `dev.local/<id>/`. The landing page fetches both apps and sites and renders them as separate sections. MVP is **static-only** — backend supervision is deliberately out of scope and documented as a follow-up.

**Tech Stack:** Python 3 (stdlib only, matches `site_manager.py` conventions), Caddy admin API (HTTP/JSON), Vite + React 19 (home page), standard `urllib.request` for Caddy calls.

**Repo scope:**
- **devtools-web-server** — core mechanism (manifest loader, Caddy client, site_manager integration, home page UI)
- **my-projects-overview** — pilot app (Vite base path, prebuild script for static data, manifest file)

---

## Design Decisions (locked in)

1. **Apps are pointers, not copies.** Manifest's `static_root` field is an absolute path to a directory somewhere on disk. Caddy reads it in place.
2. **MVP is static-only.** No backend supervision in v1. `my-projects-overview` uses a prebuild step that bakes `projects.json` from `scan_projects.py` output into `site/dist/`. Backend proxying is a Phase 3 follow-up.
3. **Caddy routes are added via the admin API**, not by editing the Caddyfile. Routes are ephemeral — re-created on each `site_manager` startup from the manifests, which are the source of truth.
4. **Route pattern:** `https://dev.local/<app-id>/*` → file_server rooted at `static_root`. `<app-id>` collides with `sites/<app-id>` — apps take precedence by being registered with higher route priority.
5. **Manifest location:** `~/.local-server/apps/<app-id>.json` (flat directory of JSON files, not subdirectories).
6. **No hot reload.** Edit a manifest → restart `site_manager` (via launchd) to pick up changes. Document this clearly.

## Manifest Schema (v1)

```json
{
  "id": "projects-overview",
  "title": "Projects Overview",
  "description": "Dashboard of all ~/projects repos with overview.md metadata",
  "static_root": "/Users/mfullerton/projects/my-projects-overview/site/dist",
  "source_repo": "/Users/mfullerton/projects/my-projects-overview"
}
```

**Required fields:** `id`, `title`, `static_root`
**Optional fields:** `description`, `source_repo` (informational, shown on home page)
**Reserved for future:** `backend` (object; ignored in v1)

## File Structure

### devtools-web-server (new + modified files)

- **Create** `site-template/apps_registry.py` — `AppManifest` dataclass + `AppRegistry` class that loads and validates `~/.local-server/apps/*.json`. Isolated from `site_manager.py` so it can be tested in isolation.
- **Create** `site-template/caddy_admin.py` — small client for the Caddy admin API (`localhost:2019`). Only the calls we need: `add_route`, `remove_route`, `list_routes`. stdlib only.
- **Create** `site-template/tests/test_apps_registry.py` — unit tests for manifest loading, validation, and error handling.
- **Create** `site-template/tests/test_caddy_admin.py` — unit tests for route payload generation (no live Caddy required; use a stub HTTP server).
- **Modify** `site-template/site_manager.py` — on startup, instantiate `AppRegistry`, load manifests, call `caddy_admin.add_route` for each app, expose new `GET /_api/apps` endpoint. Extend existing `GET /_api/sites` response OR add a combined `GET /_api/registry` (decision: keep `/_api/apps` separate; home page fetches both).
- **Modify** `home-page/src/App.tsx` (or equivalent) — fetch `/_api/apps` in parallel with `/_api/sites`, render two sections.
- **Modify** `site-template/browse.html` OR the home-page build output — add "Apps" section.
- **Modify** `README.md` and `~/.local-server/instructions.md` — document the apps layer, manifest schema, and static-only limitation.

### my-projects-overview (new + modified files)

- **Create** `scripts/build_static_site.py` — wraps `scan_projects.py` + `npm run build`. Produces `site/dist/` with `projects.json` baked into `public/` before the Vite build copies it.
- **Create** `site/public/.gitkeep` (if needed) — Vite serves `public/` as static assets.
- **Modify** `site/vite.config.js` — add `base: '/projects-overview/'` so built asset URLs are prefixed correctly.
- **Modify** `site/src/hooks/useProjects.ts` — fetch `./projects.json` (relative, resolves to `/projects-overview/projects.json`) instead of `/api/projects`. Fall back behavior: none — if the file is missing, show an error. This replaces the Node API server entirely for the deployed build.
- **Modify** `site/src/hooks/useProjects.test.ts` — update mock fetch target.
- **Create** `site/src/lib/projectsData.ts` — parser for the baked `projects.json` shape (same shape the Node server currently returns, so the React code barely changes).
- **Delete** nothing — `server/server.js` stays around for local dev (`npm run dev` with Vite proxy still works if you run `node server/server.js` manually).

### ~/.local-server (manifest drop)

- **Create** `~/.local-server/apps/projects-overview.json` — the pilot manifest. This file is NOT committed to any repo (it lives in the user's local server dir), but the plan documents its exact contents.

---

## Phase 1: Core mechanism (devtools-web-server)

> **Worktree:** Create a worktree in `~/projects/devtools-web-server` via `EnterWorktree` before starting.

### Task 1: Create `AppManifest` dataclass and failing validation test

**Files:**
- Create: `site-template/apps_registry.py`
- Create: `site-template/tests/test_apps_registry.py`

- [ ] **Step 1: Write the failing test**

```python
# site-template/tests/test_apps_registry.py
import json
import pytest
from pathlib import Path
from apps_registry import AppManifest, ManifestError


def test_manifest_loads_minimal_valid_json(tmp_path):
    manifest_file = tmp_path / "foo.json"
    manifest_file.write_text(json.dumps({
        "id": "foo",
        "title": "Foo",
        "static_root": str(tmp_path),
    }))
    m = AppManifest.from_file(manifest_file)
    assert m.id == "foo"
    assert m.title == "Foo"
    assert m.static_root == Path(tmp_path)
    assert m.description == ""
    assert m.source_repo is None


def test_manifest_rejects_missing_required_field(tmp_path):
    manifest_file = tmp_path / "bad.json"
    manifest_file.write_text(json.dumps({"id": "bad", "title": "Bad"}))
    with pytest.raises(ManifestError, match="static_root"):
        AppManifest.from_file(manifest_file)


def test_manifest_rejects_nonexistent_static_root(tmp_path):
    manifest_file = tmp_path / "foo.json"
    manifest_file.write_text(json.dumps({
        "id": "foo",
        "title": "Foo",
        "static_root": "/does/not/exist",
    }))
    with pytest.raises(ManifestError, match="static_root.*not exist"):
        AppManifest.from_file(manifest_file)


def test_manifest_rejects_id_mismatch(tmp_path):
    manifest_file = tmp_path / "foo.json"
    manifest_file.write_text(json.dumps({
        "id": "bar",  # filename is foo.json but id is bar
        "title": "Bar",
        "static_root": str(tmp_path),
    }))
    with pytest.raises(ManifestError, match="id.*filename"):
        AppManifest.from_file(manifest_file)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/projects/devtools-web-server/site-template && python3 -m pytest tests/test_apps_registry.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'apps_registry'`

- [ ] **Step 3: Implement `AppManifest`**

```python
# site-template/apps_registry.py
"""Load and validate app manifests from ~/.local-server/apps/."""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


class ManifestError(ValueError):
    """Raised when an app manifest is invalid."""


@dataclass
class AppManifest:
    id: str
    title: str
    static_root: Path
    description: str = ""
    source_repo: Optional[Path] = None

    @classmethod
    def from_file(cls, path: Path) -> "AppManifest":
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError) as e:
            raise ManifestError(f"{path.name}: cannot read JSON: {e}") from e

        if not isinstance(data, dict):
            raise ManifestError(f"{path.name}: top-level must be an object")

        for required in ("id", "title", "static_root"):
            if required not in data:
                raise ManifestError(f"{path.name}: missing required field '{required}'")

        expected_id = path.stem
        if data["id"] != expected_id:
            raise ManifestError(
                f"{path.name}: 'id' ({data['id']!r}) must match filename ({expected_id!r})"
            )

        static_root = Path(data["static_root"]).expanduser()
        if not static_root.exists():
            raise ManifestError(
                f"{path.name}: static_root does not exist: {static_root}"
            )
        if not static_root.is_dir():
            raise ManifestError(
                f"{path.name}: static_root is not a directory: {static_root}"
            )

        source_repo = data.get("source_repo")
        if source_repo is not None:
            source_repo = Path(source_repo).expanduser()

        return cls(
            id=data["id"],
            title=data["title"],
            static_root=static_root,
            description=data.get("description", ""),
            source_repo=source_repo,
        )
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd ~/projects/devtools-web-server/site-template && python3 -m pytest tests/test_apps_registry.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add site-template/apps_registry.py site-template/tests/test_apps_registry.py
git commit -m "feat(apps): add AppManifest dataclass with validation"
```

---

### Task 2: Add `AppRegistry` loader with directory scanning

**Files:**
- Modify: `site-template/apps_registry.py`
- Modify: `site-template/tests/test_apps_registry.py`

- [ ] **Step 1: Add failing registry tests**

```python
# Append to tests/test_apps_registry.py
from apps_registry import AppRegistry


def test_registry_loads_all_valid_manifests(tmp_path):
    apps_dir = tmp_path / "apps"
    apps_dir.mkdir()
    root_a = tmp_path / "a"
    root_a.mkdir()
    root_b = tmp_path / "b"
    root_b.mkdir()
    (apps_dir / "alpha.json").write_text(json.dumps({
        "id": "alpha", "title": "Alpha", "static_root": str(root_a),
    }))
    (apps_dir / "beta.json").write_text(json.dumps({
        "id": "beta", "title": "Beta", "static_root": str(root_b),
    }))

    reg = AppRegistry(apps_dir)
    reg.load()
    apps = reg.list_all()
    assert len(apps) == 2
    assert {a.id for a in apps} == {"alpha", "beta"}


def test_registry_skips_invalid_and_reports_errors(tmp_path):
    apps_dir = tmp_path / "apps"
    apps_dir.mkdir()
    (apps_dir / "good.json").write_text(json.dumps({
        "id": "good", "title": "Good", "static_root": str(tmp_path),
    }))
    (apps_dir / "bad.json").write_text("not json")

    reg = AppRegistry(apps_dir)
    reg.load()
    assert len(reg.list_all()) == 1
    assert reg.list_all()[0].id == "good"
    assert len(reg.errors) == 1
    assert "bad.json" in reg.errors[0]


def test_registry_handles_missing_directory(tmp_path):
    reg = AppRegistry(tmp_path / "does-not-exist")
    reg.load()
    assert reg.list_all() == []
    assert reg.errors == []


def test_registry_ignores_non_json_files(tmp_path):
    apps_dir = tmp_path / "apps"
    apps_dir.mkdir()
    (apps_dir / "README.md").write_text("not a manifest")
    (apps_dir / ".DS_Store").write_bytes(b"")
    reg = AppRegistry(apps_dir)
    reg.load()
    assert reg.list_all() == []
    assert reg.errors == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/projects/devtools-web-server/site-template && python3 -m pytest tests/test_apps_registry.py -v`
Expected: 4 new tests FAIL with `ImportError: cannot import name 'AppRegistry'`

- [ ] **Step 3: Implement `AppRegistry`**

Append to `site-template/apps_registry.py`:

```python
class AppRegistry:
    """Loads and holds AppManifest instances from a directory."""

    def __init__(self, apps_dir: Path):
        self.apps_dir = apps_dir
        self._apps: dict[str, AppManifest] = {}
        self.errors: list[str] = []

    def load(self) -> None:
        self._apps.clear()
        self.errors.clear()
        if not self.apps_dir.is_dir():
            return
        for path in sorted(self.apps_dir.iterdir()):
            if not path.is_file() or path.suffix != ".json":
                continue
            try:
                manifest = AppManifest.from_file(path)
            except ManifestError as e:
                self.errors.append(str(e))
                continue
            self._apps[manifest.id] = manifest

    def list_all(self) -> list[AppManifest]:
        return list(self._apps.values())

    def get(self, app_id: str) -> Optional[AppManifest]:
        return self._apps.get(app_id)
```

- [ ] **Step 4: Run all registry tests**

Run: `cd ~/projects/devtools-web-server/site-template && python3 -m pytest tests/test_apps_registry.py -v`
Expected: 8 passed

- [ ] **Step 5: Commit**

```bash
git add site-template/apps_registry.py site-template/tests/test_apps_registry.py
git commit -m "feat(apps): add AppRegistry with directory scanning"
```

---

### Task 3: Caddy admin API client (route payload generation)

**Files:**
- Create: `site-template/caddy_admin.py`
- Create: `site-template/tests/test_caddy_admin.py`

- [ ] **Step 1: Write the failing test**

```python
# site-template/tests/test_caddy_admin.py
from caddy_admin import build_app_route


def test_build_app_route_static_only():
    route = build_app_route(
        app_id="projects-overview",
        static_root="/Users/mike/projects/my-projects-overview/site/dist",
    )
    assert route["@id"] == "app-projects-overview"
    assert route["match"] == [{"path": ["/projects-overview/*"]}]
    handle = route["handle"]
    assert len(handle) == 1
    subroute = handle[0]
    assert subroute["handler"] == "subroute"
    # Must strip the /projects-overview prefix, then file_server from static_root
    strip = subroute["routes"][0]["handle"][0]
    assert strip["handler"] == "rewrite"
    assert strip["strip_path_prefix"] == "/projects-overview"
    fs = subroute["routes"][0]["handle"][1]
    assert fs["handler"] == "file_server"
    assert fs["root"] == "/Users/mike/projects/my-projects-overview/site/dist"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd ~/projects/devtools-web-server/site-template && python3 -m pytest tests/test_caddy_admin.py -v`
Expected: FAIL with `ModuleNotFoundError`

- [ ] **Step 3: Implement `build_app_route`**

```python
# site-template/caddy_admin.py
"""Minimal Caddy admin API client for the apps layer.

Generates Caddy route JSON and installs it via the admin endpoint at
localhost:2019. stdlib only.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

CADDY_ADMIN = "http://localhost:2019"


def build_app_route(app_id: str, static_root: str) -> dict[str, Any]:
    """Build a Caddy route that serves an app's static bundle at /<id>/*.

    The route strips the /<id> prefix before handing off to file_server so
    the built index.html and assets resolve correctly.
    """
    prefix = f"/{app_id}"
    return {
        "@id": f"app-{app_id}",
        "match": [{"path": [f"{prefix}/*"]}],
        "handle": [
            {
                "handler": "subroute",
                "routes": [
                    {
                        "handle": [
                            {
                                "handler": "rewrite",
                                "strip_path_prefix": prefix,
                            },
                            {
                                "handler": "file_server",
                                "root": static_root,
                            },
                        ]
                    }
                ],
            }
        ],
    }
```

- [ ] **Step 4: Run test**

Run: `cd ~/projects/devtools-web-server/site-template && python3 -m pytest tests/test_caddy_admin.py -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add site-template/caddy_admin.py site-template/tests/test_caddy_admin.py
git commit -m "feat(apps): add Caddy route payload builder"
```

---

### Task 4: Install and remove routes via Caddy admin API

**Files:**
- Modify: `site-template/caddy_admin.py`
- Modify: `site-template/tests/test_caddy_admin.py`

- [ ] **Step 1: Add failing tests for install/remove against a stub HTTP server**

```python
# Append to tests/test_caddy_admin.py
import http.server
import json as _json
import threading
from unittest.mock import patch

import pytest
from caddy_admin import install_route, remove_route, CaddyAdminError


class _Stub(http.server.BaseHTTPRequestHandler):
    received: list[dict] = []

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(length).decode()
        self.received.append({
            "method": "POST",
            "path": self.path,
            "body": _json.loads(body) if body else None,
        })
        self.send_response(200)
        self.end_headers()

    def do_DELETE(self):
        self.received.append({"method": "DELETE", "path": self.path})
        self.send_response(200)
        self.end_headers()

    def log_message(self, *args, **kwargs):
        pass


@pytest.fixture
def stub_caddy():
    _Stub.received = []
    server = http.server.HTTPServer(("127.0.0.1", 0), _Stub)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    yield f"http://127.0.0.1:{port}", _Stub
    server.shutdown()


def test_install_route_posts_to_caddy(stub_caddy):
    admin_url, stub = stub_caddy
    route = {"@id": "app-foo", "match": [], "handle": []}
    with patch("caddy_admin.CADDY_ADMIN", admin_url):
        install_route(route)
    assert len(stub.received) == 1
    assert stub.received[0]["method"] == "POST"
    assert stub.received[0]["path"] == "/config/apps/http/servers/srv0/routes"
    assert stub.received[0]["body"] == route


def test_remove_route_by_id(stub_caddy):
    admin_url, stub = stub_caddy
    with patch("caddy_admin.CADDY_ADMIN", admin_url):
        remove_route("app-foo")
    assert len(stub.received) == 1
    assert stub.received[0]["method"] == "DELETE"
    assert stub.received[0]["path"] == "/id/app-foo"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd ~/projects/devtools-web-server/site-template && python3 -m pytest tests/test_caddy_admin.py -v`
Expected: 2 new tests FAIL with `ImportError`

- [ ] **Step 3: Implement install/remove**

Append to `site-template/caddy_admin.py`:

```python
class CaddyAdminError(RuntimeError):
    """Raised when a Caddy admin API call fails."""


def _http(method: str, url: str, payload: dict | None = None) -> None:
    data = _json_dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={"Content-Type": "application/json"} if data else {},
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status >= 300:
                raise CaddyAdminError(f"{method} {url}: HTTP {resp.status}")
    except urllib.error.URLError as e:
        raise CaddyAdminError(f"{method} {url}: {e}") from e


def _json_dumps(obj: Any) -> str:
    return json.dumps(obj)


def install_route(route: dict) -> None:
    """POST a route to the first HTTP server's routes list."""
    _http(
        "POST",
        f"{CADDY_ADMIN}/config/apps/http/servers/srv0/routes",
        payload=route,
    )


def remove_route(route_id: str) -> None:
    """DELETE a route by its @id."""
    _http("DELETE", f"{CADDY_ADMIN}/id/{route_id}")
```

- [ ] **Step 4: Run tests**

Run: `cd ~/projects/devtools-web-server/site-template && python3 -m pytest tests/test_caddy_admin.py -v`
Expected: 3 passed

- [ ] **Step 5: Verify the Caddyfile srv0 assumption**

Run: `curl -s http://localhost:2019/config/apps/http/servers/ | python3 -m json.tool | head -20`
Expected: a JSON object with a key (probably `srv0`) containing a `routes` array. If the key isn't `srv0`, update `install_route`'s URL accordingly. Document the actual server key.

- [ ] **Step 6: Commit**

```bash
git add site-template/caddy_admin.py site-template/tests/test_caddy_admin.py
git commit -m "feat(apps): install and remove routes via Caddy admin API"
```

---

### Task 5: Wire `AppRegistry` into `site_manager.py` startup

**Files:**
- Modify: `site-template/site_manager.py`

- [ ] **Step 1: Read current startup code**

Run: `grep -n "def main\|APPS_DIR\|SITES_DIR" site-template/site_manager.py`
Expected: find the `main()` function and any existing path constants.

- [ ] **Step 2: Add manifest loading to startup**

Near the top of `site_manager.py`, next to the existing `SITES_DIR` constant, add:

```python
APPS_DIR = Path.home() / ".local-server" / "apps"
```

Import the new modules at the top:

```python
from apps_registry import AppRegistry
from caddy_admin import build_app_route, install_route, remove_route, CaddyAdminError
```

In `main()` (or wherever the HTTP server is set up), before the server starts listening, add:

```python
app_registry = AppRegistry(APPS_DIR)
app_registry.load()
for err in app_registry.errors:
    log_event("app_manifest_error", "-", {"error": err})
for app in app_registry.list_all():
    try:
        # Clean stale route first (idempotent across restarts)
        try:
            remove_route(f"app-{app.id}")
        except CaddyAdminError:
            pass
        install_route(build_app_route(app.id, str(app.static_root)))
        log_event("app_registered", app.id, {"static_root": str(app.static_root)})
    except CaddyAdminError as e:
        log_event("app_register_failed", app.id, {"error": str(e)})
```

Store `app_registry` on the handler class (or module global) so endpoints can access it in Task 6.

- [ ] **Step 3: Manual smoke test with a fake app**

```bash
mkdir -p ~/.local-server/apps
mkdir -p /tmp/fake-app
echo '<html><body>hello from fake-app</body></html>' > /tmp/fake-app/index.html
cat > ~/.local-server/apps/fake-app.json <<EOF
{"id":"fake-app","title":"Fake","static_root":"/tmp/fake-app"}
EOF
brew services restart local-server.site-manager  # or however it's launched
curl -sL http://localhost:2080/fake-app/
```

Expected: `<html><body>hello from fake-app</body></html>`

- [ ] **Step 4: Tear down fake app**

```bash
rm ~/.local-server/apps/fake-app.json
rm -rf /tmp/fake-app
brew services restart local-server.site-manager
```

- [ ] **Step 5: Commit**

```bash
git add site-template/site_manager.py
git commit -m "feat(apps): load manifests and register Caddy routes on startup"
```

---

### Task 6: Expose `GET /_api/apps` endpoint

**Files:**
- Modify: `site-template/site_manager.py`

- [ ] **Step 1: Find the existing routing table**

Run: `grep -n "_api\|sites\|handle_\|do_GET" site-template/site_manager.py | head -30`
Expected: locate where `/_api/sites` is handled.

- [ ] **Step 2: Add `/_api/apps` handler beside `/_api/sites`**

Follow the exact pattern used for `/_api/sites`. The response is a JSON list:

```python
# In the GET handler, alongside the existing /_api/sites branch:
if self.path == "/_api/apps":
    apps = [
        {
            "id": a.id,
            "title": a.title,
            "description": a.description,
            "static_root": str(a.static_root),
            "source_repo": str(a.source_repo) if a.source_repo else None,
            "url": f"/{a.id}/",
        }
        for a in app_registry.list_all()
    ]
    self._respond_json(200, apps)
    return
```

Use whatever helper (`_respond_json` or equivalent) the existing sites endpoint uses — **do not invent new response helpers**.

- [ ] **Step 3: Manual test**

```bash
# with fake-app manifest in place from Task 5, or a fresh one
curl -s http://localhost:2080/_api/apps | python3 -m json.tool
```

Expected: JSON list with one entry for fake-app.

- [ ] **Step 4: Commit**

```bash
git add site-template/site_manager.py
git commit -m "feat(apps): add GET /_api/apps endpoint"
```

---

### Task 7: Home page — render apps section

**Files:**
- Modify: `~/.local-server/home/` source (Vite React app). Locate the source repo first:

- [ ] **Step 1: Locate the home page source**

Run: `grep -rn "Local Sites\|useSites\|_api/sites" ~/projects/devtools-web-server 2>/dev/null | head`
Expected: find the source directory (likely `devtools-web-server/home-page/` or similar).

- [ ] **Step 2: Add `useApps` hook**

Create a new hook alongside the existing `useSites`:

```typescript
// src/hooks/useApps.ts
import { useEffect, useState } from "react";

export interface AppEntry {
  id: string;
  title: string;
  description: string;
  url: string;
  source_repo: string | null;
}

export function useApps() {
  const [apps, setApps] = useState<AppEntry[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/_api/apps")
      .then((r) => {
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
        return r.json();
      })
      .then((data: AppEntry[]) => {
        setApps(data);
        setLoading(false);
      })
      .catch((e) => {
        setError(String(e));
        setLoading(false);
      });
  }, []);

  return { apps, loading, error };
}
```

- [ ] **Step 3: Render the Apps section in `App.tsx`**

Add a new section ABOVE the existing Sites section, with a distinct heading:

```tsx
import { useApps } from "./hooks/useApps";

// inside App():
const { apps } = useApps();

// in the JSX, before the Sites section:
{apps.length > 0 && (
  <section className="apps-section">
    <h2>Apps <span className="tag">permanent</span></h2>
    <ul className="app-list">
      {apps.map((a) => (
        <li key={a.id}>
          <a href={a.url}>{a.title}</a>
          {a.description && <p>{a.description}</p>}
        </li>
      ))}
    </ul>
  </section>
)}
```

Match the existing styling conventions — do not introduce a new design language.

- [ ] **Step 4: Build and copy to ~/.local-server/home**

Run the home page's existing build+deploy script (grep history for how it's currently built). Verify:

```bash
curl -s http://localhost:2080/ | grep -i apps
```

Expected: the page source contains "apps" in the rendered React output.

- [ ] **Step 5: Commit**

```bash
git add home-page/src/hooks/useApps.ts home-page/src/App.tsx
git commit -m "feat(home): render apps section alongside sites"
```

---

### Task 8: Document the apps layer

**Files:**
- Modify: `~/.local-server/instructions.md` (bump the version in the devtools-web-server template source that installs it)
- Modify: `devtools-web-server/README.md`

- [ ] **Step 1: Append "Complex Sites (Apps)" section to instructions.md**

```markdown
## Complex Sites (Apps)

For sites that need to live outside `~/.local-server/sites/` — typically a
real repo with its own build process — use the apps layer instead.

1. Build the site's static bundle wherever its source lives. The output
   directory must contain an `index.html` at its root.
2. Drop a manifest in `~/.local-server/apps/<id>.json`:

    ```json
    {
      "id": "<id>",
      "title": "<Human-readable name>",
      "description": "<one-line description>",
      "static_root": "/absolute/path/to/built/dist",
      "source_repo": "/absolute/path/to/repo"
    }
    ```

3. Restart the site manager to register the route:

    ```bash
    brew services restart local-server.site-manager
    ```

4. Visit `https://dev.local/<id>/`.

**v1 limitations:**
- Static bundles only. Apps that need a live backend must run it themselves;
  there is no per-app backend supervisor in v1.
- No hot reload on manifest change. Edit → restart site manager.
- The Vite/bundler base path in the source project must match `/<id>/` so
  asset URLs resolve. For Vite this is `base: '/<id>/'` in `vite.config.js`.
```

- [ ] **Step 2: Sync to live**

Run the existing instruction-sync command (grep for it) or manually copy to `~/.local-server/instructions.md`.

- [ ] **Step 3: Commit**

```bash
git add site-template/instructions.md README.md  # or wherever it lives
git commit -m "docs(apps): document the apps layer and v1 limitations"
```

---

### Task 9: Finish the worktree (Phase 1)

- [ ] **Step 1: Push and open PR**

```bash
git push -u origin worktree-<branch-name>
gh pr create --title "feat: add apps layer to ~/.local-server" --body "$(cat <<'EOF'
## Summary

Adds a permanent-apps tier to ~/.local-server alongside the existing
ephemeral sites tier. Apps are declared by JSON manifests in
~/.local-server/apps/ and reference source repos in place — no copying
into the local server directory.

v1 is static-only; backend supervision is deferred to a future phase.

## Test plan

- [x] Unit tests for AppRegistry, AppManifest, caddy_admin
- [ ] Smoke test: fake-app manifest serves hello world
- [ ] Smoke test: /_api/apps returns registered apps
- [ ] Home page renders Apps section
EOF
)"
```

- [ ] **Step 2: Merge and clean up**

After review:

```bash
gh pr merge --squash --delete-branch
# back in main worktree:
ExitWorktree (action: remove)
```

---

## Phase 2: Migrate my-projects-overview as the first app

> **Worktree:** This repo now opts into worktree-workflow-rule. Create a worktree in `~/projects/my-projects-overview` via `EnterWorktree` before starting.

### Task 10: Vite base path + smoke test a local build

**Files:**
- Modify: `site/vite.config.js`

- [ ] **Step 1: Set the base path**

```js
// site/vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  base: '/projects-overview/',
  server: {
    port: 5174,
    proxy: {
      '/api': 'http://localhost:3457'
    }
  },
  test: {
    environment: 'jsdom',
  }
});
```

- [ ] **Step 2: Build and inspect**

```bash
cd site && npm run build
grep -o '/projects-overview/assets/[^"]*' dist/index.html | head
```

Expected: asset URLs prefixed with `/projects-overview/`.

- [ ] **Step 3: Commit**

```bash
git add site/vite.config.js
git commit -m "build(site): set vite base path to /projects-overview/"
```

---

### Task 11: Prebuild script that bakes `projects.json`

**Files:**
- Create: `scripts/build_static_site.py`
- Modify: `site/package.json` (add `prebuild` script)

- [ ] **Step 1: Write the prebuild script**

```python
#!/usr/bin/env python3
"""Bake projects.json into site/public/ so the Vite build picks it up.

Reuses scan_projects.py's scanning logic but emits a single JSON file
in the shape the React app expects (list of {id, folder, markdown}).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROJECTS_SUBDIR = REPO / "projects"
LIVE_PROJECTS = Path.home() / "projects"
OUTPUT = REPO / "site" / "public" / "projects.json"


def main() -> int:
    if not PROJECTS_SUBDIR.is_dir():
        print(f"error: {PROJECTS_SUBDIR} does not exist", file=sys.stderr)
        return 1

    live = set()
    if LIVE_PROJECTS.is_dir():
        live = {p.name for p in LIVE_PROJECTS.iterdir() if p.is_dir()}

    entries = []
    for project_dir in sorted(PROJECTS_SUBDIR.iterdir(), key=lambda p: p.name.lower()):
        if not project_dir.is_dir() or project_dir.name.startswith("."):
            continue
        overview = project_dir / "overview.md"
        if not overview.exists():
            continue
        entries.append({
            "id": project_dir.name,
            "folder": "active" if project_dir.name in live else "unknown",
            "markdown": overview.read_text(),
        })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(entries, indent=2) + "\n")
    print(f"wrote {len(entries)} projects to {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Wire into Vite build**

```json
// site/package.json
{
  "scripts": {
    "dev": "vite",
    "prebuild": "python3 ../scripts/build_static_site.py",
    "build": "vite build",
    ...
  }
}
```

- [ ] **Step 3: Test**

```bash
cd site && npm run build
ls public/projects.json dist/projects.json
```

Expected: both files exist. `dist/projects.json` should have ~38 entries.

- [ ] **Step 4: Update .gitignore**

Add `site/public/projects.json` to `site/.gitignore` — it's generated, not source.

- [ ] **Step 5: Commit**

```bash
git add scripts/build_static_site.py site/package.json site/.gitignore
git commit -m "build(site): add prebuild step that bakes projects.json"
```

---

### Task 12: Switch `useProjects` from `/api/projects` to baked JSON

**Files:**
- Modify: `site/src/hooks/useProjects.ts`
- Modify: `site/src/hooks/useProjects.test.ts`

- [ ] **Step 1: Update the failing test first**

```typescript
// site/src/hooks/useProjects.test.ts — update the existing test
it("fetches projects.json relative to base", async () => {
  globalThis.fetch = vi.fn().mockResolvedValue({
    ok: true,
    json: async () => [{ id: "foo", folder: "active", markdown: "# Foo" }],
  });
  const { result } = renderHook(() => useProjects());
  await waitFor(() => expect(result.current.loading).toBe(false));
  expect(fetch).toHaveBeenCalledWith("./projects.json");
  expect(result.current.projects).toHaveLength(1);
});
```

- [ ] **Step 2: Run the test to confirm it fails**

Run: `cd site && npm test -- useProjects`
Expected: fail because current code fetches `/api/projects`.

- [ ] **Step 3: Update the hook**

```typescript
// site/src/hooks/useProjects.ts — change this one line:
fetch('./projects.json')
```

Leave the rest of the file alone. The `.` prefix + Vite base path means this resolves to `/projects-overview/projects.json` in the deployed build and to `/projects.json` in `npm run dev` (which still works because the prebuild populates `public/`).

- [ ] **Step 4: Run the test**

Run: `cd site && npm test -- useProjects`
Expected: pass.

- [ ] **Step 5: Full test suite**

Run: `cd site && npm test`
Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add site/src/hooks/useProjects.ts site/src/hooks/useProjects.test.ts
git commit -m "feat(site): load projects from baked projects.json"
```

---

### Task 13: Create the app manifest and verify end-to-end

**Files:**
- Create: `~/.local-server/apps/projects-overview.json` (not committed — lives on user's machine)

- [ ] **Step 1: Full build from clean**

```bash
cd ~/projects/my-projects-overview/site
rm -rf dist public/projects.json
npm run build
ls dist/index.html dist/projects.json dist/assets/
```

Expected: all present, asset URLs in `dist/index.html` start with `/projects-overview/`.

- [ ] **Step 2: Drop the manifest**

```bash
mkdir -p ~/.local-server/apps
cat > ~/.local-server/apps/projects-overview.json <<EOF
{
  "id": "projects-overview",
  "title": "Projects Overview",
  "description": "Dashboard of all ~/projects repos with overview.md metadata",
  "static_root": "$HOME/projects/my-projects-overview/site/dist",
  "source_repo": "$HOME/projects/my-projects-overview"
}
EOF
```

- [ ] **Step 3: Restart site manager**

```bash
brew services restart local-server.site-manager
```

- [ ] **Step 4: Verify end-to-end**

```bash
curl -s http://localhost:2080/_api/apps | python3 -m json.tool
# Expected: entry for projects-overview

curl -sL http://localhost:2080/projects-overview/ | head -20
# Expected: built index.html

curl -s http://localhost:2080/projects-overview/projects.json | python3 -m json.tool | head
# Expected: baked projects array

open https://dev.local/projects-overview/
# Expected: full dashboard renders, all 38 projects visible
```

- [ ] **Step 5: Verify it appears on the home page**

```bash
open https://dev.local/
```

Expected: "Apps" section at the top, "Projects Overview" card, clicking it navigates to the app.

- [ ] **Step 6: Update `.claude/rules/atomic-site-updates.md`**

The current rule says "HTML site under `site/`" must be regenerated atomically with overview changes. Update it to reflect that `site/` is now a Vite app, and that a `site/dist/` rebuild (via `npm run build`) is the correct regeneration — the prebuild step handles baking `projects.json` automatically.

- [ ] **Step 7: Commit (inside my-projects-overview)**

```bash
git add .claude/rules/atomic-site-updates.md
git commit -m "docs: update atomic-site-updates rule for vite build"
```

- [ ] **Step 8: Open PR, merge, exit worktree**

```bash
git push -u origin worktree-<branch-name>
gh pr create --title "feat: deploy projects-overview as a local-server app" --body "..."
# after merge:
gh pr merge --squash --delete-branch
ExitWorktree (action: remove)
```

---

## Phase 3 (deferred — documented here for future reference)

**Backend supervision.** Add an optional `backend` object to the manifest schema:

```json
{
  "backend": {
    "command": ["node", "server/server.js"],
    "cwd": "/path/to/repo",
    "port": 3457,
    "healthcheck": "/api/health"
  }
}
```

site_manager would spawn and supervise the process, install a reverse-proxy route for `/<id>/api/*` → `localhost:<port>`, restart on crash with backoff, stream stdout/stderr to `~/.local-server/logs/<id>.log`, and stop on manifest removal or site_manager shutdown.

This is a real project in its own right (pid tracking, signal handling, log rotation, crash backoff, graceful shutdown). Defer until there's a second app that actually needs it — the static-bundle approach is sufficient for my-projects-overview and most dashboard-style apps.

---

## Self-Review

**Spec coverage:**
- Apps tier alongside sites ✓ (Tasks 1–5)
- Pointer-based (no copies) ✓ (AppManifest.static_root is a Path to external location)
- Landing page shows both ✓ (Task 7)
- my-projects-overview as first app ✓ (Tasks 10–13)
- Backends optional ✓ (v1 static only, Phase 3 documented)

**Placeholder scan:** none found — every step has concrete code, file paths, and expected output.

**Type consistency:** `AppManifest` fields referenced identically in Tasks 1, 2, 5, 6. `AppEntry` TS interface matches the JSON emitted by the `/_api/apps` Python handler in Task 6. Caddy route `@id` uses the `app-<id>` convention consistently in Tasks 3, 4, 5.

**One known unknown (flagged in Task 4 Step 5):** the actual Caddy server key in the admin API (`srv0` vs something else). Step 5 verifies and adjusts.
