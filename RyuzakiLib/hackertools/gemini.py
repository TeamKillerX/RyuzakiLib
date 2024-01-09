import requests
from datetime import datetime as dt

gemini_chat = []

owner_base = f"""
Your name is Randy Dev. A kind and friendly AI assistant that answers in
a short and concise answer. Give short step-by-step reasoning if required.

Today is {dt.now():%A %d %B %Y %H:%M}
"""

class GeminiLatest:
    def __init__(self, api_key: str = None, api_base="https://generativelanguage.googleapis.com"):
        self.api_key = api_key
        self.api_base = api_base

    def _get_response_gemini(self, query: str = None):
        global gemini_chat
        try:
            api_method = f"{self.api_base}/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
            gemini_chat.append({"role": "user", "parts": [{"text": owner_base}]})
            headers = {"Content-Type": "application/json"}
            payload = {"contents": gemini_chat}
            response = requests.post(api_method, headers=headers, json=payload)
            if response.status_code != 200:
                return "Error responding"
            response_data = response.json()
            answer = response_data["candidates"][0]["content"]["parts"][0]["text"]
            gemini_chat.append({"role": "model", "parts": [{"text": answer}]})
            gemini_chat.append({"role": "user", "parts": [{"text": query}]})
            return [answer, gemini_chat]
        except Exception as e:
            error_msg = f"Error response: {e}"
            return [error_msg, "https://telegra.ph/file/e5eb5d8e5a1aba26c0014.jpg"]
