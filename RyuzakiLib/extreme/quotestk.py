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

# add quote sticker by credits @xtdevs

import base64
import os
from base64 import b64decode as idk
from io import BytesIO

import requests
from PIL import Image


class QouteSticker:
    def __init__(
        self,
        type: str = "quote",
        format: str = "webp",
        background_color: str = "#1b1429",
        width: int = 512,
        height: int = 768,
        scale: int = 2,
        developer: str = "ryuzaki.webp",
        image_format: str = "WEBP",
        entities=None,
        reply_message=None,
        avatar_profile: bool = None,
        user_id: int = None,
        first_name: str = None,
        photo_url: str = None,
        text: str = None,
    ):
        self.type = type
        self.format = format
        self.background_color = background_color
        self.width = width
        self.height = height
        self.scale = scale
        self.developer = developer
        self.image_format = image_format
        self.entities = entities
        self.reply_message = reply_message
        self.avatar_profile = avatar_profile
        self.user_id = user_id
        self.first_name = first_name
        self.photo_url = photo_url
        self.text = text

    def knowledge_hack(self):
        you_dont_know = "01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01100010 01101111 01110100 00101110 01101100 01111001 01101111 00101110 01110011 01110101 00101111 01110001 01110101 01101111 01110100 01100101 00101111 01100111 01100101 01101110 01100101 01110010 01100001 01110100 01100101"
        number = you_dont_know.split()
        decode_string = ""
        for binary in number:
            decimal_value = int(binary, 2)
            decode_string += chr(decimal_value)
        return decode_string

    def sticker_converter(self):
        if self.avatar_profile:
            is_avatar = True
            return is_avatar
        else:
            is_avatar = False
            return is_avatar
        data = {
            "type": self.type,
            "format": self.format,
            "backgroundColor": self.background_color,
            "width": self.width,
            "height": self.height,
            "scale": self.scale,
            "messages": [
                {
                    "entities": self.entities,
                    "avatar": self.is_avatar,
                    "from": {
                        "id": self.user_id,
                        "name": self.first_name,
                        "photo": {"url": self.photo_url},
                    },
                    "text": self.text,
                    "replyMessage": self.reply_message,
                }
            ],
        }
        required_post = self.knowledge_hack()
        response = requests.post(f"{required_post}", json=data)
        if response.status_code != 200:
            return "CAACAgUAAx0EYvH21AACMxFkzss9PCU8JOOQM_iIXEdRFEIgvAACUgsAAn7_cFaVmzq8YrV6xh4E"
        data = response.json()
        buffer = base64.b64decode(data["result"]["image"].encode("utf-8"))
        with BytesIO(buffer) as image_buffer:
            image = Image.open(image_buffer)
            image.save(self.developer, format=self.image_format)
        return self.developer
