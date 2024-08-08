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
### BetaRag New (AI)
```python
from RyuzakiLib import BetaRag

x = BetaRag(token="api key", user_id=0, mongo_url="your mongo")

response = await x.rag_chat("how to javascript code?")
print(response)
```
