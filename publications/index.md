---
title: Publications
nav:
  order: 1
  tooltip: Published works
---

# Publications

{% include search-box.html %}
{% include search-info.html %}

{% assign sorted_citations = site.data.citations | sort: "date" | reverse %}
{% assign current_year = "" %}

{% for citation in sorted_citations %}
  {% assign year = citation.date | slice: 0, 4 %}
  {% if year != current_year %}
    <h2>{{ year }}</h2> <!-- <<< richtige HTML-Überschrift -->
    {% assign current_year = year %}
  {% endif %}
  
  {% include citation.html item=citation style="rich" %}
{% endfor %}
