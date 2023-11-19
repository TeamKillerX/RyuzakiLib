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

import requests
import base64
import os
from base64 import b64decode as idk
from io import BytesIO
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
        return "".join(chr(int(binary, 2)) for binary in number)

    def sticker_converter(self):
        return bool(self.avatar_profile)
