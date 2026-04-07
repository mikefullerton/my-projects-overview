# mikefullerton.com

## Project Summary

Mike Fullerton's personal portfolio and resume website showcasing his professional background as a software engineer and creative pursuits as a drummer. Static HTML/CSS site deployed via GitHub Pages at mikefullerton.com.

## Type & Tech Stack

- **Project Type:** Static personal website/portfolio
- **Technologies:** HTML5, CSS3 (custom styles with CSS variables), vanilla (no frameworks)
- **Font:** Inter (Google Fonts)
- **Hosting:** GitHub Pages
- **Deployment:** GitHub Actions workflow (`actions/deploy-pages@v4`)
- **Design:** Mobile-responsive grid-based layout with dark theme (#0a0a0a)
- **SEO:** Open Graph, Twitter Cards, JSON-LD Person schema

## GitHub URL

`git@github.com:mikefullerton/mikefullerton.com.git`

## Directory Structure

```
mikefullerton.com/
├── .claude/
│   ├── settings.local.json          # Local settings with bash permissions
│   └── worktrees/
├── .github/
│   └── workflows/
│       └── deploy.yml               # GitHub Actions Pages deployment
├── .superpowers/                    # (untracked) brainstorm artifacts
├── images/
│   ├── mike-drums.jpg              # Hero image (860KB, optimized from 16MB)
│   └── og-image.jpg                # Open Graph preview (247KB)
├── .gitignore
├── .nojekyll                        # GitHub Pages Jekyll disable flag
├── CNAME                            # Domain: mikefullerton.com
├── CLAUDE.md                        # Auto-merge PR rule
├── index.html                       # Main website
├── styles.css                       # Styling
└── cats_and_dogs_quotes.md         # (untracked) notes file
```

## Key Files & Components

**index.html** -- Semantic HTML5 with:
- SEO optimization: meta descriptions, Open Graph tags, Twitter Card tags, JSON-LD Person schema
- Hero section with photo
- Bio covering drumming, Scratchy Fish band, software engineering (Microsoft, Apple)
- Social links (LinkedIn, Twitter/X, Facebook, Instagram) with SVG icons

**styles.css** -- Dark theme with CSS variables:
- Background: #0a0a0a, Text: #e8e8e8
- Accent colors: blue (#6db3ff) for professional, red (#ff8e8e) for creative
- 2-column grid on desktop (300px photo + text), responsive mobile
- Hover effects, transitions

**CLAUDE.md** -- Auto-merge all PRs: `gh pr merge --squash --admin` immediately after creation

**.github/workflows/deploy.yml** -- Deploys to GitHub Pages on push to `gh-pages` using `actions/deploy-pages@v4`

## Claude Configuration

- **CLAUDE.md:** Auto-merge all PRs with `gh pr merge --squash --admin`
- **.claude/settings.local.json:** Allows git operations (init, remote, fetch, checkout, add, commit, push, reset), tree command, and file opening
- **.claude/worktrees/** -- Worktree support directory

## Planning & Research Documents

None committed. `.superpowers/` directory exists but is untracked.

## Git History & Current State

**Current Branch:** gh-pages
**Total Commits:** 15

**Recent Commits:**
1. `2026-04-06` -- chore: add .gitignore (HEAD)
2. `2026-02-09` -- Center social icons below all content (#9)
3. `2026-02-09` -- Fix spelling: emphasises -> emphasizes (#8)
4. `2026-02-09` -- Re-crop OG preview image to include full face
5. `2026-02-09` -- Add project CLAUDE.md with auto-merge rule (#7)

**Major milestones:**
- Modern layout redesign (commit 0e0a9ab)
- Responsive mobile layout (#5)
- Hero image optimization 16MB -> 844KB (#4)
- GitHub Pages deployment setup (#1-#3)

**Status:** Untracked files: `.superpowers/`, `cats_and_dogs_quotes.md`

## Build & Test Commands

No build step -- static site deployed directly to GitHub Pages.

**Deployment:** Push to `gh-pages` -> GitHub Actions deploys via `deploy.yml`
**Local testing:** Open `index.html` in browser

## Notes

- Intentionally dependency-free static site for performance and simplicity
- Auto-merge PR policy indicates "ship it" philosophy for this project
- Custom domain `mikefullerton.com` via CNAME record
- Site emphasizes three aspects: drummer, professional engineer (Microsoft/Apple), creative builder (Scratchy Fish)
