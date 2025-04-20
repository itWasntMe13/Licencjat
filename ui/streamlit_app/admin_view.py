import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st
from core.services.common.maintenance_service import MaintenanceService
from core.setup import create_book_indexes

def show():
    st.title("🛠️ Panel administracyjny")
    st.markdown("Opcje zarządzania danymi aplikacji.")

    if st.button("🧹 Usuń wszystkie książki"):
        MaintenanceService.truncate_books()
        st.success("Usunięto wszystkie książki.")

    if st.button("🔁 Zaktualizuj indeksy książek"):
        create_book_indexes(force_update=True)
        st.success("Indeksy zostały zaktualizowane.")
