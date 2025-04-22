# Ogólne
from core.config.config import PROJECT_ROOT
from core.utils.common_utils import load_json_file
from core.utils.gpt_utils import check_openai_version

OPENAI_VERSION = check_openai_version() # Wersja zainstalowanej biblioteki OpenAI

# Konfiguracja GPT

PROMPTS = load_json_file(PROJECT_ROOT / "config/prompts.json")
OUTPUT_TOKEN_PERCENTAGE = 0.2 # Procent MAX_TOKENS, który zostanie przeznaczony na odpowiedź modelu
MODEL = "gpt-4omini" # Domyślny model do użycia
MODEL_TEMPERATURE = 0.7 # Temperatura modelu

