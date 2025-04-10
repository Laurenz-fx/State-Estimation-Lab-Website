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
    data=year.items
    component="citation"
    style="rich"
    sort="date"
    sort_order="desc"
    grid=false
  %}
{% endfor %}
