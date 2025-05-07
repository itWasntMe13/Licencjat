import streamlit as st
from core.services.books.book_service import BookService
from core.services.gpt.gpt_service import GptService
from core.config.gpt import GptConfig
from core.utils.common_utils import load_json_file
from core.config import BOOKS_DIR
from core.utils.gpt_utils import count_tokens

def show():
    st.title("⚙️ Asystent AI")

    # Załaduj książkę z kontekstu sesji
    selected_book = st.session_state.get("selected_book", None)
    if not selected_book:
        st.warning("Najpierw wybierz książkę we właściwym widoku.")
        return

    # Utwórz domyślny obiekt konfiguracji GPT
    gpt_config = GptConfig(model="gpt-4o-mini", max_tokens=128000, temperature=0.7, output_percentage=0.2, prompt_percentage=0.8)

    st.subheader(f"Książka: {selected_book.title}")
    st.markdown("Wygeneruj opracowanie książki za pomocą AI.")

    if GptService.is_summarizable(selected_book.content, gpt_config):
        # Koszt streszczenia
        token_count = count_tokens(selected_book.content)
        cost = token_count * 0.000002 / 1000
        st.markdown(f"**Koszt streszczenia: {cost:.2f} PLN\tTokeny: {token_count}**")
        if st.button("📄 Wygeneruj streszczenie"):
            with st.spinner("Generuję streszczenie..."):
                gpt_service = GptService(api_key=st.secrets["OPENAI_API_KEY"])
                summary = gpt_service.summarize_text(gpt_config, selected_book.content)
                st.session_state["summary"] = summary
                st.success("Streszczenie wygenerowane!")

        if st.session_state.get("summary"):
            st.markdown(f"### 📘 Streszczenie {selected_book.title}:")
            st.text_area("Wynik:", st.session_state["summary"], height=400)
    else:
        st.error("📏 Książka zbyt długa, aby ją streścić przy obecnej konfiguracji.")
        token_count = count_tokens(selected_book.content)
        st.markdown(f"**Tokeny w książce: {token_count}\tMaksymalna liczba tokenów do przetworzenia: {gpt_config.prompt_percentage * gpt_config.max_tokens}**")
