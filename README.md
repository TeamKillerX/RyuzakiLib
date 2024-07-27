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

# or

from RyuzakiLib import *
```

### Learn Python
```python
import asyncio

class example_python:
      @staticmethod
      def hello_world():
          asyncio.sleep(5)

# examples usage
example_python.hello_world()
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
from RyuzakiLib import SibylBan

x = SiblyBan.ban(user_id)
xb = SiblyBan.banlist(user_id)
xub = SiblyBan.unban(user_id)
results = SiblyBan.banlist_all()
```

### Profile Clone
• Example usage
```python
from RyuzakiLib import Clone

message = Clone.clone() # need parameter

showing = Clone.sclone() # need parameter
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
from RyuzakiLib import RendyDevChat

results = await RendyDevChat.chat_hacked(latest_model="list-model", list_model_all=True)
print(results)

response = await RendyDevChat.chat_hacked("hello world")
print(response)
```

### AI image Generator New?
* AI image Generator new features are available here
- parameter
```python
from RyuzakiLib import RendyDevChat

query = "Cat in a Hat"
response = await RendyDevChat.image_generator(query)
print(response)
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

### Example Google Reverse Image
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib import GoogleReverseImage

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

### Gemini AI New (Free)
- No authorization needed
- Gemini Pro and Gemini Flash (Without RyuzakiLib API keys)
- Multi-Turn Conversation

```python
from RyuzakiLib import GeminiLatest

mongo_url = "....."
api_key = "....."
user_id = 0
geni = GeminiLatest(api_keys=api_key, mongo_url=mongo_url, user_id=user_id)

# Get response (private in python)
answer, gemini_chat = geni._GeminiLatest__get_response_gemini(query)
print(answer)

# Get response image to text
from RyuzakiLib import GeminiLatest

caption = message.reply_to_message.caption
file_path = await message.reply_to_message.download()

x = GeminiLatest(api_keys="api key here")
response = x.get_response_image(caption, file_path)
print(response)
```

- Gemini AI New:  Get [API key Here](https://makersuite.google.com/app/apikey) from Google Dev

### Blackbox New AI
```python
from RyuzakiLib import Blackbox
import os

varname = "DATABASE_URL"

value = os.environ.get(varname.upper(), None)

mongo_uri = value
db_name = "tiktokbot"

blackbox = Blackbox(mongo_uri, db_name)

user_id = "user666"
query = "What is todays date?"

results = await blackbox.chat(query, user_id=user_id)
print(results)
```

### BetaRag New (AI)
```python
from RyuzakiLib import BetaRag

x = BetaRag(token="api key", user_id=0, mongo_url="your mongo")

response = await x.rag_chat("how to javascript code?")
print(response)
```

- You can ask support [@KillerXSupport](https://t.me/KillerXSupport)

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
from RyuzakiLib.api.reqs import AsyicXSearcher

url ="https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"

payload = {
    "query": "hello world",
    "bard_api_key": "cookie token here",
    "is_login": True
}

headers = {
    "accept": "application/json",
}

response = await AsyicXSearcher.search(url, post=True, re_json=True, headers=headers, json=payload)
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
