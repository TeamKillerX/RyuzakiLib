### Requests
```python
from RyuzakiLib.api.req import RequestsUrl

url = "your api here"
params = {}
code = RequestsUrl(url, params=params, 200)
response = code.geturl() # parameter posturl()
if isinstance(response, str):
    print(response)
else:
    print(response["json"])
```
