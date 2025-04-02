from core.config import REQUIRED_DIRS
from pathlib import Path

def build_environment():
    for directory in REQUIRED_DIRS:
        try:
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"Utworzono katalog: {directory}")
        except Exception as e:
            print(f"Nie udało się utworzyć katalogu: {directory}. Błąd: {e}")
