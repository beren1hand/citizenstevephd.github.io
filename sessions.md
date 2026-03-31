---
layout: default
title: All Sessions
---

# 📚 Citizen Steve's Oval Hours

## All Sessions

**Location:** The Oval, Ohio State University  
**Time:** Sundays, 2:00 PM - 3:30 PM  
**Format:** Evidence presentation, open discussion, Q&A

Each session examines one critical question about American democracy and constitutional governance using evidence-based analysis and founding principles.

---

{% for post in site.posts %}
<div class="card">

## {{ post.title }}

**{{ post.date | date: "%A, %B %d, %Y" }}**  
**2:00 PM - 3:30 PM, The Oval**

{{ post.excerpt }}

{% if post.date <= site.time %}
<a href="{{ post.url | relative_url }}" class="button">📋 View Full Outline & Evidence</a>
{% else %}
*Full outline will be available closer to session date*
{% endif %}

</div>
{% endfor %}

---

## 🗽 Public Forum Rights

These sessions occur in a traditional public forum under Ohio law (ORC 3345.0215) and OSU policy. All viewpoints welcome. Free speech protected.

**Not affiliated with OSU** - see [About](/about) page for legal framework and disclaimer.

---

<a href="/" class="button button-blue">🏛️ Back to Home</a>
