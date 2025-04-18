from core.config import BOOKS_DIR
from core.utils import txt_request, save_txt_file


class BookService:



    @staticmethod
    def download_book_txt(book_detail, save_dir=BOOKS_DIR) -> str:
        """
        Pobiera treść książki na podstawie obiektu BookDetail.
        :param book_detail:
        :param save_dir:
        :return: Treść książki w string-u.
        """
        url = book_detail.txt_url  # book_detail.txt_url to URL do książki w formacie TXT
        book = txt_request(url)

        try:
            return book.decode("utf-8") # Dekodowanie bajtów na string
        except UnicodeDecodeError as e:
            print(f"Błąd dekodowania książki {book_detail.title}: {e}")
            return None

    @staticmethod
    def split_text_into_fragments(text: str, fragment_length: int = 3000) -> list[str]:
        """
        Dzieli tekst na fragmenty o zadanej długości (domyślnie 3000 znaków).

        :param text: Tekst wejściowy do podziału.
        :param fragment_length: Maksymalna długość pojedynczego fragmentu.
        :return: Lista fragmentów tekstu.
        """
        fragments = []
        text_length = len(text)
        for i in range(0, text_length, fragment_length):
            fragments.append(text[i:i + fragment_length])
        return fragments