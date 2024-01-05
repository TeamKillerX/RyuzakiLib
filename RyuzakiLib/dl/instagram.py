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
from pyrogram import Client, filters
from pyrogram.types import Message

# Instagram rapidapi : https://rapidapi.com/maatootz/api/instagram-downloader-download-instagram-videos-stories


class InstagramUrl:
    def __init__(self, apikey, link):
        self.apikey = apikey
        self.link = link

    def instagram_downloader(self):
        url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
        querystring = {"url": self.link}
        headers = {
            "X-RapidAPI-Key": self.apikey,
            "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com",
        }
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code != 200:
            return "Failed api please try again"
        dataig = response.json()
        try:
            igdownloader = dataig["media"]
        except Exception as e:
            return f"Error request {e}"
        if igdownloader:
            try:
                return igdownloader
            except Exception as e:
                return f"Error request. {e}"
        else:
            return "Failed to api Instagram please try again"
