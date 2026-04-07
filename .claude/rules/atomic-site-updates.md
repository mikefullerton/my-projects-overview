---
description: Site HTML must be regenerated whenever overview files or index.md change
globs: "projects/*/overview.md,index.md,site/**"
---

# Atomic Site Updates

When `/update-project-overview` is invoked, the HTML site under `site/` must be regenerated as part of the same atomic commit.

- Every `projects/<name>/overview.md` change must produce an updated `site/projects/<name>.html`
- Every `index.md` change must produce an updated `site/index.html`
- The commit that updates overviews must also include the regenerated site files
- Never commit overview changes without the corresponding site update, and vice versa
