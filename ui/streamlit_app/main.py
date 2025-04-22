import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
from ui.streamlit_app import main_view, admin_view

# taskkill /f /im streamlit.exe - zabij wszystkie procesy streamlit.exe
# Sidebar – nawigacja
st.sidebar.title("📚 Nawigacja")
page = st.sidebar.radio("Wybierz tryb:", ["📖 Użytkownik", "🛠️ Admin", "⚙️ Asystent AI"])

# Widoki
if page == "📖 Użytkownik":
    main_view.show()
elif page == "🛠️ Admin":
    admin_view.show()
elif page == "⚙️ Asystent AI":
    st.title("Asystent AI")
    st.markdown("Wkrótce dostępne! Pracujemy nad tym, aby dostarczyć Ci najlepsze doświadczenie.")
