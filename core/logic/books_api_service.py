import requests
import json
from app.books.exceptions import TooLongName, HTMLResponse
from core.config import WL_API_BOOKS_URL, BOOKS_INDEX_PATH, BOOKS_INDEX_RAW_PATH, BOOKS_DETAILS_DIR, BOOKS_DIR
from core.models.book_detail import BookDetail
from core.utils import json_request, txt_request, save_json_file, save_txt_file

def download_books_index_raw_json(save_path=BOOKS_INDEX_RAW_PATH, url=WL_API_BOOKS_URL) -> None:
    """
    Pobiera surowy indeks książek z API Wolnych Lektur i zapisuje go do pliku JSON.
    :param save_path:
    :param url:
    :return:
    """
    json_file = json_request(url)
    save_json_file(json_file, save_path)

def download_book_details_json(book_index, save_dir=BOOKS_DETAILS_DIR) -> None:
    """
    Pobiera szczegóły książki na podstawie pola href z obiektu BookIndex i zapisuje je do pliku JSON.
    :param book:
    :param save_dir:
    :return:
    """
    url = book_index.href # book_index.href to URL do detali książki
    json_file = json_request(url)

    # Stworzenie obiektu klasy BookDetail
    book_detail = BookDetail.from_api_dict(json_file)

    # Ścieżka zapisu to slug z obiektu BookIndex
    save_path = save_dir / f"{book_index.slug}.json"

    # Serializacja obiektu BookDetail do JSON-a
    save_json_file(book_detail.to_dict(), save_path)

# Pobranie txt książki na podstawie pola txt_url z obiektu BookDetail
def download_book_txt(book_detail, save_dir=BOOKS_DIR) -> None:
    """
    Pobiera książkę na podstawie pola txt_url z obiektu BookDetail i zapisuje ją do pliku TXT.
    :param book_detail:
    :param save_dir:
    :return:
    """
    url = book_detail.txt_url # book_detail.txt_url to URL do książki w formacie TXT
    book = txt_request(url)

    # Zapisanie książki do pliku TXT
    save_path = save_dir / f"{book_detail.title}.txt"
    save_txt_file(book, save_path)
