import { useState } from 'react';
import type { FolderGroup } from '../lib/types.ts';

interface Props {
  groups: FolderGroup[];
  currentProject: string | null;
  onSelectProject: (id: string) => void;
  onShowDashboard: () => void;
}

export default function Sidebar({ groups, currentProject, onSelectProject, onShowDashboard }: Props) {
  const [search, setSearch] = useState('');
  const q = search.toLowerCase();

  const total = groups.reduce((n, g) => n + g.projects.length, 0);

  return (
    <nav>
      <div className="nav-title" onClick={onShowDashboard} style={{ cursor: 'pointer' }}>Projects</div>
      <div className="nav-sub">{total} projects &middot; {groups.length} folders</div>

      <div style={{ padding: '0 16px', marginBottom: '20px' }}>
        <input
          type="text"
          placeholder="Search..."
          value={search}
          onChange={e => setSearch(e.target.value)}
          style={{
            width: '100%', background: 'var(--bg)', color: 'var(--text)',
            border: '1px solid var(--border)', borderRadius: '4px',
            padding: '6px 10px', fontFamily: 'var(--mono)', fontSize: '0.7rem',
            outline: 'none',
          }}
        />
      </div>

      <div className="nav-section">Overview</div>
      <a
        href="#"
        className={currentProject === null ? 'active' : ''}
        onClick={e => { e.preventDefault(); onShowDashboard(); }}
      >
        Dashboard
      </a>

      {groups.map(g => {
        const filtered = q ? g.projects.filter(p =>
          p.id.toLowerCase().includes(q) || p.name.toLowerCase().includes(q) || p.summary.toLowerCase().includes(q)
        ) : g.projects;

        if (filtered.length === 0) return null;

        return (
          <div key={g.folder}>
            <div className="nav-section">~/projects/{g.folder}/</div>
            {filtered.map(p => (
              <a
                key={p.id}
                href={`#${p.id}`}
                className={currentProject === p.id ? 'active' : ''}
                onClick={e => { e.preventDefault(); onSelectProject(p.id); }}
              >
                {p.name}
              </a>
            ))}
          </div>
        );
      })}
    </nav>
  );
}
