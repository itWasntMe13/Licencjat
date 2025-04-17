# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28
from core import setup
from core.logic import books_api_service, books_logic
from core.services import book_service, book_index_service, book_detail_service, book_index_raw_service

if __name__ == '__main__':

    """
    Budowa środowiska.
    """
    # setup.build_environment() # Budujemy środowisko

    """
    Obsługa API Wolnych Lektur od pobrania surowego indeksu książek do pobrania książki.
    """
    book_index_raw_service.BookIndexRawService.download_books_index_raw_json() # Pobranie surowego indeksu książek
    book_index_service.BookIndexService.create_books_index_json() # Stworzenie pliku JSON z "naszym" indeksem książek
    book = books_logic.choose_a_book() # Wybór książki zwraca obiekt BookIndex
    book_detail_service.BookDetailService.download_book_details_json(book) # Pobranie detali książki
    book_detail = book_detail_service.BookDetailService.load_book_details_json(book) # Wczytanie detali książki w formie obiektu BookDetail
    book_service.BookService.download_book_txt(book_detail) # Pobranie książki na podstawie obiektu BookDetail

    """
    Na ten moment mamy wszystkie dane i pliki książek/książki. 
    Od teraz zamykamy komunikację z API Wolnych Lektur i przechodzimy do komunikacji z OpenAI.
    """

    # GPT