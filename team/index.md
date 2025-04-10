---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# Team

{% include section.html %}

## Faculty and Phd Students

<div class="team-grid-wrapper">
  {% include list.html data="members" component="portrait" filter="role != 'undergrad'" sort="lastname" grid=true %}
</div>

## Undergrad Students

<div class="team-grid-wrapper">
  {% include list.html data="members" component="portrait" filter="role == 'undergrad'" grid=true %}
</div>

## Alumni

<ul class="alumni-list">
  {% for alumni in site.data.alumni %}
    <li>{{ alumni.name }}</li>
  {% endfor %}
</ul>

