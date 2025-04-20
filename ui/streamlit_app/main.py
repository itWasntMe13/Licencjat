import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import streamlit as st
from ui.streamlit_app import main_view, admin_view

# Sidebar – nawigacja
st.sidebar.title("📚 Nawigacja")
page = st.sidebar.radio("Wybierz tryb:", ["📖 Użytkownik", "🛠️ Admin"])

# Widoki
if page == "📖 Użytkownik":
    main_view.show()
elif page == "🛠️ Admin":
    admin_view.show()
