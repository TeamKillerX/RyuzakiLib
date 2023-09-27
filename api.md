### Faster Downloader
```python
from RyuzakiLib.api.fullstack import FullStackDev

# - Supported jpg, mp4, mp3

link_url = "https://example.jpg"

FullStackDev(domain_url=link_url, filename="photo.jpg", type_mode="wb").faster_downloader()
```
- Now you've saved it, see for example photo.jpg

* <b>parameter</b>
- <code>filename="example.mp4"</code>
- <code>type_mode="wb"</code>

• <b>You can't do this</b>
```python
- FullStackDev().ryuzaki_get()
- FullStackDev().ryuzaki_post()
- FullStackDev().fastapi_get()
- FullStackDev().faster_downloader()
```

* <b>Do something like example</b>
```python
import RyuzakiLib.api.fullstack as example
print(dir(example))
```
