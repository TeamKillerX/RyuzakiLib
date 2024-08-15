import requests

from RyuzakiLib.api.reqs import AsyicXSearcher


class FluxAi:
    @staticmethod
    async def schellwithflux(args, auto_enhancer=False, re_content=False):
        API_URL = "https://randydev-ryuzaki-api.hf.space/api/v1/akeno/fluxai"
        payload = {
            "user_id": 1191668125,  # Please don't edit here
            "args": args,
            "auto_enhancer": auto_enhancer
        }
        response = requests.post(API_URL, json=payload)
        return response.content if re_content else response.json()
