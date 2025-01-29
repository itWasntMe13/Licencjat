# import requests
# import simplejson as json
#
# response_API = requests.get("https://random.dog/woof.json")
#
# # Wypisanie statusu połączenia z API
# print(response_API.status_code)
#
# #print(response_API.content)
# #print(type(response_API.content))
#
#
# pobrany_json = str(response_API.content)[2:-1]
#
#
# # Zapis pobranego pliku .json
# open("woof.json", "w").write(pobrany_json)
#
#
# # Otwórz plik JSON
# with open("woof.json", "r") as json_file:
#     # Wczytaj dane JSON z pliku
#     data = json.load(json_file)
#
# # Pobierz link z danych JSON
# url = data["url"]
#
# API_zdjecia = requests.get(url)
# zdjecie = API_zdjecia.content
#
# try:
#     open("zdjecie.jpg", "wb").write(zdjecie)
#     print("Zapisano zdjęcie pieska.")
# except:
#     print("Zdjęcie nie jest w formacie .jpg.")
#
# import requests
# import simplejson as json
#
# def pobranie_jsona(nazwa_pliku, url):
#
#     response_API = requests.get(url)
#     plik_json = response_API.content
#
#     open(nazwa_pliku, "wb").write(plik_json)
#
# def pobranie_ksiazki(nazwa_pliku, url):
#
#     response_API = requests.get(url)
#     ksiazka = response_API.content
#
#     open(nazwa_pliku, "wb").write(ksiazka)
#
# def otwarcie_jsona(nazwa_pliku):
#
#     with open(nazwa_pliku, "r", encoding="utf-8") as plik:
#         dane = json.load(plik)
#     return dane
#
# def otwarcie_ksiazki(nazwa_pliku):
#
#     with open(nazwa_pliku, "r", encoding="utf-8") as plik:
#         dane = plik.read()
#     return dane
#
# def generuj_HTML_kategorii(plik_json):
#     for encja in dane:
#         print(encja["name"])
#
# url_jsona = "https://wolnelektury.pl/api/kinds/?format=json"
# pobranie_jsona("rodzaje.json", url_jsona)
#
# url_ksiazki = "https://wolnelektury.pl/media/book/txt/adas.txt"
# pobranie_ksiazki("adas.txt", url_ksiazki)
#
# dane = otwarcie_jsona("rodzaje.json")
#
# download_book(normalized_text_title, "https://wolnelektury.pl/media/book/txt/" + normalized_text_title + ".txt")
#
#
#
#
# def create_normalized_list_of_downloadable_txt_books():
#     if os.path.exists("json_files//downloadable_txt_books.json"):
#         return json.load(open("json_files//downloadable_txt_books.json", "r", encoding="utf-8"))
#
#     else:
#         list_of_downloadable_txt_books_titles = []
#         title_list, normalized_title_list = create_titles_list(), create_normalized_titles_list()
#         print(normalized_title_list)
#
#         # Downloading books using titles from json file
#         for normalized_title in normalized_title_list:
#
#             url = book_list[normalized_title_list.index(normalized_title)].url
#             url_segments = url.split("/")
#             url_last_segment = url_segments[-2]
#
#             try:
#
#                 download_book(normalized_title, "https://wolnelektury.pl/media/book/txt/" + url_last_segment + ".txt")
#
#                 if normalized_title not in list_of_downloadable_txt_books_titles:
#                     list_of_downloadable_txt_books_titles.append(normalized_title)
#
#             except Exception as e:
#                 print(f"Exception raised while trying to download txt file of the book: {normalized_title} {e}")
#
#         with open("json_files//downloadable_txt_books.json", "w", encoding="utf-8") as file:
#             file.write(json.dumps(list_of_downloadable_txt_books_titles, ensure_ascii=False, indent=4))
#
#         return list_of_downloadable_txt_books_titles
from unidecode import unidecode
print(unidecode("***** 12341"))

