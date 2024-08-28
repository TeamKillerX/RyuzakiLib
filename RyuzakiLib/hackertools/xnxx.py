import wget

from RyuzakiLib.api.reqs import async_search


class PornoHub:
    def __init__(self, token=None, base_api_dev: str = "https://akeno.randydev.my.id"):
        self.base_api_dev = base_api_dev
        self.token = token

    async def x_search(self, query=None):
        url = f"{self.base_api_dev}/akeno/xnxxsearch-v2?query={query}&api_key={self.token}"
        res = await async_search(url, re_json=True)
        results = res["randydev"]["results"]
        y = res["randydev"]["results"][0]
        link = y["link"]
        title = y["title"]
        return [link, title, results]

    async def x_download(self, query=None, url=None, is_stream=False):
        if is_stream and url:
            url_ = f"{self.base_api_dev}/akeno/xnxx-dl-v2?link={url}&api_key={self.token}"
            response = await async_search(url_, re_json=True)
            file_path = wget.download(response["randydev"]["results"]["url"])
            thumb = wget.download(response["randydev"]["results"]["thumb"])
            title = response["randydev"]["results"].get("title", "Powered by Randydev")
            return file_path, thumb, title
        else:
            schub = await self.x_search(query=query)
            url_dl = f"{self.base_api_dev}/akeno/xnxx-dl-v2?link={schub[0]}&api_key={self.token}"
            response = await async_search(url_dl, re_json=True)
            file_path = wget.download(response["randydev"]["results"]["url"])
            thumb = wget.download(response["randydev"]["results"]["thumb"])
            title = response["randydev"]["results"].get("title", "Powered by Randydev")
            return file_path, thumb, title
