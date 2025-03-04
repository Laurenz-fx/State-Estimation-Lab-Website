import scholarly
import yaml
import os

# Liste der Lab-Mitglieder
lab_members = ['Dieter Fox', 'Markus Grotz', 'Yi Li', 'Marius Memmel', 'Helen Wang', 'Jiafei Duan', 'Joel Jang', 'Ge Yan']

# Funktion, die Autoren eines Papers extrahiert
def get_authors_from_paper(paper):
    return paper.get('authors', [])

# Lade Papers von Google Scholar
def fetch_papers_from_google_scholar():
    return scholarly.search_pubs('Dieter Fox')

# Verarbeite die Papers
papers = fetch_papers_from_google_scholar()

# Erstelle eine Liste von relevanten Publikationen
relevant_papers = []

# Überprüfe, ob mindestens ein Lab-Mitglied als Autor dabei ist
for paper in papers:
    authors = get_authors_from_paper(paper)
    if any(member in authors for member in lab_members):
        print(f"Paper {paper['title']} enthält ein Lab-Mitglied.")
        # Erstelle das Paper-Objekt für die Website
        relevant_papers.append({
            'id': paper.get('doi', 'No DOI'),
            'title': paper['title'],
            'authors': authors,
            'link': paper.get('url', 'No URL'),
            'date': paper.get('date', 'No Date'),
            'image': paper.get('image', 'No Image'),
            'buttons': [
                {'type': 'website', 'link': paper.get('url', 'No URL')}
            ],
            'tags': paper.get('tags', []),
            'repo': paper.get('repo', 'No Repo')
        })
    else:
        print(f"Paper {paper['title']} enthält keine Lab-Mitglieder.")

# Speichern der relevanten Paper in einer YAML-Datei
with open('_data/publications.yml', 'w') as file:
    yaml.dump(relevant_papers, file)
