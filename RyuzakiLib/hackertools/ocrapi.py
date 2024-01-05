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


import json

import requests
from pyrogram import Client, filters
from pyrogram.types import Message


class OcrApiUrl:
    def __init__(self, api_key, url, language):
        self.api_key = api_key
        self.url = url
        self.language = language

    def ocr_space_url(self, overlay=False):
        payload = {
            "url": self.url,
            "isOverlayRequired": overlay,
            "apikey": self.api_key,
            "language": self.language,
        }
        try:
            response = requests.post("https://api.ocr.space/parse/image", data=payload)
            response.raise_for_status()
            return response.content.decode()
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

    def now_send_text(self):
        try:
            test_url = self.ocr_space_url()
            parsed_response = json.loads(test_url)
            if "ParsedResults" in parsed_response and len(parsed_response["ParsedResults"]) > 0:
                return parsed_response["ParsedResults"][0]["ParsedText"]
            else:
                return "No text found in the image."
        except (json.JSONDecodeError, KeyError):
            return "Error parsing the OCR response."
