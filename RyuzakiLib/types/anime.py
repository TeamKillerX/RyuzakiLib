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
from base64 import b64decode as what
from io import BytesIO

import requests
from PIL import Image
from pyrogram import Client, filters
from pyrogram.types import Message


class AnimeStyled:
    def init(self, apikey, input):
        self.apikey = apikey
        self.input = input

    def HuggingTokenAnime(self):
        nice_good = what("aHVnZ2luZ2ZhY2UuY28=").decode("utf-8")
        https = "https://"
        api_inference = "api-inference"
        hugging = f"{nice_good}"
        models = "models"
        dev = "Linaqruf"
        repo = "animagine-xl"
        rendydev_code = f"{https}{api_inference}.{hugging}/{models}/{dev}/{repo}"
        headers = {"Authorization": f"Bearer {self.apikey}"}
        payload = {"inputs": f"{self.input}"}
        response = requests.post(rendydev_code, headers=headers, json=payload)
        return response.content if response.status_code == 200 else "Api Invalid"

    def NowSendImage(self):
        image_bytes = self.HuggingTokenAnime()
        try:
            with Image.open(BytesIO(image_bytes)) as img:
                output_buffer = BytesIO()
                img.save(output_buffer, format="JPEG")
                output_buffer.seek(0)
            return output_buffer
        except Exception as e:
            return f"Error: {e}"
