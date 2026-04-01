---
layout: default
title: Home
---

# 🇺🇸 Welcome to Citizen Steve PhD

## Evidence-Based Education on American Democracy

**Citizen Steve's Oval Hours:** Public education on critical questions about American democracy and constitutional governance.

**Location:** The Oval, Ohio State University (traditional public forum)  
**Time:** Wednesdays, 1:00 PM - 2:00 PM  
**Approach:** PhD-level rigor, accessible presentation, all evidence sourced

---

## Upcoming Sessions

{% assign future_posts = site.posts | where_exp: "post", "post.date >= site.time" | sort: "date" %}
{% assign past_posts = site.posts | where_exp: "post", "post.date < site.time" | sort: "date" | reverse %}

{% if future_posts.size > 0 %}
### Next Up

{% for post in future_posts limit:3 %}
<div class="card">

#### {{ post.title }}
**{{ post.date | date: "%A, %B %d, %Y" }}**  
**1:00 PM - 2:00 PM, The Oval**

{% if post.date <= site.time %}
<a href="{{ post.url | relative_url }}" class="button">📋 View Full Outline</a>
{% else %}
*Full outline and evidence will be available closer to session date*
{% endif %}

</div>
{% endfor %}
{% endif %}

{% if past_posts.size > 0 %}
### Recent Sessions

{% for post in past_posts limit:2 %}
<div class="card">

#### {{ post.title }}
**{{ post.date | date: "%B %d, %Y" }}**

<a href="{{ post.url | relative_url }}" class="button">📖 View Session</a>

</div>
{% endfor %}

<a href="/sessions" class="button button-blue">📚 View All Sessions</a>
{% endif %}

---

## Principles

✅ **Evidence-based** - Every claim sourced and documented  
✅ **Constitutional focus** - Grounded in founding principles  
✅ **Cross-partisan sources** - Fox News, court records, Trump appointees  
✅ **Question-driven** - Inviting exploration, not imposing conclusions  
✅ **Public forum** - Open to all, free speech protected under Ohio law

---

## About Citizen Steve

**Citizen Steve** is an individual exercising First Amendment rights in a public forum. These sessions are not affiliated with The Ohio State University - they represent personal political speech protected under the Constitution and Ohio law.

The costume and persona establish clear separation from professional role. This is scholarship in service of democracy.

<a href="/about" class="button button-blue">📜 Learn More About Legal Framework</a>

---

## 🗽 Free Speech on Campus

These sessions occur in a **traditional public forum** (The Oval) under Ohio law and OSU policy. All viewpoints are welcome. Evidence-based inquiry is protected speech.

See [About](/about) page for complete legal framework and disclaimer.
