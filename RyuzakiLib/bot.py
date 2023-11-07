import requests

class API:
    def __init__(
        self,
        bot_token: str=None
    ):
        self.bot_token = bot_token

    def get_me(self, re_json: bool=False):
        url = f"https://api.telegram.org/bot{self.bot_token}/getMe"
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)"
        }
        if re_json:
            response = requests.post(url, headers=headers).json()
            return response
        else:
            response = requests.post(url, headers=headers)
            return response

    def send_message(
        self,
        chat_id: str=None,
        text: str=None,
        disable_web_page_preview: bool=False,
        disable_notification: bool=False,
        reply_to_message_id: int=None,
        parse_mode=None,
        re_json: bool=False
    ):
        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": disable_web_page_preview,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id,
            "chat_id": chat_id
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json"
        }
        if re_json:
            response = requests.post(url, json=payload, headers=headers).json()
            return response
        else:
            response = requests.post(url, json=payload, headers=headers)
            return response
