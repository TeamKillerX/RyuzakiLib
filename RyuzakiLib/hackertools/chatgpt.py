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
        query: str=None,
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
        latest_version: bool = False,
    ):
        if isinstance(message, Message):
            blacklist = self.get_blacklist_from_file()
            if message.from_user.id in blacklist:
                return "Blocked User"
        if not latest_version:
            return f"WTF THIS {self.query}"
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
            if not response or "message" not in response:
                print(response)
                raise ValueError("Invalid Response from Server")
            return response.get("message")
        except Exception as e:
            return f"Error Api {e}"

    def get_response_model(
        self,
        model_id: int=None,
        is_models: bool=False,
        re_json: bool=False,
        status_ok: bool=False
    ):
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-model"
        params = {
            "query": self.query,
            "model_id": model_id,
            "is_models": is_models
        }
        response = requests.post(url, json=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        if status_ok:
            return response.json() if re_json else response
        else:
            return f"WTF THIS {self.query}"

    def get_response_beta(self, joke: bool = False):
        url = "https://freegptapi.hop.sh/neural/api"
        params = {"query": self.query}
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        if not joke:
            return f"WTF THIS {self.query}"
        check_response = response.json()
        return check_response.get("answer")

    def get_response_bing(self, bing: bool = False):
        url = f"https://api.freegpt4.ddns.net/?text={self.query}"
        response = requests.get(url)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        return response.text if bing else f"WTF THIS {self.query}"

    def get_response_llama(self, llama: bool = False):
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/llama"
        params = {"query": self.query}
        response = requests.get(url, json=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        if not llama:
            return f"WTF THIS {self.query}"
        check_response = response.json()
        return check_response["randydev"]["message"]

    def get_response_turbo3(self, turbo3: bool = False):
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt3-turbo"
        params = {"query": self.query}
        response = requests.get(url, json=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        if not turbo3:
            return f"WTF THIS {self.query}"
        check_response = response.json()
        return check_response["randydev"]["message"]

    def get_response_gemini_pro(
        self,
        api_key: str=None,
        re_json: bool = False,
        is_gemini_pro: bool = False
    ):
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"
        headers = {
            "accept": "application/json",
            "api-key": api_key
        }
        params = {"query": self.query}
        response = requests.post(url, headers=headers, json=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        if is_gemini_pro:
            return response.json() if re_json else response
        else:
            return f"WTF THIS {self.query}"

    def get_response_google_ai(
        self,
        api_key: str=None,
        re_json: bool = False,
        is_chat_bison: bool = False,
        is_google: bool = False
    ):
        if is_chat_bison:
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/v1beta2-google-ai"
        else:
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/google-ai"
        headers = {
            "accept": "application/json",
            "api-key": api_key
        }
        params = {"query": self.query}
        response = requests.post(url, headers=headers, json=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        if is_google:
            return response.json() if re_json else response
        else:
            return f"WTF THIS {self.query}"

    def get_risma_image_generator(
        self,
        api_key: str=None,
        is_opendalle: bool = False
    ):
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/opendalle"
        headers = {
            "accept": "application/json",
            "api-key": api_key
        }
        payload = {"query": self.query}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"

        return response.json() if is_opendalle else response

    def multi_chat_response(
        self,
        api_key: str=None,
        is_multi_chat: bool = False
    ):
        if not is_multi_chat:
            return self.get_response_llama(llama=True)
        response_str = self.get_response_gemini_pro(
            api_key=api_key,
            re_json=True,
            is_gemini_pro=True,
        )
        return response_str["randydev"].get("message")
