import requests

from config import BOT_ID, TOKEN


def bot_token_acces(bot_id, token):
    url = f"https://api.telegram.org/bot{bot_id}{token}/sendMessage"
    return url


def send_message(user_id, text):
    urls = bot_token_acces(BOT_ID, TOKEN)
    payload = {
        "chat_id": user_id,
        "text": text,
        "disable_web_page_preview": True,
        "disable_notification": False,
        "reply_to_message_id": None,
    }
    headers = {
        "accept": "application/json",
        "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        "content-type": "application/json",
    }
    response = requests.post(urls, json=payload, headers=headers)
    return response.text
