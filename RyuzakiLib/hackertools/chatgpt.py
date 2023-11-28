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
import os
import json
import base64
from pyrogram import Client, filters
from pyrogram.types import Message
from base64 import b64decode as idk

class RendyDevChat:
    def __init__(
        self,
        query,
        binary="01101000 01110100 01110100 01110000 01110011 00111010 00101111 00101111 01100001 01110000 01101001 00101110 01110011 01100001 01100110 01101111 01101110 01100101 00101110 01100100 01100101 01110110 00101111 01100011 01101000 01100001 01110100 01100111 01110000 01110100",
    ):
        self.query = query
        self.binary = binary

    @staticmethod
    def knowledge_hack(text_code):
        you_dont_know = "".join(text_code)
        number = you_dont_know.split()
        return "".join(chr(int(binary, 2)) for binary in number)

    def get_blacklist_from_file(self):
        try:
            with open("blacklist.json", "r") as file:
                blacklist = json.load(file)
            return set(blacklist)
        except FileNotFoundError:
            return set()

    def get_response(
        self,
        message,
        version: int = 3,
        chat_mode: str = "assistant",
        latest_version: bool = None,
    ):
        if isinstance(message, Message):
            blacklist = self.get_blacklist_from_file()
            if message.from_user.id in blacklist:
                return "Blocked User"
        if latest_version:
            response_url = self.knowledge_hack(self.binary)
            payloads = {
                "message": self.query,
                "version": version,
                "chat_mode": chat_mode,
                "dialog_messages": "[{'bot': '', 'user': ''}]",
            }
            try:
                response = requests.post(
                    f"{response_url}",
                    json=payloads,
                    headers={"Content-Type": "application/json"},
                ).json()
                if not (response and "message" in response):
                    print(response)
                    raise ValueError("Invalid Response from Server")
                return response.get("message")
            except Exception as e:
                return f"Error Api {e}"
        else:
            return f"WTF THIS {self.query}"

    def get_response_model(self, model_id: int=None, is_models: bool=False):
        url = "https://lexica.qewertyy.me/models"
        if is_models:
            params = {"model_id": model_id, "prompt": self.query}
            response = requests.post(url, params=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            answer = check_response.get("content")
            return answer
        else:
            params = {"model_id": 5, "prompt": self.query}
            response = requests.post(url, params=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            answer = check_response.get("content")
            return answer

    def get_response_beta(self, joke: bool = None):
        url = "https://freegptapi.hop.sh/neural/api"
        params = {"query": self.query}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        if joke:
            check_response = response.json()
            answer = check_response.get("answer")
            return answer
        else:
            return f"WTF THIS {self.query}"

    def get_response_bing(self, bing: bool = None):
        url = f"https://api.freegpt4.ddns.net/?text={self.query}"
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        if bing:
            check_response = response.text
            return check_response
        else:
            return f"WTF THIS {self.query}"
