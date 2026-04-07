// Simple markdown-to-HTML renderer. No dependencies.
// Handles: headings, paragraphs, lists, code blocks, inline code, bold, tables, links.

function escapeHtml(s: string): string {
  return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function inlineFormat(text: string): string {
  // Bold
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  // Inline code
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  // Links [text](url)
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2">$1</a>');
  return text;
}

export function renderMarkdown(md: string): string {
  const lines = md.split('\n');
  const out: string[] = [];
  let inCode = false;
  let inList = false;
  let inTable = false;
  let tableHeaderDone = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Code blocks
    if (line.startsWith('```')) {
      if (inList) { out.push('</ul>'); inList = false; }
      if (inTable) { out.push('</tbody></table>'); inTable = false; tableHeaderDone = false; }
      if (inCode) {
        out.push('</code></pre>');
        inCode = false;
      } else {
        out.push('<pre><code>');
        inCode = true;
      }
      continue;
    }
    if (inCode) {
      out.push(escapeHtml(line));
      continue;
    }

    // Skip H1 (title shown separately)
    if (line.startsWith('# ') && !line.startsWith('## ')) continue;

    // Table detection: line contains | and next line is separator (---|---)
    if (line.includes('|') && !line.startsWith('#')) {
      const nextLine = i + 1 < lines.length ? lines[i + 1] : '';
      const isTableSep = /^\|?[\s-:|]+\|[\s-:|]+/.test(nextLine);

      if (!inTable && isTableSep) {
        // Start table with header
        if (inList) { out.push('</ul>'); inList = false; }
        inTable = true;
        tableHeaderDone = false;
        const cells = line.split('|').map(c => c.trim()).filter(Boolean);
        out.push('<table><thead><tr>');
        cells.forEach(c => out.push(`<th>${inlineFormat(escapeHtml(c))}</th>`));
        out.push('</tr></thead><tbody>');
        continue;
      }
      if (inTable && !tableHeaderDone && /^\|?[\s-:|]+\|[\s-:|]+/.test(line)) {
        tableHeaderDone = true;
        continue;
      }
      if (inTable) {
        const cells = line.split('|').map(c => c.trim()).filter(Boolean);
        if (cells.length > 0) {
          out.push('<tr>');
          cells.forEach(c => out.push(`<td>${inlineFormat(escapeHtml(c))}</td>`));
          out.push('</tr>');
          continue;
        }
      }
    }

    // End table on empty line or non-table line
    if (inTable && (!line.includes('|') || line.trim() === '')) {
      out.push('</tbody></table>');
      inTable = false;
      tableHeaderDone = false;
      if (line.trim() === '') continue;
    }

    // Headings
    if (line.startsWith('#### ')) {
      if (inList) { out.push('</ul>'); inList = false; }
      out.push(`<h4>${inlineFormat(escapeHtml(line.slice(5)))}</h4>`);
      continue;
    }
    if (line.startsWith('### ')) {
      if (inList) { out.push('</ul>'); inList = false; }
      out.push(`<h3>${inlineFormat(escapeHtml(line.slice(4)))}</h3>`);
      continue;
    }
    if (line.startsWith('## ')) {
      if (inList) { out.push('</ul>'); inList = false; }
      out.push(`<h2>${inlineFormat(escapeHtml(line.slice(3)))}</h2>`);
      continue;
    }

    // Ordered list
    if (/^\d+\.\s/.test(line)) {
      if (!inList) { out.push('<ol>'); inList = true; }
      const text = line.replace(/^\d+\.\s/, '');
      out.push(`<li>${inlineFormat(escapeHtml(text))}</li>`);
      continue;
    }

    // Unordered list
    if (line.startsWith('- ') || line.startsWith('* ')) {
      if (!inList) { out.push('<ul>'); inList = true; }
      const text = line.slice(2);
      out.push(`<li>${inlineFormat(escapeHtml(text))}</li>`);
      continue;
    }

    // End list
    if (inList && line.trim() === '') {
      // Check if next line continues the list
      const next = i + 1 < lines.length ? lines[i + 1] : '';
      if (!next.startsWith('- ') && !next.startsWith('* ') && !/^\d+\.\s/.test(next)) {
        out.push(out[out.length - 1]?.includes('<ol>') || out.some(l => l === '<ol>') ? '</ol>' : '</ul>');
        inList = false;
      }
      continue;
    }

    // Paragraph
    if (line.trim()) {
      if (inList) {
        out.push('</ul>');
        inList = false;
      }
      out.push(`<p>${inlineFormat(escapeHtml(line))}</p>`);
    }
  }

  if (inList) out.push('</ul>');
  if (inCode) out.push('</code></pre>');
  if (inTable) out.push('</tbody></table>');

  return out.join('\n');
}

export function extractTitle(md: string): string {
  const match = md.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : '';
}

export function extractSummary(md: string): string {
  const match = md.match(/## Project Summary\s+(.+?)(?:\n\n|\n##)/s);
  if (!match) return '';
  const first = match[1].trim().split('\n')[0];
  return first.length > 160 ? first.slice(0, 157) + '...' : first;
}

export function extractTechTags(md: string): string[] {
  // Look for tech stack section, extract from bullet items
  const section = md.match(/## Type & Tech Stack\s+([\s\S]+?)(?:\n## )/);
  if (!section) return [];
  const tags: string[] = [];
  const lines = section[1].split('\n');
  for (const line of lines) {
    const m = line.match(/\*\*(?:Type|Language|Tech|Shared core|Frontend|Backend|UI|Framework).*?:\*\*\s*(.+)/i);
    if (m) {
      m[1].split(',').slice(0, 3).forEach(t => {
        const tag = t.trim().replace(/\(.*\)/, '').trim();
        if (tag && tag.length < 25) tags.push(tag);
      });
    }
  }
  return tags.slice(0, 5);
}
