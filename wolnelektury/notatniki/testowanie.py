from API_handling import download_json_file
import json
import os


    download_json_file(".\\books.json", "https://wolnelektury.pl/api/books/?format=json")

with open(".\\json_files\\books.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

    for book in json_data:
        print(book["title"])

    # Count the number of books in the database
    print(f"Number of books in the database: {len(json_data)}")
