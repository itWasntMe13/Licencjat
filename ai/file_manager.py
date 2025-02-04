import glob
import datetime
import os
import PIL.Image
from config import GLOBAL_PATH

# Funkcja budująca strukturę folderów
def check_file_structure():
    # Wczytujemy zmienną globalną ze ścieżką projektu
    global_path = GLOBAL_PATH

    # Lista wszystkich ścieżek programu
    required_paths = [
        "files/ai/summary_parts",
        "files/ai/summaries",
        "files/ai/debug_data",
        "files/ai/debug_data/dalle",
        "files/ai/debug_data/gpt",
        "files/ai/output_data/dalle",
        "files/ai/output_data/dalle/images",
        "files/ai/output_data/dalle/info",
        "files/ai/output_data/gpt",
        "files/wolne_lektury/books",
        "files/wolne_lektury/api_errors",
        "files/wolne_lektury/json_files",
    ]

    # Sprawdzamy, które foldery nie istnieją
    missing_folders = []
    for rel_path in required_paths:
        full_path = os.path.join(global_path, rel_path)
        if not os.path.exists(full_path):
            missing_folders.append(full_path)

    # Jeśli brakuje jakichś folderów, wyświetlamy je i pytamy użytkownika o utworzenie
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
def gen_img_name(path):
    # Pobieramy aktualną datę i godzinę
    now = datetime.datetime.now()

    # Tworzymy nazwę folderu na podstawie daty
    folder_path = f"{path}/dalle_img_{now.year}-{now.month:02d}-{now.day:02d}"

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
        print(f"Próba zapisania obrazu do pliku: {path}...")
        image.save(path)  # Zapisz obraz przy użyciu PIL
        # Jeśli obraz został zapisany, powiadom użytkownika
        if os.path.exists(path):
            print(f"Obraz zapisany pomyślnie jako {path}")
        else:
            print(f"Nie udało się zapisać obrazu jako {path}")
    except Exception as e:
        return f"An error occurred while saving an image: {e}"

# Funkcja łącząca powstałe teksty z katalogu responses w jeden plik .txt
def merge_responses(summary_parts_path, save_summary_to):
    try:
        with open(save_summary_to, "a", encoding="utf-8") as file:
            for file_name in glob.glob(f"{summary_parts_path}/*.txt"):
                with open(file_name, "r", encoding="utf-8") as file_to_read:
                    file.write(file_to_read.read())
    except Exception as e:
        return f"An error occurred while merging responses: {e}"
