#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import requests
import os
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.api.fullstack import FullStackDev


class TiktokUrl:
    def __init__(self, url):
        self.url = url

    def tiktok_downloader(self, ryuzaki: bool = None):
        tiktok_url = self.url
        api_devs = "https://api.sdbots.tech"
        parameter = f"tiktok?url={tiktok_url}"
        api_url = f"{api_devs}/{parameter}"
        response = requests.get(api_url)

        if response.status_code != 200:
            return "Error: Unable to fetch data from the TikTok API"

        try:
            results = response.json()
            caption = results.get("result", {}).get("desc", "")

            if ryuzaki:
                video_url = results.get("result", {}).get("withoutWaterMarkVideo", "")
                if video_url:
                    return [video_url, caption]
            else:
                music_mp3 = results.get("result", {}).get("music", "")
                if music_mp3:
                    return [music_mp3, caption]

            return "Error: TikTok data not found or unsupported format"
        except Exception as e:
            return f"Error: {e}"


def faster_tiktok_downloader(link: str = None, ryuzaki_default: str = "ryuzaki.mp4"):
    if not link:
        return "Missing Tiktok Link"
    try:
        obj = TiktokUrl(url=link).tiktok_downloader(ryuzaki=True)
        super = FullStackDev(
            domain_url=obj[0], filename=ryuzaki_default, type_mode="wb"
        )
        saved = super.faster_downloader()
        return saved
    except Exception as e:
        return f"Error: {e}"
