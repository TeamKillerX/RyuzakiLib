import google.generativeai as genai
from datetime import datetime as dt

gemini_chat = []

owner_base = f"""
Your name is Randy Dev. A kind and friendly AI assistant that answers in
a short and concise answer. Give short step-by-step reasoning if required.

Today is {dt.now():%A %d %B %Y %H:%M}
"""

class GeminiLatest:
    def __init__(self, api_key: str=None):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)

    def _get_response_gemini(self, query: str=None):
        global gemini_chat
        try:
            gemini_chat.append({"role": "user", "parts": [owner_base]})
            model = genai.GenerativeModel("gemini-pro")
            response_genai = model.generate_content(gemini_chat)
            gemini_chat.append({"role": "model", "parts": [response_genai.text]})
            gemini_chat.append({"role": "user", "parts": [query]})
            return [response_genai.text, gemini_chat]
        except Exception as e:
            return f"Error response: {e}"
