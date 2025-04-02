from app.wolnelektury.functions import *
from app.wolnelektury.classes import *
from thefuzz import process

# Funkcja pozwalająca użytkownikowi wybrać tytuł książki z listy do pobrania
def download_requsted_book() -> str:
    # Pobieramy listę tytułów książek
    titles_list = create_unique_titles_list()

    # Dopóki użytkownik nie wybierze dostępnego tytułu, powtarzamy zapytanie
    while True:
        requested_title = input("Podaj tytuł książki, którą chcesz pobrać:")
        potential_titles = []

        # Wyświetlamy listę tytułów książek, które zawierają podany tytuł, przy użyciu algorytmu fuzzy matching
        for title in titles_list:
            title_fuzzy = process.extractOne(requested_title, [title], score_cutoff=80)
            if title_fuzzy:
                potential_titles.append(title_fuzzy[0])

        # Jeśli nie znaleziono żadnej książki o podanym tytule, zwracamy błąd
        if len(potential_titles) == 0:
            print("Nie znaleziono książki o podanym tytule. Proszę spróbować ponownie.")
            continue
        # Jeśli znaleziono jedną książkę o podanym tytule, zwracamy ją
        elif len(potential_titles) == 1:
            chosen_title = potential_titles[0]
            break
        # Jeśli znaleziono więcej niż jedną książkę o podanym tytule, proponujemy wybór
        else:
            print(f"Znaleziono {len(potential_titles)} książek dla wybranego tytułu. Wybierz jedną z poniższych:")

            # Wyświetlamy numerowaną listę tytułów książek
            for i in range(len(potential_titles)):
                print(f"{i + 1}. {potential_titles[i]}") # +1, bo indeksujemy od 1 dla wygody użytkownika
            # Pobieramy wybór użytkownika
            selected_title_number = input("Wpisz numer książki, która Cię interesuje z listy, lub wpisz 0 aby wpisać tytuł ponownie:")

            # Sprawdzamy, czy użytkownik wpisał odpowiedni typ danych
            try:
                selected_title_index = int(selected_title_number) - 1
            # W przypadku wpisania niepoprawnego typu danych prośba o ponowne wpisanie numeru
            except Exception as e:
                print("Podano niepoprawny typ danych. Proszę ponownie wyszukać książkę.")
                continue

            # Jeśli użytkownik wpisał 0, prośba o ponowne wpisanie tytułu
            if selected_title_index == -1:
                continue
            # Jeśli istnieje wartość potential_titles[selected_title_index], to zwracamy ją
            elif potential_titles[selected_title_index]:
                chosen_title = potential_titles[selected_title_index]
                break
            # W przeciwnym wypadku prośba o ponowne wpisanie numeru
            else:
                print("Nie odnaleziono wskazanego numer książki. Proszę wpisać numer ponownie.")
                continue

    # Normalizujemy wybrany tytuł
    normalized_chosen_title = normalize_title(chosen_title)
    # Pobieramy obiekt książki o wybranym tytule
    requested_book_object = get_book_by_normalized_title(normalized_chosen_title)
    # Tworzymy scieżkę zapisu książki
    book_save_path = f"{GLOBAL_PATH}\\files\\wolne_lektury\\books"
    # Pobieramy książkę o wybranym tytule
    download_book(normalized_chosen_title, "txt", create_download_url(requested_book_object, "txt"),  book_save_path)
    print(f"Pobrano książkę o tytule {chosen_title}.")

    return chosen_title

# Funkcja zlecająca pobranie książki o podanym tytule
def download_books(title) -> None:
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
