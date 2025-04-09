---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %} Team

{% include section.html %}

<div class="team-grid-wrapper">
  {% include list.html data="members" component="portrait" filter="role == 'faculty'" grid=true %}
  {% include list.html data="members" component="portrait" filter="role != 'faculty'" sort="last_name" grid=true %}
</div>
