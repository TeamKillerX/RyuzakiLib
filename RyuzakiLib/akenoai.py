import requests

from RyuzakiLib.api.reqs import async_search

class AkenoAI:
    def __init__(self, base_api_dev: str = "https://akeno.randydev.my.id"):
        self.base_api_dev = base_api_dev
        self.connected = False
        self.api_key = None

    async def signup(self, gmail: str, username: str):
        if not gmail.endswith("@gmail.com"):
            return "Invalid gmail"
        payload = {"gmail": gmail, "username": username}
        response = await async_search(
            self.base_api_dev + "/register",
            json=payload,
            post=True,
            re_json=True
        )
        return response

    async def get_api_key(self, username: str):
        response = await async_search(
            f"{self.base_api_dev}/get_api_key?api_key={username}",
            re_json=True
        )
        return response

    async def connect(self, username: str):
        response = await self.get_api_key(username)
        if response.get("requests_made", 0) >= 15:
            return "The limit has been reached"
        else:
            self.connected = True
            self.api_key = username
            return None

    async def hentai(self, query: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        response = await async_search(
            f"{self.base_api_dev}/akeno/hentai?query={query}&api_key={self.api_key}",
            re_json=True
        )
        return response

    async def pornopics(self, query: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        response = await async_search(
            f"{self.base_api_dev}/akeno/pornpics?query={query}&api_key={self.api_key}",
            re_json=True
        )
        return response

    async def x_search(self, query: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        url = f"{self.base_api_dev}/akeno/xnxxsearch-v2?query={query}&api_key={self.api_key}"
        response = await async_search(url, re_json=True)
        return response

    async def x_download(self, url: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        url_ = f"{self.base_api_dev}/akeno/xnxx-dl-v2?link={url}&api_key={self.api_key}"
        response = await async_search(url_, re_json=True)
        return response
        
    async def delete_api_key(self, delete_project: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        if delete_project == self.api_key:
            response = requests.delete(
                f"{self.base_api_dev}/delete_api_key_by_username?username={self.api_key}"
            ).json()
            return response
        else:
            return "Ok Done 🗿"
