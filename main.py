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
    # title = "Kaczor Donald"
    # title = "Zielona mila"
    # title = "Mein Kampf" # ma blokadę :)
    # PROMPTY
    # title = "Harry Potter"
    title = "Reksio"
    tag_generation_prompt = (f"Wskaż tagi na podstawie których DALL-E utworzy obraz mający być okładką tekstu: {title}"
                           f" W odpowiedzi którą mi przekażesz mają znaleźć się tylko te tagi, bez dodatkowego komentarza.")

    # ROLE SYSTEMU
    summary_system_role = "Jesteś pisarzem streszczeń. Tworzysz streszczenia dla podanych tytułów."
    tag_generation_role = "Jesteś asystentem w obsłudze DALL-E."

    gpt_summary_obj = api_manager.GPTPrompt(title)
    gpt_tag_generation_obj = api_manager.GPTPrompt(tag_generation_prompt)

    gpt_summary_obj.get_gpt(save_response=True, system_role = summary_system_role)
    gpt_tag_generation_obj.get_gpt(system_role = tag_generation_role)

    dalle_prompt = gpt_tag_generation_obj.response

    print(dalle_prompt)
    # Dodać obsługę generowania większej ilości zdjęć

    # Przy generowaniu większej ilości zdjęć seryjnie dalle
    # każdy błąd w zapytaniu może spowodować przerwanie działania programu
    # # W związku z tym, trzeba będzie zaimplementować obsługę błędów

    dalle_gen_img_obj = api_manager.DALLEPrompt(dalle_prompt)

    dalle_gen_img_obj.get_dalle()
    dalle_gen_img_obj.show_response_img()
    # print(dalle_prompt)
    # print(dalle_prompt.__str__())
