export interface ProjectInfo {
  id: string;
  name: string;
  folder: string;      // e.g. "active", "paused", "tests"
  summary: string;
  techTags: string[];
  overviewHtml: string; // rendered HTML from markdown
  rawMarkdown: string;  // original markdown
}

export interface FolderGroup {
  folder: string;
  projects: ProjectInfo[];
}
