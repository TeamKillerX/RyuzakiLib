# credits @xtdevs

import asyncio

import requests

from RyuzakiLib.dl.tiktok import TiktokUrl


def link_tiktok(input):
    code = TiktokUrl(input, ryuzaki=True)
    video = code.tiktok_downloader()
    url = video[0]
    r = requests.get(url, allow_redirects=True)
    filename = "tiktok.mp3"
    saved = open(filename, "wb").write(r.content)
    return saved


async def download_save_tiktok():
    link = input("Enter your TikTok link: ")
    video = link_tiktok(str(link))
    print(f"Successfully Tiktok Downloader")


if __name__ == "__main__":
    asyncio.run(download_save_tiktok())
