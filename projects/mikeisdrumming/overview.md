# mikeisdrumming

## Project Summary

A GitHub Pages landing page for "Mike Is Drumming," a personal music/drumming project. Currently a minimal "Coming Soon" placeholder page with a custom domain (mikeisdrumming.com, via CNAME). Includes research on music service APIs (Spotify, Tidal, Beatport, SoundCloud, Deezer, and others) for potential DJ-focused features.

## Type & Tech Stack

- **Type**: Static website (landing page / coming soon)
- **Languages**: HTML, CSS
- **Hosting**: GitHub Pages with custom domain
- **Domain**: mikeisdrumming.com (CNAME configured)

## GitHub URL

`git@github.com:mikefullerton/mikeisdrumming.git`

## Directory Structure

```
mikeisdrumming/
├── .claude/
│   └── settings.json                # Permission allowlists
├── CNAME                             # Custom domain (mikeisdrumming.com)
├── index.html                        # Landing page ("Coming Soon")
├── README.md                         # Minimal readme
└── Research/
    └── music-service-apis.md        # Music streaming API research
```

## Key Files & Components

- `index.html` -- Minimal dark-themed landing page with "Mike Is Drumming" title and "Coming Soon" text
- `CNAME` -- Custom domain configuration
- `Research/music-service-apis.md` -- Comprehensive research on music streaming and data APIs (Spotify, Tidal, Beatport, SoundCloud, Deezer, Pandora, Amazon Music, MusicBrainz, Genius, Discogs), aggregator services, DJ-specific comparisons, DJ software compatibility matrix, community libraries, and recommendations

## Claude Configuration

- `.claude/settings.json` -- Permission allowlists for GitHub auth, git operations (init, remote, add, commit, push), web search, and brew install
- No CLAUDE.md or project-level rules

## Planning & Research Documents

- `Research/music-service-apis.md` -- Detailed API research covering major streaming platforms, music data APIs, aggregator services, DJ software compatibility, community tools, and recommendations for DJ-focused applications

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-06 -- "chore: add .gitignore"
- **Working tree**: Clean
- **Total commits**: 4
- **Recent activity**: GitHub Pages setup with custom domain (Feb 2026), music API research (Jan 2026), gitignore added (Apr 2026)
- **Key commits**: Initial commit, music service API research, GitHub Pages landing page (#1)

## Build & Test Commands

```bash
# No build step -- static HTML
# Deploy: Push to main branch (GitHub Pages auto-deploys)
git push origin main
```

## Notes

- Very early stage -- only a "Coming Soon" placeholder page
- The music-service-apis.md research document is substantial and covers potential integration paths
- Project is paused -- the research exists but no features have been built yet
- Custom domain configured via CNAME file
