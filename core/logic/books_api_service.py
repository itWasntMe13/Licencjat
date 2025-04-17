import requests
import json
from app.books.exceptions import TooLongName, HTMLResponse
from core.config import WL_API_BOOKS_URL, BOOKS_INDEX_PATH, BOOKS_INDEX_RAW_PATH, BOOKS_DETAILS_DIR, BOOKS_DIR
from core.models.book_detail import BookDetail
from core.utils import get_json_request, load_json_file

def download_books_index_raw_json(save_path=BOOKS_INDEX_RAW_PATH, url=WL_API_BOOKS_URL) -> None:
    """
    Pobiera surowy indeks książek z API Wolnych Lektur i zapisuje go do pliku JSON.
    :param save_path:
    :param url:
    :return:
    """
    json_file = get_json_request(url)

    # Zapisz JSONa
    with open(save_path, "w", encoding="utf-8") as file_stream:
        json.dump(json_file, file_stream, ensure_ascii=False, indent=4)

def download_book_details_json(book_index, save_dir=BOOKS_DETAILS_DIR) -> None:
    """
    Pobiera szczegóły książki na podstawie pola href z obiektu BookIndex i zapisuje je do pliku JSON.
    :param book:
    :param save_dir:
    :return:
    """
    # Utworzenie adresu URL do pliku JSON
    url = book_index.href + "?format=json"
    print(f"Adres URL do pobrania: {url}")
    # Pobranie danych z API
    json_file = get_json_request(url)

    # Stworzenie obiektu klasy BookDetail
    book_detail = BookDetail.from_api_dict(json_file)

    # Ścieżka zapisu
    save_path = save_dir / f"{book_index.slug}.json"

    # Serializacja do pliku
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(book_detail.__dict__, f, ensure_ascii=False, indent=4)  # Do zastąpienia funkcją z utils

    print(f"Zapisano dane szczegółowe książki: {book_detail.title}")

# Pobranie txt książki na podstawie pola txt_url z obiektu BookDetail
def download_book_txt(book_detail, save_dir=BOOKS_DIR) -> None:
    """
    Pobiera książkę na podstawie pola txt_url z obiektu BookDetail i zapisuje ją do pliku TXT.
    :param book_detail:
    :param save_dir:
    :return:
    """
    # Utworzenie adresu URL do pliku TXT
    url = book_detail.txt_url + "?format=txt"
    print(f"Adres URL do pobrania: {url}")

    # Pobranie danych z API
    response_api = requests.get(url)
    book = response_api.content

    # Sprawdzenie, czy książka została poprawnie pobrana (czy nie jest HTML-em)
    if book.split()[0] == b'<html>':
        print("Nie udało się pobrać książki. Odpowiedź API to HTML.")
    else:
        # Sprawdzenie, czy nazwa pliku nie jest za długa
        file_name = book_detail.title
        if len(file_name) > 200:
            raise TooLongName

        # Zapisanie książki
        with open(f"{save_dir}\\{file_name}.txt", "wb") as file_stream:
            file_stream.write(book)
