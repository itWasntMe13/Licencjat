from ai import api_manager, file_manager, text_manager
from wolnelektury.normalization import normalize_title
from ai.file_manager import merge_responses
from config import GLOBAL_PATH

def get_final_summary():

    summary_parts_path = f"{GLOBAL_PATH}\\files\\ai\\summary_parts"
    summaries_path = f"{GLOBAL_PATH}\\files\\ai\\summaries"

    merge_responses(summary_parts_path, summaries_path, "final_summary.txt")

    text_name = "merged_responses"
    extension = "txt"
    file_path = "./ai/output_data/gpt/merged_responses.txt"

    # Wczytujemy cały tekst z pliku
    whole_text = file_manager.load_file(file_path)

    # Dzielimy tekst na fragmenty
    list_of_fragments = text_manager.split_text(whole_text, 60000)

    # Wyświetlamy listę fragmentów
    for i in range(0, len(list_of_fragments)):
        print(list_of_fragments[i])

    # Określamy instrukcje dla GPT
    # Tym razem pozwolimy mu na bardziej kreatywne streszczenie
    instructions_for_gpt = ("Utwórz streszczenie poniższego tekstu. "
                            "Odpowiedź może być kreatywna i może być rozbudowana."
                            "\nTekst:")

    # Dla każdego fragmentu tworzymy obiekt zapytania do API
    for fragment in list_of_fragments:
        # Określamy ścieżkę do zapisu odpowiedzi, która po każdym fragmencie będzie się zmieniać
        save_response_path = f".\\ai\\responses\\{text_name}_streszczenie_{list_of_fragments.index(fragment):06}.txt"
        # Łączymy instrukcje z fragmentem
        prompt = f"{instructions_for_gpt}\n{fragment}"
        # Tworzymy obiekt
        prompt_object = api_manager.GPTPrompt(prompt)
        # Wysyłamy zapytanie do API z włączonym zapisem informacji
        prompt_object.get_gpt(save_info=True, save_to=save_response_path, save_response=True, system_role=instructions_for_gpt)
        print(f"Response saved in {save_response_path}")


def create_summary_files(title):
    # Określamy nazwę tekstu i dokładając rozszerzenie tworzymy pełną nazwę pliku
    extension = "txt"
    title = normalize_title(title)
    file_name = f"./books/txt/{title}.{extension}"

    # Wczytujemy cały tekst z pliku
    whole_text = file_manager.load_file(file_name)
    # Dzielimy tekst na fragmenty
    list_of_fragments = text_manager.split_text(whole_text, 15000)

    # Wyświetlamy listę fragmentów
    for i in range(0, len(list_of_fragments)):
         print(list_of_fragments[i])

    # Określamy instrukcje dla GPT
    summary_system_role = ("Utwórz streszczenie poniższego fragmentu tekstu. "
                            "Odpowiedź ma zawierać jedynie streszczenie, żadnych wstępów lub komentarzy tak, by móc ten fragment połączyć z poprzednim i następnym."
                            "\nTekst:")

    # Dla każdego fragmentu tworzymy obiekt zapytania do API
    for fragment in list_of_fragments:
        # Określamy ścieżkę do zapisu odpowiedzi, która po każdym fragmencie będzie się zmieniać
        save_response_path = f"{WORKING_DIRECTORY}\\responses\\{title}_streszczenie_{list_of_fragments.index(fragment):06}.txt"
        # Łączymy instrukcje z fragmentem
        prompt = f"{summary_system_role}\n{fragment}"
        # Tworzymy obiekt
        gpt_summary_obj = api_manager.GPTPrompt(prompt)
        # Wysyłamy zapytanie do API z włączonym zapisem informacji
        gpt_summary_obj.get_gpt(save_response=True, system_role=summary_system_role, save_to=save_response_path)
        print(f"Response saved in {save_response_path}")
