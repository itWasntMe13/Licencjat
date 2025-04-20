import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from core.config import BOOKS_DIR
from core.utils.common_utils import load_json_file
from core.services.books.book_index_service import BookIndexService
from core.services.books.book_browsing_service import BookBrowsingService
from core.services.books.book_detail_service import BookDetailService
from core.services.books.book_service import BookService

def show():
    # Tytuł aplikacji
    st.title("Przeglądarka książek")
    query = st.text_input("Wyszukaj książkę", "") # Query do wyszukiwania książek

    # Pobieramy indeks książek z pamięci sesji
    book_index_list = BookIndexService.load_books_index_json()

    if query:
        matches = BookBrowsingService.search_books(book_index_list, query, limit=50)

        if matches:
            options = [f"{book.title} - {book.author}" for book in matches]
            selected = st.selectbox("Wybierz książkę:", options)

            if selected:
                selected_index = options.index(selected)
                chosen_book = matches[selected_index]

                # Pobieramy detale książki, która została wybrana
                BookDetailService.download_book_details_json(chosen_book)
                book_detail = BookDetailService.load_book_details_json(chosen_book)

                st.markdown(f"### {book_detail.title}")
                st.markdown(f"**Autor:** {book_detail.author}")
                st.markdown(f"**Gatunek:** {book_detail.genre}")
                st.markdown(f"**Epoka:** {book_detail.epoch}")
                st.markdown(f"**Rodzaj:** {book_detail.kind}")

                if not book_detail.txt_url:
                    st.error("Niestety, serwis Wolne Lektury aktualnie nie udostępnia pliku TXT tej książki.")
                else:
                    # Ścieżka do pliku JSON z obiektem Book
                    book_path = BOOKS_DIR / f"{book_detail.slug}.json"
                    book_content = None

                    # Jeśli książka już istnieje lokalnie
                    if book_path.exists():
                        st.info("Książka już pobrana — wczytuję z lokalnego pliku.")
                        book_dict = load_json_file(book_path)
                        book_content = book_dict.get("content")

                    # Pobieranie książki
                    if st.button("Pobierz książkę"):
                        book_obj = BookService.create_book_object(book_detail, save=True)
                        book_content = book_obj.content
                        st.success("Książka została pobrana i zapisana.")

                    # Wyświetlanie treści książki, jeśli jest dostępna
                    if book_content:
                        st.markdown("---")
                        st.subheader("Treść książki")
                        st.text_area("Podgląd:", book_content, height=500)
