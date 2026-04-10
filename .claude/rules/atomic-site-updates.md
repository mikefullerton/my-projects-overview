---
description: Rebuild and redeploy the local-server app after any overview change
globs: "projects/*/overview.md,index.md,site/**"
---

# Site Rebuild After Overview Changes

The dashboard under `site/` is a Vite React app deployed as a local-server
app at `dev.local/projects-overview/`. The built output (`site/dist/`) is
gitignored — the source of truth for project data is the set of
`projects/<name>/overview.md` files, baked into `site/public/projects.json`
by the `prebuild` step.

After any commit that modifies `projects/<name>/overview.md` or `index.md`,
rebuild and redeploy:

```bash
cd site && npm run build
```

The `prebuild` script (`scripts/build_static_site.py`) regenerates
`projects.json` from the current overview files before `vite build` runs.
The app manifest at `~/.local-server/apps/projects-overview.json` points
Caddy at `site/dist/` in place, so no copying is needed after the build.
