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
from datetime import datetime as dt
from typing import Optional

import requests
from g4f.client import Client as Clients_g4f
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.api.fullstack import FullStackDev
from RyuzakiLib.api.reqs import AsyicXSearcher
from RyuzakiLib.hackertools.blackbox import Blackbox

API_KEYS = "6398769dabd9fe0e49bedce0354b40a9b1a69d9594dc9d48c1d8a2a071c51e89"

owner_base = f"""
Your name is Randy Dev. A kind and friendly AI assistant that answers in
a short and concise answer. Give short step-by-step reasoning if required.

- Powered by @xtdevs on telegram
Today is {dt.now():%A %d %B %Y %H:%M}
"""

class RendyDevChat:
    @staticmethod
    async def chat_hacked(
        base_api_dev = "https://private-akeno.randydev.my.id",
        args: str = None,
        latest_model: str = "openai-latest",
        model_id: Optional[int] = None,
        user_id: Optional[int] = 0,
        mongo_url: Optional[str] = None,
        system_prompt: Optional[str] = owner_base,
        api_key: Optional[str] = None,
        list_model_all: Optional[bool] = False,
        is_working_dev: Optional[bool] = True
    ):
        if latest_model == "openai-v2":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/chatgpt-old"
            else:
                url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-old"
            params = {"query": args}
            check_response = requests.post(url, json=params).json()
            return check_response["randydev"]["message"]
        elif latest_model == "blackbox":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/blackbox?api_key={api_key}"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/blackbox"
            params = {"query": args}
            check_response = requests.post(url, json=params).json()
            return check_response["randydev"]["message"]
        elif latest_model == "list-model":
            if list_model_all:
                text = """
                ```python
                openai-v2
                gemini-pro
                google-ai
                betagoogle-ai
                """
                return text
            else:
                return "you can check set list_model_all=True"
        elif latest_model == "gemini-pro":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/gemini-ai-pro"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"
            payload = {
                "query": args,
                "mongo_url": mongo_url,
                "user_id": user_id,
                "is_multi_chat": True
            }
            headers = {"accept": "application/json", "api-key": API_KEYS}
            check_response = requests.post(url, headers=headers, json=payload).json()
            return check_response["randydev"]["message"]
        elif latest_model == "microsoft":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/faceai?api_key={api_key}"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/faceai"
            payload = {
                "query": args,
                "clients_name": "microsoft/Phi-3-mini-4k-instruct",
            }
            headers = {"accept": "application/json"}
            check_response = requests.post(url, headers=headers, json=payload).json()
            return check_response["randydev"]["message"]
        elif latest_model == "gemma":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/faceai?api_key={api_key}"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/faceai"
            payload = {
                "query": args,
                "clients_name": "google/gemma-1.1-7b-it",
            }
            headers = {"accept": "application/json"}
            check_response = requests.post(url, headers=headers, json=payload).json()
            return check_response["randydev"]["message"]
        elif latest_model == "mistralai":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/faceai?api_key={api_key}"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/faceai"
            payload = {
                "query": args,
                "clients_name": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            }
            headers = {"accept": "application/json"}
            check_response = requests.post(url, headers=headers, json=payload).json()
            return check_response["randydev"]["message"]
        elif latest_model == "faceh4":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/faceai?api_key={api_key}"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/faceai"
            payload = {
                "query": args,
                "clients_name": "HuggingFaceH4/zephyr-7b-beta",
            }
            headers = {"accept": "application/json"}
            check_response = requests.post(url, headers=headers, json=payload).json()
            return check_response["randydev"]["message"]
        elif latest_model == "google-ai":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/google-ai?api_key={api_key}"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/google-ai"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args}
            check_response = requests.post(url, headers=headers, json=params).json()
            return check_response["randydev"]["message"]
        elif latest_model == "betagoogle-ai":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/v1beta2-google-ai?api_key={api_key}"
            else:
                url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/v1beta2-google-ai"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args}
            check_response = requests.post(url, headers=headers, json=params).json()
            return check_response["randydev"]["message"]
        elif latest_model == "gpt-4-turbo":
            if is_working_dev:
                url = f"{base_api_dev}/ryuzaki/chatgpt-custom"
            else:
                url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-custom"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args, "model": "gpt-4-turbo"}
            check_response = requests.post(url, headers=headers, json=params).json()
            return check_response["randydev"]["message"]
        elif latest_model == "gpt-4o":
            clients_x = Clients_g4f()
            response = clients_x.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": args}
                ],
            )
            return response.choices[0].message.content

    @staticmethod
    def download_images(image_urls):
        downloaded_paths = []
        for i, url in enumerate(image_urls, start=1):
            filename = f"image_{i}.png"
            FullStackDev.fast(url, filename=filename)
        downloaded_paths.append(filename)
        return downloaded_paths

    @staticmethod
    async def image_generator(
        args,
        api_key: str = None,
        base_api_dev="https://private-akeno.randydev.my.id",
        is_working_dev=True
    ):
        if is_working_dev:
            url = f"{base_api_dev}/ryuzaki/dalle3xl?api_key={api_key}"
        else:
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/dalle3xl"
        headers = {"accept": "application/json", "api-key": API_KEYS}
        payload = {"query": args}
        check_response = requests.post(url, headers=headers, json=payload).json()
        return check_response
