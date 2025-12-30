# Getting Started with Your Astro Site

## 🎉 Welcome!

Your retro cyber climate portfolio is ready! This guide will help you get started.

## 📁 Project Structure

```
llplm-astro/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── Header.astro     # Navigation header with theme toggle
│   │   ├── Footer.astro     # Footer with social links & ASCII art
│   │   ├── PixelEarth.astro # Rotating pixelated Earth visualization
│   │   └── PublicationCard.astro # Publication display card
│   ├── layouts/
│   │   └── BaseLayout.astro # Main page layout
│   ├── pages/              # Your website pages (auto-routed)
│   │   ├── index.astro     # Homepage (bio)
│   │   ├── publications.astro
│   │   ├── cv.astro
│   │   ├── photos.astro
│   │   └── 404.astro
│   ├── styles/
│   │   └── global.css      # Color palette & retro effects
│   └── utils/
│       └── bibParser.ts    # BibTeX parser for publications
├── public/                 # Static assets (copied as-is)
│   ├── data/
│   │   ├── papers.bib      # ✅ Migrated from Jekyll
│   │   └── cv.pdf          # ⚠️  Add your CV here
│   ├── photos/             # Photo projects
│   └── assets/
│       └── pic_llplm.JPG   # ✅ Migrated from Jekyll
└── package.json
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd /home/lpalma/git/llplm-astro
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

Visit **http://localhost:4321** to see your site!

### 3. Make Changes

The site will auto-reload as you edit files. Try:
- Edit `src/pages/index.astro` to change your bio
- Modify `src/styles/global.css` to tweak colors
- Update `public/data/papers.bib` to change publications

## 📝 Content Management

### Publications

**File**: `public/data/papers.bib`

```bibtex
@article{unique_id,
  title={Your Paper Title},
  author={Author, Name and Another, Author},
  year={2025},
  journal={Journal Name},
  doi={10.1234/example},
  url={https://example.com/paper},
  selected={true}  % Mark as featured
}
```

- Publications automatically sort by year (newest first)
- Use `selected={true}` to feature important papers
- The parser handles standard BibTeX fields

### CV

**File**: `public/data/cv.pdf`

Just replace this PDF file. The CV page will automatically display it.

### Photos

**Structure**: `public/photos/your-project-name/`

Each photo project needs:
1. A folder in `public/photos/`
2. An `info.json` file
3. Images

```json
{
  "title": "Mountain Photography",
  "description": "Analogue shots from the Pyrenees",
  "cover": "cover.jpg",
  "date": "2024",
  "photos": ["photo1.jpg", "photo2.jpg", "photo3.jpg"]
}
```

### Profile Image

**File**: `public/assets/pic_llplm.JPG`

Replace with your photo (any image format works, update filename in `index.astro` if needed).

## 🎨 Customization

### Colors

Edit `src/styles/global.css`:

```css
:root {
  --bg-primary: #EBE9E0;      /* Background color */
  --accent-blue: #0000FF;      /* Link & accent color */
  --text-primary: #1a1a1a;     /* Main text color */
  /* ... more colors ... */
}
```

### Bio

Edit `src/pages/index.astro`:
- Update text in the `<p>` tags
- Adjust years calculation if needed
- Modify layout

### Navigation

Edit `src/components/Header.astro`:
- Add/remove nav items in `navItems` array
- Change site title

### Footer Social Links

Edit `src/components/Footer.astro`:
- Update URLs in `socialLinks` array
- Add/remove social platforms

## 🌍 Climate Visuals

### Pixelated Earth

The rotating Earth in `src/components/PixelEarth.astro` can be customized:

```javascript
// Change rotation speed
rotation += 0.005;  // Lower = slower

// Change colors
const colors = {
  ocean: '#0000FF',
  land: '#00AA00',
  ice: '#FFFFFF',
  desert: '#CCAA66',
};
```

### Add More Visualizations

Ideas for climate-themed elements:
- Temperature stripe patterns
- Animated precipitation data
- Climate anomaly charts
- Weather icons in ASCII art

## 🚢 Deployment

### Option 1: GitHub Pages

```bash
# Build
npm run build

# Deploy dist/ folder to gh-pages branch
# (or configure GitHub Actions)
```

### Option 2: Vercel (Recommended)

1. Push to GitHub
2. Connect repo to Vercel
3. Deploy automatically

Vercel config (auto-detected for Astro):
```
Build Command: npm run build
Output Directory: dist
```

### Option 3: Netlify

Similar to Vercel - just connect your repo.

## 🔧 Development Commands

```bash
npm run dev      # Start dev server
npm run build    # Build for production
npm run preview  # Preview production build locally
```

## 🎯 What's Different from Jekyll?

| Feature | Jekyll | Astro |
|---------|--------|-------|
| Language | Ruby | JavaScript/TypeScript |
| Speed | Slower | Faster ⚡ |
| Dev Server | `bundle exec jekyll serve` | `npm run dev` |
| Build | Generated in `_site/` | Generated in `dist/` |
| Content | YAML + Markdown | Direct file imports |
| Publications | `papers.bib` parsed by plugin | `papers.bib` parsed at build time |

## 💡 Tips

1. **Fast refresh**: Astro reloads almost instantly when you save
2. **TypeScript**: Optional but helps catch errors
3. **Components**: Create reusable `.astro` components
4. **Static**: Everything is pre-built - super fast loading
5. **SEO**: Add meta tags in `BaseLayout.astro`

## 🐛 Troubleshooting

### Publications not showing?
- Check `public/data/papers.bib` exists
- Verify BibTeX syntax (closing braces, commas)
- Check browser console for errors

### Photos not loading?
- Ensure `info.json` has correct format
- Check image paths match `info.json`
- Images should be in same folder as `info.json`

### Styles not applying?
- Clear browser cache
- Check CSS syntax in `global.css`
- Verify CSS custom properties used correctly

## 📚 Learn More

- [Astro Docs](https://docs.astro.build)
- [Astro Component Syntax](https://docs.astro.build/en/core-concepts/astro-components/)
- [Tailwind CSS](https://tailwindcss.com/docs) (if you want to use it)

## 🎨 Next Steps

1. Add your CV PDF to `public/data/cv.pdf`
2. Add photo projects to `public/photos/`
3. Test the site locally
4. Customize colors/fonts to your taste
5. Deploy!

Enjoy your new site! 🚀
