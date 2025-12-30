# Portfolio website code

Built with Astro. Features a retro cybernetic aesthetic with climate data visualizations.

## Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Content Management

### Publications
- Edit `public/data/papers.bib` to update publications
- Publications are automatically parsed and displayed
- Use `selected = {true}` in BibTeX to mark featured papers

### CV
- Replace `public/data/cv.pdf` with your CV
- The CV page will automatically display it

### Photos
- Add photo projects to `public/photos/`
- Each project needs an `info.json` file:

```json
{
  "title": "Project Name",
  "description": "Project description",
  "cover": "cover.jpg",
  "date": "2025",
  "photos": ["photo1.jpg", "photo2.jpg"]
}
```

### Profile Image
- Replace `public/assets/pic_llplm.JPG` with your photo

## Features

- 🎨 Swiss Design color palette (beige + blue light mode, terminal green dark mode)
- 🌍 Pixelated rotating Earth visualization
- 📚 Automatic publication parsing from .bib files
- 📱 Fully responsive design
- 🌓 Light/dark theme toggle
- ⚡ Fast static site generation with Astro

## Deployment

### GitHub Pages
```bash
npm run build
# Deploy dist/ folder to gh-pages branch
```

### Vercel (Recommended)
```bash
vercel --prod
```

## Customization

- Colors: Edit `src/styles/global.css` CSS variables
- Layout: Modify `src/layouts/BaseLayout.astro`
- Components: Add/edit files in `src/components/`
- Pages: Add/edit files in `src/pages/`

## Tech Stack

- **Astro** - Static site generator
- **TypeScript** - Type safety
- **CSS** - Custom properties for theming
- **JetBrains Mono** - Monospace font

## License

MIT
