import os
from utils import check_openai_version

# Zmienne globalne
GLOBAL_PATH = os.path.dirname(os.path.abspath(__file__)) # Ścieżka do katalogu projektu
OPENAI_VERSION = check_openai_version() # Wersja biblioteki OpenAI
MY_API_KEY = "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" # Klucz API
CHARACTERS_LIMIT = 10000 # Limit znaków w jednym zapytaniu do API
TOKEN_LIMIT = 4096 # Limit tokenów w jednym zapytaniu do API
DEFAULT_MODEL = "gpt-3.5-turbo" # Domyślny model do zapytań do API
