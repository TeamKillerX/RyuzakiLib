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
                assistant_reply = response["choices"][0]["message"]["content"]
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
        return response.choices[0].text

    def chat_message_turbo(
        self,
        query: str=None,
        role: str="user",
        model: str="gpt-3.5-turbo"
    ):
        chat_completion = openai.ChatCompletion.create(
            messages=[{"role": role, "content": query}],
            model=model,
            top_p=0.1,
            timeout=2.5
        )
        return chat_completion

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
