

def create_books_index_json(save_path=BOOKS_INDEX_PATH, raw_index_path=BOOKS_INDEX_RAW_PATH) -> None:
    books_index_raw_json = load_json_file(raw_index_path)

    # Tworzymy obiekty klasy BookIndex
    books_index = [BookIndex.from_raw_dict(book) for book in books_index_raw_json]

    # Zamieniamy obiekty na słowniki
    books_index_dicts = [book.to_dict() for book in books_index]

    # Zapisujemy do books_index.json
    with open(save_path, "w", encoding="utf-8") as file_stream:
        json.dump(books_index_dicts, file_stream, ensure_ascii=False, indent=4)

def load_books_index_json(path=BOOKS_INDEX_PATH) -> list[BookIndex]:
    raw_data = load_json_file(path)
    if raw_data is None:
        return []
    return [BookIndex(**book_dict) for book_dict in raw_data]

def choose_a_book(books: list[BookIndex]) -> BookIndex:
    print("Wybierz książkę do pobrania:")
    for i, book in enumerate(books):
        print(f"{i + 1}. {book.title} - {book.author}")

    choice = int(input("Wybierz numer książki: ")) - 1
    if choice < 0 or choice >= len(books):
        print("Niepoprawny wybór.")
        return None

    return books[choice]