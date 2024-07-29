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
from g4f.client import Client
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.api.fullstack import FullStackDev
from RyuzakiLib.api.reqs import AsyicXSearcher
from RyuzakiLib.hackertools.blackbox import Blackbox

API_KEYS = "29db8322f22d425d7023c499610fc2419f8ff44e0bd3f63edd90d2994bf76b49"

class RendyDevChat:
    @staticmethod
    async def chat_hacked(
        args: str = None,
        latest_model: str = "openai-latest",
        model_id: Optional[int] = None,
        user_id: Optional[int] = 0,
        mongo_url: Optional[str] = None,
        list_model_all: Optional[bool] = False
    ):
        if latest_model == "openai-v2":
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-old"
            params = {"query": args}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                json=params
            )
            return check_response["randydev"]["message"]
        elif latest_model == "blackbox":
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/blackbox"
            params = {"query": args}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                json=params
            )
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
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"
            payload = {
                "query": args,
                "mongo_url": mongo_url,
                "user_id": user_id,
                "is_multi_chat": True
            }
            headers = {"accept": "application/json", "api-key": API_KEYS}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                headers=headers,
                json=payload
            )
            return check_response["randydev"]["message"]
        elif latest_model == "microsoft":
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/faceai"
            payload = {
                "query": args,
                "clients_name": "microsoft/Phi-3-mini-4k-instruct",
            }
            headers = {"accept": "application/json"}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                headers=headers,
                json=payload
            )
            return check_response["randydev"]["message"]
        elif latest_model == "gemma":
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/faceai"
            payload = {
                "query": args,
                "clients_name": "google/gemma-1.1-7b-it",
            }
            headers = {"accept": "application/json"}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                headers=headers,
                json=payload
            )
            return check_response["randydev"]["message"]
        elif latest_model == "mistralai":
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/faceai"
            payload = {
                "query": args,
                "clients_name": "mistralai/Mixtral-8x7B-Instruct-v0.1",
            }
            headers = {"accept": "application/json"}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                headers=headers,
                json=payload
            )
            return check_response["randydev"]["message"]
        elif latest_model == "faceh4":
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/faceai"
            payload = {
                "query": args,
                "clients_name": "HuggingFaceH4/zephyr-7b-beta",
            }
            headers = {"accept": "application/json"}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                headers=headers,
                json=payload
            )
            return check_response["randydev"]["message"]
        elif latest_model == "google-ai":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/google-ai"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                headers=headers,
                json=params
            )
            return check_response["randydev"]["message"]
        elif latest_model == "betagoogle-ai":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/v1beta2-google-ai"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                headers=headers,
                json=params
            )
            return check_response["randydev"]["message"]
        elif latest_model == "gpt-4-turbo":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-custom"
            headers = {"accept": "application/json", "api-key": API_KEYS}
            params = {"query": args, "model": "gpt-4-turbo"}
            check_response = await AsyicXSearcher.search(
                url,
                post=True,
                re_json=True,
                headers=headers,
                json=params
            )
            return check_response["randydev"]["message"]
        elif latest_model == "gpt-4o":
            client = Client()
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": args}],
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
    async def image_generator(args):
        url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/dalle3xl"
        headers = {"accept": "application/json", "api-key": API_KEYS}
        payload = {"query": args}
        check_response = await AsyicXSearcher.search(
            url,
            post=True,
            re_json=True,
            headers=headers,
            json=payload
        )
        return check_response
