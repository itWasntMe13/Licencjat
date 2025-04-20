import shutil
import os
from core.config import BOOKS_DIR, BOOK_DETAILS_DIR, BOOKS_INDEX_PATH, BOOKS_INDEX_RAW_PATH

class MaintenanceService:
    """
    Funkcje pomocnicze pozwalające na resetowanie stanu aplikacji z poziomu jej interfejsu.
    """
    @staticmethod
    def clear_books(directory=BOOKS_DIR):
        """
        Usuwa wszystkie książki z katalogu BOOKS_DIR.
        """
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)