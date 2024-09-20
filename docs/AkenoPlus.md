### AkenoPlus Fast
```python
from RyuzakiLib import AkenoPlus

key = "your_api_key_from_email"

_ = AkenoPlus(key=key)

response = await _.hentai()

do = await _.get_json(response)

data = do.randydev.results[0].video_1

vid = _.download_now(data, remove=True)
await message.reply_video(vid, has_spoiler=True)
```
### Attribute
```python
_.terabox(link)
_.terabox_v2(link)
_.chatgpt_old(query)
_.blackbox(query)
_.hentai()
_.fbdown(link)
_.fdownloader(link)
_.capcut(link)
```
