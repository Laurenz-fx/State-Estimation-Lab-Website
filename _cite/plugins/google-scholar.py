from scholarly import scholarly
import requests
import yaml  # Zum Bearbeiten von YAML-Dateien
import os

# Fixed Google Scholar ID for Dieter Fox
SCHOLAR_ID = "DqXsbPAAAAAJ"

def load_allowed_authors(filename=os.path.join("_data", "allowed*authors.yaml")):
    """Lädt die Liste der erlaubten Autoren aus einer YAML-Datei."""
    try:
        with open(filename, "r") as file:
            data = yaml.safe_load(file)
            return set(data.get("allowed_authors", []))
    except FileNotFoundError:
        print(f"Warning: {filename} nicht gefunden. Keine Filterung angewendet.")
        return set()

ALLOWED_AUTHORS = load_allowed_authors()

def ensure_list_of_dicts(data):
    """Ensure that data is always a list of dictionaries."""
    if not isinstance(data, list):
        # Falls die Antwort keine Liste ist, erstellen wir eine leere Liste
        data = []
    
    # Wenn die Antwort keine Dictionaries enthält, dann erstellen wir ein leeres Dictionary für jedes Element
    return [{'id': entry} if not isinstance(entry, dict) else entry for entry in data]


def get_publications():
    """Holt Publikationen und filtert nach erlaubten Autoren."""
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=['publications'])
    publications = author.get('publications', [])
    publications = ensure_list_of_dicts(publications)

    # Filter nach erlaubten Autoren
    filtered_publications = []
    for pub in publications:
        authors = pub.get("bib", {}).get("author", "")
        if any(author in ALLOWED_AUTHORS for author in authors.split(" and ")):  # Google Scholar gibt "and" als Trenner aus
            filtered_publications.append(pub)

    return filtered_publications



def get_doi(title):
    """Search for the DOI of a publication using CrossRef."""
    url = f"https://api.crossref.org/works?query.title={title}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        items = data.get("message", {}).get("items", [])
        if items:
            return items[0].get("DOI", "DOI not found")
    return "DOI not found"

def save_dois_to_yaml(dois, filename='sources.yaml'):
    """Append new DOIs to the YAML file without removing existing ones."""
    try:
        with open(filename, 'r') as file:
            existing_data = yaml.safe_load(file) or []
    except FileNotFoundError:
        existing_data = []

    # Neue DOIs hinzufügen, falls sie noch nicht existieren
    existing_dois = {entry["id"] for entry in existing_data}
    for doi_entry in dois:
        if doi_entry["id"] not in existing_dois:
            existing_data.append(doi_entry)

    with open(filename, 'w') as file:
        yaml.dump(existing_data, file, default_flow_style=False)

def main(*args):
    publications = get_publications()
    if not publications:
        return
    
    dois = []
    for pub in publications:
        title = pub["bib"].get("title", "Unknown")
        doi = get_doi(title)
        if doi != "DOI not found":
            dois.append({"id": f"doi:{doi}"})
        print(f"Title: {title}\nDOI: {doi}\n")
    
    # Speichern der DOIs in der YAML-Datei
    return dois

if __name__ == "__main__":
    main()
