from core.utils import check_openai_version

# Wszystkie zmienne konfiguracyjne. Zmienianie ich jest... niezalecane.

from pathlib import Path

# Główna ścieżka projektu (tam, gdzie main.py)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Katalog z plikami operacyjnymi
FILES_DIR = PROJECT_ROOT / "files"

# Wolne Lektury – książki, lista, błędy
WL_DIR = FILES_DIR / "wolne_lektury"
BOOKS_DIR = WL_DIR / "books"
WL_JSON_DIR = WL_DIR / "json_files"
API_ERRORS_DIR = WL_DIR / "api_errors"

# AI – streszczenia, debug, output
AI_DIR = FILES_DIR / "ai"
SUMMARY_PARTS_DIR = AI_DIR / "summary_parts"
DEBUG_GPT_DIR = AI_DIR / "debug_data"
GPT_OUTPUT_DIR = AI_DIR / "output_data"

# Katalog frontendowy (jeśli osadzasz HTML z backendu)
FRONTEND_DIR = PROJECT_ROOT / "frontend"

# Lista katalogów do utworzenia na starcie
REQUIRED_DIRS = [
    BOOKS_DIR,
    WL_JSON_DIR,
    API_ERRORS_DIR,
    SUMMARY_PARTS_DIR,
    DEBUG_GPT_DIR,
    GPT_OUTPUT_DIR,
]

OPENAI_VERSION = check_openai_version() # Wersja biblioteki OpenAI
MY_API_KEY = "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" # Klucz API
CHARACTERS_LIMIT = 10000 # Limit znaków w jednym zapytaniu do API
TOKEN_LIMIT = 4096 # Limit tokenów w jednym zapytaniu do API
DEFAULT_MODEL = "gpt-3.5-turbo" # Domyślny model do zapytań do API
