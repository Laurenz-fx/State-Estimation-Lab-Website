---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %} Team

{% include section.html %}

{% capture list %}
  {% include list.html data="members" component="portrait" filter="role == 'pi'" grid=true %}
  {% include list.html data="members" component="portrait" filter="role != 'pi'" grid=true %}
{% endcapture %}

{{ list | markdownify }}
