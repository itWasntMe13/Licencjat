import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st
from core.services.common.maintenance_service import MaintenanceService

def show():
    st.title("🛠️ Panel administracyjny")
    st.markdown("Opcje zarządzania aplikacją. Niektóre funkcjonalności pozwalają na serwisowe rozwiązywanie problemów aplikacji.")

    st.subheader("Zarządzanie książkami.")

    # Budowa katalogów. Może rozwiązywać niektóre problemy aplikacji.
    if st.button("📂 Utwórz katalogi na dane wejściowe i wyjściowe"):
        MaintenanceService.build_environment()
        st.success("Katalogi zostały utworzone.")

    if st.button("🗑️ Usuń wszystkie książki oraz ich szczegóły"):
        if st.button("Potwierdź usunięcie", key="confirm_delete_books"):
            MaintenanceService.clear_books_dir()
            MaintenanceService.clear_books_details_dir()
            st.success("Książki oraz ich szczegóły zostały usunięte.")
        else:
            st.warning("Aby potwierdzić usunięcie, kliknij ponownie przycisk.")

    if st.button("🔁 Zaktualizuj indeksy książek"):
        MaintenanceService.create_book_indexes(force_update=True)
        st.success("Indeksy zostały zaktualizowane.")
