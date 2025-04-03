from app.books.books_json_handler import download_json_books_file, download_book
from app.books.normalization import normalize_title
import json
import os
import glob


# Creating a class for books
class Book:

    def __init__(self, title=None, author=None, kind=None, epoch=None, has_audio=None, url=None, genre=None):
        self.title = title
        self.author = author
        self.kind = kind
        self.epoch = epoch
        self.has_audio = "Tak" if has_audio else "Nie"
        self.url = url
        self.normalized_title = normalize_title(title)
        self.genre = genre

    def __str__(self):
        return (f"Tytuł: {self.title}\n"
                f"Autor: {self.author}\n"
                f"Rodzaj: {self.kind}\n"
                f"Epoka: {self.epoch}\n"
                f"Audio: {self.has_audio}\n"
                f"URL: {self.url}\n"
                f"Genre: {self.genre}\n"
                f"Normalized Title: {self.normalized_title}")


def create_books_list() -> list:
    _books_list = []

    try:
        if not os.path.exists(".\\json_files\\books.json"):
            download_json_books_file()

        if not os.path.exists(".\\json_files\\books.json"):
            raise Exception("Failed to download json books file.")

        with open(".\\json_files\\books.json", "r", encoding="utf-8") as file_stream:
            data = file_stream.read()
            json_data = json.loads(data)

            for book in json_data:
                obj = Book(
                    book["title"],
                    book["author"],
                    book["kind"],
                    book["epoch"],
                    book["has_audio"],
                    book["url"],
                    book["genre"]
                )
                _books_list.append(obj)
    except Exception as e:
        print(f"Exception raised while creating book list: {e}")

    return _books_list


# Create a list of books
books_list = create_books_list()


# Create a list of unique books
def create_unique_books_list() -> list:
    _unique_books_list = []

    try:
        for book in books_list:
            if book not in _unique_books_list:
                _unique_books_list.append(book)
    except Exception as e:
        print(f"Exception raised while creating unique book list: {e}")

    return _unique_books_list


# Create a list of unique books
unique_books_list = create_unique_books_list()
# From now on every function below uses unique_books_list


# Creates a list of titles
def create_titles_list() -> list:
    titles_list = []

    # Creating lists of titles and normalized titles
    try:
        for book in unique_books_list:
            titles_list.append(book.title)
    except Exception as e:
        raise Exception(f"Exception raised while creating titles list: {e}")

    return titles_list

# Creates a list of unique titles
def create_unique_titles_list() -> list:
    unique_titles_list = []

    # Creating lists of titles and normalized titles
    try:
        for book in unique_books_list:
            if book.title not in unique_titles_list:
                unique_titles_list.append(book.title)
    except Exception as e:
        raise Exception(f"Exception raised while creating unique titles list: {e}")

    return unique_titles_list

# Creates a list of normalized, unique titles
def create_normalized_titles_list() -> list:
    normalized_titles_list = []

    # Creating lists of titles and normalized titles
    try:
        for title in create_titles_list():
            normalized_titles_list.append(normalize_title(title))
    except Exception as e:
        raise Exception(f"Exception raised while creating normalized title list: {e}")

    return normalized_titles_list


# Returns a Book object by its title
def get_book_by_title(title) -> Book:
    try:
        for book in unique_books_list:
            if book.title == title:
                return book
    except Exception as e:
        raise Exception(f"Exception raised while getting book by title: {e}")


# Returns a Book object by its normalized title
def get_book_by_normalized_title(normalized_title) -> Book:
    try:
        for book in unique_books_list:
            if book.normalized_title == normalized_title:
                return book
    except Exception as e:
        raise Exception(f"Exception raised while getting book by normalized title: {e}")


# Creates download url for a given book in given file type
def create_download_url(book, file_type) -> str:

    # Getting last segment of the URL
    url = book.url
    url_segments = url.split("/")
    url_last_segment = url_segments[-2]

    return f"https://wolnelektury.pl/media/book/{file_type}/{url_last_segment}.{file_type}"


# Downloading downloadable, unique books in given format
def download_available_books(file_type) -> None:
    # Downloading unique books
    for title in create_titles_list():
        try:
            # Getting Book object by its title
            book = get_book_by_title(title)
            url = create_download_url(book, file_type)
            download_book(book.normalized_title, file_type, url)
        except Exception as e:
            print(f"Exception raised while downloading book: {e}")


# Creates a list of every unique book that can be downloaded in given format
def create_downloadable_books_json(file_type) -> None:
    try:
        _downloadable_books_list = []
        download_available_books(file_type)

        for file_name in glob.glob(f"books//{file_type}//*.{file_type}"):
            file_name = file_name.split("\\")[-1]
            title = file_name.split(".")[0]

            book = get_book_by_normalized_title(title)
            _downloadable_books_list.append(book)

        # Save the list of downloadable books to a JSON file
        with open(f".//json_files//downloadable_{file_type}_books.json", "w", encoding="utf-8") as file_stream:
            json.dump([book.__dict__ for book in _downloadable_books_list], file_stream, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Exception raised while creating downloadable books json for: {e}\n"
              f"Requested file type: {file_type}")


# Create a max recursive attempts constant so the recursive function doesn't run forever
CREATE_DOWNLOADABLE_BOOKS_LIST_MAX_RECURSIVE_ATTEMPTS = 3


def create_downloadable_books_list(file_type, recursive_attempts=0) -> list:
    _downloadable_books_list = []

    if os.path.exists(f".//json_files//downloadable_{file_type}_books.json"):
        with open(f".//json_files//downloadable_{file_type}_books.json", "r", encoding="utf-8") as file_stream:
            data = file_stream.read()
            json_data = json.loads(data)

            for book in json_data:
                obj = Book(
                    book["title"],
                    book["author"],
                    book["kind"],
                    book["epoch"],
                    book["has_audio"],
                    book["url"],
                    book["genre"]
                )
                _downloadable_books_list.append(obj)
        return _downloadable_books_list

    elif recursive_attempts < CREATE_DOWNLOADABLE_BOOKS_LIST_MAX_RECURSIVE_ATTEMPTS:
        try:
            create_downloadable_books_json(file_type)
            return create_downloadable_books_list(file_type, recursive_attempts + 1)
        except Exception as e:
            print(f"Exception raised while creating downloadable books list: {e}\n"
                  f"Requested file type: {file_type}")
    else:
        print(f"Max recursive attempts reached. Unable to create downloadable books list.")
        return []
