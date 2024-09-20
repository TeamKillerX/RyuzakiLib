import requests
import aiohttp

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
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/terabox-v1?link={link}", headers=self.headers) as response:
                return await response.json()

    async def terabox_v2(self, link=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/terabox-v2?link={link}", headers=self.headers) as response:
                return await response.json()

    async def chatgpt_old(self, query=None):
        payload={"query": query}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/ryuzaki/chatgpt-old", json=payload, headers=self.headers) as response:
                return await response.json()

    async def hentai(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/hentai", headers=self.headers) as response:
                return await response.json()

    async def get_json(self, response=None):
        return DictToObj(response)
