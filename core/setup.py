from pandas.io.common import file_exists

from core.config import REQUIRED_DIRS, BOOKS_INDEX_RAW_PATH, BOOKS_INDEX_PATH
from pathlib import Path
from core.services.books import book_index_raw_service, book_index_service

def build_environment():
    """
    Tworzy strukturę plików projektu.
    :return:
    """
    for directory in REQUIRED_DIRS:
        try:
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"Utworzono katalog: {directory}")
        except Exception as e:
            print(f"Nie udało się utworzyć katalogu: {directory}. Błąd: {e}")

def create_book_indexes(force_update=True):
    """
    Tworzy indeksy książek.
    :param force_update:
    :return:
    """
    if force_update or not file_exists(BOOKS_INDEX_RAW_PATH):
        book_index_raw_service.BookIndexRawService.download_books_index_raw_json()

    if force_update or not file_exists(BOOKS_INDEX_PATH):
        book_index_service.BookIndexService.create_books_index_json()
