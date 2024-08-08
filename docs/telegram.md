### Learn Telegram Bot API
```python

from RyuzakiLib.bot import API

api = API(bot_token="your_token")

# supported here
api.send_message()
api.send_photo()
api.send_sticker()
api.send_audio()
api.send_document()
api.forward_message()

# you can pass
sent_message = api.send_message(chat_id=chat_id, text=text)

sent_sticker = api.send_sticker(chat_id=chat_id, sticker=sticker)

# your own developer
urls = api.telegram("SendMessage")
payload = {}
headers = {}
response = requests.post(urls, json=payload, headers=headers)
print(response.text)
```
