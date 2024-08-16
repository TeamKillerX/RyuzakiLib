from RyuzakiLib.api.reqs import AsyicXSearcher
import requests
from datetime import datetime as dt

class CloudFlare:
    @staticmethod
    async def run(prompt, account_id, api_token):
        payload = {"messages": prompt}
        if account_id and api_token:
            API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/@cf/meta/llama-3-8b-instruct"
            headers = {"Authorization": f"Bearer {API_TOKEN}"}
            response = requests.post(f"{API_BASE_URL}", headers=headers, json=payload)
            if response.status_code != 200:
                return None
            return response.json()
        else:
            return "Required account_id and api_token"
