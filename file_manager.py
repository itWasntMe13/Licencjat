import glob


# Funkcja wczytująca plik o podanej ścieżce
def load_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        return f"An error occurred: {e}"


# Funkcja łącząca powstałe teksty z katalogu responses w jeden plik .txt
def merge_responses():
    try:
        with open("./output_data/merged_responses.txt", "w", encoding="utf-8") as file:
            for file_name in glob.glob("./responses/*.txt"):
                with open(file_name, "r", encoding="utf-8") as file_to_read:
                    file.write(file_to_read.read())
    except Exception as e:
        return f"An error occurred: {e}"


# Funkcja usuwająca ostatnie 6 linii z każdego pliku .txt w ./responses
# Funkcja pozwala usunąć zbędne informacje o zapytaniu
def remove_last_6_lines():
    try:
        for file_name in glob.glob("./responses/*.txt"):
            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(file_name, "w", encoding="utf-8") as file:
                file.writelines(lines[:-6])
    except Exception as e:
        return f"An error occurred: {e}"


# Funkcja usuwająca pierwsze 10 znaków z każdego pliku .txt w ./responses
# Funkcja pozwala usunąć zbędne informacje o zapytaniu
def remove_first_10_chars():
    try:
        for file_name in glob.glob("./responses/*.txt"):
            with open(file_name, "r", encoding="utf-8") as file:
                lines = file.readlines()
            with open(file_name, "w", encoding="utf-8") as file:
                for line in lines:
                    file.write(line[10:])
    except Exception as e:
        return f"An error occurred: {e}"