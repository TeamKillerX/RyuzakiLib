import requests
from datetime import datetime as dt

gemini_chat = []

owner_base = f"""
Your name is Randy Dev. A kind and friendly AI assistant that answers in
a short and concise answer. Give short step-by-step reasoning if required.

Today is {dt.now():%A %d %B %Y %H:%M}
"""

class GeminiLatest:
    def __init__(self, api_key: str=None, api_base="https://generativelanguage.googleapis.com"):
        self.api_key = api_key
        self.api_base = api_base

    def _get_response_gemini(self, query: str=None):
        global gemini_chat
        try:
            api_method = f"{self.api_base}/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
            gemini_chat.append({"role": "user", "parts": [{"text": owner_base}]})
            headers = {"Content-Type": "application/json"}
            payload = {"contents": gemini_chat}
            response = requests.post(url, headers data=payload)
            if response.status_code != 200:
                return "Error responding"
            response_data = response.json()
            answer = response_data["candidates"]
            for results in answer:
                message = results.get("text") or results
            gemini_chat.append({"role": "model", "parts": [{"text": message}]})
            gemini_chat.append({"role": "user", "parts": [{"text": query}]})
            return [message, gemini_chat]
        except Exception as e:
            return f"Error response: {e}"
