from RyuzakiLib.api.reqs import AsyicXSearcher

class FluxAi:
    @staticmethod
    async def schellwithflux(args, auto_enhanger=False, re_content=False):
        API_URL = "https://randydev-ryuzaki-api.hf.space/api/v1/akeno/fluxai"
        payload = {
            "user_id": 1191668125,  # Please don't edit here
            "args": args,
            "auto_enhanger": auto_enhanger
        }
        response = requests.post(API_URL, json=payload)
        if response.status_code != 200:
            return None
        if re_content:
            return response.content
        else:
            return response.json()
