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
