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
