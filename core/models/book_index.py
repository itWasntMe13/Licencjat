from dataclasses import dataclass
from typing import Optional

@dataclass
class BookIndex:
    id: str               # full_sort_key
    title: str
    author: str
    kind: str
    epoch: str
    genre: str
    url: str
    href: str
    downloaded: bool = False
    path_to_file: Optional[str] = None

    @staticmethod
    def from_raw_dict(data: dict) -> "BookIndex":
        return BookIndex(
            id=data["full_sort_key"],
            title=data["title"],
            author=data["author"],
            kind=data["kind"],
            epoch=data["epoch"],
            genre=data["genre"],
            url=data["url"],
            href=data["href"],
        )

