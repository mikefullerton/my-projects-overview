import { describe, it, expect } from 'vitest';
import { groupByFolder } from './useProjects.ts';
import type { ProjectInfo } from '../lib/types.ts';

function makeProject(id: string, folder: string): ProjectInfo {
  return { id, name: id, folder, summary: '', techTags: [], overviewHtml: '', rawMarkdown: '' };
}

describe('groupByFolder', () => {
  it('groups projects by folder', () => {
    const projects = [
      makeProject('a', 'active'),
      makeProject('b', 'active'),
      makeProject('c', 'paused'),
    ];
    const groups = groupByFolder(projects);
    expect(groups).toHaveLength(2);
    expect(groups[0].folder).toBe('active');
    expect(groups[0].projects).toHaveLength(2);
    expect(groups[1].folder).toBe('paused');
    expect(groups[1].projects).toHaveLength(1);
  });

  it('orders folders: active, other, paused, personal, tests', () => {
    const projects = [
      makeProject('z', 'tests'),
      makeProject('a', 'active'),
      makeProject('p', 'personal'),
      makeProject('o', 'other'),
      makeProject('x', 'paused'),
    ];
    const groups = groupByFolder(projects);
    expect(groups.map(g => g.folder)).toEqual(['active', 'other', 'paused', 'personal', 'tests']);
  });

  it('returns empty for no projects', () => {
    expect(groupByFolder([])).toEqual([]);
  });
});
