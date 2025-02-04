from ai import api_manager, summary_creator
from wolnelektury import wolnelektury_handler
from ai.file_manager import check_file_structure
# WAŻNE - PROGRAM KORZYSTA Z BIBLIOTEKI OPENAI==0.28

if __name__ == '__main__':
    check_file_structure() # Sprawdzamy, czy istnieją wymagane katalogi.


    # title = wolnelektury_handler.download_requsted_book()
    # summary_creator.create_summary_files(title)
