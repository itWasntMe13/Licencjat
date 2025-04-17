from core.config import BOOKS_INDEX_PATH, BOOKS_INDEX_RAW_PATH, BOOKS_DETAILS_DIR
from core.models.book_detail import BookDetail
from core.models.book_index import BookIndex
from core.utils import load_json_file
import json
from rapidfuzz import process, fuzz

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
    with open(save_path, "w", encoding="utf-8") as file_stream:
        json.dump(books_index_dicts, file_stream, ensure_ascii=False, indent=4)

def load_books_index_json(path=BOOKS_INDEX_PATH) -> list[BookIndex]:
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

def load_book_details_json(book, load_directory=BOOKS_DETAILS_DIR) -> BookDetail:
    """
    Wczytuje szczegóły książki z pliku JSON. Zwraca obiekt BookDetail.
    :param book: Obiekt BookIndex
    :param load_directory: Katalog, w którym znajdują się pliki JSON z danymi szczegółowymi książek
    :return: Obiekt BookIndex z danymi szczegółowymi
    """

    # Ścieżka do pliku JSON
    file_path = load_directory / f"{book.slug}.json"

    # Wczytujemy dane z pliku JSON
    book_detail = load_json_file(file_path)

    # Tworzymy obiekt BookDetail
    book_detail = BookDetail.from_json_dict(book_detail)
    return book_detail

def choose_a_book(index_path=BOOKS_INDEX_PATH) -> BookIndex:
    """
    Wybiera książkę z indeksu na podstawie podanego tytułu. Zwraca obiekt BookIndex.
    :param index_path:
    :return:
    """
    # Wczytujemy indeks książek
    books_index_list = load_books_index_json(index_path)

    # Wyszukujemy tytuły
    query = input("Wpisz tytuł książki: ")
    matched_books = search_books(books_index_list, query)

    # Wyświetlamy wyniki
    if matched_books:
        print("Znalezione książki:")
        for i, book in enumerate(matched_books):
            print(f"{i + 1}. {book.title} – {book.author} ({book.epoch})")
            print(f"   {book.href}")
    else:
        print("Nie znaleziono żadnych książek.")

    # Wybieramy książkę
    book_index = int(input("Wybierz książkę (numer): ")) - 1
    if 0 <= book_index < len(matched_books):
        selected_book = matched_books[book_index]
        print(f"Wybrano książkę: {selected_book.title} – {selected_book.author} ({selected_book.epoch})")
        return selected_book
    else:
        print("Niepoprawny numer książki.")
        return None


def search_books(books_index_list, query: str, limit: int = 25) -> list[BookIndex]:
    """
    Wyszukuje książki w indeksie na podstawie podanego zapytania.
    :param books_index_list:
    :param query:
    :param limit:
    :return:
    """
    # Tworzymy listę tytułów książek
    titles = [book.title for book in books_index_list]

    # Wyszukujemy najlepsze dopasowania
    matches = process.extract(query, titles, scorer=fuzz.ratio, limit=limit) # matches to lista krotek (tytuł, wynik dopasowania)

    matched_books = []
    for match in matches:
        title = match[0] # Wyciągamy tytuł z krotki, którą zwraca process.extract
        book = next((book for book in books_index_list if book.title == title), None) # Szukamy obiektu BookIndex na podstawie tytułu
        if book:
            matched_books.append(book) # Dodajemy obiekt BookIndex do listy dopasowanych książek

    return matched_books # Zwracamy listę dopasowanych książek

