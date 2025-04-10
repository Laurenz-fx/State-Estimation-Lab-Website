---
title: Publications
nav:
  order: 1
  tooltip: Published works
---

# Publications

{% include search-box.html %}
{% include search-info.html %}

{% assign publications = site.data.citations | sort: "date" | reverse %}
{% assign last_year = "" %}

{% for pub in publications %}
  {% assign pub_year = pub.date | date: "%Y" %}
  
  {% if pub_year != last_year %}
  ## {{ pub_year }}
  {% assign last_year = pub_year %}
  {% endif %}

  {% include citation.html d=pub style="rich" %}
{% endfor %}
