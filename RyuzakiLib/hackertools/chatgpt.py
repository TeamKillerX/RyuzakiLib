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
from base64 import b64decode
from base64 import b64decode as idk
from typing import Optional

import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.api.fullstack import FullStackDev
from RyuzakiLib.hackertools.blackbox import Blackbox

API_KEYS = "29db8322f22d425d7023c499610fc2419f8ff44e0bd3f63edd90d2994bf76b49"

class RendyDevChat:
    @staticmethod
    def chat_hacked(
        args: str = None,
        latest_model: str = "openai-latest",
        model_id: Optional[int] = None,
        user_id: Optional[int] = 0,
        mongo_url: Optional[str] = None,
        list_model_all: Optional[bool] = False
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
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-old"
            params = {"query": args}
            response = requests.post(url, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "blackbox":
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/blackbox"
            params = {"query": args}
            response = requests.post(url, json=params)
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
                gemini-pro
                google-ai
                betagoogle-ai
                chatbot
                """
                return text
            else:
                return "you can check set list_model_all=True"
        elif latest_model == "gemini-pro":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"
            payload = {
                "query": args,
                "mongo_url": mongo_url,
                "user_id": user_id,
                "is_multi_chat": True
            }
            headers = {"accept": "application/json", "api-key": API_KEYS}
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "beta-rag":
            payload = {
                "query": args,
                "user_id": user_id
            }
            headers = {"accept": "application/json"}
            response = requests.post(
                "https://randydev-ryuzaki-api.hf.space/ryuzaki/beta-rag",
                headers=headers,
                json=payload
            )
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "google-ai":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/google-ai"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args}
            response = requests.post(url, headers=headers, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "betagoogle-ai":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/v1beta2-google-ai"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args}
            response = requests.post(url, headers=headers, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "chatbot":
            base="aHR0cHM6Ly9hcGkuc2Fmb25lLmRldi9jaGF0Ym90",
            api_url = b64decode(base).decode("utf-8")
            params = {
                "query": args,
                "user_id": 0,
                "bot_name": "Ryuzaki Dev",
                "bot_master": "@Randydev_bot",
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

    @staticmethod
    def download_images(image_urls):
        downloaded_paths = []
        for i, url in enumerate(image_urls, start=1):
            filename = f"image_{i}.png"
            FullStackDev.fast(url, filename=filename)
        downloaded_paths.append(filename)
        return downloaded_paths

    @staticmethod
    def image_generator(args):
        url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/dalle3xl"
        headers = {"accept": "application/json", "api-key": API_KEYS}
        payload = {"query": args}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"
        check_response = response.json()
        return check_response
