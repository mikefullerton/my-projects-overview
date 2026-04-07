import type { FolderGroup } from '../lib/types.ts';

interface Props {
  groups: FolderGroup[];
  onSelectProject: (id: string) => void;
}

export default function ProjectGrid({ groups, onSelectProject }: Props) {
  return (
    <div className="section" id="projects">
      <div className="section-header">
        <h2>Projects</h2>
        <span className="count">
          {groups.reduce((n, g) => n + g.projects.length, 0)} projects
        </span>
      </div>
      <div className="project-grid">
        {groups.map(g => (
          <div key={g.folder}>
            <div className="project-group-header">~/projects/{g.folder}/</div>
            {g.projects.map(p => (
              <div
                key={p.id}
                className="project-card"
                onClick={() => onSelectProject(p.id)}
              >
                <div className="card-top">
                  <h3>{p.name}</h3>
                </div>
                <div className="tagline">{p.summary}</div>
                {p.techTags.length > 0 && (
                  <div className="tech-stack">
                    {p.techTags.map(t => (
                      <span key={t} className="tech-tag">{t}</span>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}
