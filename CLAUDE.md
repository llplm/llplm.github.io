# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal portfolio website for Lluís Palma built with Astro. It features a retro cybernetic aesthetic with climate data visualizations, publications management via BibTeX parsing, and a photography gallery. The site uses a Swiss Design color palette in light mode (beige + blue) and terminal green in dark mode.

## Development Commands

```bash
# Install dependencies
npm install

# Start development server (http://localhost:4321)
npm run dev

# Build for production (outputs to dist/)
npm run build

# Preview production build locally
npm run preview
```

## Architecture

### Core Structure

- **src/layouts/BaseLayout.astro** - Main layout wrapper for all pages, includes global CSS, Header, Footer, and theme toggle script
- **src/pages/** - File-based routing (index.astro, publications.astro, cv.astro, photos.astro, blog.astro, 404.astro)
- **src/components/** - Reusable UI components (Header, Footer, PixelEarth, PublicationCard)
- **src/utils/bibParser.ts** - BibTeX parser for publications with LaTeX character cleaning
- **src/styles/global.css** - CSS custom properties for theming, retro effects (CRT scanlines, glitch animations, pixelation)
- **public/** - Static assets served as-is (data files, photos, assets)

### Theme System

The site uses CSS custom properties with a `data-theme` attribute toggle:
- Theme state stored in localStorage
- Toggle function defined globally in BaseLayout.astro as `window.toggleTheme()`
- Two color schemes: light (Swiss Design beige + blue) and dark (terminal green)
- CRT scanline effect applied via `body::before` pseudo-element

### Publications System

Publications are managed via BibTeX:
1. **Source**: `public/data/papers.bib` - BibTeX formatted publication list
2. **Parser**: `src/utils/bibParser.ts` - Parses BibTeX at build time, cleans LaTeX characters, extracts metadata
3. **Display**: `src/pages/publications.astro` - Reads file via Node.js `fs`, groups by year, shows featured papers
4. **Featured Papers**: Use `selected={true}` in BibTeX entries to mark as featured

Key parser features:
- Cleans LaTeX special characters and accents (e.g., `\'{i}` → `í`)
- Sorts publications by year (descending)
- Extracts: title, author, year, journal, booktitle, volume, pages, doi, url, arxiv, abstract, citations
- `formatAuthors()` utility truncates long author lists

### Photos System

Simple filesystem-based photo gallery:
- **Location**: `public/photos/` - Recursively scans for image files (.jpg, .jpeg, .png, .gif, .webp)
- **Display**: `src/pages/photo.astro` - Uses Node.js `fs.readdirSync()` at build time
- Features:
  - Responsive grid layout that preserves original image aspect ratios
  - Click-to-expand lightbox with keyboard navigation (arrow keys, ESC)
  - Pixelated hover effect consistent with retro theme
  - Next/Previous navigation in lightbox mode

### PixelEarth Component

Animated canvas visualization (`src/components/PixelEarth.astro`):
- 200x200 canvas with pixelated rendering
- Draws rotating Earth with color-coded regions (ocean, land, ice, desert)
- Rotation driven by `requestAnimationFrame` loop
- Displays climate stats (CO₂, temperature anomaly)
- Uses 4px pixel size for retro aesthetic

## Configuration

- **astro.config.mjs** - Site URL: `https://llplm.github.io`, integrations: MDX + Tailwind, output: static
- **tsconfig.json** - Extends `astro/tsconfigs/strict`, JSX configured for React (though not currently used)
- No custom Tailwind config - uses Tailwind integration defaults

## Content Management

### Publications
Edit `public/data/papers.bib` with standard BibTeX format. Use `selected={true}` to feature papers.

### CV
Replace `public/data/cv.pdf` with updated CV file.

### Photos
Add image files to `public/photos/` - they'll be automatically discovered and displayed.

### Profile Image
Update `public/assets/pic_llplm.JPG` and reference in pages as needed.

## Key Implementation Details

- **Build-time Data Loading**: Publications and photos are loaded at build time using Node.js `fs` module in Astro components (server-side only)
- **No Client-Side Fetching**: All data is embedded during static site generation
- **Global Script**: Theme toggle is defined in BaseLayout.astro as a global `window.toggleTheme()` function for cross-component access
- **Sticky Header**: Navigation uses `position: sticky` with z-index layering
- **Retro Effects**: Global CSS provides `.retro-border`, `.retro-button`, `.pixelated`, `.glitch-text`, `.blink` utility classes

## Navigation Structure

Defined in `src/components/Header.astro`:
- About (/)
- Publications (/publications)
- Blog (/blog)
- CV (/cv)
- Photo (/photo)

Active page detection via `Astro.url.pathname` comparison.

## Styling Approach

Hybrid CSS approach:
- CSS custom properties in `global.css` for theming
- Scoped `<style>` blocks in `.astro` components
- Tailwind available but minimally used (imported via integration)
- Monospace font: JetBrains Mono from Google Fonts

## Deployment

Static site outputs to `dist/` directory. Configured for GitHub Pages deployment at `https://llplm.github.io`.
