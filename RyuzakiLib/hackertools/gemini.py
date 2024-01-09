import google.generativeai as genai

gemini_chat = []

class GeminiLatest:
    def __init__(self, api_key: str=None):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)

    def _get_response_gemini(query: str=None):
        global gemini_chat
        try:
            gemini_chat.append({"role": "user", "parts": [query]})
            model = genai.GenerativeModel("gemini-pro")
            response_genai = model.generate_content(gemini_chat)
            gemini_chat.append({"role": "model", "parts": [response_genai.text]})
            return [response_genai.text, gemini_chat]
        except Exception as e:
            return f"Error response: {e}"
