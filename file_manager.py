import glob
import datetime
import os
import PIL.Image

def check_file_structure():
    # Tworzymy listę, do której będziemy dodawać informacje o brakujących folderach
    missing_folders = []

    if not os.path.exists("./output_data"):
        missing_folders.append("./output_data")

    if not os.path.exists("./output_data/dalle"):
        missing_folders.append("./output_data/dalle")

    if not os.path.exists("./output_data/dalle/images"):
        missing_folders.append("./output_data/dalle/images")

    if not os.path.exists("./output_data/dalle/info"):
        missing_folders.append("./output_data/dalle/info")

    if not os.path.exists("./output_data/gpt"):
        missing_folders.append("./output_data/gpt")

    if not os.path.exists("./input_data"):
        missing_folders.append("./input_data")

    if not os.path.exists("./debug_data"):
        missing_folders.append("./debug_data")

    if not os.path.exists("./debug_data/dalle"):
        missing_folders.append("./debug_data/dalle")

    if not os.path.exists("./debug_data/gpt"):
        missing_folders.append("./debug_data/gpt")

    # Jeśli brakujące foldery istnieją, to pytamy użytkownika, czy chce je utworzyć
    if missing_folders:
        print("Brakujące foldery:")
        for folder in missing_folders:
            print(f"- {folder}")
        if input("Mogą powodować błędy programu. Czy chcesz je utworzyć? [T/n]: ").lower() == "t":
            for folder in missing_folders:
                os.makedirs(folder, exist_ok=True)
        else:
            return "Niektóre foldery nie istnieją, może to spowodować błędy w działaniu programu."

# Funkcja wczytująca plik o podanej ścieżce
def load_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"An error occurred while loading a file: {e}"

# Funkcja dodająca treść do pliku o podanej ścieżce
def append_file(path, content):
    # Jeśli plik nie istnieje, zostanie utworzony
    if not glob.glob(path):
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(f"{datetime.datetime.now}\n") # Dodajemy datę i godzinę
                file.write(content) # Dodajemy treść
                file.write("\n" + "-" * 50 + "\n\n") # Dodajemy znacznik końca wpisu
        except Exception as e:
            return f"An error occurred while creating a new file: {e}"
    else:
        try:
            with open(path, "a", encoding="utf-8") as file:
                file.write(f"{datetime.datetime.now()}\n") # Dodajemy datę i godzinę
                file.write(content) # Dodajemy treść
                file.write("\n" + "-" * 50 + "\n\n") # Dodajemy znacznik końca wpisu
        except Exception as e:
            return f"An error occurred while appending to an existing file: {e}"

# Funkcja zapisująca treść do pliku o podanej ścieżce
def save_file(path, content):
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(f"{datetime.datetime.now()}\n") # Dodajemy datę i godzinę
            file.write(content) # Dodajemy treść
    except Exception as e:
        return f"An error occurred: {e}"

# Funkcja tworząca folder o podanej ścieżce
def create_folder(path):
    try:
        os.makedirs(path, exist_ok=True)
    except Exception as e:
        return f"An error occurred while creating a folder: {e}"

# Funkcja do generowania nazwy pliku w formacie img_XXXX.png, przy czym XXXX to niepowtarzalne ID pliku
def gen_img_name():
    # Pobieramy aktualną datę i godzinę
    now = datetime.datetime.now()

    # Tworzymy nazwę folderu na podstawie daty
    folder_path = f"output_data/dalle/images/dalle_img_{now.year}-{now.month:02d}-{now.day:02d}"

    # Jeśli folder jeszcze nie istnieje to tworzymy go
    if not os.path.exists(folder_path):
        create_folder(folder_path)
        print(f"Folder {folder_path} utworzony")

    # Sprawdzamy najwyższe ID pliku na podstawie ostatnich 4 znaków nazwy pliku, jeśli folder nie jest pusty, jeśli folder jest pusty to ID = 1
    if not os.listdir(folder_path):
        img_id = 1
    else:
        img_id = max([int(file_name[4:8]) for file_name in os.listdir(folder_path)]) + 1

    # Zwracamy ścieżkę pliku w formacie img_XXXX.png
    return f"{folder_path}/img_{img_id:04d}"
    # 04d oznacza, że liczba ma być zawsze 4 cyfrowa, jeśli jest mniej niż 4 cyfry, to zostaną dodane zera na początku

# Funkcja zapisująca obraz do pliku o podanej ścieżce (domyślnie generuje nazwę pliku przy pomocy funkcji gen_img_name())
def save_image(image):
    path = gen_img_name()

    try:
        content_type = image.format  # Pobierz format obrazu
        extension = content_type.lower() # Przekonwertuj format na małe litery
        path = f"{path}.{extension}"  # Dodaj rozszerzenie do ścieżki
        print(f"Próba zapisania obrazu do pliku: {path}")
        image.save(path)  # Zapisz obraz przy użyciu PIL
    except Exception as e:
        return f"An error occurred while saving an image: {e}"

# Funkcja łącząca powstałe teksty z katalogu responses w jeden plik .txt
def merge_responses():
    try:
        with open("./output_data/merged_responses.txt", "w", encoding="utf-8") as file:
            for file_name in glob.glob("./responses/*.txt"):
                with open(file_name, "r", encoding="utf-8") as file_to_read:
                    file.write(file_to_read.read())
    except Exception as e:
        return f"An error occurred while merging responses: {e}"

# Funkcja usuwająca ostatnie 6 linii z każdego pliku .txt w ./responses
# Funkcja pozwala usunąć zbędne informacje o zapytaniu
# def remove_last_6_lines():
#     try:
#         for file_name in glob.glob("./responses/*.txt"):
#             with open(file_name, "r", encoding="utf-8") as file:
#                 lines = file.readlines()
#             with open(file_name, "w", encoding="utf-8") as file:
#                 file.writelines(lines[:-6])
#     except Exception as e:
#         return f"An error occurred while removing last 6 lines: {e}"
#
# # Funkcja usuwająca pierwsze 10 znaków z każdego pliku .txt w ./responses
# # Funkcja pozwala usunąć zbędne informacje o zapytaniu
# def remove_first_10_chars():
#     try:
#         for file_name in glob.glob("./responses/*.txt"):
#             with open(file_name, "r", encoding="utf-8") as file:
#                 lines = file.readlines()
#             with open(file_name, "w", encoding="utf-8") as file:
#                 for line in lines:
#                     file.write(line[10:])
#     except Exception as e:
#         return f"An error occurred while removing first 10 characters: {e}"