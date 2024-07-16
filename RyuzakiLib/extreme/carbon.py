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

import base64
from base64 import b64decode
from io import BytesIO
from typing import Optional

import requests
from aiohttp import ClientSession
from gpytranslate import SyncTranslator
from pyrogram import Client, filters
from pyrogram.types import Message

aiosession = ClientSession()


class Carbon:
    @staticmethod
    async def make_carbon(
        code: str = None,
        title: Optional[str] = "Ryuzaki",
        theme: Optional[str] = "breeze",
        auto_translate: Optional[str] = "auto",
        darkmode: Optional[bool] = True,
        rayso=False
    ):
        base="aHR0cHM6Ly9hcGkuc2Fmb25lLmRldi9yYXlzbw=="
        filename = "rayso.jpg"
        if rayso:
            api_url = b64decode(base).decode("utf-8")
            x = requests.post(
                f"{api_url}",
                json={
                    "code": code,
                    "title": title,
                    "theme": theme,
                    "padding": 64,
                    "language": auto_translate,
                    "darkMode": darkmode,
                },
            )
            if x.status_code != 200:
                return "Error api Gay"
            data = x.json()
            try:
                image_data = base64.b64decode(data["image"])
                f = BytesIO(image_data)
                f.name = filename
                return f
            except Exception as e:
                return f"Error: {e}"
        else:
            url = "https://carbonara.solopov.dev/api/cook"
            async with aiosession.post(url, json={"code": code}) as resp:
                image = BytesIO(await resp.read())
            image.name = "carbon.png"
            return image
