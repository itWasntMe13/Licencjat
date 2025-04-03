from dataclasses import dataclass

@dataclass
class BookDetail:
    title: str
    author: str
    txt_url: str
    book_url: str

    @staticmethod
    def from_dict(data: dict) -> "BookDetail":
        return BookDetail(
            title=data.get("title", ""),
            author=data["authors"][0]["name"] if data.get("authors") else "",
            txt_url=data.get("txt", ""),
            book_url=data.get("url", "")
        )
