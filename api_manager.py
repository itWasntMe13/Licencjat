import openai
import tiktoken
import requests
import PIL.Image
from io import BytesIO

# Mój osobisty klucz API
MY_API_KEY = "sk-dUeOCCtcjrcBJyuZ9GKGLsV8fZyS99GFWG0_FxcfBzT3BlbkFJKjap0jGwXzRMlw1FEEZZHuROU4c5EN7nFrGUTjU0UA"


# Klasa do obsługi API dla GPT-3.5
class GPTPrompt:
    def __init__(self, prompt, api_key=MY_API_KEY, model="gpt-3.5-turbo", token_limit=4096):
        openai.api_key = api_key  # Ustawienie klucza API dla OpenAI
        self.model = model  # Model AI, w projekcie używamy GPT-3.5 Turbo
        self.token_limit = token_limit  # Limit tokenów na odpowiedź
        self.prompt = prompt  # Zapytanie do API
        self.response = None  # Odpowiedź z API
        self.cost = None  # Przybliżony koszt zapytania i odpowiedzi
        self.input_tokens = self.count_tokens(prompt)  # Liczbę tokenów w zapytaniu można wyliczyć od razu
        self.output_tokens = None  # Liczba tokenów w odpowiedzi

    # Metoda wyświetlająca informacje o obiekcie
    def __str__(self):
        return (
            f"Prompt: {self.prompt}\n"
            f"Response: {self.response}\n"
            f"Cost: {self.cost}\n"
            f"Input tokens: {self.input_tokens}\n"
            f"Output tokens: {self.output_tokens}"
        )

    # Funkcja odbierająca odpowiedź i generująca informacje o zapytaniu
    def get_gpt_response(self, save_to, save_info=False, save_response=False, save_prompt=False):
        self.response = self.__send_prompt()
        self.output_tokens = self.count_tokens(self.response)
        self.cost = self.__cost()
        # Zapisz informacje o zapytaniu/odpowiedzi do pliku, jeśli save_info = True
        self.__save_response_info(save_to) if save_info else None
        # Zapisz odpowiedź do pliku, jeśli save_response = True
        self.__save_response(save_to, save_prompt) if save_response else None

    # Funkcja zliczająca tokeny w tekście
    def count_tokens(self, text):
        # Przypisanie kodowania tokenów dla modelu
        encoding = tiktoken.encoding_for_model(self.model)
        return len(encoding.encode(text))

    # Funkcja zapisująca odpowiedź do pliku (aktualnie nieużywana z uwagi na save_info)
    def __save_response(self, save_to, save_prompt=False):
        with open(f"{save_to}.txt", "a", encoding="utf-8") as file:
            file.write(f"Prompt: {self.prompt}\n")
            file.write(f"Response: {self.response}\n")
            file.write("\n" + "-" * 50 + "\n\n")

    # Funkcja zapisująca odpowiedź i informacje o zapytaniu do pliku
    def __save_response_info(self, save_to):
        with open(f"{save_to}.txt", "a", encoding="utf-8") as file:
            file.write(f"Response: {self.response}\n")
            file.write(f"Cost: {self.cost}\n")
            file.write(f"Input tokens: {self.input_tokens}\n")
            file.write(f"Output tokens: {self.output_tokens}\n")
            file.write("\n" + "-" * 50 + "\n\n")

    # Funkcja do wysłania zapytania do API
    def __send_prompt(self):
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "Jesteś pisarzem streszczeń."},
                    {"role": "user", "content": self.prompt}
                ],
                max_tokens=1000,
                n=1,
                stop=None,
                temperature=0.7
            )

            response = response['choices'][0]['message']['content'].strip()
            return response

        except Exception as e:
            return f"An error occurred: {e}"

    # Funkcja obliczająca łączny koszt zapytania i odpowiedzi
    def __cost(self):
        cost_per_1000_tokens_prompt = 0.0015
        cost_per_1000_tokens_response = 0.002

        prompt_tokens = self.count_tokens(self.prompt)
        response_tokens = self.count_tokens(self.response)

        # Obliczenie kosztu na podstawie ilości tokenów * koszt za 1000 tokenów
        prompt_cost = (prompt_tokens / 1000) * cost_per_1000_tokens_prompt
        response_cost = (response_tokens / 1000) * cost_per_1000_tokens_response
        return prompt_cost + response_cost


# Klasa do obsługi API dla DALL-E
class DALLEPrompt:
    def __init__(self, prompt, api_key=MY_API_KEY, model="dall-e-2.0", size="1024x1024", n=1,
                 save_img_to="./output_data/dalle/img/dalle_img", save_info_to="./output_data/dalle/info/dalle_info",
                 save_img=True, save_info=True, save_url=False, save_prompt=True):
        openai.api_key = api_key  # Ustawienie klucza API dla OpenAI
        self.model = model  # Model AI, w projekcie używamy DALL-E 2.0
        self.prompt = prompt  # Zapytanie do API
        self.size = size  # Rozmiar obrazka
        self.n = n  # Ilość obrazków do wygenerowania
        self.response = None  # Odpowiedź z API (URL obrazka)
        self.URL = None  # URL obrazka
        self.cost = self.__cost()  # Przybliżony koszt zapytania i odpowiedzi
        self.img = None  # Obrazek z odpowiedzi
        self.save_img_to = save_img_to  # Ścieżka do zapisu obrazka
        self.save_info_to = save_info_to  # Ścieżka do zapisu informacji o zapytaniu i odpowiedzi
        self.save_img = save_img  # Czy zapisać obrazek
        self.save_info = save_info  # Czy zapisać informacje
        self.save_url = save_url  # Czy zapisać URL
        self.save_prompt = save_prompt  # Czy zapisać prompt

    # Metoda wyświetlająca informacje o obiekcie
    def __str__(self):
        return (
            f"Prompt: {self.prompt}\n"
            f"Cost: {self.cost}\n"
            f"URL: {self.URL}\n"
        )

    def get_dalle(self):
        self.response = self.__send_prompt()
        self.URL = self.__extract_response_url()
        self.img = self.__download_img()
        if self.save_info:
            self.__save_response_info(self.save_info_to, self.save_prompt)
        # if self.save_url:
        #    self.__save_response_url(self.save_info_to)
        if self.save_img:
            self.__save_img(self.save_img_to)

    # Funkcja do wyświetlania odpowiedzi (obrazka) w Pythonie za pomocą PIL
    def show_response_img(self):
        self.img.show()

    # Funkcja do wysłania zapytania do API
    def __send_prompt(self, save_debug_to='./debug_data/dalle/debug_data') -> dict:
        try:
            response = openai.Image.create(
                prompt=self.prompt,
                n=1,
                size=self.size,
            )

            # Jeśli odpowiedź nie jest słownikiem to zwróć komunikat-przydatne do debugowania
            if not isinstance(response, dict):
                print('Response is not a dictionary')

            # Zapisanie informacji debugowania
            with open(f"{save_debug_to}.txt", "a", encoding="utf-8") as file:
                # Zapis response z funkcji __send_prompt
                file.write(f"Response: {response}\n")
                file.write("\n" + "-" * 50 + "\n\n")

            return response
        except Exception as e:
            return {"error": f"An error occurred: {e}"}

    # Funkcja do wyciągnięcia URL z odpowiedzi
    def __extract_response_url(self):
        # Sprawdzamy, czy odpowiedź jest poprawna
        if isinstance(self.response, dict):
            try:
                # Zwracamy pierwszy URL z listy "data"
                return self.response['data'][0]['url']
            except (KeyError, IndexError):
                return "URL not found in the response"
        else:
            return "Invalid response format"

    # Funkcja pobierająca img z odpowiedzi
    def __download_img(self) -> PIL.Image:
        print(self.URL) # Do debugowania
        response = requests.get(self.URL)
        print(response)  # Do debugowania
        response.raise_for_status()  # Sprawdza, czy odpowiedź HTTP jest błędem
        img = PIL.Image.open(BytesIO(response.content))
        print("Image downloaded successfully.")  # Do debugowania
        return img  # Zwracamy pobrany obraz

    # Funkcja zapisująca img z odpowiedzi do pliku
    def __save_img(self, save_img_to) -> None:
        img = self.img
        if img:
            content_type = img.format  # Pobierz format obrazu
            extension = content_type.lower()  # Konwertuj na małe litery
            save_path = f"{save_img_to}.{extension}"  # Zapisz z odpowiednim rozszerzeniem
            img.save(save_path)

    # Funkcja zapisująca URL odpowiedzi do pliku
    def __save_response_url(self, save_info_to):
        with open(f"{save_info_to}_url.txt", "a", encoding="utf-8") as file:
            file.write(f"Response URL: {self.response}\n")
            file.write("\n" + "-" * 50 + "\n\n")

    # Funkcja zapisująca informacje o zapytaniu i odpowiedzi do pliku
    def __save_response_info(self, save_info_to, save_prompt=True):
        with open(f"{save_info_to}_info.txt", "a", encoding="utf-8") as file:
            if save_prompt:
                file.write(f"Prompt: {self.prompt}\n")
            file.write(f"Response URL: {self.response}\n")
            file.write(f"Cost: {self.cost}\n")
            file.write("\n" + "-" * 50 + "\n\n")

    # Funkcja obliczająca koszt zapytania
    def __cost(self):
        # Koszt zależy od rozmiaru obrazka i użytego modelu
        if self.model == "dall-e-2.0":
            if self.size == "256":
                return 0.016
            elif self.size == "512":
                return 0.018
            elif self.size == "1024":
                return 0.02
            else:
                return 0.01
        elif self.model == "dall-e-3":
            if self.size == "1024":
                return 0.01




#     # Nazwa pliku, który chcesz otworzyć
#     file_name = "o_dwoch_takich_co_ukradli_ksiezyc_002.txt"
#
#     # Otwieranie pliku i odczytywanie jego zawartości
#     try:
#         with open(file_name, 'r', encoding='utf-8') as file:
#             file_content = file.read()  # Odczytanie całej zawartości pliku do zmiennej
#
#         # Policz tokeny w zawartości pliku
#         file_tokens = count_tokens(file_content)
#         print(f"Liczba tokenów w pliku: {file_tokens}")
#
#         # Przygotowanie promptu
#         prompt = (
#             "Utwórz streszczenie tekstu z pliku. Streszczenie nie może zawierać żadnych "
#             "dodatkowych informacji, które nie są zawarte w tekście:\n\n"
#             f"{file_content}"
#         )
#
#         # Policz tokeny w prompt
#         prompt_tokens = count_tokens(prompt)
#         print(f"Liczba tokenów w prompt: {prompt_tokens}")
#
#         # Wysłanie zapytania do modelu
#         reply = send_gpt3_5_prompt(prompt)
#     except FileNotFoundError:
#         print(f"Plik {file_name} nie został znaleziony.")
#     except Exception as e:
#         print(f"Wystąpił błąd: {e}")
