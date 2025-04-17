from core.config import BOOKS_DIR
from core.utils import txt_request, save_txt_file


class BookService:
    @staticmethod
    def download_book_txt(book_detail, save_dir=BOOKS_DIR) -> None:
        """
        Pobiera książkę na podstawie pola txt_url z obiektu BookDetail i zapisuje ją do pliku TXT.
        :param book_detail:
        :param save_dir:
        :return:
        """
        url = book_detail.txt_url  # book_detail.txt_url to URL do książki w formacie TXT
        book = txt_request(url)

        # Zapisanie książki do pliku TXT
        save_path = save_dir / f"{book_detail.title}.txt"
        save_txt_file(book, save_path)
