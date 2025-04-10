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

  <div class="citation-year-group">
    {% for pub in year.items %}
      {% include citation.html
        title=pub.title
        authors=pub.authors
        publisher=pub.publisher
        date=pub.date
        link=pub.link
        image=pub.image
        description=pub.description
      %}
    {% endfor %}
  </div>

{% endfor %}
