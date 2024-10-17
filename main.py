import file_manager
import summary_creator
import text_manager
import api_manager

# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28

if __name__ == '__main__':
    # summary_creator.create_summary_files()

    # Usuwamy ostatnie 6 linii z każdego pliku w ./responses
    # file_manager.remove_last_6_lines()

    # Usuwamy pierwsze 10 znaków z każdego pliku w ./responses
    # file_manager.remove_first_10_chars()

    # Tworzymy nowy plik na podstawie merge_responses()
    # file_manager.merge_responses()

    # Tworzymy prompt do API DALL-E
    # prompt = "Władca Pierścieni"
    # prompt = "Titanic at night"
    title = "Kaczor Donald"
    gpt_to_dalle_prompt = (f"Wskaż tagi na podstawie których DALL-E utworzy obraz mający być okładką tekstu: {title}"
                           f"W odpowiedzi którą mi przekażesz mają znaleźć się tylko te tagi, bez dodatkowego komentarza.")

    gpt_prompt = api_manager.GPTPrompt(title)
    gpt_to_dalle_prompt = api_manager.GPTPrompt(gpt_to_dalle_prompt)

    gpt_prompt.get_gpt(save_response=True, system_role = "Jesteś pisarzem streszczeń. Tworzysz streszczenia dla podanych tytułów.")
    gpt_to_dalle_prompt.get_gpt(system_role = "Jesteś asystentem w obsłudze DALL-E.")

    print(gpt_prompt)
    print(gpt_to_dalle_prompt.response)
    # Dodać obsługę generowania większej ilości zdjęć

    # Przy generowaniu większej ilości zdjęć seryjnie,
    # każdy błąd w zapytaniu może spowodować przerwanie działania programu
    # # W związku z tym, trzeba będzie zaimplementować obsługę błędów

    dalle_prompt = api_manager.DALLEPrompt(gpt_to_dalle_prompt.response)

    dalle_prompt.get_dalle()
    dalle_prompt.show_response_img()
    # print(dalle_prompt)
    # print(dalle_prompt.__str__())
