from core.config import BOOKS_INDEX_PATH
from core.models.book_index import BookIndex
from rapidfuzz import process, fuzz
from core.services.book_index_service import BookIndexService

def choose_a_book(index_path=BOOKS_INDEX_PATH) -> BookIndex:
    """
    Wybiera książkę z indeksu na podstawie podanego tytułu. Zwraca obiekt BookIndex.
    :param index_path:
    :return:
    """
    # Wczytujemy indeks książek
    books_index_list = BookIndexService.load_books_index_json(index_path)

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

