import requests

class GeminiLatest:
    def __init__(self, api_key: str = None, api_base="https://generativelanguage.googleapis.com"):
        self.api_key = api_key
        self.api_base = api_base

    def _get_response_gemini(self, query: str = None, gemini_chat: list = None, append_text: str = None):
        if gemini_chat is None:
            gemini_chat = []
        try:
            api_method = f"{self.api_base}/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
            headers = {"Content-Type": "application/json"}
            payload = {"contents": gemini_chat}
            response = requests.post(api_method, headers=headers, json=payload)
            if response.status_code != 200:
                return "Error responding"
            response_data = response.json()
            for candidate in response_data["candidates"]:
                for x in candidate["content"]["parts"]:
                    answer = x["text"]
            if append_text is not None:
                gemini_chat.append({"role": "model", "parts": [{"text": append_text}]})
            return answer, gemini_chat
        except Exception as e:
            error_msg = f"Error response: {e}"
            return error_msg, "https://telegra.ph/file/e5eb5d8e5a1aba26c0014.jpg"
