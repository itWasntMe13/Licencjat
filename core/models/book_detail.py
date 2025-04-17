class BookDetail:
    def __init__(
        self,
        title: str,
        txt_url: str,
        author: str,
        epoch: str,
        genre: str
    ):
        self.title = title
        self.txt_url = txt_url
        self.author = author
        self.epoch = epoch
        self.genre = genre

    @staticmethod
    def from_api_dict(data: dict) -> "BookDetail":
        return BookDetail(
            title=data.get("title"),
            txt_url=data.get("txt"),
            author=data.get("authors", [{}])[0].get("name"),
            epoch=data.get("epochs", [{}])[0].get("name"),
            genre=data.get("genres", [{}])[0].get("name")
        )

    def from_json_dict(data: dict) -> "BookDetail":
        return BookDetail(
            title=data.get("title"),
            txt_url=data.get("txt_url"),
            author=data.get("author"),
            epoch=data.get("epoch"),
            genre=data.get("genre")
        )

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "txt_url": self.txt_url,
            "author": self.author,
            "epoch": self.epoch,
            "genre": self.genre
        }