import { useState, useEffect, useCallback } from 'react';
import type { ProjectInfo } from '../lib/types.ts';

interface Props {
  project: ProjectInfo;
  onBack: () => void;
}

// Safe: overviewHtml is rendered from our own local markdown files by our
// own renderer (lib/markdown.ts), never from user input or external sources.

export default function ProjectDetail({ project, onBack }: Props) {
  const [showRaw, setShowRaw] = useState(false);

  const handleKeyDown = useCallback((e: KeyboardEvent) => {
    if (e.key === 'Escape') setShowRaw(false);
  }, []);

  useEffect(() => {
    document.addEventListener('keydown', handleKeyDown);
    return () => document.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyDown]);

  return (
    <div className="section">
      <div style={{ marginBottom: '24px' }}>
        <button className="btn btn-ghost btn-small" onClick={onBack}>&larr; All Projects</button>
      </div>

      <div className="detail-header">
        <h1>{project.name}</h1>
        <button className="raw-btn" onClick={() => setShowRaw(true)}>Raw</button>
      </div>

      {/* eslint-disable-next-line -- content is from our own local markdown files, not user input */}
      <div className="md-content" dangerouslySetInnerHTML={{ __html: project.overviewHtml }} />

      {showRaw && (
        <div className="raw-overlay" onClick={e => { if (e.target === e.currentTarget) setShowRaw(false); }}>
          <div className="raw-panel">
            <div className="raw-panel-header">
              <span className="raw-panel-title">{project.id}/overview.md</span>
              <button className="raw-close" onClick={() => setShowRaw(false)}>&times;</button>
            </div>
            <div className="raw-panel-body">
              <pre>{project.rawMarkdown}</pre>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
