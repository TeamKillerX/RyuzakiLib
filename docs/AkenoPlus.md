### AkenoPlus Fast
```python
from RyuzakiLib import AkenoPlus

key = "your_api_key_from_email"

_ = AkenoPlus(key=ok)

response = await _.hentai()

do = await _.get_json(response)

data = do.randydev.results[0].video_1

vid = _.download_now(data, remove=True)
await message.reply_video(vid, has_spoiler=True)
```
### Attribute
