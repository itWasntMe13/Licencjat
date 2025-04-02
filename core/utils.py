from importlib.metadata import version, PackageNotFoundError

# Funkcja do sprawdzenia wersji biblioteki openai
def check_openai_version():
    try:
        version_openai = version("openai")
        print(f"Zainstalowana wersja openai: {version_openai}")
        return version_openai
    except PackageNotFoundError:
        print("Biblioteka openai nie jest zainstalowana.")
        return None
    