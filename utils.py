from importlib.metadata import version, PackageNotFoundError

# Funkcje pomocnicze
# Pobranie klucza API z pliku
# def get_api_key():
#     path = "./ai/api_key.txt"
#     # Obsługa braku pliku z kluczem API
#     try:
#         with open(path, "r", encoding="utf-8") as file:
#             return file.read().strip()
#     except FileNotFoundError:
#         print("Brak pliku z kluczem API.")
#         print(f"Proszę utworzyć plik pod ścieżką {path} i umieścić w nim klucz API.")

# Funkcja do sprawdzenia wersji biblioteki openai
def check_openai_version():
    try:
        version_openai = version("openai")
        print(f"Zainstalowana wersja openai: {version_openai}")
        return version_openai
    except PackageNotFoundError:
        print("Biblioteka openai nie jest zainstalowana.")
        return None