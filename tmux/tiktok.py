# credits @xtdevs

import asyncio
from os import mkdir
from RyuzakiLib.dl.tiktok import TiktokUrl
from pathlib import Path

DOWNLOAD = Path() / "download"

def link_tiktok(input):
    code = TiktokUrl(input, ryuzaki=True)
    video = code.tiktok_downloader()
    return video[0]

async def download_save_tiktok():
    link = input("Enter your TikTok link: ")
    video = link_tiktok(str(link))
    save_to = DOWNLOAD / video
    mkdir(save_to)
    print(f"Successfully Tiktok Downloader: {save_to}")

if __name__ == "__main__":
    asyncio.run(download_save_tiktok())
