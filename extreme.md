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
code = CarbonRaySo()
img = code.make_carbon_rayso()
```
* <b>Parameter</b>
- `code : "string"`
- `title: "string"` <b>[Optional]</b>
- `theme: "string"`
- `setlang: "language code"` <b>[Optional]</b>
- `auto_translate: boolean` <b>[Optional]</b>
- `ryuzaki: boolean` <b>[Optional]</b>

### Telegram User Info
```python
# < class RyuzakiLib.extreme.userinfo.TelegramUserInfo >

user_id = 123456
hacking = await TelegramUserInfo(user_id).who_is(client)
if hacking[0]: # using photo
   # code here
