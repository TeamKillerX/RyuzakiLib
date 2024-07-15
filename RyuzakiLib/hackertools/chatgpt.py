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

import base64
import json
import os
from base64 import b64decode as idk

import requests
from pyrogram import Client, filters
from RyuzakiLib.hackertools.blackbox import Blackbox
from pyrogram.types import Message
from typing import Optional

# You can free api key this // only developer reset api key :)
API_KEYS = "29db8322f22d425d7023c499610fc2419f8ff44e0bd3f63edd90d2994bf76b49"

class RendyDevChat:
    def __init__(self) -> None:
        pass

    @staticmethod
    def chat_hacked(
        args: str = None,
        latest_model: str = "openai-latest",
        model_id: Optional[int] = None,
        user_id: Optional[int] = None,
        mongo_url: Optional[str] = None,
        list_model_all: Optional[bool] = False,
        is_google_beta: Optional[bool] = False
        
    ):
        if latest_model == "openai-latest":
            response_url = "https://api.safone.dev/chatgpt"
            payloads = {
                "message": args,
                "version": 3,
                "chat_mode": "assistant",
                "dialog_messages": "[{'bot': '', 'user': ''}]",
            }
            try:
                response = requests.post(
                    response_url,
                    json=payloads,
                    headers={"Content-Type": "application/json"},
                ).json()
                if not (response and "message" in response):
                    print(response)
                    raise ValueError("Invalid Response from Server")
                return response.get("message")
            except Exception as e:
                return f"Error Api {e}"
        elif latest_model == "openai-v2":
            url = "https://codes.randydev.my.id/ryuzaki/chatgpt-old"
            params = {"query": args}
            response = requests.post(url, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "blackbox":
            response = Blackbox.chat(args)
            return response.get("answer")
        elif latest_model == "openai-turbo":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt3-turbo"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            payload = {"query": args}
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "list-model":
            if list_model_all:
                text = """
                ```python
                New Model List
                openai-latest
                openai-v2
                openai-turbo
                gemini-pro
                google-ai
                blackbox
                """
                return text
            else:
                return "you can check set list_model_all=True"
        elif latest_model == "gemini-pro":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {
                "query": args,
                "mongo_url": mongo_url,
                "user_id": user_id,
                "is_multi_chat": True,
            }
            response = requests.post(url, headers=headers, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response
        elif latest_model == "google-ai":
            if is_google_beta:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/v1beta2-google-ai"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/google-ai"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args}
            response = requests.post(url, headers=headers, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response

    @staticmethod
    def image_generator(args, dalle_pro: bool = False):
        if dalle_pro:
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/opendalle"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            payload = {"query": args}
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response
        else:
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/dalle3xl"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            payload = {"query": args}
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response
