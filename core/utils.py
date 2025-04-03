from importlib.metadata import version, PackageNotFoundError
import requests
import json

# Funkcja do sprawdzenia wersji biblioteki openai
def check_openai_version():
    try:
        version_openai = version("openai")
        print(f"Zainstalowana wersja openai: {version_openai}")
        return version_openai
    except PackageNotFoundError:
        print("Biblioteka openai nie jest zainstalowana.")
        return None

# Zaciągnięcie JSONa
def load_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file_stream:
            data = json.load(file_stream)
        return data
    except FileNotFoundError:
        print(f"Plik {file_path} nie został znaleziony.")
        return None
    except json.JSONDecodeError:
        print(f"Błąd podczas dekodowania pliku JSON: {file_path}")
        return None
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
        return None

def get_json_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdza, czy odpowiedź nie zawiera błędów
        print("Pobrano dane z API.")
        # Print danych z API
        print(f"Status code: {response.status_code}")
        return response.json()
    except requests.RequestException as e:
        print(f"Wystąpił błąd podczas pobierania danych z API: {e}")
        return None