### Anime-Styled

* Get hugging token : [APIKEY HERE](https://huggingface.co/settings/tokens)

```python
# < class RyuzakiLib.types.anime.AnimeStyled >

from RyuzakiLib.types import AnimeStyled

code = AnimeStyled(apikey, input)
img = code.NowSendImage()
# logic code here
```
### Waifu random
```python
# import here
# < class RyuzakiLib.types.waifu.SendWaifuRandom >

code = SendWaifuRandom()
image_url = code.send_waifu_pics()
# logic code here
```
