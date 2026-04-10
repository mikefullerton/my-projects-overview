import { useState, useEffect } from 'react';
import type { ProjectInfo, FolderGroup } from '../lib/types.ts';
import { renderMarkdown, extractTitle, extractSummary, extractTechTags } from '../lib/markdown.ts';

export function useProjects() {
  const [projects, setProjects] = useState<ProjectInfo[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('./projects.json')
      .then(res => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data: Array<{ id: string; folder: string; markdown: string }>) => {
        const parsed = data.map(p => ({
          id: p.id,
          name: extractTitle(p.markdown) || p.id,
          folder: p.folder,
          summary: extractSummary(p.markdown),
          techTags: extractTechTags(p.markdown),
          overviewHtml: renderMarkdown(p.markdown),
          rawMarkdown: p.markdown,
        }));
        setProjects(parsed);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return { projects, loading, error };
}

export function groupByFolder(projects: ProjectInfo[]): FolderGroup[] {
  const map = new Map<string, ProjectInfo[]>();
  for (const p of projects) {
    const list = map.get(p.folder) || [];
    list.push(p);
    map.set(p.folder, list);
  }
  const order = ['active', 'other', 'paused', 'personal', 'tests', 'unknown'];
  return order
    .filter(f => map.has(f))
    .map(f => ({ folder: f, projects: map.get(f)! }));
}
