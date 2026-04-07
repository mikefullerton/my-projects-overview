import type { ProjectInfo, FolderGroup } from '../lib/types.ts';

interface Props {
  projects: ProjectInfo[];
  groups: FolderGroup[];
}

export default function StatsBar({ projects, groups }: Props) {
  const cards = [
    { val: projects.length, label: 'Projects', cls: 'accent' },
    { val: groups.length, label: 'Folders', cls: 'blue' },
  ];

  return (
    <div className="stats-bar">
      {cards.map((c, i) => (
        <div key={i} className={`stat-card ${c.cls}`}>
          <div className="stat-value">{c.val}</div>
          <div className="stat-label">{c.label}</div>
        </div>
      ))}
    </div>
  );
}
