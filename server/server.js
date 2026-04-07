import { createServer } from 'node:http';
import { readdir, readFile } from 'node:fs/promises';
import { join } from 'node:path';

const PORT = Number(process.env.PORT || 3457);
const PROJECTS_BASE = join(import.meta.dirname, '..', 'projects');

// Map of folder names to disk paths
const PROJECT_FOLDERS = {
  active: join(process.env.HOME, 'projects', 'active'),
  other: join(process.env.HOME, 'projects', 'other'),
  paused: join(process.env.HOME, 'projects', 'paused'),
  personal: join(process.env.HOME, 'projects', 'personal'),
  tests: join(process.env.HOME, 'projects', 'tests'),
};

async function getProjects() {
  const entries = await readdir(PROJECTS_BASE, { withFileTypes: true });
  const projects = [];

  for (const entry of entries) {
    if (!entry.isDirectory()) continue;
    const overviewPath = join(PROJECTS_BASE, entry.name, 'overview.md');
    let markdown;
    try {
      markdown = await readFile(overviewPath, 'utf-8');
    } catch {
      continue;
    }

    // Determine which folder this project lives in on disk
    let folder = 'unknown';
    for (const [name, dirPath] of Object.entries(PROJECT_FOLDERS)) {
      try {
        const contents = await readdir(dirPath);
        if (contents.includes(entry.name)) {
          folder = name;
          break;
        }
      } catch {
        // folder doesn't exist
      }
    }

    projects.push({
      id: entry.name,
      folder,
      markdown,
    });
  }

  // Sort by folder order, then alphabetically within folder
  const folderOrder = ['active', 'other', 'paused', 'personal', 'tests', 'unknown'];
  projects.sort((a, b) => {
    const fa = folderOrder.indexOf(a.folder);
    const fb = folderOrder.indexOf(b.folder);
    if (fa !== fb) return fa - fb;
    return a.id.localeCompare(b.id);
  });

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
