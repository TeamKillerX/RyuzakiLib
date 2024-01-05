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

# JANGAN COPAS INI LU KEK KONTOL
# TANYA KE SUPPORT @KillerXSupport

import base64
from base64 import b64decode

import requests
from pyrogram import Client, filters
from pyrogram.types import Message


class CustomUrl:
    def __init__(self, url=None, website="mediafire"):
        self.url = url
        self.website = website

    def tools_downloader(self):
        parameter = b64decode("aHR0cDovL2Rvd25sb2FkLnJhbmR5ZGV2Lm15Lmlk").decode("utf-8")
        api_url = f"{parameter}/{self.website}?link={self.url}"
        x = requests.get(api_url)
        if x.status_code != 200:
            return "Error request"
        try:
            response = x.json()
            download = response["data"]["file"]["url"]["directDownload"]
            author_username = response["data"]["file"]["metadata"]["id"]
            file_size = response["data"]["file"]["metadata"]["size"]["readable"]
            return [download, author_username, file_size]
        except Exception as e:
            return f"Error: {e}"
