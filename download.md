### Tiktok Downloader
```python
from RyuzakiLib.dl.tiktok import TiktokUrl

url = "https://www.tiktok.com/@memenyengir/video/7229996795965852955"

code = TiktokUrl(url, True)
video = code.tiktok_downloader()
print(video)
```

### Facebook Downloader
```python
< # class RyuzakiLib.dl.facebook.FacebookUrl >

code = FacebookUrl(apikey, url)
test = code.tiktok.downloader()
```

### Instagram Downloader
```python
< # class RyuzakiLib.dl.instagram.InstagramUrl >

code = InstagramUrl(apikey, url)
test = code.instagram.downloader()
```
