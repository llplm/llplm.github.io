# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based academic personal website using the **al-folio** theme, deployed to GitHub Pages. It serves as a portfolio/CV site for Lluís Palma, featuring academic publications, CV, and research content.

## Build & Development Commands

```bash
# Install dependencies
bundle install

# Local development server (auto-reloads on changes)
bundle exec jekyll serve

# Production build
JEKYLL_ENV=production bundle exec jekyll build

# Build with Latent Semantic Indexing (for related posts)
bundle exec jekyll build --lsi
```

### Docker Development

```bash
# Using Docker Compose
docker-compose up

# Local Docker build
docker-compose -f docker-local.yml up
```

### Deployment

Deployment is automatic via GitHub Actions on push to `master` or `main` branches. The workflow:
1. Checks out code
2. Sets up Ruby 3.2.2
3. Installs Jupyter and Mermaid CLI
4. Builds with `JEKYLL_ENV=production`
5. Deploys `_site` folder to GitHub Pages using JamesIves/github-pages-deploy-action

For manual deployment:
```bash
bin/deploy [--no-push] [-s SRC_BRANCH] [-d DEPLOY_BRANCH]
```
Manual deployment builds with `--lsi` flag and creates a `gh-pages` branch.

## Architecture

### Content Structure

- `_pages/` - Main site pages (about.md, cv.md, publications.md, photo.md)
- `_posts/` - Blog posts
- `_projects/` - Project cards
- `_news/` - News announcements
- `_bibliography/papers.bib` - Academic publications in BibTeX format
- `_data/` - YAML data files:
  - `cv.yml` - CV structure
  - `coauthors.yml` - Co-author metadata
  - `venues.yml` - Conference/journal metadata
- `assets/json/resume.json` - JSON Resume format data

### Templates & Styling

- `_layouts/` - Page templates:
  - `about.html` - Homepage layout
  - `cv.html` - CV page using data from `_data/cv.yml`
  - `bib.html` - Individual bibliography entry rendering
  - `post.html`, `distill.html` - Blog post layouts
  - `archive-*.html` - Archive pages for tags, categories, years
- `_includes/` - Reusable components:
  - `header.html`, `footer.html`, `head.html` - Site structure
  - `social.html` - Social media links
  - `cv/` - CV section partials
  - `resume/` - JSON Resume format partials
- `_sass/` - SCSS stylesheets:
  - `_base.scss` - Core styles with retro terminal aesthetic
  - `_themes.scss` - Light/dark mode definitions (beige light mode, dark terminal)
  - `_variables.scss` - Color palette and design tokens
  - `_cv.scss`, `_distill.scss`, `_layout.scss` - Page-specific styles

**Custom Theme**: Site uses a retro terminal aesthetic with JetBrains Mono font, beige light mode, and CRT screen effects for visual flair.

### Custom Plugins

`_plugins/` contains Ruby plugins:
- `cache-bust.rb` - Appends cache-busting hashes to asset URLs
- `details.rb` - Custom Liquid tags for detail/summary blocks
- `external-posts.rb` - Fetches external blog posts (e.g., from Medium)
- `file-exists.rb` - Liquid filter to check file existence
- `hideCustomBibtex.rb` - Filters out custom BibTeX fields from display

## Key Configuration

Main configuration is in `_config.yml`:
- **Site metadata**: Title, author name, email, social links (GitHub, Twitter/Bluesky, Google Scholar, ORCID)
- **jekyll-scholar**: BibTeX bibliography settings (source: `_bibliography/papers.bib`, style: APA, max 3 authors visible)
- **Theme**: Light/dark mode toggle, syntax highlighting (github/native themes)
- **Blog**: Pagination enabled, related posts enabled (max 5), permalink format `/blog/:year/:title/`
- **Plugins**: Full list includes jekyll-scholar, jekyll-archives, jekyll-jupyter-notebook, jekyll-diagrams, and more
- **Features**: Math typesetting (MathJax), medium zoom, masonry layout, darkmode, tooltips, progress bar

## Technology Stack

- **Jekyll 4.x** with Ruby 3.2.2+
- **Bootstrap 4.6.1** for styling
- **jekyll-scholar** for academic bibliography management
- **MathJax 3.2** for LaTeX math rendering
- **Kramdown** for Markdown processing
- **Mermaid** for diagrams (via jekyll-diagrams)
- **Jupyter** for notebook rendering

## Content Management

### Adding Publications

Add entries to `_bibliography/papers.bib` using BibTeX format. Supported custom fields:
- `abbr` - Conference/journal abbreviation badge (define in `_data/venues.yml`)
- `abstract` - Paper abstract (shown on click)
- `pdf`, `html`, `code`, `poster`, `slides` - Links to resources
- `preview` - Preview image filename (from `assets/img/publication_preview/`)
- `selected` - Mark as featured publication (`selected={true}`)
- `altmetric` - Altmetric badge ID
- Co-authors can be linked via `_data/coauthors.yml` for profile pictures/links

Publications are rendered using `_layouts/bib.html` and grouped by year in descending order.

### Editing CV

Edit `_data/cv.yml` following the structure:
- Sections: education, work, awards, etc.
- Each section has `title`, `type`, and `contents` array
- Contents support nested structures with `title`, `year`, `institution`, `description`
- The CV page uses `_includes/cv/` partials to render each section type

### Blog Posts

Create Markdown files in `_posts/` with format: `YYYY-MM-DD-title.md`
- Front matter must include: `layout: post`, `title`, `date`
- Optional: `tags`, `categories`, `description`, `related_posts`
- Blog is currently marked as "work in progress" with a message displayed on the blog page
