#!/usr/bin/env python3
"""
Migration script to copy content from Jekyll site to Astro site
"""

import os
import shutil
from pathlib import Path

# Paths
JEKYLL_ROOT = Path("/home/lpalma/git/llplm.github.io")
ASTRO_ROOT = Path("/home/lpalma/git/llplm-astro")

def migrate_publications():
    """Copy publications .bib file"""
    print("📚 Migrating publications...")

    src = JEKYLL_ROOT / "_bibliography" / "papers.bib"
    dst = ASTRO_ROOT / "public" / "data" / "papers.bib"

    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"   ✓ Copied {src} → {dst}")
    else:
        print(f"   ⚠ Source not found: {src}")

def migrate_profile_image():
    """Copy profile image"""
    print("🖼️  Migrating profile image...")

    # Find profile image
    src = JEKYLL_ROOT / "assets" / "img" / "pic_llplm.JPG"
    dst = ASTRO_ROOT / "public" / "assets" / "pic_llplm.JPG"

    if src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        print(f"   ✓ Copied {src} → {dst}")
    else:
        print(f"   ⚠ Source not found: {src}")

def migrate_cv_pdf():
    """Look for CV PDF and copy it"""
    print("📄 Looking for CV PDF...")

    # Common CV locations
    possible_locations = [
        JEKYLL_ROOT / "assets" / "pdf" / "cv.pdf",
        JEKYLL_ROOT / "assets" / "pdf" / "CV_LluisPalma.pdf",
        JEKYLL_ROOT / "assets" / "cv.pdf",
    ]

    dst = ASTRO_ROOT / "public" / "data" / "cv.pdf"
    dst.parent.mkdir(parents=True, exist_ok=True)

    found = False
    for src in possible_locations:
        if src.exists():
            shutil.copy2(src, dst)
            print(f"   ✓ Copied {src} → {dst}")
            found = True
            break

    if not found:
        print("   ⚠ No CV PDF found. You'll need to add one manually to /public/data/cv.pdf")

def create_photo_project_example():
    """Create example photo project structure"""
    print("📷 Creating example photo project...")

    example_dir = ASTRO_ROOT / "public" / "photos" / "example-project"
    example_dir.mkdir(parents=True, exist_ok=True)

    # Create info.json
    info = {
        "title": "Example Project",
        "description": "Replace this with your photo project",
        "cover": "cover.jpg",
        "date": "2025",
        "photos": ["photo1.jpg", "photo2.jpg"]
    }

    import json
    with open(example_dir / "info.json", "w") as f:
        json.dump(info, f, indent=2)

    print(f"   ✓ Created {example_dir}/info.json")
    print("   ⚠ Add your photos to /public/photos/example-project/")

def create_readme():
    """Create README with instructions"""
    print("📝 Creating README...")

    readme_content = """# Lluís Palma - Retro Cyber Climate Portfolio

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
"""

    with open(ASTRO_ROOT / "README.md", "w") as f:
        f.write(readme_content)

    print("   ✓ Created README.md")

def create_gitignore():
    """Create .gitignore"""
    gitignore_content = """# Dependencies
node_modules/

# Build output
dist/
.astro/

# Environment
.env
.env.local

# Logs
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Editor
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
"""

    with open(ASTRO_ROOT / ".gitignore", "w") as f:
        f.write(gitignore_content)

    print("   ✓ Created .gitignore")

def main():
    print("🚀 Starting content migration from Jekyll to Astro")
    print(f"   Source: {JEKYLL_ROOT}")
    print(f"   Target: {ASTRO_ROOT}\n")

    # Run migrations
    migrate_publications()
    migrate_profile_image()
    migrate_cv_pdf()
    create_photo_project_example()
    create_readme()
    create_gitignore()

    print("\n✅ Migration complete!")
    print("\nNext steps:")
    print("1. cd /home/lpalma/git/llplm-astro")
    print("2. npm install")
    print("3. npm run dev")
    print("4. Visit http://localhost:4321")
    print("\n💡 Check README.md for full documentation")

if __name__ == "__main__":
    main()
