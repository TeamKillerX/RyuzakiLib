### Tiktok Downloader
```python
from RyuzakiLib.dl.tiktok import Tiktok

url = "https://www.tiktok.com/@memenyengir/video/7229996795965852955"

api_name = "example.com"
response = await Tiktok.download(api_name, url)
print(response[0])
```
