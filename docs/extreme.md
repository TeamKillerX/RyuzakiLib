---
icon: sunglasses
---

# extreme

#### Carbon

```python
# < class RyuzakiLib.extreme.carbon.Carbon >
write = "Hello World"
send_image = await Carbon.make_carbon(write)
```

#### Carbon RaySo

```python
# < class RyuzakiLib.extreme.rayso.CarbonRaySo >
write = "Hello World"
code = CarbonRaySo(code=write) # parameter
img = code.make_carbon_rayso()
```

* Parameter
* `code : "string"`
* `title: "string"` \[Optional]
* `theme: "string"`
* `setlang: "language code"` \[Optional]
* `auto_translate: boolean` \[Optional]
* `check_sticker: boolean` \[Optional]
* `ryuzaki: boolean` \[Optional]

#### Telegram User Info

```python
# < class RyuzakiLib.extreme.userinfo.TelegramUserInfo >

user_id = 123456
hacking = await TelegramUserInfo(user_id).who_is(client)
if hacking[0]: # using photo
   # code here
```

#### Website Screenshot Url

```python
# < class RyuzakiLib.extreme.webshot.WebShotUrl >

url = "https://google.com"
code = WebShotUrl(url)
img = code.send_screenshot()
```

* Parameter
* `url: "string"` \[Required]
* `width: integers` \[Optional]
* `height: integers` \[Optional]
* `scale: integers` \[Optional]
* `delay: integers` \[Optional]
* `screenshot_full: boolean` \[Optional]
