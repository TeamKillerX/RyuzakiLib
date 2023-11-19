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

import os
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from base64 import b64decode


class ChatbotAi:
    def __init__(
        self,
        query,
        user_id: int = None,
        base="aHR0cHM6Ly9hcGkuc2Fmb25lLmRldi9jaGF0Ym90",
        bot_name="Ryuzaki Dev",
        bot_master="@Randydev_bot",
    ):
        self.query = query
        self.user_id = user_id
        self.base = base
        self.bot_name = bot_name
        self.bot_master = bot_master

    def get_response_ai(self):
        api_url = b64decode(self.base).decode("utf-8")
        params = {
            "query": self.query,
            "user_id": self.user_id,
            "bot_name": self.bot_name,
            "bot_master": self.bot_master,
        }
        x = requests.get(f"{api_url}", params=params)
        if x.status_code != 200:
            return "Error api request"
        try:
            y = x.json()
            response = y["response"]
            return response
        except Exception as e:
            return f"Error {e}"
