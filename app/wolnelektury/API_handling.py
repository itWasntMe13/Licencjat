import requests
import json
import os
from app.wolnelektury.exceptions import TooLongName, HTMLResponse


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

def download_json_books_file(file_name="books.json", url="https://wolnelektury.pl/api/books/?format=json") -> None:
    try:
        # Download JSON file
        response_api = requests.get(url)
        json_file = response_api.content

        # Create a directory if it doesn't exist
        if not os.path.exists(".\\json_files"):
            os.mkdir(".\\json_files")

        # Save JSON file with JSON module
        with open(f".\\json_files\\{file_name}", "w", encoding="utf-8") as file_stream:
            json.dump(json.loads(json_file), file_stream, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Exception while downloading JSON file: '{file_name}' error: {e}")


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