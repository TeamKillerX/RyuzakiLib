# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Developer Credits: @xtdevs

import os
import time

import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from tqdm import tqdm


class FacebookUrl:
    def __init__(self, apikey, link):
        self.apikey = apikey
        self.link = link

    def facebook_downloader(self):
        url = "https://facebook-video-and-reel-downloader.p.rapidapi.com/"
        querystring = {"url": self.link}

        headers = {
            "X-RapidAPI-Key": self.apikey,
            "X-RapidAPI-Host": "facebook-video-and-reel-downloader.p.rapidapi.com",
        }
        response = requests.request("GET", url, headers=headers, params=querystring)

        if response.status_code != 200:
            return "Error requests api"
        data_facebook = response.json()
        try:
            facebook_hd = data_facebook["sd"]
        except Exception as e:
            return f"Error request {e}"

        facebook_url = requests.get(facebook_hd, stream=True)
        if not facebook_hd:
            return "Error please try again facebook"
        if not facebook_url:
            return "Error please try again"
        total_size = int(facebook_url.headers.get("content-length", 0))
        send_video_path = "ryuzaki.mp4"
        progress_bar = ""
        with open(send_video_path, "wb") as f:
            bytes_received = 0
            progress = 0
            for data in facebook_url.iter_content(chunk_size=4096):
                f.write(data)
                bytes_received += len(data)
                progress = int(bytes_received / total_size * 100)
                new_progress_bar = f"Downloading {progress}% of {total_size}"
                if new_progress_bar != progress_bar:
                    return new_progress_bar
        return send_video_path
