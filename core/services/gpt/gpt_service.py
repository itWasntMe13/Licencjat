import openai

class GptService:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def summarize_text(self, text: str, system_prompt: str = None) -> str:
        prompt = system_prompt or "Stwórz streszczenie poniższego tekstu."

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content