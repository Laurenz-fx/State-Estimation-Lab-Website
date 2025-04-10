---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# Team

{% include section.html %}

<div class="team-grid-wrapper">
  {% include list.html data="members" component="portrait" filter="role == 'Faculty'" grid=true %}
</div>

<div class="team-grid-wrapper">
  {% include list.html data="members" component="portrait" filter="role != 'Faculty' and role != 'undergrad'" sort="lastname" grid=true %}
</div>

<hr class="team-divider">

<div class="team-grid-wrapper">
  {% include list.html data="members" component="portrait" filter="role == 'undergrad'" grid=true %}
</div>
