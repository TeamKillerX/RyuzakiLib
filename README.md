# RyuzakiLib

![pro](https://github.com/TeamKillerX/RyuzakiLib/assets/90479255/dfa2f321-9b36-4045-a321-bcfdd4366514)

[![pykillerx - Version](https://img.shields.io/pypi/v/RyuzakiLib?style=round)](https://pypi.org/project/RyuzakiLib)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/RyuzakiLib?label=DOWNLOADS&style=round)](https://pypi.org/project/RyuzakiLib)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/TeamKillerX/RyuzakiLib/graphs/commit-activity)
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/TeamKillerX/RyuzakiLib)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://makeapullrequest.com)
![Codeql](https://github.com/TeamKillerX/RyuzakiLib/actions/workflows/codeql.yml/badge.svg)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/TeamKillerX/RyuzakiLib/dev.svg)](https://results.pre-commit.ci/latest/github/TeamKillerX/RyuzakiLib/dev)

# Disclaimer
> [!WARNING]
> RyuzakiLib is used to help your account activities on Telegram<br>We are not responsible for what you misuse in this repository!<br>Be careful when using this repository!<br>If one of the members misuses this repository, we are forced to ban you<br>Never ever abuse this repository

# Installing
* `pip3 install -U RyuzakiLib`
* windows or linux
```
pip3 install git+https://github.com/TeamKillerX/RyuzakiLib
```

### Import Here
```python
from RyuzakiLib.hackertools.chatgpt import RendyDevChat
from RyuzakiLib.hackertools.github import GithubUsername
from RyuzakiLib.hackertools.rmbg import RemoveBg
from RyuzakiLib.hackertools.reverse import GoogleReverseImage
from RyuzakiLib.hackertools.ipinfo import WhoisIpHacker
from RyuzakiLib.hackertools.ocrapi import OcrApiUrl
from RyuzakiLib.hackertools.prefixes import CustomPrefixes
```

### Learn Python
```python
import asyncio

class example_python:
      def __init__(self):
         pass

      def hello_world(self):
          asyncio.sleep(5)

# examples usage
ok = example_python()
test = ok.hello_world()
```

### Tutorial FastAPI
```python
from fastapi import FastAPI
from RyuzakiLib.hackertools.chatgpt import RendyDevChat
from RyuzakiLib.hackertools.openai import OpenAiToken

app = FastAPI()

@app.get("/read")
def hello():
    return {"message": "Hello World"}

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0")
```
- Like example this [`RyuzakiLib API`](https://private.randydev.my.id)
* [x] Requirements: `fastapi` and `RyuzakiLib`

### Spamwatch
• Example usage
```python
from RyuzakiLib.spamwatch.clients import SibylBan

clients = SibylBan(api_key="your_api_key_here")

message = clients.add_ban(user_id=client.me.id, reason="scammer", is_banned=True)
await message.reply_text(message)

# Part 2
showing = clients.get_ban(user_id=client.me.id, banlist=True)
print(showing)

# Part 3
results = clients.get_all_banlist()
print(results)
```

### Profile Clone
• Example usage
```python
from RyuzakiLib.profile.user import ProfileClone

clients = ProfileClone(api_key="your_api_key_here")

message = clients.add_profile_clone() # need parameter

showing = clients.get_profile_clone() # need parameter
print(showing)
```

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

### Chatgpt New?
* Chatgpt's new features are available here
- parameter

```python
from RyuzakiLib.hackertools.chatgpt import RendyDevChat

query = "Hello World"

code = RendyDevChat(query)
message_output = code.get_response(message, latest_version=True)
message_output_2 = code.get_response_beta(joke=True)
message_output_3 = code.get_response_bing(bing=True)
message_output_4 = code.get_response_model() # parameter model_id: integers and is_models: boolean
message_output_5 = code.get_response_llama(llama=True)
message_output_6 = code.get_response_gemini_pro(api_key=api_key, re_json=True, is_gemini_pro=True)
message_output_7 = code.get_response_google_ai(api_key=api_key, re_json=True, is_chat_bison=True, is_google=True)
message_output_8 = code.multi_chat_response(api_key=api_key, is_multi_chat=True)

print(message_output)
print(message_output_2)
print(message_output_3)
print(message_output_4)
print(message_output_5)
print(message_output_6)
print(message_output_7)
print(message_output_8)
```

### AI image Generator New?
* AI image Generator new features are available here
- parameter
```python
import base64
from io import BytesIO
from PIL import Image
from RyuzakiLib.hackertools.chatgpt import RendyDevChat

query = "Hello World"
code = RendyDevChat(query)
response = code.get_risma_image_generator(api_key=api_key, is_opendalle=True)

image_data = base64.b64decode(response["randydev"].get("data"))
image = Image.open(BytesIO(image_data))
```

### Continue Conversation
```python
from RyuzakiLib import OpenAiToken

api_base = "https://api.example.com/v1"
api_key = ""
query = "hello world"
response = OpenAiToken(api_key=api_key, api_base=api_base).chat_message_turbo(
    query=query,
    model="gpt-4",
    is_stream=False
)

print(response[0])
```

### Example Chatgpt
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools.chatgpt import RendyDevChat

query = "Hello World"
response = RendyDevChat(query).get_response(message, latest_version=True)
await message.reply(response)
```

### Example Google Reverse Image
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools.reverse import GoogleReverseImage

url = "https://example/jpg"
apikey = "api key token"
response = GoogleReverseImage(url, apikey)
results = response.get_reverse()
print(results)
```
### New Features
```python
# Create by @xtdevs
# Prefixes Custom

from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools.prefixes import CustomPrefixes
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

db_name = "custom_prefixes"
user_id = message.from_user.id
prefix = [".", "+", "-"]
set_handler = CustomPrefixes(db_name, user_id, prefix, collection, True) # parameter upsert using set True or False
set_handler.add_prefixes()
now_show_prefix = set_handler.get_prefix()
print(now_show_prefix)
```
* you can ask support [@KillerXSupport](https://t.me/KillerXSupport)

### Test your bots
```bash
- git clone https://github.com/TeamKillerX/RyuzakiLib
- cd RyuzakiLib
- pip3 install -r ryuzaki.txt
- nano buildbot/secrets/env.py
- ctrl s + x to save
- bash start.sh
```

### RyuzakiLib API

![IMG_20231209_213430_940](https://github.com/TeamKillerX/RyuzakiLib-API/assets/90479255/f26513f7-cdf4-44ee-9a08-f6b27e6b99f7)

## Authentication
> **Warning** Do not expose the `__Secure-1PSID`
```python
import requests

url ="https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"

payload = {
    "query": "hello world",
    "bard_api_key": "cookie token here",
    "is_login": True
}

headers = {
    "accept": "application/json",
    "api-key": "get api key from @randydev_bot"
}
response = requests.post(url, headers=headers, json=payload).json()
print(response)
```

* `bard_api_key` : (optional)
* `is_login` : default `False` (optional)

1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.

Note that while I referred to `__Secure-1PSID` value as an API key for convenience, it is not an officially provided API key. Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.

`bard_api_key={__Secure-1PSID}`


### Tutorial Requests in Python
>Request body schema
* `json=payload`
```python
response = requests.post(url, headers=headers, json=payload).json()
```

> Query Parameters
* `params=params`
```python
response = requests.post(url, headers=headers, params=params).json()
```

You can find the [`Ryuzaki API`](https://private.randydev.my.id)

### Ryuzaki API Request (API Keys)

- Full Name : (...)
- Email address : (...)
- Telegram Username : (....)
- Project Domain [Optional] : (....)

- Why you want to use this API and or why we should give you access?

(......)

* Choose your one

1. [ ] ChatGPT-4 Free Access
2. [ ] I wont use this API for anything illegal
3. [ ] 5 USD/Month - Etc

~ Starting january 1, 2024, remove the `/token_api_key` command in [ryuzaki bots](https://t.me/randydev_bot)

### Ryuzaki API Pricing (API keys)
> [!NOTE]
> - Picsart Pro (7 days)
> - Gemini Ultra (7 days)
> - Beta3 Google AI (7 days)
> - Beta2 Google AI (7 days)
> - Anime Styled (7 days)

* Only Developed by
- [@xtdevs](https://t.me/xtdevs)
- [@TrueSaiyan](https://t.me/TrueSaiyan)
- [@moiusrname](https://t.me/moiusrname)
- [@Hackintush](https://t.me/Hackintush)

* Contact Support: [@xtdevs](https://t.me/xtdevs)

### Troubleshoot
Sometimes errors occur, but we are here to help! This guide covers some of the most common issues we’ve seen and how you can resolve them. However, this guide isn’t meant to be a comprehensive collection of every 🤗 FastAPI issue. For more help with troubleshooting your issue, try:
* [Contact Support](https://t.me/xtdevs)

# License
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)
TeamKillerX is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

<h4 align="center">Copyright (C) 2019 - 2024 The RyuzakiLib <a href="https://github.com/TeamKillerX">TeamKillerX</a>
<a href="https://t.me/xtdevs">@xtdevs</a>
</h4>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Project [RyuzakiLib](https://github.com/TeamKillerX/) is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

### Contributing
* [Fork the project](https://github.com/TeamKillerX/RyuzakiLib) and send pull requests

<a href="https://github.com/TeamKillerX/RyuzakiLib/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=TeamKillerX/RyuzakiLib" />
</a>

### Credits
* [![TeamKillerX-Devs](https://img.shields.io/static/v1?label=TeamkillerX&message=devs&color=critical)](https://t.me/xtdevs)
* Pyrogram by : [Dan](https://github.com/pyrogram/pyrogram)
* PY-Tgcalls by : [Pytgcalls](https://github.com/pytgcalls/pytgcalls)
