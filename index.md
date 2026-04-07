---
layout: default
title: Home
show_hero: true
description: "Revolution. American-Style!"
---

<h2 class="home-title text-red">🇺🇸 Revolution. American-Style!</h2>

<p class="home-mantra text-blue">We get loud. We get in the way. We get out the vote! ✊🏿✊🏾✊🏽✊🏼✊🏻</p>

- The founders fought a violent revolution **so we'd never have to fight one again** — they gave us a Constitution, the rule of law, and the tools for **peaceful transitions of power** 📜
- Those tools require <span class="text-red-bold">free and fair elections</span> with **every eligible citizen able to vote** 🗳️ — voter restrictions suppress turnout and harm democracy, while evidence of substantial voter fraud is essentially <span class="text-red-bold">nonexistent</span>
- The **suffragists** showed us how to fight for those tools — they marched, they disrupted, they got arrested, and <span class="text-red-bold">they won</span> ✊
- The **civil rights movement** showed us again — sit-ins, boycotts, freedom rides, bold and creative acts of non-violent resistance that <span class="text-red-bold">changed the law of the land</span>
- This is our inheritance. **Not quiet compliance. Not polite silence.** Tools only work if you **pick them up.**
  - **Active.**
  - **Non-violent.**
  - **Disruptive.**
  - <span class="text-red-bold">Democracy-shaking protest.</span>
- That's the American tradition. <span class="text-red-bold">It's time to use it.</span> 🗽

---

<h2 class="home-title">📣 Sessions</h2>

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

<div class="about-section" markdown="1">

<h2 class="home-title">📄 Academic Paper on the Epstein Files</h2>

**WARNING: Contains PhD-level firepower.** 🔥

- Citizen Steve didn't just make a sign and yell on the Oval — he wrote a **full academic paper** on why the Epstein cover-up is a direct threat to American democracy 🇺🇸
- The horrors alleged in the Epstein files aren't "extraordinary claims" — they're **historically ordinary features of concentrated, unaccountable power**
- The paper lays out a clear framework: **prosecutorial vs. epistemic vs. investigative** standards — and shows how conflating them protects the powerful
- The government's own desperate suppression of documents is <span class="text-red-bold">evidence of the severity of what they're hiding</span>
- The rational warrant for a full investigation is <span class="text-red-bold">overwhelming</span> — if your senator says "there's no evidence," hand them this paper 🦅

<a href="/epstein_academic/" class="button button-blue">📄 Read the Full Academic Paper</a>

</div>

<div class="about-section" markdown="1">

<h2 class="home-title">🦅 About Citizen Steve</h2>

**Citizen Steve** provides **evidence-based education** examining critical questions about American democracy and constitutional governance. Five weekly sessions, each driven by a **single question**, using PhD-level rigor in accessible presentation.

**The goal:** To examine whether current governance patterns match the **monarchical behaviors America's founders rejected** — using their own standards. ⚖️

**Location:** 📍 The Oval at <span class="text-red-bold">THE</span> Ohio State University

**Time:** 🕐 Wednesdays, 1:00–2:00 PM for the rest of the Spring '26 semester

<div class="disclaimer" markdown="1">

**Disclaimer:** Citizen Steve does not represent The Ohio State University. These sessions are conducted by an individual exercising personal First Amendment rights in a traditional public forum. They are not sponsored, endorsed, or affiliated with OSU. The Oval is a traditional public forum under Ohio law (ORC 3345.0215) and OSU policy. The costume and persona establish clear separation from any professional role. All activities comply with Ohio Senate Bill 1 (2025), which protects academic freedom and free speech.

</div>
</div>
