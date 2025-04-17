from core.config import BOOKS_INDEX_PATH, BOOKS_INDEX_RAW_PATH
from core.models.book_index import BookIndex
from core.utils import load_json_file, save_json_file

class BookIndexService:
    @staticmethod
    def load_books_index_json(path: str) -> list[BookIndex]:
        """
        Wczytuje indeks książek z pliku JSON. Zwraca listę obiektów BookIndex.
        :param path:
        :return:
        """
        # Wczytujemy indeks książek z pliku JSON
        raw_data = load_json_file(path)

        # Tworzymy listę obiektów BookIndex
        books_index = [BookIndex.from_raw_dict(book) for book in raw_data]
        return books_index

    @staticmethod
    def create_books_index_json(save_path=BOOKS_INDEX_PATH, raw_index_path=BOOKS_INDEX_RAW_PATH) -> None:
        """
        Tworzy plik JSON z indeksem książek na podstawie surowego indeksu pobranego z API Wolnych Lektur.
        :param save_path:
        :param raw_index_path:
        :return:
        """
        # Ładujemy raw JSON-a
        books_index_raw_json = load_json_file(raw_index_path)

        # Tworzymy obiekty klasy BookIndex
        books_index = [BookIndex.from_raw_dict(book) for book in books_index_raw_json]

        # Zamieniamy obiekty na słowniki
        books_index_dicts = [book.to_dict() for book in books_index]

        # Zapisujemy do books_index.json
        save_json_file(books_index_dicts, save_path)