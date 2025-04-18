from core.config import BOOKS_INDEX_PATH
from core.models.books.book_index import BookIndex
from rapidfuzz import process, fuzz
from core.services.books.book_index_service import BookIndexService

class BookBrowsingService:
    @staticmethod
    def choose_a_book(book_index_list) -> BookIndex:
        """
        Wybiera książkę z indeksu. Zwraca obiekt BookIndex.
        :param book_index_list:
        :return:
        """
        # Wyszukujemy książki
        query = input("Wyszukaj książkę: ")
        matched_books = BookBrowsingService.search_books(book_index_list, query)

        # Wyświetlamy wyniki
        if matched_books:
            print("Znalezione książki:")
            for i, book in enumerate(matched_books):
                print(f"{i + 1}. {book.title} – {book.author}")
                print(f"   {book.href}")
        else:
            print("Nie znaleziono żadnych książek.")

        # Wybieramy książkę
        book_index = int(input("Wybierz książkę (numer): ")) - 1
        if 0 <= book_index < len(matched_books):
            selected_book = matched_books[book_index]
            print(f"Wybrano książkę: {selected_book.title} – {selected_book.author}")
            return selected_book
        else:
            print("Niepoprawny numer książki.")
            return None

    @staticmethod
    def search_books(books_index_list: list[BookIndex], query: str, limit: int = 25) -> list[BookIndex]:
        """
        Wyszukuje książki w indeksie na podstawie podanego zapytania.
        :param books_index_list:
        :param query:
        :param limit:
        :return:
        """
        # Mapujemy każdego search_stringa na krotkę (title, author). search_string to nasz klucz na podstawie którego odzyskamy krotkę.
        search_map = {f"{book.title} – {book.author}": (book.title, book.author) for book in books_index_list}

        # Fuzzy robi za nas robotę i zwraca listę krotek (search_string, score).
        matches = process.extract(query, search_map.keys(), scorer=fuzz.ratio, limit=limit)

        matched_books = []
        for match in matches: # Dla każdej krotki (search_string, score) wyciągamy search_string i szukamy w search_map.
            search_string = match[0]
            title, author = search_map[search_string] # title + author to krotka, którą znajdujemy na podstawie search_stringa.
            # Szukamy pierwszej książki, która ma tytuł i autora z krotki title, author.
            book = next((book for book in books_index_list if book.title == title and book.author == author), None)
            if book:
                matched_books.append(book) # Jeśli książka istnieje, uznajemy ją za pożądaną przez użytkownika i zwracamy.

        return matched_books
