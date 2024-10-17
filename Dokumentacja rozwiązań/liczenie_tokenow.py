import tiktoken

if __name__ == '__main__':
    # Przykładowy tekst
    text = "Testowy tekst do obliczenia liczby tokenów."
    # Wybór modelu AI - w tym przypadku "gpt-3.5-turbo"
    model = "gpt-3.5-turbo"

    # Określenie modelu na podstawie którego tekst będzie tokenizowany
    encoding = tiktoken.encoding_for_model(model)
    # Tokenizacja tekstu i zapisanie wyniku do listy tokenów
    token_list = encoding.encode(text)
    # Ilość tokenów jest równa długości listy tokenów
    print(len(encoding.encode(text)))
