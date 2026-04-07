# mikefullerton.com

## Project Summary

Mike Fullerton's personal portfolio and resume website showcasing his professional background as a software engineer and creative pursuits as a drummer. Static HTML/CSS site deployed via GitHub Pages.

## Type & Tech Stack

- **Project Type:** Static personal website/portfolio
- **Technologies:** HTML5, CSS3 (custom styles with CSS variables), vanilla (no frameworks)
- **Font:** Inter (Google Fonts)
- **Hosting:** GitHub Pages
- **Deployment:** GitHub Actions workflow
- **Design:** Mobile-responsive grid-based layout with dark theme

## GitHub URL

`https://github.com/mikefullerton/mikefullerton.com`

## Directory Structure

```
mikefullerton.com/
├── .claude/
│   ├── settings.local.json          # Local settings with bash permissions
│   └── worktrees/
│       └── new-website-design/      # Experimental React/Vite redesign
├── .github/
│   └── workflows/
│       └── deploy.yml               # GitHub Actions Pages deployment
├── .superpowers/
│   └── brainstorm/
├── images/
│   ├── mike-drums.jpg              # Hero image (840KB)
│   └── og-image.jpg                # Open Graph preview (241KB)
├── .gitignore
├── .nojekyll                        # GitHub Pages Jekyll disable flag
├── CNAME                            # Domain: mikefullerton.com
├── CLAUDE.md                        # Auto-merge PR rule
├── index.html                       # Main website (92 lines)
├── styles.css                       # Styling (309 lines)
└── cats_and_dogs_quotes.md         # Untracked notes file
```

## Key Files & Components

**index.html** — Semantic HTML5 with:
- SEO optimization: meta descriptions, Open Graph tags, Twitter Card tags, JSON-LD schema
- Hero section with photo (clickable lightbox)
- Bio covering drumming, Scratchy Fish band, software engineering (Microsoft, Apple)
- Social links (LinkedIn, Twitter/X, Facebook, Instagram) with SVG icons

**styles.css** — Dark theme with CSS variables:
- Background: #0a0a0a, Text: #e8e8e8
- Accent colors: blue (#6db3ff) for professional, red (#ff8e8e) for creative
- 2-column grid on desktop (300px photo + text), responsive mobile
- Lightbox, hover effects, transitions

**CLAUDE.md** — Auto-merge all PRs: `gh pr merge --squash --admin` immediately after creation

## Claude Configuration

- `.claude/settings.local.json` — Allows git operations, tree command, file opening
- `.claude/worktrees/new-website-design/` — Experimental React/Vite redesign (separate from deployed version)

## Planning & Research Documents

- `.superpowers/brainstorm/` — Brainstorming artifacts from development sessions
- `cats_and_dogs_quotes.md` — Untracked notes (not committed)

## Git History & Current State

**Recent Commits:**
1. `2026-04-06` — chore: add .gitignore (HEAD)
2. `2026-02-09` — Center social icons below all content (#9)
3. `2026-02-09` — Fix spelling: emphasises → emphasizes (#8)
4. `2026-02-09` — Re-crop OG preview image to include full face
5. `2026-02-09` — Add project CLAUDE.md with auto-merge rule (#7)

**Major milestones:**
- Modern layout redesign (commit 0e0a9ab)
- Responsive mobile layout (#5)
- Hero image optimization 16MB → 844KB (#4)
- GitHub Pages deployment setup (#1-#3)

**Current Branch:** gh-pages
**Status:** 1 commit ahead of origin, untracked files (.superpowers/, quotes file)

## Build & Test Commands

No build step — static site deployed directly to GitHub Pages.

**Deployment:** Push to `gh-pages` → GitHub Actions deploys via `deploy.yml`
**Local testing:** Open `index.html` in browser, test responsive at 320px/768px/900px

## Notes

- Intentionally dependency-free static site for performance and simplicity
- Auto-merge PR policy indicates "ship it" philosophy
- Custom domain `mikefullerton.com` via CNAME
- Site emphasizes three aspects: drummer, professional engineer (Microsoft/Apple), creative builder
- Experimental React/Vite redesign exists in worktrees but is not deployed
