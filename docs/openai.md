### Continue Conversation
```python
from RyuzakiLib import OpenAI

api_base = "https://api.example.com/v1"
api_key = ""
query = "hello world"
response = await OpenAI(api_key=api_key, api_base=api_base).chat_message_turbo(
    query=query,
    model="gpt-4",
    is_stream=False
)

print(response[0])
```
