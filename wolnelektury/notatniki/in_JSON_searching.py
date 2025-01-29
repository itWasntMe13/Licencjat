import os
import json


def look_for_book_title(title):
    try:
        if not os.path.exists(".\\json_files\\books.json"):
            raise Exception("File books.json does not exist.")
        else:
            with open(".\\json_files\\books.json", "r", encoding="utf-8") as file:
                data = file.read()
                json_data = json.loads(data)

                for book in json_data:
                    if book["title"] == title:
                        return f"Book {title} found in the database."
                return f"Book {title} not found in the database."
    except Exception as e:
        return f"Exception raised while looking for book title: {e}"
