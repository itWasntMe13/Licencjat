from classes import create_downloadable_books_list
from functions import clear_the_project

if __name__ == "__main__":

    # Clearing the project
    clear_the_project()

    # Creating lists of usable books to use in the program
    file_type = "txt"

    # Downloading all downloadable books in given format
    # download_available_books(file_type)

    # Taking care of possible exceptions
    try:
        if file_type not in ["txt", "pdf", "epub", "mobi"]:
            raise Exception("Wrong file type.")

        downloadable_books_list = create_downloadable_books_list(file_type)

        # Printing the list of downloadable books
        for i in range(1, 200):
            print(downloadable_books_list[i])
        print(len(downloadable_books_list))
    except Exception as e:
        print(f"Exception raised while creating list of downloadable books: {e}")

    # wanted_word = input("Podaj szukane słowo: ")
    # text_title = input("Podaj nazwę tekstu w którym chcesz wyszukać wybrane słowo: ")
    # print(count_word_repetitions("chleb", "Dziady", book_list))
    # print(count_word_repetitions("chleb", "Lalka"))
    # print(count_word_repetitions("chleb", "Dziady"))
    # print(count_word_repetitions("wino", "Lalka"))
    # print(count_word_repetitions("chleb", "Zbrodnia i kara"))
