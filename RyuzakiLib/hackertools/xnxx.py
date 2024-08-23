import wget

from RyuzakiLib.api.reqs import async_search


class PornoHub:
    def __init__(self):
        pass

    async def x_search(self, query=None):
        url = f"https://randydev-ryuzaki-api.hf.space/akeno/xnxxsearch?query={query}"
        res = await async_search(url, re_json=True)
        results = res["randydev"]["results"]
        y = res["randydev"]["results"][0]
        link = y["link"]
        title = y["title"]
        return [link, title, results]

    async def x_download(self, query=None, url=None, is_stream=False):
        if is_stream and url:
            url_ = f"https://randydev-ryuzaki-api.hf.space/akeno/xnxx-dl?link={url}"
            response = await async_search(url_, re_json=True)
            file_path = wget.download(response["randydev"]["results"]["url"])
            thumb = wget.download(response["randydev"]["results"]["thumb"])
            return file_path, thumb
        else:
            schub = await self.x_search(query=query)
            url_dl = f"https://randydev-ryuzaki-api.hf.space/akeno/xnxx-dl?link={schub[0]}"
            response = await async_search(url_dl, re_json=True)
            file_path = wget.download(response["randydev"]["results"]["url"])
            thumb = wget.download(response["randydev"]["results"]["thumb"])
            return file_path, thumb
