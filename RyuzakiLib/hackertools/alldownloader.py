import requests


class DictToObj:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObj(value))
            else:
                setattr(self, key, value)

    def __repr__(self):
        return f"{self.__dict__}"

class AkenoPlus:
    def __init__(self, key: str):
        self.api_endpoint = "https://akeno.randydev.my.id"
        self.headers = {"x-akeno-key": key}

    async def terabox(self, link=None):
        url = f"https://akeno.randydev.my.id/akeno/terabox-v1?link={link}"
        response = requests.get(
            f"{self.api_endpoint}/akeno/terabox-v1?link={link}",
            headers=self.headers
        )
        return response.json()

    async def terabox_v2(self, link=None):
        response = requests.get(
            f"{self.api_endpoint}/akeno/terabox-v2?link={link}",
            headers=self.headers
        )
        return response.json()

    async def chatgpt_old(self, query=None):
        payload={"query": query}
        response = requests.post(
            f"{self.api_endpoint}/ryuzaki/chatgpt-old",
            json=payload
        )
        return response.json()

    async def hentai(self):
        response = requests.get(
            f"{self.api_endpoint}/akeno/hentai",
            headers=self.headers
        )
        return response.json()

    async def get_json(self, response=None):
        return DictToObj(response)
