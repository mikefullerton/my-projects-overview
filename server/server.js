import { createServer } from 'node:http';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';

const PORT = Number(process.env.PORT || 3457);
const PROJECTS_BASE = join(import.meta.dirname, '..', 'projects');
const PROJECTS_LIVE = join(process.env.HOME, 'projects');

async function getProjects() {
  const entries = await readdir(PROJECTS_BASE, { withFileTypes: true });
  const projects = [];

  // Read live projects dir once to check existence
  let liveEntries = new Set();
  try {
    liveEntries = new Set(await readdir(PROJECTS_LIVE));
  } catch {
    // ignore
  }

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const overviewPath = join(PROJECTS_BASE, entry.name, 'overview.md');
    let markdown;
    try {
      markdown = await readFile(overviewPath, 'utf-8');
    } catch {
      continue;
    }

    // All live projects now live directly under ~/projects/
    const folder = liveEntries.has(entry.name) ? 'active' : 'unknown';

    projects.push({
      id: entry.name,
      folder,
      markdown,
    });
  }

  // Sort alphabetically (case-insensitive)
  projects.sort((a, b) => a.id.toLowerCase().localeCompare(b.id.toLowerCase()));

  return projects;
}

const server = createServer(async (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  if (req.url === '/api/projects') {
    try {
      const projects = await getProjects();
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(projects));
    } catch (err) {
      res.writeHead(500, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify({ error: err.message }));
    }
    return;
  }

  res.writeHead(404, { 'Content-Type': 'application/json' });
  res.end(JSON.stringify({ error: 'not found' }));
});

server.listen(PORT, () => {
  console.log(`Projects Overview API running on http://localhost:${PORT}`);
});
