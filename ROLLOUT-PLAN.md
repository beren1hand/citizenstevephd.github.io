# Citizen Steve PhD - Rollout Plan (Posts-Based)

**Strategy:** Jekyll posts auto-reveal on their scheduled dates

---

## How It Works

**Jekyll's built-in post system:**
- Posts dated in the future don't appear on site until that date
- All 5 sessions created now in `_posts/` directory
- Automatically appear on their scheduled dates
- No manual navigation updates needed!

**File naming convention:**
```
_posts/YYYY-MM-DD-slug.md
```

**Front matter includes:**
```yaml
---
layout: default
title: "Session Title"
date: 2026-MM-DD HH:MM:SS -0400
categories: sessions
---
```

---

## What's Already Set Up

✅ **All 5 session posts created:**
- `2026-03-30-session-1-unjustified-war.md` (full outline)
- `2026-04-06-session-2-corruption.md` (placeholder)
- `2026-04-13-session-3-epstein.md` (placeholder)
- `2026-04-20-session-4-police-state.md` (placeholder)
- `2026-04-27-session-5-monarchy.md` (placeholder)

✅ **Homepage automatically shows:**
- Upcoming sessions (future dates)
- Recent sessions (past dates)
- Links to full outlines when available

✅ **Sessions page:**
- Archive of all posts
- Chronological order
- Links active when dates pass

---

## Reveal Schedule

**Automatic - no action required:**
- March 30: Session 1 appears (full outline already there)
- April 6: Session 2 appears (need to flesh out)
- April 13: Session 3 appears (need to flesh out)
- April 20: Session 4 appears (need to flesh out)
- April 27: Session 5 appears (need to flesh out)

---

## What You Need to Do

### Before Launch (This Week)
1. **Clone and deploy to GitHub:**
   ```bash
   cd ~/projects
   git clone /home/shared_home_for_bots/repos/citizenstevephd.git
   cd citizenstevephd
   git remote add github git@github.com:yourusername/citizenstevephd.git
   git push github main
   ```

2. **Enable GitHub Pages** in repo settings

3. **Point DNS** citizenstevephd.com → GitHub Pages

4. **Test:** Site goes live with Session 1 already visible (March 30 is past when you deploy)

---

### Before Each Session (Optional - Flesh Out Posts)

**Week before April 6:**
- Edit `_posts/2026-04-06-session-2-corruption.md`
- Add full outline with evidence (like Session 1)
- Commit and push

**Week before April 13:**
- Edit `_posts/2026-04-13-session-3-epstein.md`
- Add full outline
- Commit and push

**And so on...**

**OR:** Leave them as placeholders - they'll still appear on schedule, just with less detail.

---

## Adding More Sessions Later

**It's trivial now!**

Just create a new file in `_posts/`:
```bash
# Create new session post
touch _posts/2026-05-04-session-6-whatever.md

# Edit with outline
# Commit and push
```

**Jekyll automatically:**
- Adds it to sessions archive
- Shows it on homepage when date arrives
- Generates proper URL

**No site structure changes needed.**

---

## URL Structure

Posts automatically get clean URLs:
- `/sessions/2026/03/30/session-1-unjustified-war/`
- `/sessions/2026/04/06/session-2-corruption/`
- etc.

---

## Navigation

**Current navigation is simple:**
```
🏛️ Home | 📜 About | 📚 Sessions | 🔍 Resources
```

**That's it. No need to add individual session links.**

Sessions page shows all posts in chronological order.

---

## Benefits of This Approach

✅ **Scalable:** Add sessions anytime, no navigation changes  
✅ **Automatic:** Posts appear on schedule without manual updates  
✅ **Flexible:** Can add 6th, 7th, 8th session easily  
✅ **Clean:** No hardcoded lists to maintain  
✅ **Standard:** Using Jekyll as designed  

---

## Editing Existing Posts

**To update Session 1 (or any post):**

```bash
cd ~/projects/citizenstevephd
git pull origin main  # Get latest from shared repo

# Edit the post
nano _posts/2026-03-30-session-1-unjustified-war.md

# Commit and deploy
git add _posts/
git commit -m "Update Session 1 outline"
git push origin main  # To shared repo
git push github main  # Deploy to site
```

**Changes appear immediately on site.**

---

## Post Front Matter Explained

```yaml
---
layout: default              # Use site's default layout
title: "Session Title"       # Appears in browser tab, page header
date: 2026-03-30 14:00:00 -0400  # Date + time (EST = -0400)
categories: sessions         # Can filter by category later
---
```

**The date controls when post appears:**
- Future date → Hidden until that date
- Past/current date → Visible immediately

---

## Testing Locally (Optional)

If you want to see future posts before their dates:

```bash
cd ~/projects/citizenstevephd
bundle install
bundle exec jekyll serve --future

# Visit http://localhost:4000
# All posts visible regardless of date
```

**Without `--future` flag:** Jekyll respects dates (like production)

---

## Workflow Summary

**Now (one time):**
1. Clone repo
2. Push to GitHub
3. Enable GitHub Pages
4. Point DNS

**Ongoing (optional):**
1. Edit `_posts/2026-XX-XX-filename.md` to flesh out
2. Commit and push
3. Post auto-appears on its date

**That's it!** Much simpler than manual navigation updates.

---

## Success Metrics

**Site works if:**
- Session 1 visible on homepage (date has passed)
- Sessions 2-5 show as "coming soon" (future dates)
- Each Sunday, new session appears automatically
- Archive page shows all sessions chronologically

**No manual intervention required between now and April 27.**

---

## Quick Reference: GitHub Deployment

```bash
# One-time setup
cd ~/projects
git clone /home/shared_home_for_bots/repos/citizenstevephd.git
cd citizenstevephd
git remote add github git@github.com:yourusername/citizenstevephd.git
git push github main

# Then enable GitHub Pages in repo settings:
# Settings → Pages → Source: main branch → Save

# Point DNS:
# Add CNAME: citizenstevephd.com → yourusername.github.io
# Or A records to GitHub Pages IPs

# Site live at https://citizenstevephd.com
```

**You're done. Posts will appear on schedule automatically. 🇺🇸**

---

**Questions?** This approach is much cleaner. You can add sessions 6, 7, 8 later without touching site structure.
