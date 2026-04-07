import { describe, it, expect } from 'vitest';
import { renderMarkdown, extractTitle, extractSummary, extractTechTags } from './markdown.ts';

describe('renderMarkdown', () => {
  it('skips H1 headings', () => {
    const html = renderMarkdown('# Title\n\nHello');
    expect(html).not.toContain('<h1>');
    expect(html).toContain('<p>Hello</p>');
  });

  it('renders H2 headings', () => {
    const html = renderMarkdown('## Section');
    expect(html).toContain('<h2>Section</h2>');
  });

  it('renders H3 headings', () => {
    const html = renderMarkdown('### Subsection');
    expect(html).toContain('<h3>Subsection</h3>');
  });

  it('renders paragraphs', () => {
    const html = renderMarkdown('Hello world');
    expect(html).toContain('<p>Hello world</p>');
  });

  it('renders bold text', () => {
    const html = renderMarkdown('This is **bold** text');
    expect(html).toContain('<strong>bold</strong>');
  });

  it('renders inline code', () => {
    const html = renderMarkdown('Use `npm install`');
    expect(html).toContain('<code>npm install</code>');
  });

  it('renders unordered lists', () => {
    const html = renderMarkdown('- Item 1\n- Item 2');
    expect(html).toContain('<ul>');
    expect(html).toContain('<li>Item 1</li>');
    expect(html).toContain('<li>Item 2</li>');
    expect(html).toContain('</ul>');
  });

  it('renders ordered lists', () => {
    const html = renderMarkdown('1. First\n2. Second');
    expect(html).toContain('<ol>');
    expect(html).toContain('<li>First</li>');
    expect(html).toContain('<li>Second</li>');
  });

  it('renders code blocks', () => {
    const html = renderMarkdown('```\nconst x = 1;\n```');
    expect(html).toContain('<pre><code>');
    expect(html).toContain('const x = 1;');
    expect(html).toContain('</code></pre>');
  });

  it('escapes HTML in code blocks', () => {
    const html = renderMarkdown('```\n<div>test</div>\n```');
    expect(html).toContain('&lt;div&gt;test&lt;/div&gt;');
  });

  it('renders links', () => {
    const html = renderMarkdown('[click here](https://example.com)');
    expect(html).toContain('<a href="https://example.com">click here</a>');
  });

  it('renders tables', () => {
    const md = '| Name | Type |\n| --- | --- |\n| Foo | Bar |';
    const html = renderMarkdown(md);
    expect(html).toContain('<table>');
    expect(html).toContain('<th>Name</th>');
    expect(html).toContain('<td>Foo</td>');
    expect(html).toContain('</table>');
  });

  it('handles a full overview-like document', () => {
    const md = `# My Project

## Project Summary

This is a test project for validating the markdown renderer.

## Type & Tech Stack

- **Type:** Web application
- **Language:** TypeScript
- **Framework:** React 19

## GitHub URL

\`git@github.com:user/repo.git\`

## Directory Structure

\`\`\`
src/
├── index.ts
└── lib/
\`\`\`

## Notes

- First note with **bold** and \`code\`
- Second note
`;
    const html = renderMarkdown(md);
    expect(html).not.toContain('<h1>');
    expect(html).toContain('<h2>Project Summary</h2>');
    expect(html).toContain('<h2>Type &amp; Tech Stack</h2>');
    expect(html).toContain('<strong>Type:</strong>');
    expect(html).toContain('<code>git@github.com:user/repo.git</code>');
    expect(html).toContain('<pre><code>');
    expect(html).toContain('src/');
    expect(html).toContain('<li>First note with <strong>bold</strong> and <code>code</code></li>');
  });
});

describe('extractTitle', () => {
  it('extracts H1 title', () => {
    expect(extractTitle('# My Project\n\nSome text')).toBe('My Project');
  });

  it('returns empty string if no title', () => {
    expect(extractTitle('No title here')).toBe('');
  });
});

describe('extractSummary', () => {
  it('extracts first paragraph after Project Summary heading', () => {
    const md = '## Project Summary\n\nThis is the summary.\n\n## Next Section';
    expect(extractSummary(md)).toBe('This is the summary.');
  });

  it('truncates long summaries', () => {
    const long = 'A'.repeat(200);
    const md = `## Project Summary\n\n${long}\n\n## Next`;
    const result = extractSummary(md);
    expect(result.length).toBeLessThanOrEqual(163);
    expect(result).toContain('...');
  });

  it('returns empty for missing section', () => {
    expect(extractSummary('## Other\n\nText')).toBe('');
  });
});

describe('extractTechTags', () => {
  it('extracts tech tags from Type & Tech Stack section', () => {
    const md = `## Type & Tech Stack

- **Type:** Web application
- **Language:** TypeScript
- **Framework:** React 19, Vite

## Next`;
    const tags = extractTechTags(md);
    expect(tags).toContain('Web application');
    expect(tags).toContain('TypeScript');
    expect(tags).toContain('React 19');
  });

  it('returns empty array for missing section', () => {
    expect(extractTechTags('## Other\n\nText')).toEqual([]);
  });
});
