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

from pyrogram import Client, filters
from pyrogram.types import Message
from base64 import b64decode
import requests
import base64
from io import BytesIO

class CarbonRaySo:
    def __init__(
        self,
        code,
        title="Ryuzaki Dev",
        theme=None,
        ryuzaki: bool=None
    ):
        self.code = code
        self.title = title
        self.theme = theme
        self.ryuzaki = ryuzaki

    def make_carbon_rayso(self):
        api_url = b64decode("aHR0cHM6Ly9hcGkuc2Fmb25lLm1lL3JheXNv").decode("utf-8")
        if self.ryuzaki:
            x = requests.post(
                f"{api_url}",
                json={
                    "code": self.code,
                    "title": self.title,
                    "theme": self.theme,
                    "darkMode": True
                }
            )
            if x.status_code != 200:
                return "Error api Gay"
            data = x.json()
            try:
                image_data = base64.b64decode(data["image"])
                with BytesIO(image_data) as f:
                    f.name = "ray.jpg"
                return f
            except Exception as e:
                return f"Error: {e}"
        else:
            x = requests.post(
                f"{api_url}",
                json={
                    "code": self.code,
                    "title": self.title,
                    "theme": "breeze",
                    "darkMode": True
                }
            )
            if x.status_code != 200:
                return "Error api Gay"
            data = x.json()
            try:
                image_data = base64.b64decode(data["image"])
                with BytesIO(image_data) as f:
                    f.name = "ray.jpg"
                return f
            except Exception as e:
                return f"Error: {e}"
