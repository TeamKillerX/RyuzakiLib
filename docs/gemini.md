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
