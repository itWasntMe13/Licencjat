import os
from ai.api_manager import check_openai_version, get_api_key

# Zmienne globalne
GLOBAL_PATH = os.path.dirname(os.path.abspath(__file__)) # Ścieżka do katalogu projektu
OPENAI_VERSION = check_openai_version() # Wersja biblioteki OpenAI
MY_API_KEY = get_api_key() # Klucz API
