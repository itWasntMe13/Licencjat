# import api_manager
# import file_manager
# import text_manager
#
# text_name = "merged_responses"
# extension = "txt"
# file_path = f"./output_data/{text_name}.{extension}"
#
# # Wczytujemy cały tekst z pliku
# whole_text = file_manager.load_file(file_path)
#
# # Dzielimy tekst na fragmenty
# list_of_fragments = text_manager.split_text(whole_text, 15000)
#
# # Wyświetlamy listę fragmentów
# for i in range(0, len(list_of_fragments)):
#     print(list_of_fragments[i])
#
# # Określamy instrukcje dla GPT
# # Tym razem pozwolimy mu na bardziej kreatywne streszczenie
# instructions_for_gpt = ("Utwórz streszczenie poniższego tekstu. "
#                         "Odpowiedź może być kreatywna i może być rozbudowana."
#                         "\nTekst:")
#
# # Dla każdego fragmentu tworzymy obiekt zapytania do API
# for fragment in list_of_fragments:
#     # Określamy ścieżkę do zapisu odpowiedzi, która po każdym fragmencie będzie się zmieniać
#     save_response_path = f".\\responses\\{text_name}_streszczenie_{list_of_fragments.index(fragment):06}.txt"
#     # Łączymy instrukcje z fragmentem
#     prompt = f"{instructions_for_gpt}\n{fragment}"
#     # Tworzymy obiekt
#     prompt_object = api_manager.GPTPrompt(prompt)
#     # Wysyłamy zapytanie do API z włączonym zapisem informacji
#     prompt_object.get_response(save_info=True, save_to=save_response_path)
#     print(f"Response saved in {save_response_path}")
#
#
# def create_summary_files():
#     # Określamy nazwę tekstu i dokładając rozszerzenie tworzymy pełną nazwę pliku
#     text_name = "O Dwóch Takich Co Ukradli Księżyc"
#     extension = "txt"
#     file_name = f"{text_name}.{extension}"
#
#     # Wczytujemy cały tekst z pliku
#     whole_text = file_manager.load_file(file_name)
#     # Dzielimy tekst na fragmenty
#     list_of_fragments = text_manager.split_text(whole_text, 15000)
#
#     # # Wyświetlamy listę fragmentów
#     # for i in range(0, len(list_of_fragments)):
#     #     print(list_of_fragments[i])
#
#     # Określamy instrukcje dla GPT
#     instructions_for_gpt = ("Utwórz streszczenie poniższego tekstu. "
#                             "Odpowiedź ma zawierać jedynie streszcznie, żadnych wstępów lub komentarzy."
#                             "\nTekst:")
#
#     # Dla każdego fragmentu tworzymy obiekt zapytania do API
#     for fragment in list_of_fragments:
#         # Określamy ścieżkę do zapisu odpowiedzi, która po każdym fragmencie będzie się zmieniać
#         save_response_path = f".\\responses\\{text_name}_streszczenie_{list_of_fragments.index(fragment):06}.txt"
#         # Łączymy instrukcje z fragmentem
#         prompt = f"{instructions_for_gpt}\n{fragment}"
#         # Tworzymy obiekt
#         prompt_object = api_manager.GPTPrompt(prompt)
#         # Wysyłamy zapytanie do API z włączonym zapisem informacji
#         prompt_object.get_response(save_info=True, save_info_path=save_response_path)
#         print(f"Response saved in {save_response_path}")
#
#     # Tworzymy obiekt, który jest zapytaniem do API i określamy treść zapytania
#     # prompt_object = api_manager.GPTPrompt(prompt)
#     #
#     # # Wysyłamy zapytanie do API
#     # prompt_object.get_response(save_info=True, save_info_path=save_response_path)
#     #
#     # # Wyświetlamy dane z obiektu
#     # print(prompt_object)
#     # print(f"Response saved in {save_response_path}")