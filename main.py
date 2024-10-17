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
    prompt = "Władca Pierścieni"
    # prompt = "Titanic at night"

    gpt_prompt = api_manager.GPTPrompt(prompt)

    gpt_prompt.get_gpt(save_response=True)
    print(gpt_prompt)
    # Dodać obsługę generowania większej ilości zdjęć

    # Przy generowaniu większej ilości zdjęć seryjnie,
    # każdy błąd w zapytaniu może spowodować przerwanie działania programu
    # # W związku z tym, trzeba będzie zaimplementować obsługę błędów
    # dalle_prompt = api_manager.DALLEPrompt(prompt)
    #
    # dalle_prompt.get_dalle()
    # dalle_prompt.show_response_img()
    # print(dalle_prompt)
    # print(dalle_prompt.__str__())
