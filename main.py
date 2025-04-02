from app.ai import summary_creator
from app.wolnelektury import wolnelektury_handler
# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28

if __name__ == '__main__':

    # Pobieramy książkę i zapisujemy jej tytuł w zmiennej
    title = wolnelektury_handler.download_requsted_book()

    summary = summary_creator.get_summary(title, _save_summary=True)
    # Tworzymy streszczenie książki

    # Wyświetlamy streszczenie
    print(summary)
