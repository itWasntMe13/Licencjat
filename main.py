from ai import api_manager, summary_creator
from ai.api_manager import MY_API_KEY
from wolnelektury import wolnelektury_handler
from ai.file_manager import check_file_structure
# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28

if __name__ == '__main__':
    check_file_structure() # Sprawdzamy, czy istnieją wymagane katalogi.

    # title = wolnelektury_handler.download_requsted_book()


    # ROLE SYSTEMU
    # summary_system_role = "Jesteś pisarzem streszczeń. Tworzysz streszczenia dla podanych tytułów."
    # tag_generation_role = "Jesteś asystentem w obsłudze DALL-E."

    # summary_creator.create_summary_files(title)


    # gpt_summary_obj = api_manager.GPTPrompt(title)
    # gpt_tag_generation_obj = api_manager.GPTPrompt(tag_generation_prompt)
    #
    # gpt_summary_obj.get_gpt(save_response=True, system_role = summary_system_role)
    # gpt_tag_generation_obj.get_gpt(system_role = tag_generation_role)
    #
    # dalle_prompt = gpt_tag_generation_obj.response
    #
    # print(dalle_prompt)
    # # Dodać obsługę generowania większej ilości zdjęć
    #
    # # Przy generowaniu większej ilości zdjęć seryjnie dalle
    # # każdy błąd w zapytaniu może spowodować przerwanie działania programu
    # # # W związku z tym, trzeba będzie zaimplementować obsługę błędów
    #
    # dalle_gen_img_obj = api_manager.DALLEPrompt(dalle_prompt)
    #
    # dalle_gen_img_obj.get_dalle()
    # dalle_gen_img_obj.show_response_img()
    # print(dalle_prompt)
    # print(dalle_prompt.__str__())
