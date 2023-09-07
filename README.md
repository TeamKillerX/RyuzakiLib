# RyuzakiLib

# Disclaimer
```
        ⚠️ WARNING FOR YOU ️ ️⚠️
RyuzakiLib is used to help your account activities on Telegram
We are not responsible for what you misuse in this repository
!  Be careful when using this repository!
If one of the members misuses this repository, we are forced to ban you
Never ever abuse this repository 
```

# Installing 
`pip3 install -U RyuzakiLib`

### Example Chatgpt
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hacktools import RendyDevChat, GoogleReverseImage

query = "Hello World"
chat = RendyDevChat(query)
response = chat.get_response()
await message.reply(response)
```

### Example Google Reverse Image
```python
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hacktools import RendyDevChat, GoogleReverseImage

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

from RyuzakiLib.hacktools import set_prefixes
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]

user_id = message.from_user.id
prefix = "."
set_handler = set_prefixes(user_id, prefix, collection)
prefixes_new = set_handler.add_prefixes()
```

# License 
[![License](https://www.gnu.org/graphics/agplv3-155x51.png)](LICENSE)   
TeamKillerX is licensed under [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) v3 or later.

<h4 align="center">Copyright (C) 2019 - 2023 <a href="https://github.com/TeamKillerX">TeamKillerX</a></h4>

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

# Credits 
* [![TeamKillerX-Devs](https://img.shields.io/static/v1?label=TeamkillerX&message=devs&color=critical)](https://t.me/xtdevs)
* Pyrogram by : [Dan](https://github.com/pyrogram/pyrogram)
* Api tools by : unknown 
