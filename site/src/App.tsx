import { useState, useCallback } from 'react';
import { useProjects, groupByFolder } from './hooks/useProjects.ts';
import Sidebar from './components/Sidebar.tsx';
import StatsBar from './components/StatsBar.tsx';
import ProjectGrid from './components/ProjectGrid.tsx';
import ProjectDetail from './components/ProjectDetail.tsx';

export default function App() {
  const { projects, loading, error } = useProjects();
  const [currentProject, setCurrentProject] = useState<string | null>(null);

  const groups = groupByFolder(projects);

  const selectProject = useCallback((id: string) => {
    setCurrentProject(id);
    window.scrollTo({ top: 0 });
    history.pushState({ project: id }, '', `#${id}`);
  }, []);

  const showDashboard = useCallback(() => {
    setCurrentProject(null);
    window.scrollTo({ top: 0 });
    history.pushState({}, '', window.location.pathname);
  }, []);

  // Handle browser back/forward
  useState(() => {
    const handler = (e: PopStateEvent) => {
      if (e.state?.project) setCurrentProject(e.state.project);
      else setCurrentProject(null);
    };
    window.addEventListener('popstate', handler);

    // Handle initial hash
    if (window.location.hash) {
      const id = window.location.hash.replace('#', '');
      if (projects.find(p => p.id === id)) setCurrentProject(id);
    }

    return () => window.removeEventListener('popstate', handler);
  });

  if (loading) return <div className="app"><main style={{ padding: '80px 48px', color: 'var(--text-dim)' }}>Loading...</main></div>;
  if (error) return <div className="app"><main style={{ padding: '80px 48px', color: 'var(--red)' }}>Error: {error}</main></div>;

  const selected = currentProject ? projects.find(p => p.id === currentProject) : null;

  return (
    <div className="app">
      <Sidebar
        groups={groups}
        currentProject={currentProject}
        onSelectProject={selectProject}
        onShowDashboard={showDashboard}
      />
      <main>
        {selected ? (
          <ProjectDetail project={selected} onBack={showDashboard} />
        ) : (
          <>
            <div className="page-header">
              <h1><span>Project</span> Overview</h1>
              <div className="title-rule"></div>
              <p>Comprehensive documentation of all projects &mdash; {projects.length} projects across {groups.length} folders.</p>
            </div>
            <StatsBar projects={projects} groups={groups} />
            <ProjectGrid groups={groups} onSelectProject={selectProject} />
          </>
        )}
      </main>
    </div>
  );
}
