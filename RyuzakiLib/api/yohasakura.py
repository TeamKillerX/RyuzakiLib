from RyuzakiLib.api.reqs import AsyicXSearcher


class SearchAPI:
    def __init__(self, api_key="6398769dabd9fe0e49bedce0354b40a9b1a69d9594dc9d48c1d8a2a071c51e89"):
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
