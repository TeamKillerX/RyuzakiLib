### RyuzakiLib API

![IMG_20231209_213430_940](https://github.com/TeamKillerX/RyuzakiLib-API/assets/90479255/f26513f7-cdf4-44ee-9a08-f6b27e6b99f7)

## Authentication
> **Warning** Do not expose the `__Secure-1PSID`
```python
from RyuzakiLib.api.reqs import AsyicXSearcher

url ="https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"

payload = {
    "query": "hello world",
    "bard_api_key": "cookie token here",
    "is_login": True
}

headers = {
    "accept": "application/json",
}

response = await AsyicXSearcher.search(url, post=True, re_json=True, headers=headers, json=payload)
print(response)
```

* `bard_api_key` : (optional)
* `is_login` : default `False` (optional)

1. Visit https://bard.google.com/
2. F12 for console
3. Session: Application → Cookies → Copy the value of  `__Secure-1PSID` cookie.

Note that while I referred to `__Secure-1PSID` value as an API key for convenience, it is not an officially provided API key. Cookie value subject to frequent changes. Verify the value again if an error occurs. Most errors occur when an invalid cookie value is entered.

`bard_api_key={__Secure-1PSID}`


### Faster Downloader
```python
from RyuzakiLib.api.fullstack import FullStackDev

# - Supported jpg, mp4, mp3

link_url = "https://example.jpg"

await FullStackDev.fast(url=link_url, filename="photo.jpg", type_mode="wb")
```
- Now you've saved it, see for example photo.jpg

* <b>parameter</b>
- <code>filename="example.mp4"</code>
- <code>type_mode="wb"</code>

* <b>Do something like example</b>
```python
import RyuzakiLib.api.fullstack as example
print(dir(example))
```
