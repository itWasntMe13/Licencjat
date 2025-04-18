class Book:
    def __init__(
        self,
        title: str,
        author: str,
        kind: str,
        epoch: str,
        genre: str,
        content: str
    ):
        self.title = title
        self.author = author
        self.kind = kind
        self.epoch = epoch
        self.genre = genre
        self.content = content

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "kind": self.kind,
            "epoch": self.epoch,
            "genre": self.genre,
            "content": self.content
        }

    def from_dict(data: dict) -> "Book":
        return Book(
            title=data.get("title"),
            author=data.get("author"),
            kind=data.get("kind"),
            epoch=data.get("epoch"),
            genre=data.get("genre"),
            content=data.get("content")
        )