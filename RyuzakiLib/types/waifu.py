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

from random import choice

import requests
from pyrogram import Client, filters
from pyrogram.types import Message


class SendWaifuRandom:
    @staticmethod
    def send_waifu_pics():
        LIST_SFW_JPG = ["neko", "waifu", "megumin"]
        waifu_api = "https://api.waifu.pics/sfw"
        waifu_category = choice(LIST_SFW_JPG)
        waifu_param = f"{waifu_api}/{waifu_category}"

        response = requests.get(waifu_param)

        if response.status_code != 200:
            return "Sorry, there was an error processing your request. Please try again later"

        data_waifu = response.json()
        try:
            waifu_image_url = data_waifu["url"]
        except Exception as e:
            return f"Error request {e}"

        if waifu_image_url:
            try:
                return waifu_image_url
            except Exception as e:
                return f"**Info Error:** {e}"
        else:
            return "Not found waifu"
