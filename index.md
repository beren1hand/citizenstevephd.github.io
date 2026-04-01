---
layout: default
title: Home
show_hero: true
---

## Sessions

{% assign sessions = site.posts | sort: "date" %}
<ul class="session-list">
{% for post in sessions %}
  {% assign session_num = forloop.index %}
  {% assign post_ts = post.date | date: "%s" | plus: 0 %}
  {% assign now_ts = site.time | date: "%s" | plus: 0 %}
  {% assign title = post.title | remove: "Session 1: " | remove: "Session 2: " | remove: "Session 3: " | remove: "Session 4: " | remove: "Session 5: " %}
  <li>
    <span class="session-number">{{ session_num }}.</span>
    {% if post_ts <= now_ts %}
      <a href="{{ post.url | relative_url }}">{{ title }}</a>
    {% else %}
      <span class="coming-soon">{{ title }}</span>
      <span class="coming-soon-badge">Coming Soon</span>
    {% endif %}
    <span class="session-date">{{ post.date | date: "%B %-d, %Y" }}</span>
  </li>
{% endfor %}
</ul>

---

<div class="about-section" markdown="1">

## About Citizen Steve

**Citizen Steve** provides evidence-based education examining critical questions about American democracy and constitutional governance. Five weekly sessions, each driven by a single question, using PhD-level rigor in accessible presentation.

**The approach:** Not telling you what to think—providing evidence so you can decide for yourself. Every claim sourced. Conservative and cross-partisan sourcing (Fox News, court records, Trump's own appointees). Grounded in founding principles.

**The goal:** To examine whether current governance patterns match the monarchical behaviors America's founders rejected—using their own standards.

**Location:** The Oval at THE Ohio State University (traditional public forum)
**Time:** Wednesdays, 1:00–2:00 PM
**Contact:** [steve@citizenstevephd.com](mailto:steve@citizenstevephd.com)

<div class="disclaimer" markdown="1">

**Disclaimer:** Citizen Steve does not represent The Ohio State University. These sessions are conducted by an individual exercising personal First Amendment rights in a traditional public forum. They are not sponsored, endorsed, or affiliated with OSU. The Oval is a traditional public forum under Ohio law (ORC 3345.0215) and OSU policy. The costume and persona establish clear separation from any professional role. All activities comply with Ohio Senate Bill 1 (2025), which protects academic freedom and free speech.

</div>
</div>
