# scratchyfish.com

## Project Summary

A Jekyll-based static website for Scratchy Fish, a progressive jazz rock band from San Jose, California. The site features band member bios with photo toggle (dog/person), music pages, video gallery, photo gallery, show listings, news posts (including auto-generated posts for YouTube videos), and a contact page. Hosted on GitHub Pages with a custom domain (scratchyfish.com). Content is data-driven via JSON files in `_data/` and Jekyll templating.

## Type & Tech Stack

- **Type**: Static website (band/music)
- **Framework**: Jekyll (GitHub Pages)
- **Languages**: HTML, CSS, Liquid templates
- **Content**: JSON data files (`_data/`), Markdown posts (`_posts/`)
- **Hosting**: GitHub Pages with custom domain
- **Domain**: scratchyfish.com (CNAME configured)
- **Dependencies**: Gemfile (kramdown markdown processor)

## GitHub URL

`git@github.com:mikefullerton/scratchyfish.com.git`

## Directory Structure

```
scratchyfish.com/
├── .claude/
│   └── settings.local.json          # Permission allowlists
├── _config.yml                       # Jekyll configuration
├── _data/                            # JSON data files (band members, shows, etc.)
├── _includes/                        # Partial templates
├── _layouts/                         # Page layouts
├── _posts/                           # News/blog posts (14+ posts)
├── assets/                           # Images, CSS, static assets
├── bio/                              # Band member bio subpages
├── bio.html                          # Band bio page
├── CNAME                             # Custom domain (scratchyfish.com)
├── contact.html                      # Contact page
├── friends.html                      # Friends/links page
├── Gemfile                           # Ruby dependencies
├── index.html                        # Homepage
├── music.html                        # Music page
├── news.html                         # News listing
├── photos.html                       # Photo gallery
├── robots.txt                        # Search engine directives
├── shows.html                        # Show listings
├── sitemap.xml                       # XML sitemap
└── video.html                        # Video gallery
```

## Key Files & Components

- `_config.yml` -- Jekyll config: title "Scratchy Fish", kramdown markdown, GitHub Pages theme disabled, custom domain URL
- `_data/` -- JSON data files driving band member bios, shows, posts, videos
- `bio.html` -- Band bio page with dog/person photo toggle feature
- `friends.html` -- Links to friends and associated acts
- `music.html` -- Music player/links page
- `video.html` -- Video gallery (YouTube embeds, full-width entries)
- `_posts/` -- 14+ news posts including auto-generated entries for YouTube videos
- `index.html` -- Homepage with latest news and featured content

## Claude Configuration

- `.claude/settings.local.json` -- Permission allowlists for git operations, web fetching (scratchyfish.com, youtube.com, unsplash.com, idiotfish.net, linktr.ee), image processing (sips, curl, yt-dlp), GitHub CLI, and web search
- No CLAUDE.md or project-level rules

## Planning & Research Documents

None found.

## Git History & Current State

- **Branch**: main
- **Last commit**: 2026-04-05 -- "git ignore change"
- **Working tree**: Clean
- **Total commits**: 15+ (viewed)
- **Recent activity**: Photo toggle features (Jan 2026), video gallery improvements, external image localization, gitignore updates (Apr 2026)
- **Key recent changes**: Phil Bernosky bio/photo additions, external image URL fixes, video gallery full-width layout, news posts for YouTube videos

## Build & Test Commands

```bash
# Local development (requires Jekyll/Ruby)
bundle install
bundle exec jekyll serve

# Deploy: Push to main branch (GitHub Pages auto-deploys)
git push origin main
```

## Notes

- All external images have been downloaded to local assets to avoid broken links
- Band member bios feature a dog/person photo toggle (each member has both a regular photo and a dog photo)
- The site uses a null remote theme (custom HTML/CSS, no Jekyll theme gem)
- CNAME file configures the custom domain scratchyfish.com
