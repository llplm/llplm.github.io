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

Deployment is automatic via GitHub Actions on push to master. For manual deployment:
```bash
bin/deploy
```

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

### Templates

- `_layouts/` - Page templates (default, post, cv, distill, bib)
- `_includes/` - Reusable components (header, footer, CV sections)
- `_sass/` - SCSS stylesheets

### Custom Plugins

`_plugins/` contains Ruby plugins for cache busting, bibliography helpers, and other Jekyll extensions.

## Key Configuration

Main configuration is in `_config.yml`:
- Site metadata and social links
- jekyll-scholar settings for BibTeX bibliography (source: `_bibliography/`, style: APA)
- Theme settings (light/dark mode, syntax highlighting)
- Plugin configuration

## Technology Stack

- **Jekyll 4.x** with Ruby 3.2.2+
- **Bootstrap 4.6.1** for styling
- **jekyll-scholar** for academic bibliography management
- **MathJax 3.2** for LaTeX math rendering
- **Kramdown** for Markdown processing

## Adding Publications

Add entries to `_bibliography/papers.bib` using BibTeX format. Supported fields:
- `abbr` - Conference/journal abbreviation badge
- `abstract` - Paper abstract
- `pdf`, `html`, `code`, `poster`, `slides` - Links to resources
- `preview` - Preview image filename
- `selected` - Mark as featured publication
