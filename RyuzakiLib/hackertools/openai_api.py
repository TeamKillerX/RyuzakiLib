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

import random
from datetime import datetime as dt
from typing import Optional

import g4f
import openai
import requests
from motor.motor_asyncio import AsyncIOMotorClient

gpt3_conversation_history = []

list_user_agent = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; BV6000_RU) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; ELUGA U3 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; U; Android 10; en-US; GM1901 Build/QKQ1.190716.003) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.14.0.1221 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-T515 Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 YaApp_Android/10.51/apad YaSearchBrowser/10.51",
    "Mozilla/5.0 (Linux; arm_64; Android 10; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 YaApp_Android/20.123.0 YaSearchBrowser/20.123.0 BroPP/1.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 9; BKL-AL20; HMSCore 5.1.1.303; GMSCore 21.02.14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 HuaweiBrowser/11.0.7.303 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; arm; Android 5.1.1; SM-J120F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 YaBrowser/20.12.3.116.00 SA/3 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2670.9 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 OPR/74.0.3911.107 (Edition 360-1)",
    "Mozilla/5.0 (Linux; Android 10; MAR-LX1B Build/HUAWEIMAR-L21B) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 SznProhlizec/7.12.2a",
]

class OpenAI:
    def __init__(
        self,
        api_key: str = "",
        api_base: str = None, #https://api.openai.com/v1
        mongo_url: str = None,
        user_id: int = None
    ):
        self.api_key = api_key
        self.api_base = api_base
        self.user_id = user_id
        self.mongo_url = mongo_url
        self.client = AsyncIOMotorClient(self.mongo_url)
        self.db = self.client.tiktokbot
        self.collection = self.db.users
        openai.api_key = self.api_key
        openai.api_base = self.api_base

    async def continue_conversation(self, user_message: str = None):
        openai_chat = await self._get_openai_chat_from_db()
        openai_chat.append({"role": "user", "content": user_message})
        try:
            response = openai.ChatCompletion.create(
                messages=openai_chat,
                model="gpt-3.5-turbo",
                timeout=1.0,
            )
            assistant_reply = response["choices"][0].message.content
            openai_chat.append({"role": "assistant", "content": assistant_reply})
            await self._update_openai_chat_in_db(openai_chat)
            return assistant_reply
        except Exception as e:
            error_msg = f"Error response: {e}"
            return error_msg

    async def _get_openai_chat_from_db(self):
        get_data_user = {"user_id": self.user_id}
        document = await self.collection.find_one(get_data_user)
        return document.get("openai_chat", []) if document else []

    async def _update_openai_chat_in_db(self, openai_chat):
        get_data_user = {"user_id": self.user_id}
        document = await self.collection.find_one(get_data_user)
        if document:
            await self.collection.update_one({"_id": document["_id"]}, {"$set": {"openai_chat": openai_chat}})
        else:
            await self.collection.insert_one({"user_id": self.user_id, "openai_chat": openai_chat})

    async def _clear_history_in_db(self):
        unset_clear = {"openai_chat": None}
        return await self.collection.update_one({"user_id": self.user_id}, {"$unset": unset_clear})

    async def message_output(self, query: str = None):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{query}\n:",
            temperature=0,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
        )
        return response

    async def chat_message_turbo(
        self,
        query: str = None,
        model: str = "gpt-3.5-turbo",
        is_stream=False
    ):
        if is_stream:
            openai_chat = await self._get_openai_chat_from_db()
            openai_chat.append({"role": "user", "content": query})
            try:
                chat_completion = openai.ChatCompletion.create(
                    model=model,
                    messages=openai_chat,
                    stream=True
                )
                if isinstance(chat_completion, dict):
                    answer = chat_completion.choices[0].message.content
                else:
                    answer = ""
                    for token in chat_completion:
                        content = token["choices"][0]["delta"].get("content")
                        if content is not None:
                            answer += content
                openai_chat.append({"role": "assistant", "content": answer})
                await self._update_openai_chat_in_db(openai_chat)
                return answer
            except Exception:
                errros_msg = f"Error responding: API long time (timeout 600)"
                return errros_msg
        else:
            openai_chat = await self._get_openai_chat_from_db()
            openai_chat.append({"role": "user", "content": query})
            try:
                chat_completion = openai.ChatCompletion.create(
                    messages=openai_chat,
                    model=model
                )
                answer = chat_completion["choices"][0].message.content
                openai_chat.append({"role": "assistant", "content": answer})
                await self._update_openai_chat_in_db(openai_chat)
                return answer
            except Exception:
                errros_msg = f"Error responding: API long time (timeout 600)"
                return errros_msg

    async def chat_message_api(
        self,
        query: str = None,
        default_url: Optional[str] = None,
        request_url: Optional[str] = None,
        user_agent: Optional[str] = None,
        _api_key: Optional[str] = None,
        bard_api_key: Optional[str] = None,
        model: str = "gpt-3.5-turbo",
        continue_conversations: Optional[list] = [],
        is_authorization: Optional[bool] = False,
        need_auth_cookies: Optional[bool] = False,
        is_different: Optional[bool] = False,
    ):
        if continue_conversations is None:
            continue_conversations = []
        if is_authorization:
            api_key = f"Bearer {_api_key}"
        else:
            api_key = ""
        selected_user_agent = random.choice(list_user_agent) or user_agent
        headers = {
            "Content-Type": "application/json",
            "Authorization": api_key,
            "User-Agent": selected_user_agent,
        }
        continue_conversations.append({"role": "user", "content": query})
        json_data = {
            "model": model,
            "messages": continue_conversations,
        }
        if is_different:
            method_url = (
                request_url + "/chat/completions"
                if request_url
                else default_url
                if default_url
                else None
            )
            response = requests.post(method_url, headers=headers, json=json_data)
            if response.status_code != 200:
                return "Error responding: API limits"
            response_data = response.json()
            if response_data:
                answer = (
                    response_data["choices"][0]["message"]["content"]
                    if response_data
                    else response_data["error"]
                )
                continue_conversations.append({"role": "assistant", "content": answer})
                return answer
            else:
                answer = "Not responding: Not Found Results"
                return answer
        else:
            if need_auth_cookies:
                selected_new_model = g4f.models.default or model
                new_response = g4f.ChatCompletion.create(
                    model=selected_new_model,
                    messages=continue_conversations,
                    provider="",
                    cookies={"__Secure-1PSID": bard_api_key},
                    auth=True,
                )
                return new_response
            else:
                answer = "Not responding: Not Found Results"
                return answer

    async def api_chat(self, query, model):
        gpt_conversation_history = []
        gpt_conversation_history.append({"role": "user", "content": query})
        try:
            chat_completion = openai.ChatCompletion.create(
                model=model,
                messages=gpt_conversation_history,
                stream=False
            )
            if isinstance(chat_completion, dict):
                answer = chat_completion.choices[0].message.content
            else:
                answer = ""
                for token in chat_completion:
                    content = token["choices"][0]["delta"].get("content")
                    if content is not None:
                        answer += content
            gpt_conversation_history.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            return f"Error requests: {e}"

    async def photo_output(self, query: str = None):
        response = openai.Image.create(prompt=query, n=1, size="1024x1024")
        return response["data"][0]["url"]

    async def client_images_generate(
        self,
        query: str = None,
        model: str = "dall-e-3",
        quality: str = "standard",
        size: str = "1024x1024",
        n: int = 1,
    ):
        chat_image_generate = openai.Image.create(
            prompt=query, model=model, quality=quality, size=size, n=n
        )
        return chat_image_generate

    async def audio_transcribe(self, file_path):
        with open(file_path, "rb") as path:
            transcript = openai.Audio.transcribe("whisper-1", path)
        return transcript
