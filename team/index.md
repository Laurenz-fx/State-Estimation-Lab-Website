---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# Team

<div class="team-grid-wrapper">
  {% include list.html data="members" component="portrait" filter="role == 'faculty'" grid=true %}
  {% include list.html data="members" component="portrait" filter="role != 'faculty'" sort="lastname" grid=true %}
</div>
