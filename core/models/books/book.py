class Book:
    def __init__(
        self,
        slug: str,
        title: str,
        author: str,
        kind: str,
        epoch: str,
        genre: str,
        content: str,
        can_summarize: bool = False,
    ):
        self.slug = slug
        self.title = title
        self.author = author
        self.kind = kind
        self.epoch = epoch
        self.genre = genre
        self.content = content
        self.can_summarize = can_summarize

    def to_dict(self) -> dict:
        return {
            "slug": self.slug,
            "title": self.title,
            "author": self.author,
            "kind": self.kind,
            "epoch": self.epoch,
            "genre": self.genre,
            "content": self.content,
            "can_summarize": self.can_summarize,
        }

    def from_dict(data: dict) -> "Book":
        return Book(
            slug=data.get("slug"),
            title=data.get("title"),
            author=data.get("author"),
            kind=data.get("kind"),
            epoch=data.get("epoch"),
            genre=data.get("genre"),
            content=data.get("content"),
            can_summarize=data.get("can_summarize", False),
        )
