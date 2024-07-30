from RyuzakiLib.api.reqs import AsyicXSearcher

class SearchAPI:
    def __init__(self, api_key="29db8322f22d425d7023c499610fc2419f8ff44e0bd3f63edd90d2994bf76b49"):
        self.url = "https://randydev-ryuzaki-api.hf.space/ryuzaki"
        self.api_key = api_key
        self.headers = {"accept": "application/json", "api-key": self.api_key}

    async def custom(self, api_name, post=False, payload=None):
        response = await AsyicXSearcher.search(
            self.url + f"/{api_name}",
            post=post,
            headers=self.headers,
            re_json=True,
            json=payload
        )
        return response
