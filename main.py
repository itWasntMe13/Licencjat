# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28
from core import setup
from core.logic import create_index


if __name__ == '__main__':
    # Budowa środowiska
    # setup.build_environment() # Budujemy środowisko
    # create_index.download_books_index_raw_json() # Pobieramy surowy indeks książek
    create_index.create_books_index_json()

