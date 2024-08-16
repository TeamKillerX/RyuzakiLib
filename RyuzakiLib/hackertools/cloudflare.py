from datetime import datetime as dt

import requests

from RyuzakiLib.api.reqs import AsyicXSearcher

owner_base = f"""
Your name is Randy Dev. A kind and friendly AI assistant that answers in
a short and concise answer. Give short step-by-step reasoning if required.

- Powered by @xtdevs on telegram
Today is {dt.now():%A %d %B %Y %H:%M}
"""

class CloudFlare:
    @staticmethod
    async def run(prompt, account_id, api_token):
        payload = {
            "messages": [
                {"role": "system", "content": owner_base},
                {"role": "user", "content": prompt}
            ],
        }
        if account_id and api_token:
            API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/meta/llama-3-8b-instruct"
            headers = {"Authorization": f"Bearer {api_token}"}
            response = requests.post(f"{API_BASE_URL}", headers=headers, json=payload)
            if response.status_code != 200:
                return None
            return response.json()["result"].get("response")
        else:
            return "Required account_id and api_token"
