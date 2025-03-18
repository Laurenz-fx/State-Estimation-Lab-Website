import requests

url = "https://api.crossref.org/works?query.title=Test"

try:
    response = requests.get(url, timeout=10)  # 10 Sekunden Timeout
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text[:500]}")  # Nur ersten 500 Zeichen anzeigen
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")