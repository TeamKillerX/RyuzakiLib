### API endpoint
- don't ask [`@xtdevs`](https://t.me/xtdevs) on telegram

### Short url Generator for tracking IP
```python
import requests

headers = {
  "x-akeno-key": "your api key"
}
payload = {
  "original_url": "your link like facebook.com",
  "user_email": "your email"
}
url = "https://akeno.randydev.my.id/api/shorten_url"
response = requests.post(url, json=payload, headers=headers).json()
print(response)
```
