from importlib.metadata import version, PackageNotFoundError
import requests

# Funkcja do sprawdzenia wersji biblioteki openai
def check_openai_version():
    try:
        version_openai = version("openai")
        print(f"Zainstalowana wersja openai: {version_openai}")
        return version_openai
    except PackageNotFoundError:
        print("Biblioteka openai nie jest zainstalowana.")
        return None

def get_json_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdza, czy odpowiedź nie zawiera błędów
        return response.json()
    except requests.RequestException as e:
        print(f"Wystąpił błąd podczas pobierania danych z API: {e}")
        return None