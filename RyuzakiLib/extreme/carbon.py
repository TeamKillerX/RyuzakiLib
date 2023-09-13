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
from io import BytesIO
from aiohttp import ClientSession
from pyrogram import Client, filters
from pyrogram.types import Message

aiosession = ClientSession()

class CarbonSuper:
    def __init__(
        self,
        code,
        color=None,
        ryuzaki: bool=None
    ):
        self.code = code
        self.color = color
        self.ryuzaki = ryuzaki

    async def make_carbon(self):
        url = "https://carbonara.solopov.dev/api/cook"
        if self.ryuzaki:
            async with aiosession.post(url, json={"code": self.code, "backgroundColor": self.color}) as resp:
                image = BytesIO(await resp.read())
            image.name = "carbon.png"
            return image
        else:
            async with aiosession.post(url, json={"code": self.code}) as resp:
                image = BytesIO(await resp.read())
            image.name = "carbon.png"
            return image
