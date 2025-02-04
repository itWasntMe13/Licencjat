from ai import summary_creator
from wolnelektury import wolnelektury_handler
from ai.file_manager import check_file_structure
# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28

if __name__ == '__main__':
    check_file_structure() # Sprawdzamy, czy istnieją wymagane katalogi.

    # Pobieramy książkę i zapisujemy jej tytuł w zmiennej
    title = wolnelektury_handler.download_requsted_book()

    summary = summary_creator.get_summary(title, _save_summary=True)
    # Tworzymy streszczenie książki

    # Wyświetlamy streszczenie
    print(summary)
