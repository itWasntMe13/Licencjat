import requests
import json
import os
from app.books.exceptions import TooLongName, HTMLResponse
from core.config import WL_API_BOOKS_URL, BOOKS_INDEX_PATH, BOOKS_INDEX_RAW_PATH
from core.utils import get_json_request, load_json_file

from core.models.book_index import BookIndex

def download_books_index_raw_json(save_path=BOOKS_INDEX_RAW_PATH, url=WL_API_BOOKS_URL) -> None:
    # Download JSON file
    json_file = get_json_request(url)

    # Save JSON file with JSON module
    with open(save_path, "w", encoding="utf-8") as file_stream:
        json.dump(json_file, file_stream, ensure_ascii=False, indent=4)



# def create_book_detail_json(book: BookIndex) -> None:
#     try:
#         # Pobranie danych z API
#         api_data = get_json_request(book.href) # Do zastąpienia funkcją z utils
#
#         # Stworzenie obiektu klasy BookDetail
#         book_detail = BookDetail.from_api_dict(api_data)
#
#         # Ścieżka zapisu
#         save_path = BOOK_DETAILS_DIR / f"{book.slug}.json"
#
#         # Serializacja do pliku
#         with open(save_path, "w", encoding="utf-8") as f:
#             json.dump(book_detail.__dict__, f, ensure_ascii=False, indent=4) # Do zastąpienia funkcją z utils
#
#         print(f"Zapisano dane szczegółowe książki: {book.title}")
#
#     except Exception as e:
#         print(f"Nie udało się pobrać danych dla książki '{book.title}': {e}")

def download_book(file_name, file_type, url, book_save_path):
    if len(file_name) > 200:
        raise TooLongName

    # Download book
    response_api = requests.get(url)
    book = response_api.content

    # Check if book was downloaded correctly (if it's not an HTML)
    if book.split()[0] == b'<html>':
        # Save HTML file
        with open(f".\\api_errors\\{file_type}\\{file_name}.{file_type}", "wb") as file_stream:
            file_stream.write(book)
            raise HTMLResponse
    else:
        # Save book
        with open(f"{book_save_path}\\{file_type}\\{file_name}.{file_type}", "wb") as file_stream:
            file_stream.write(book)
            print(f"Zapisano książkę pod ściężką: {book_save_path}\\{file_type}\\{file_name}.{file_type}")

def force_download_book(file_name, file_type, url) -> None:
    try:
        # Download book
        response_api = requests.get(url)
        book = response_api.content

        # Check if book was downloaded correctly (if it's not an HTML)
        if book.split()[0] == b'<html>':
            # Save HTML file
            with open(f".\\api_errors\\{file_type}\\{file_name}.{file_type}", "wb") as file_stream:
                file_stream.write(book)
            raise HTMLResponse
        else:
            # Save book
            with open(f".\\books\\{file_type}\\{file_name}.{file_type}", "wb") as file_stream:
                file_stream.write(book)

    except Exception as e:
        print(f"Exception while force downloading book: '{file_name}' error: {e}")