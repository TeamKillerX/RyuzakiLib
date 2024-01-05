import requests


class CloneBot:
    def __init__(self, api_key: str = None, bot_token: str = None):
        self.api_key = api_key
        self.bot_token = bot_token

    def _clone_chatgpt(self, clone=False, re_json=False):
        url = f"https://randydev.my.id/clone/chatgpt-bot?bot_token={self.bot_token}"
        headers = {"accept": "application/json", "api-key": self.api_key}
        if clone:
            if re_json:
                try:
                    response = requests.post(url, headers=headers).json()
                    return response
                except Exception as e:
                    return f"Error request: {e}"
            else:
                try:
                    response = requests.post(url, headers=headers)
                    return response.text
                except Exception as e:
                    return f"Error request: {e}"
        else:
            return "Error required clone=True"
