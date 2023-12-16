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

class OpenAiToken:
    def __init__(self, api_key: str=None):
        self.api_key = api_key
        openai.api_key = self.api_key

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

    def photo_output(self, query: str=None):
        response = openai.Image.create(prompt=query, n=1, size="1024x1024")
        return response["data"][0]["url"]

    def chat_message_turbo(
        self,
        query: str=None,
        role: str="user",
        model: str="gpt-3.5-turbo"
    ):
        chat_completion = openai.ChatCompletion.create(
            messages=[{"role": role, "content": query}],
            model=model
        )
        return chat_completion

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
            quality=standard,
            size=size,
            n=n
        )
        return chat_image_generate

    def audio_transcribe(self, file_path):
        with open(file_path, "rb") as path:
            transcript = openai.Audio.transcribe("whisper-1", path)
        return transcript
