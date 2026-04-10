# Scratchyfish.com

## Project Summary

A static website for Scratchy Fish, a progressive jazz rock band from San Jose, California. Built with Jekyll and hosted as a static site with music, photos, news, shows, and biography content. Features a responsive design for band promotion and fan engagement with news feed, video gallery, and band member information.

## Type & Tech Stack

**Project Type:** Static website (Jekyll-based)

**Core Technologies:**
- **Jekyll** — Static site generator with Liquid templates
- **HTML/CSS/Sass** — Frontend markup and styling
- **YAML** — Data files and Jekyll configuration
- **Markdown** — Content authoring
- **Git Pages** — Deployment and hosting

**Architecture:**
- Jekyll template system with reusable layouts
- Data-driven content via YAML front matter
- Asset pipeline for images, CSS, JavaScript
- Static site with no backend requirements

## GitHub URL

`git@github.com:mikefullerton/scratchyfish.com.git`

https://github.com/mikefullerton/scratchyfish.com

## Directory Structure

```
scratchyfish.com/
├── _config.yml                      # Jekyll configuration
├── _data/                           # Data files (YAML)
│   └── [band members, posts, etc.]
├── _includes/                       # Reusable template components
├── _layouts/                        # Page layout templates
├── _posts/                          # Blog posts (16+ markdown files)
├── assets/                          # Images, CSS, JavaScript
│   ├── [band photos]
│   ├── [album artwork]
│   └── [styles]
├── bio/                             # Band member biographies
├── bio.html                         # Generated biography page
├── contact.html                     # Contact form/information
├── friends.html                     # Related artists/friends
├── index.html                       # Homepage
├── music.html                       # Music/albums page
├── news.html                        # News feed
├── photos.html                      # Photo gallery
├── shows.html                       # Upcoming shows
├── video.html                       # Video gallery
├── Gemfile                          # Ruby dependencies
├── CNAME                            # Domain configuration
├── robots.txt                       # SEO configuration
├── sitemap.xml                      # Sitemap for indexing
├── .claude/                         # Claude Code configuration
├── .gitignore
└── README.md
```

## Key Files & Components

**Configuration:**
- `_config.yml` — Jekyll site configuration (title, URL, markdown, permalinks)

**Content Pages:**
- `index.html` — Homepage with band info and featured content
- `music.html` — Music/albums section
- `shows.html` — Upcoming shows and tour dates
- `photos.html` — Photo gallery
- `video.html` — Video gallery
- `news.html` — News feed
- `bio.html` — Generated band member biographies
- `contact.html` — Contact information
- `friends.html` — Related artists and collaborators

**Content Management:**
- `_data/` — YAML data files for band members, posts, and structured content
- `_posts/` — Blog posts with metadata (16+ news articles)

**Templates:**
- `_layouts/` — Reusable page layouts (default, post, etc.)
- `_includes/` — Reusable template components (navigation, headers, footers)

**Assets:**
- `assets/` — Images, stylesheets, JavaScript
- Downloaded local images (band photos, album artwork, video thumbnails)

**SEO & Metadata:**
- `sitemap.xml` — XML sitemap for search engines
- `robots.txt` — Robot exclusion rules
- `CNAME` — Domain configuration for scratchyfish.com

## Claude Configuration

**Configuration Files:**
- `.claude/` — Claude Code configuration for site development

## Planning & Research Documents

No dedicated planning/research directories found. Content management handled through Jekyll data files and front matter.

## Git History & Current State

**Recent Activity:**
- `9137754` git ignore change
- `af35af2` chore: update claude local settings
- `760cd0b` Add Phil Bernosky serious bio text
- `2a846aa` Add Phil Bernosky person photo with dog/person toggle
- `72b323f` Fix remaining external image URLs in posts.json
- `5021168` Add Mike Fullerton dog photo locally
- `7e26568` Download all external images to local assets (static hosting)
- `9d27b20` Restore original dog photo URL for Mike Fullerton
- `9cce459` Fix Mike Fullerton dog photo URL
- `1fd8c7c` Sync photo toggle and translate link
- `404a6ee` Make video gallery entries full width
- `229f5da` Ensure post and video cards are full width
- `12f9785` Make video entries full width
- `3167067` Add news posts for all YouTube videos
- `aad7836` Add Art Boutiki video to videos section

**Pattern:** Steady content updates with image optimization and gallery refinement.

**Current State:**
- **Branch:** main
- **Status:** Clean working tree

## Build & Test Commands

**Build Site:**
```bash
bundle exec jekyll build        # Generate static site
bundle exec jekyll serve       # Local development server (port 4000)
```

**Install Dependencies:**
```bash
bundle install                 # Install Ruby gems
```

**Preview:**
```bash
open _site/index.html         # View generated site
```

## Notes

**Architecture Highlights:**

1. **Static Site Generation** — Jekyll compiles all content to static HTML at build time
2. **Data-Driven Content** — Band members, posts, and structured content via YAML data files
3. **Image Optimization** — Recent migration to local asset hosting (no external dependencies)
4. **Responsive Design** — Mobile-friendly layout for desktop and mobile viewing
5. **SEO Optimized** — Sitemap, robots.txt, and proper metadata for search engines

**Content Areas:**

- **Music** — Albums and music releases
- **Shows** — Tour dates and upcoming performances
- **News** — Blog posts with news and updates
- **Photos** — Band and performance photography
- **Videos** — YouTube video gallery
- **Bio** — Band member biographies with photos
- **Connect** — Contact and social links

**Recent Improvements:**

- Migration of external images to local assets (improved load time, no external dependencies)
- Photo toggle functionality for band member profiles
- Video gallery entries made full-width for better presentation
- Consistent video thumbnail sizing

**Deployment:**

Hosted as static site on GitHub Pages at scratchyfish.com via CNAME configuration. Pure static deployment with no backend requirements, ensuring fast load times and high reliability.

**Development Notes:**

- Uses Jekyll's data files for easy content management
- Liquid templating for dynamic site generation
- Git-based workflow for content updates
- All content is version-controlled
