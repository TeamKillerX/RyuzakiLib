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
from io import BytesIO

import requests


class WebShotUrl:
    def __init__(
        self,
        url=None,
        base="aHR0cHM6Ly9hcGkuc2Fmb25lLmRldi93ZWJzaG90",
        width: int = 1280,
        height: int = 720,
        scale: int = 1,
        delay: int = 0,
        quality="1920x1080",
        type_mine="JPEG",
        pixels="1024",
        cast="Z100",
        author="@xtdevs",
    ):
        self.url = url
        self.width = width
        self.height = height
        self.scale = scale
        self.delay = delay
        self.quality = quality
        self.type_mine = type_mine
        self.pixels = pixels
        self.cast = cast
        self.author = author

    def send_screenshot_quality(self):
        try:
            required_url = f"https://mini.s-shot.ru/{self.quality}/{self.type_mine}/{self.pixels}/{self.cast}/?{self.url}"
            caption = f"Powered By {self.author}"
            return [required_url, caption]
        except Exception as e:
            return f"Error {e}"

    def send_screenshot(self, screenshot_full: bool = None):
        api_url = b64decode(self.base).decode("utf-8")
        if screenshot_full:
            data = {
                "url": self.url,
                "width": self.width,
                "height": self.height,
                "scale": self.scale,
                "delay": self.delay,
                "full": True,
            }
            x = requests.post(f"{api_url}", json=data)
            if x.status_code != 200:
                return "Error request:"
            try:
                y = x.json()
                iseeyou = base64.b64decode(y["image"])
                hack = BytesIO(iseeyou)
                hack.name = "screenshot.jpg"
                return hack
            except Exception as e:
                return f"Error: {e}"
        else:
            data = {
                "url": self.url,
                "width": self.width,
                "height": self.height,
                "scale": self.scale,
                "delay": self.delay,
                "full": False,
            }
            x = requests.post(f"{api_url}", json=data)
            if x.status_code != 200:
                return "Error request:"
            try:
                y = x.json()
                iseeyou = base64.b64decode(y["image"])
                hack = BytesIO(iseeyou)
                hack.name = "screenshot.jpg"
                return hack
            except Exception as e:
                return f"Error: {e}"
