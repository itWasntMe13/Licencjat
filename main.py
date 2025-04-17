# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28
from core import setup
from core.logic import books_api_service, books_index_service

if __name__ == '__main__':

    """
    Budowa środowiska.
    """
    # setup.build_environment() # Budujemy środowisko

    """
    Obsługa API Wolnych Lektur od pobrania indeksu książek do pobrania książki.
    """
    # books_api.download_books_index_raw_json() # Pobieramy surowy indeks książek
    # books_api.create_books_index_json() # Tworzymy indeks książek
    book = books_index_service.choose_a_book() # Wybór książki zwraca obiekt BookIndex
    books_api_service.download_book_details_json(book) # Pobranie detali książki
    book_detail = books_index_service.load_book_details_json(book) # Wczytanie detali książki w formie obiektu BookDetail
    books_api_service.download_book_txt(book_detail) # Pobranie książki na podstawie obiektu BookDetail

    """
    Na ten moment mamy wszystkie dane i pliki książek/książki. 
    Od teraz zamykamy komunikację z API Wolnych Lektur i przechodzimy do komunikacji z OpenAI.
    """

    # GPT