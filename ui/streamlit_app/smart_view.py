import streamlit as st
import sys
import os
from pathlib import Path

from core.services.gpt.gpt_config_service import GptConfigService

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from core.config import BOOKS_DIR
from core.utils.common_utils import load_json_file
from core.models.books.book import Book
from core.config.gpt import GptConfig
from core.services.books.book_index_service import BookIndexService
from core.services.books.book_detail_service import BookDetailService
from core.services.books.book_service import BookService
from core.utils.gpt_utils import count_tokens


def show():
    st.title("📚 Asystent edukacyjny — opracowania i streszczenia")

    # Załaduj indeks książek
    books = BookIndexService.load_books_index_json()

    # Lista tytułów do wyboru
    options = [f"{book.title} – {book.author}" for book in books]
    selected = st.selectbox("Wybierz książkę do opracowania:", options)

    if selected:
        selected_index = options.index(selected)
        chosen_book = books[selected_index]

        # Pobierz detale i obiekt Book
        BookDetailService.download_book_details_json(chosen_book)
        book_detail = BookDetailService.load_book_details_json(chosen_book)
        book_path = BOOKS_DIR / f"{book_detail.slug}.json"

        if not book_path.exists():
            st.warning("📥 Książka jeszcze nie została pobrana. Kliknij poniżej, aby to zrobić.")
            if st.button("Pobierz książkę"):
                BookService.create_book_object(book_detail, save=True)
                st.success("Książka została pobrana i zapisana.")

        else:
            book_dict = load_json_file(book_path)
            book = Book.from_dict(book_dict)
            gpt_config = GptConfigService.load_config() # Załaduj domyślny config (można później ustawić edytowalne)

            st.markdown(f"### 📖 {book.title}")
            st.markdown(f"**Autor:** {book.author}")
            st.markdown(f"**Tokeny:** {count_tokens(book.content)} / {gpt_config.max_tokens}")

            # Akcje GPT
            st.markdown("---")
            st.subheader("🧠 Wygeneruj opracowania")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("📌 Podsumowanie"):
                    st.info("(Symulacja) Podsumowanie zostałoby tutaj wygenerowane.")

                if st.button("📋 Lista bohaterów"):
                    st.info("(Symulacja) Lista bohaterów wygenerowana.")

            with col2:
                if st.button("📚 Pełne streszczenie"):
                    st.warning("(Symulacja) Streszczenie książki w toku...")

                if st.button("🧪 Wygeneruj pytania testowe"):
                    st.info("(Symulacja) Testy zostałyby pokazane tutaj.")

            # Wyświetl fragment książki dla kontekstu
            st.markdown("---")
            st.subheader("📘 Fragment książki (pierwsze 1500 znaków)")
            st.text_area("Podgląd:", book.content[:1500], height=300)


if __name__ == "__main__":
    show()
