from app.books.normalization import (
    normalize_title,
    normalize_word,
    normalize_text
)
from app.books.books_json_handler import (
    download_book
)
from app.books.classes import (
    create_books_list,
    create_normalized_titles_list,
    create_titles_list,
)
import re
import os
import shutil

books_list = create_books_list()


def clear_the_project():
    try:
        if os.path.exists("books"):
            shutil.rmtree("books")
        if os.path.exists("json_files"):
            shutil.rmtree("json_files")
        if os.path.exists("api_errors"):
            shutil.rmtree("api_errors")
        if not (os.path.exists("books") and os.path.exists("json_files") and os.path.exists("api_errors")):
            print("Projekt został wyczyszczony.")
    except Exception as e:
        raise Exception(f"Exception raised while clearing the project: {e}")


def count_word_repetitions(wanted_word, title):

    # Creating lists of titles and normalized titles
    title_list, normalized_title_list = create_titles_list(), create_normalized_titles_list()

    # Choosing the book
    chosen_title = choose_a_book(title)

    # Downloading the book using url from the json file
    # Getting the last element of the url - the title of the book
    url = books_list[normalized_title_list.index(chosen_title)].url
    url_segments = url.split("/")
    url_last_segment = url_segments[-2]

    download_book(chosen_title, "https://wolnelektury.pl/media/book/txt/" + url_last_segment + ".txt")

    try:
        normalized_wanted_word = normalize_word(wanted_word)
        with open(f".\\books\\{chosen_title}", "r", encoding="utf-8") as file:
            normalized_text = normalize_text(file.read())
            repetitions_count = len(re.findall(r'\b' + normalized_wanted_word + r'\b', normalized_text))

        return (f"W tekście {books_list[normalized_title_list.index(chosen_title)].title} słowo " +
                normalized_wanted_word + f" występuje {repetitions_count} razy :)")
    except Exception as e:
        return f"Exception raised while normalizing wanted word: {e}"


def choose_a_book(title) -> str:
    try:
        title_list, normalized_title_list = create_titles_list(), create_normalized_titles_list()

        normalized_title = normalize_title(title)
        potential_titles = []
        normalized_potential_titles = []

        for i in range(len(books_list)):
            if normalized_title in normalized_title_list[i]:
                potential_titles.append(title_list[i])
                normalized_potential_titles.append(normalized_title_list[i])

        # Deciding on one exact title
        if len(potential_titles) == 0:
            raise Exception("Nie znaleziono książki o podanym tytule.")

        elif len(potential_titles) == 1:
            chosen_title = normalize_title(potential_titles[0])

        else:
            print(f"Znaleziono {len(potential_titles)} książek. Wybierz jedną z poniższych:")

            for title in potential_titles:
                print(books_list[normalized_title_list.index(normalize_title(title))].__str__())
            selected_title = normalize_title(input("Wpisz nazwę książki z listy:"))

            if selected_title in normalized_potential_titles:
                chosen_title = selected_title
            else:
                while True:
                    print("Nie znaleziono książki o wybranym tytule. Wybierz jedną z poniższych:")
                    for title in potential_titles:
                        print(books_list[normalized_title_list.index(normalize_title(title))].__str__())
                    selected_title = normalize_title(input("Wpisz nazwę książki z listy:"))

                    if selected_title in normalized_potential_titles:
                        chosen_title = selected_title
                        break
        return chosen_title
    except Exception as e:
        raise Exception(f"Exception raised while selecting the book: {e}")
