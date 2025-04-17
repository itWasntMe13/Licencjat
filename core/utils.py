from importlib.metadata import version, PackageNotFoundError
import requests
import json

def check_openai_version():
    """
    Sprawdza wersję zainstalowanej biblioteki openai.
    :return:
    """
    try:
        version_openai = version("openai")
        print(f"Zainstalowana wersja openai: {version_openai}")
        return version_openai
    except PackageNotFoundError:
        print("Biblioteka openai nie jest zainstalowana.")
        return None

def save_json_file(data, file_path):
    """
    Zapisuje dane do pliku JSON.
    :param data:
    :param file_path:
    :return:
    """
    try:
        with open(file_path, "w", encoding="utf-8") as file_stream:
            json.dump(data, file_stream, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku: {e}")

def save_txt_file(data, file_path):
    """
    Zapisuje dane do pliku TXT (a przynajmniej na ten moment nie ma innych zastosowań).
    :param data:
    :param file_path:
    :return:
    """
    # Czy file_path nie jest za długi?
    if len(file_path.name) > 204: # 200 znaków to maks Windowsa + 4 znaki na rozszerzenie (.txt)
        print(f"Nazwa pliku jest za długa: {file_path}")
        return
    try:
        with open(file_path, "wb") as file_stream:
            file_stream.write(data)
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania danych do pliku: {e}")

def load_json_file(file_path):
    """
    Wczytuje plik JSON i zwraca jego zawartość jako słownik.
    :param file_path:
    :return:
    """
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

def load_txt_file(file_path):
    """
    Wczytuje plik TXT i zwraca jego zawartość.
    :param file_path:
    :return:
    """
    try:
        with open(file_path, "rb") as file_stream:
            data = file_stream.read()
        return data
    except FileNotFoundError:
        print(f"Plik {file_path} nie został znaleziony.")
        return None
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
        return None

def json_request(url):
    """
    Pobiera dane z API w formacie JSON.
    :param url:
    :return:
    """
    url = url + "?format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdza, czy odpowiedź nie zawiera błędów
        return response.json()
    except requests.RequestException as e:
        print(f"Wystąpił błąd podczas pobierania danych z API: {e}")
        return None

def txt_request(url):
    """
    Pobiera dane z API w formacie TXT.
    :param url:
    :return:
    """
    url = url + "?format=txt"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdza, czy odpowiedź nie zawiera błędów
        if response.content.split()[0] == b"<html>": # Sprawdza, czy odpowiedź nie jest HTML-em
            print(f"Otrzymano HTML zamiast pliku TXT z URL: {url}")
            return None
        return response.content
    except requests.RequestException as e:
        print(f"Wystąpił błąd podczas pobierania danych z API: {e}")
        return None