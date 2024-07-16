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


import os
import shutil

import requests
from pyrogram import Client, filters
from pyrogram.types import Message


class Background:
    @staticmethod
    def removebg(api_key: str, image=None):
        endpoint = "https://api.remove.bg/v1.0/removebg"
        payload = {"size": "auto"}
        with open(f"{image}", "rb") as image_file:
            response = requests.post(
                endpoint,
                data=payload,
                headers={"X-Api-Key": api_key},
                files={"image_file": image_file},
                stream=True,
            )

        with open("output.png", "wb") as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        try:
            return "output.png"
        except Exception as e:
            return f"Error {e}"
