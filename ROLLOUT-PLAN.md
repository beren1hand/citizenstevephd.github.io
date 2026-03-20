# Citizen Steve PhD - Rollout Plan

**Strategy:** Phased weekly reveal of session details

---

## Current Status

**✅ Published (visible on site):**
- Homepage with "Oval Hours" schedule (dates + questions only)
- About page with legal framework
- Sessions page (teaser format, no details)
- Resources page (placeholder)

**✅ Created but unpublished (in repo, not linked):**
- `session1.md` - Full outline + evidence for Session 1

**📝 To be created:**
- `session2.md` through `session5.md` - Full outlines for remaining sessions

---

## Weekly Rollout Workflow

### Week Before Each Session

**1. Publish that session's detail page:**

Update `_layouts/default.html` navigation to add link:

```html
<!-- Example for Session 1 reveal (week of March 23) -->
<nav>
    <a href="{{ '/' | relative_url }}">🏛️ Home</a>
    <a href="{{ '/about' | relative_url }}">📜 About</a>
    <a href="{{ '/sessions' | relative_url }}">📚 Sessions</a>
    <a href="{{ '/session1' | relative_url }}">📅 Session 1</a>  <!-- NEW -->
    <a href="{{ '/resources' | relative_url }}">🔍 Resources</a>
</nav>
```

**2. Update homepage to link new session:**

Add button in Session 1 card:
```markdown
### 📅 Session 1: Did Donald Trump Start an Unjustified and Illegal War?
**Date:** Sunday, March 30, 2026  
**Time:** 2:00 PM - 3:30 PM  
**The Oval, OSU Campus**

<a href="/session1" class="button">📋 View Full Outline & Evidence</a>
```

**3. Commit and push:**

```bash
cd ~/projects/citizenstevephd
git add .
git commit -m "Reveal Session X outline and evidence"
git push origin main
git push github main  # Deploy to GitHub Pages
```

---

## Rollout Schedule

### Week of March 23, 2026
**Reveal:** Session 1 outline + evidence  
**Session date:** Sunday, March 30

### Week of March 30, 2026  
**Reveal:** Session 2 outline + evidence  
**Session date:** Sunday, April 6

### Week of April 6, 2026
**Reveal:** Session 3 outline + evidence  
**Session date:** Sunday, April 13

### Week of April 13, 2026
**Reveal:** Session 4 outline + evidence  
**Session date:** Sunday, April 20

### Week of April 20, 2026
**Reveal:** Session 5 outline + evidence  
**Session date:** Sunday, April 27

---

## Session Page Template

Each session page should include:

### 1. Header
- Session number and question
- Date, time, location
- Brief overview

### 2. Outline (structured)
- **Part 1: The Evidence** (30 min)
  - Key findings with sources
  - Conservative evidence prioritized
  
- **Part 2: The Monarchical Pattern** (15 min)
  - How this connects to founding principles
  - George III parallel
  
- **Part 3: Discussion & Q&A** (45 min)
  - Questions for exploration
  - Constitutional remedies

### 3. Evidence Documents Section
- Primary sources listed
- Research documentation
- Conservative sources highlighted

### 4. Discussion Ground Rules
- Evidence-based, good faith, respectful
- Public forum reminder

### 5. Navigation
- Links to schedule, home, next session
- Contact email
- Disclaimer

---

## Navigation Updates Needed

**Current navigation (all 5 sessions):**
```html
<nav>
    <a href="{{ '/' | relative_url }}">🏛️ Home</a>
    <a href="{{ '/about' | relative_url }}">📜 About</a>
    <a href="{{ '/sessions' | relative_url }}">📚 Sessions</a>
    <a href="{{ '/resources' | relative_url }}">🔍 Resources</a>
</nav>
```

**After revealing each session, add to nav:**
- Week 1: `<a href="/session1">📅 Session 1</a>`
- Week 2: `<a href="/session2">💰 Session 2</a>`
- Week 3: `<a href="/session3">🔍 Session 3</a>`
- Week 4: `<a href="/session4">🚔 Session 4</a>`
- Week 5: `<a href="/session5">👑 Session 5</a>`

**Alternative:** Create dropdown menu once multiple sessions revealed:
```html
<details>
    <summary>📚 Sessions</summary>
    <a href="/session1">📅 Session 1</a>
    <a href="/session2">💰 Session 2</a>
    <!-- etc -->
</details>
```

---

## Files to Create Before Launch

### High Priority (Week of March 23)
- ✅ `session1.md` (DONE)
- 📝 `session2.md` - Corruption/enrichment outline
- 📝 `session3.md` - Epstein network outline
- 📝 `session4.md` - ICE/police state outline
- 📝 `session5.md` - Monarchy synthesis outline

### Medium Priority
- 📝 `resources.md` update with actual resources list
- 📝 Evidence file hosting strategy (link to GitHub repo? Separate downloads page?)

### Nice to Have
- 📝 `/evidence/` directory with markdown versions of evidence files
- 📝 Printable handouts (PDF generation from markdown?)
- 📝 FAQ page

---

## Evidence Integration Strategy

**Option 1: Link to GitHub repo**
- Evidence files already in workspace
- Link directly to GitHub raw files
- Pro: Single source of truth
- Con: Less elegant than integrated site

**Option 2: Copy evidence to site**
- Create `/evidence/` directory
- Convert evidence .md files to site pages
- Pro: Everything in one place
- Con: Duplication, must keep in sync

**Option 3: Hybrid**
- Summary on site
- "Full documentation" links to GitHub
- Pro: Best of both
- Con: Maintain two presentations

**Recommendation:** Start with Option 1 (GitHub links), migrate to Option 2 if needed.

---

## Post-Session Updates

After each session, consider:

**1. Session recap:**
- Key questions that emerged
- Common concerns
- Attendance/engagement notes
- Refinements for future sessions

**2. FAQ additions:**
- Questions asked multiple times
- Clarifications needed
- Evidence requests

**3. Evidence updates:**
- New sources discovered
- Better conservative sourcing found
- Corrections/refinements

---

## Promotion Strategy (Optional)

**Week before each session:**
- Social media posts (if you use)
- Flyers on campus (if allowed/desired)
- Email to interested parties
- OSU calendar listings (if public events allowed)

**Keep it simple:**
- Date, time, location, question
- Link to citizenstevephd.com
- "Public education in public forum"

---

## Backup Plans

**If weather bad:**
- Rain: Bring umbrella, continue (you're dedicated!)
- Extreme weather: Post cancellation/reschedule on homepage

**If challenged by OSU:**
- Reference legal memo
- Stand on First Amendment rights
- Document interaction
- Continue unless physical barrier

**If low turnout:**
- Doesn't matter - you're exercising free speech
- Even one curious person = success
- Document and improve for next week

**If high turnout:**
- Bring backup handouts
- Stay on time (respect 90 min limit)
- Offer to stay after for individual Q&A

---

## Success Metrics

**Not:**
- Number of attendees
- Agreement with conclusions
- Media coverage

**But:**
- Evidence presented clearly
- Questions engaged honestly
- Constitutional conversation happening
- People thinking critically

**The goal:** Invite exploration using founders' own standards, not convert to specific viewpoint.

---

## Quick Reference: Week Before Session 1

**March 23-29, 2026:**

```bash
# 1. Update navigation in default.html
# Add Session 1 link

# 2. Update index.md
# Add button to Session 1 in card

# 3. Commit and deploy
cd ~/projects/citizenstevephd
git add _layouts/default.html index.md
git commit -m "Reveal Session 1 outline and evidence"
git push origin main
git push github main

# 4. Verify on citizenstevephd.com
# Check that Session 1 link appears and works

# 5. Prepare physical materials
# Print session1.md outline
# Prepare any handouts
# Check costume ready
```

**You're good to go!**

---

**Questions about rollout?** This is a living document - update as you learn what works.
