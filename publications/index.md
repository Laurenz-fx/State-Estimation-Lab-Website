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
{% assign publications_by_year = publications | group_by_exp: "pub", "pub.date | date: '%Y'" %}

{% for year in publications_by_year %}
  ## {{ year.name }}

  {% include list.html 
    data="citations" 
    component="citation" 
    style="rich" 
    filter="date contains '{{ year.name }}'" 
    sort="date" 
    sort_order="desc"
  %}
{% endfor %}
