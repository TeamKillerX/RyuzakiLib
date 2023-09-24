# credits @xtdevs

import asyncio
from RyuzakiLib.dl.tiktok import TiktokUrl
from pathlib import Path

DOWNLOAD = Path() / "download"

def link_tiktok(input):
    code = TiktokUrl(input, only_video=True)
    video = code.tiktok_downloader()
    return video[0]

async def download_save_tiktok():
    link = input("Enter your TikTok link: ")
    video = link_tiktok(str(link))
    save_to = DOWNLOAD / video

if __name__ == "__main__":
    asyncio.run(download_save_tiktok())
