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

import openai
import requests
from pymongo import MongoClient
from datetime import datetime as dt

gpt3_conversation_history = []

class OpenAiToken:
    def __init__(
        self,
        api_key: str = None,
        api_base: str = "https://api.openai.com/v1",
        mongo_url: str = None
    ):
        self.api_key = api_key
        self.api_base = api_base
        self.mongo_url = mongo_url
        openai.api_key = self.api_key
        openai.api_base = self.api_base

    def connect_mongo(self):
        return MongoClient(self.mongo_url)["tiktokbot"]["users"]

    def continue_conversation(
        self,
        owner_author: str="Randy Dev",
        user_id: int = None,
        user_message: str = None
    ):
        collection = self.connect_mongo()
        update_data = {"chat_user_id": user_id}

        collection.update_one({"user_id": user_id}, {"$set": update_data}, upsert=True)
        user_data = collection.find_one({"user_id": user_id})
        owner_base = f"""
        Your name is {owner_author}. A kind and friendly AI assistant that answers in
        a short and concise answer. Give short step-by-step reasoning if required.

        Today is {dt.now():%A %d %B %Y %H:%M}
        """
        if user_data:
            conversation_history = user_data.get("assistant_reply")
            if conversation_history is None:
                conversation = "No conversation history available"
            else:
                conversation = conversation_history
            try:
                response = openai.ChatCompletion.create(
                    messages=[
                        {"role": "assistant", "content": "You are a helpful assistant."},
                        {"role": "user", "content": owner_base},
                        {"role": "assistant", "content": conversation},
                        {"role": "user", "content": user_message},
                    ],
                    model="gpt-3.5-turbo",
                    top_p=0.1,
                    timeout=2.5
                )
                assistant_reply = response["choices"][0].message.content
                collection.update_one(
                    {"user_id": user_id},
                    {"$push": {"conversation_history": {"user_message": user_message, "assistant_reply": assistant_reply}}}
                )
            except Exception as e:
                assistant_reply = f"Error processing request: {str(e)}"
        else:
            assistant_reply = "User not found in the database."

        return assistant_reply

    def message_output(self, query: str=None):
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

    def chat_message_turbo(
        self,
        query: str=None,
        role: str="user",
        model: str="gpt-3.5-turbo",
        is_stream=False
    ):
        global gpt3_conversation_history
        if is_stream:
            gpt3_conversation_history.append({"role": "user", "content": query})
            try:
                chat_completion = openai.ChatCompletion.create(
                    model=model,
                    messages=gpt3_conversation_history,
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
                            gpt3_conversation_history.append({"role": "assistant", "content": answer})
                return [answer, gpt3_conversation_history]
            except Exception:
                errros_msg = f"Error responding: API long time (timeout 600)"
                return [errros_msg, "https://telegra.ph//file/32f69c18190666ea96553.jpg"]
        else:
            gpt3_conversation_history.append({"role": "user", "content": query})
            try:
                chat_completion = openai.ChatCompletion.create(
                    messages=gpt3_conversation_history,
                    model=model
                )
                answer = chat_completion["choices"][0].message.content
                gpt3_conversation_history.append({"role": "assistant", "content": answer})
                return [answer, gpt3_conversation_history]
            except Exception:
                errros_msg = f"Error responding: API long time (timeout 600)"
                return [errros_msg, "https://telegra.ph//file/32f69c18190666ea96553.jpg"]

    def chat_message_api(
        self,
        query: str=None,
        default_url: str=None,
        request_url: str=None,
        user_agent: str=None,
        _api_key: str=None,
        bard_api_key: str=None,
        model: str="gpt-3.5-turbo",
        re_json: bool=False,
        is_authorization: bool=False,
        need_auth_cookies: bool=False
    ):
        global gpt3_conversation_history
        if is_authorization:
            api_key = f"Bearer {_api_key}"
        else:
            api_key = ""
        headers = {
            "Content-Type": "application/json",
            "Authorization": api_key,
            "User-Agent": user_agent
        }
        gpt3_conversation_history.append({"role": "user", "content": query})
        if need_auth_cookies:
            cookies = {"__Secure-1PSID": bard_api_key}
            json_data = {
                "model": model,
                "messages": gpt3_conversation_history,
                "cookies": cookies
            }
        else:
            json_data = {
                "model": model,
                "messages": gpt3_conversation_history,
            }
        method_url = request_url + "/chat/completions" or default_url
        response = requests.post(method_url, headers=headers, json=json_data)
        if response.status_code != 200:
            return "Error responding: API limits"
        response_data = response.json()
        if re_json:
            if response_data:
                answer = response_data["choices"][0]["message"]["content"] if response_data else response_data["error"]
                gpt3_conversation_history.append({"role": "assistant", "content": answer})
                return [answer, gpt3_conversation_history]
            else:
                answer = "Not responding: Not Found Results"
                return [answer, "https://telegra.ph//file/32f69c18190666ea96553.jpg"]
        else:
            return response_data

    def photo_output(self, query: str=None):
        response = openai.Image.create(prompt=query, n=1, size="1024x1024")
        return response["data"][0]["url"]

    def client_images_generate(
        self,
        query: str=None,
        model: str="dall-e-3",
        quality: str="standard",
        size: str="1024x1024",
        n: int=1
    ):
        chat_image_generate = openai.Image.create(
            prompt=query,
            model=model,
            quality=quality,
            size=size,
            n=n
        )
        return chat_image_generate

    def audio_transcribe(self, file_path):
        with open(file_path, "rb") as path:
            transcript = openai.Audio.transcribe("whisper-1", path)
        return transcript
