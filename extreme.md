### Carbon
```python
# < class RyuzakiLib.extreme.carbon.CarbonSuper >
write = "Hello World"
send_image = CarbonSuper(write)
```

### Carbon RaySo
```python
# < class RyuzakiLib.extreme.rayso.CarbonRaySo >
write = "Hello World"
code = CarbonRaySo(code=write) # parameter
img = code.make_carbon_rayso()
```
* <b>Parameter</b>
- `code : "string"`
- `title: "string"` <b>[Optional]</b>
- `theme: "string"`
- `setlang: "language code"` <b>[Optional]</b>
- `auto_translate: boolean` <b>[Optional]</b>
- `check_sticker: boolean` <b>[Optional]</b>
- `ryuzaki: boolean` <b>[Optional]</b>

### Telegram User Info
```python
# < class RyuzakiLib.extreme.userinfo.TelegramUserInfo >

user_id = 123456
hacking = await TelegramUserInfo(user_id).who_is(client)
if hacking[0]: # using photo
   # code here
```

### Website Screenshot Url
```python
# < class RyuzakiLib.extreme.webshot.WebShotUrl >

url = "https://google.com"
code = WebShotUrl(url)
img = code.send_screenshot()
```
* <b>Parameter</b>
- `url: "string"` <b>[Required]</b>
- `width: integers` <b>[Optional]</b>
- `height: integers` <b>[Optional]</b>
- `scale: integers` <b>[Optional]</b>
- `delay: integers` <b>[Optional]</b>
- `screenshot_full: boolean` <b>[Optional]</b>
