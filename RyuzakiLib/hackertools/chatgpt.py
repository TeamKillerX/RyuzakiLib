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

# original api credits : https://api.safone.me/chatgpt

import requests
from pyrogram import Client, filters
from pyrogram.types import Message

class RendyDevChat:
    def __init__(self, query):
        self.query = query

    def get_response(self):
        payloads = {
            "message": self.query,
            "chat_mode": "assistant",
            "dialog_messages": "[{'bot': '', 'user': ''}]"
        }
        try:
            response = requests.post(
                "https://api.safone.me/chatgpt",
                json=payloads,
                headers={"Content-Type": "application/json"}
            ).json()
            if not (response and "message" in response):
                print(response)
                raise ValueError("Invalid Response from Server")
            return response.get("message")
        except Exception as e:
            return "Error Api {}".format(e)
