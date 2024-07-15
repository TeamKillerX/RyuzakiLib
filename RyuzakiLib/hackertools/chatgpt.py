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
from pyrogram.types import Message
from typing import Optional

class RendyDevChat:
    def __init__(self) -> None:
        pass

    @staticmethod
    def chat_hacked(
        args: str = None,
        latest_model: str = "openai-latest",
        model_id: Optional[int] = None,
        user_id: Optional[int] = None,
        api_key: Optional[str] = None,
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
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-model"
            params = {"query": args, "model_id": model_id, "is_models": True}
            response = requests.post(url, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response
        elif latest_model == "openai-beta":
            url = "https://freegptapi.hop.sh/neural/api"
            params = {"query": args}
            response = requests.post(url, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            answer = check_response.get("answer")
            return answer
        elif latest_model == "openai-bing":
            url = f"https://api.freegpt4.ddns.net/?text={args}"
            response = requests.get(url)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.text
            return check_response
        elif latest_model == "openai-llama":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/llama"
            params = {"query": args}
            response = requests.get(url, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "openai-turbo":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt3-turbo"
            headers = {"accept": "application/json", "api-key": api_key}
            payload = {"query": args}
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response["randydev"]["message"]
        elif latest_model == "model-list":
            if list_model_all:
                text = """
                ```python
                New Model List
                openai-latest
                openai-v2
                openai-beta
                openai-turbo
                openai-llama
                openai-bing
                gemini-pro
                google-ai
                """
                return text
            else:
                return "you can check set list_model_all=True"
        elif latest_model == "gemini-pro":
            url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"
            headers = {"accept": "application/json", "api-key": api_key}
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
            headers = {"accept": "application/json", "api-key": api_key}
            params = {"query": args}
            response = requests.post(url, headers=headers, json=params)
            if response.status_code != 200:
                return f"Error status: {response.status_code}"
            check_response = response.json()
            return check_response

    @staticmethod
    def get_risma_image_generator(args, api_key: str = None):
        url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/opendalle"
        headers = {"accept": "application/json", "api-key": api_key}
        payload = {"query": args}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"
        check_response = response.json()
        return check_response

    @staticmethod
    def get_dallepro_generator(args, api_key: str = None):
        url = f"https://randydev-ryuzaki-api.hf.space/ryuzaki/dalle3xl"
        headers = {"accept": "application/json", "api-key": api_key}
        payload = {"query": args}
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"
        check_response = response.json()
        return check_response
