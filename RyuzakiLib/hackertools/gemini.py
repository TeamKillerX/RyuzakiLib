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

import os

import google.generativeai as genai
import requests
from pymongo import MongoClient


class GeminiLatest:
    def __init__(
        self,
        api_keys: str = None,
        mongo_url: str = None,
        model: str = "gemini-1.5-flash-latest",
        user_id: int = None
    ):
        self.api_keys = api_keys
        self.model = model
        self.user_id = user_id
        self.mongo_url = mongo_url
        self.client = MongoClient(self.mongo_url)
        self.db = self.client.tiktokbot
        self.collection = self.db.users

        genai.configure(api_key=self.api_keys)

    def _close(self):
        self.client.close()

    def _get_gemini_chat_from_db(self):
        user_data = self.collection.find_one({"user_id": self.user_id})
        return user_data.get("gemini_chat", []) if user_data else []

    def _update_gemini_chat_in_db(self, gemini_chat):
        self.collection.update_one(
            {"user_id": self.user_id},
            {"$set": {"gemini_chat": gemini_chat}},
            upsert=True
        )

    def _clear_history_in_db(self):
        unset_clear = {"gemini_chat": None}
        return self.collection.update_one({"user_id": self.user_id}, {"$unset": unset_clear})

    def __get_response_gemini(self, query: str = None):
        try:
            generation_config = {
                "temperature": 1,
                "top_p": 0.95,
                "top_k": 64,
                "max_output_tokens": 8192,
                "response_mime_type": "text/plain",
            }
            model_flash = genai.GenerativeModel(
                model_name=self.model,
                generation_config=generation_config,
            )
            gemini_chat = self._get_gemini_chat_from_db()
            gemini_chat.append({"role": "user", "parts": [{"text": query}]})
            chat_session = model_flash.start_chat(history=gemini_chat)

            response_data = chat_session.send_message(query)
            answer = response_data.text
            gemini_chat.append({"role": "model", "parts": [{"text": answer}]})
            self._update_gemini_chat_in_db(gemini_chat)
            return answer, gemini_chat
        except Exception as e:
            error_msg = f"Rate limit exceeded after multiple attempts."
            return error_msg, gemini_chat
