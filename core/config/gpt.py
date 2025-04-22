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

class GPTConfig:
    def __init__(self, model: str, temperature: float, max_output_percent: float):
        self.model = model
        self.temperature = temperature
        self.max_output_percent = max_output_percent  # np. 0.8 = 80%

    def to_dict(self):
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_output_percent": self.max_output_percent
        }

    @staticmethod
    def from_dict(data: dict) -> "GPTConfig":
        return GPTConfig(
            model=data.get("model", "gpt-4o"),
            temperature=data.get("temperature", 0.7),
            max_output_percent=data.get("max_output_percent", 0.8)
        )

    def validate(self):
        assert 0 <= self.temperature <= 1, "Temperature musi być w zakresie 0-1"
        assert 0 < self.max_output_percent <= 1, "Max output % musi być między 0-1"
