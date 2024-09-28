import requests

from RyuzakiLib.api.reqs import async_search


class AkenoAI:
    def __init__(self, base_api_dev: str = "https://private-akeno.randydev.my.id"):
        self.base_api_dev = base_api_dev
        self.connected = False
        self.api_key = None
        self.headers = {"x-akeno-key": self.api_key}

    async def signup(self, gmail: str, username: str):
        if not gmail.endswith("@gmail.com"):
            return "Invalid gmail"
        params = {"username": username, "gmail": gmail}
        response = requests.post(
            self.base_api_dev + "/register",
            params=params
        ).json()
        return response

    async def connect(self, username: str, requests_limit: int = 30):
        response = await async_search(
            f"{self.base_api_dev}/get_api_key?api_key={username}",
            re_json=True
        )
        if response.get("requests_made", 0) >= requests_limit:
            return "The limit has been reached"
        else:
            self.connected = True
            self.api_key = username
            return None

    async def hentai(self, query: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        response = await async_search(
            f"{self.base_api_dev}/akeno/hentai?query={query}",
            re_json=True,
            headers=self.headers
        )
        return response

    async def pornopics(self, query: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        response = await async_search(
            f"{self.base_api_dev}/akeno/pornpics?query={query}",
            re_json=True,
            headers=self.headers
        )
        return response

    async def x_search(self, query: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        url = f"{self.base_api_dev}/akeno/xnxxsearch-v2?query={query}"
        return await async_search(url, re_json=True, headers=self.headers)

    async def x_download(self, url: str):
        if not self.connected or not self.api_key:
            return "Not connected or API key missing"
        url_ = f"{self.base_api_dev}/akeno/xnxx-dl-v2?link={url}"
        response = await async_search(url_, re_json=True, headers=self.headers)
        return response

    async def delete_api_key(self, email: str):
        response = requests.delete(
            f"{self.base_api_dev}/delete_api_key_by_username?email={email}"
        ).json()
        return response
