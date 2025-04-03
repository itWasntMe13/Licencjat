# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28
from core import setup
from core.logic import books_api

if __name__ == '__main__':
    # Budowa środowiska
    setup.build_environment() # Budujemy środowisko
    books_api.download_books_index_raw_json() # Pobieramy surowy indeks książek
    # books_api.create_books_index_json()

