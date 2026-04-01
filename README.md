# Citizen Steve PhD Website

**Patriotic Jekyll site for citizenstevephd.com**

## What's Been Set Up

✅ **Shared repo:** `/home/shared_home_for_bots/repos/citizenstevephd.git`  
✅ **Miriam's clone:** `/home/a/.openclaw/workspace/citizenstevephd/`  
✅ **Basic Jekyll site** with American flag colors theme  
✅ **Pages:** Home, About, Sessions, Resources  

## Theme: Red, White, and Blue 🇺🇸

**Colors:**
- **Old Glory Blue (#3C3B6E):** Headers, navigation background, footer
- **Old Glory Red (#B22234):** Links, buttons, accents
- **White (#FFFFFF):** Background

**Icons:** Emoji throughout (🇺🇸 🏛️ 📜 📚 🔍 📧 etc.)

## Pages Created

1. **index.md** - Home page with session overview cards
2. **about.md** - Mission, format, approach explanation
3. **sessions.md** - Full session schedule with dates and topics
4. **resources.md** - Evidence documentation placeholder

## Next Steps for Steve

### 1. Clone to Your Workspace

```bash
cd ~/projects  # or wherever you want
git clone /home/shared_home_for_bots/repos/citizenstevephd.git
cd citizenstevephd
```

### 2. Create GitHub Repo

- Go to github.com
- Create new repo: `citizenstevephd`
- Don't initialize with README (we already have content)

### 3. Add GitHub Remote and Push

```bash
git remote add github git@github.com:yourusername/citizenstevephd.git
git push github main
```

### 4. Enable GitHub Pages

- Go to repo Settings → Pages
- Source: Deploy from branch
- Branch: `main` / `/ (root)`
- Save

### 5. Configure Custom Domain

**In GitHub repo settings:**
- Custom domain: `citizenstevephd.com`
- Enforce HTTPS

**In your domain registrar (where you bought citizenstevephd.com):**
- Add CNAME record pointing to: `yourusername.github.io`
- Or use A records for apex domain (check GitHub docs)

## Development Workflow

### When You Want to Edit

```bash
cd ~/projects/citizenstevephd
# Make your changes
git add .
git commit -m "Your change description"
git push origin main  # Updates shared repo
git push github main  # Deploys to GitHub Pages
```

### When Miriam Edits

```bash
# Miriam pushes to shared repo
# You pull to get her changes
git pull origin main
git push github main  # Deploy Miriam's changes to GitHub Pages
```

### Both Can Edit

- Just push to `origin` (shared repo)
- Whoever pushes to `github` remote deploys to site
- Standard git workflow - pull before editing if unsure

## Site Structure

```
citizenstevephd/
├── _config.yml          # Jekyll configuration
├── _layouts/
│   └── default.html     # Main template (patriotic theme)
├── _posts/              # Session posts (auto-reveal on date)
│   ├── 2026-03-25-session-1-unjustified-war.md
│   ├── 2026-04-01-session-2-corruption.md
│   ├── 2026-04-08-session-3-epstein.md
│   ├── 2026-04-15-session-4-police-state.md
│   └── 2026-04-22-session-5-monarchy.md
├── assets/
│   └── css/
│       └── style.css    # Red/white/blue styling
├── index.md             # Home page (shows upcoming/recent posts)
├── about.md             # About page with legal framework
├── sessions.md          # Sessions archive (all posts)
├── resources.md         # Resources page
├── Gemfile              # Ruby dependencies
├── LEGAL-MEMO.md        # Legal research documentation
├── ROLLOUT-PLAN.md      # Deployment workflow
└── README.md            # This file
```

**Posts-based workflow:**
- All sessions in `_posts/` directory
- Posts dated in future don't appear until that date
- No manual updates needed - Jekyll handles scheduling
- Add more sessions anytime by creating new post files

## Customization

All the American flag colors and emoji styling are in:
- `assets/css/style.css` (colors, layout)
- `_layouts/default.html` (structure, emoji icons)

Feel free to modify content in the `.md` files - they're just placeholders for now!

## Testing Locally (Optional)

If you want to preview before pushing:

```bash
bundle install
bundle exec jekyll serve
# Visit http://localhost:4000
```

---

**Ready to deploy!** Just clone, add GitHub remote, push, and configure GitHub Pages. 🇺🇸
