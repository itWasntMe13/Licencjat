import requests
import json
import os
from wolnelektury.exceptions import TooLongName, HTMLResponse


def download_book(file_name, file_type, url):
    # Creating directories if they don't exist yet
    if not os.path.exists(".\\books"):
        os.mkdir(".\\books")
    if not os.path.exists(".\\api_errors"):
        os.mkdir(".\\api_errors")
    if not os.path.exists(f".\\books\\{file_type}"):
        os.mkdir(f".\\books\\{file_type}")
    if not os.path.exists(f".\\api_errors\\{file_type}"):
        os.mkdir(f".\\api_errors\\{file_type}")

    # If directories were not created, raise an exception
    if not (os.path.exists(".\\books")
            and os.path.exists(".\\api_errors")
            and os.path.exists(f".\\books\\{file_type}")
            and os.path.exists(f".\\api_errors\\{file_type}")):
        raise Exception("Failed to create directories. Aborting download.")

    # # Checking for files that were already downloaded
    # if os.path.exists(f".\\books\\{file_type}\\{file_name}.{file_type}"):
    #     raise Exception(f"File '{file_name}' already exists. Aborting download.")
    # if os.path.exists(f".\\api_errors\\{file_type}\\{file_name}.{file_type}"):
    #     raise Exception(f"File '{file_name}' error file already exists. Aborting download.")
    # Checking if Windows will be able to save the file
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
        with open(f".\\books\\{file_type}\\{file_name}.{file_type}", "wb") as file_stream:
            file_stream.write(book)


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