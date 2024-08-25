import requests

from RyuzakiLib.api.reqs import async_search


class AkenoAI:
    def __init__(self, base_api_dev: str = "https://akeno.randydev.my.id"):
        self.base_api_dev = base_api_dev

    async def signup(self, gmail: str, username: str):
        if not gmail.startswith("@gmail.com"):
            return "Invalid gmail"
        payload = {"gmail": gmail, "username": username}
        response = await async_seach(
            self.base_api_dev + "/register",
            json=payload,
            post=True,
            re_json=True
        )
        return response

    async def get_api_key(self, username: str):
        response = await async_seach(
            f"{self.base_api_dev}/get_api_key?api_key={username}",
            re_json=True
        )
        return response

    async def delete_api_key(self, username: str, delete_project: str):
        if delete_project == username":
            response = requests.delete(
                f"{self.base_api_dev}/delete_api_key_by_username?username={username}"
            ).json()
            return response
        else:
            return "Ok Done 🗿"
