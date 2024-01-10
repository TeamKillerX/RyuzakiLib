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

import requests
from pymongo import MongoClient


class GeminiLatest:
    def __init__(
        self,
        api_key: str = None,
        mongo_url: str=None,
        api_base="https://generativelanguage.googleapis.com",
        user_id: int=None
    ):
        self.api_key = api_key
        self.api_base = api_base
        self.user_id = user_id
        self.mongo_url = mongo_url
        self.client = MongoClient(self.mongo_url)
        self.db = self.client.tiktokbot
        self.collection = self.db.users

    def __del__(self):
        self.client.close()

    def _get_response_gemini(self, query: str = None):
        try:
            gemini_chat = self._get_gemini_chat_from_db()

            gemini_chat.append({"role": "user", "parts": [{"text": query}]})
            api_method = f"{self.api_base}/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
            headers = {"Content-Type": "application/json"}
            payload = {"contents": gemini_chat}
            response = requests.post(api_method, headers=headers, json=payload)

            if response.status_code != 200:
                return "Error responding", gemini_chat

            response_data = response.json()
            answer = response_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")

            gemini_chat.append({"role": "model", "parts": [{"text": answer}]})
            self._update_gemini_chat_in_db(gemini_chat)
            return answer, gemini_chat
        except Exception as e:
            error_msg = f"Error response: {e}"
            return error_msg, gemini_chat

    def _get_gemini_chat_from_db(self):
        get_data_user = {"user_id": self.user_id}
        document = self.collection.find_one(get_data_user)
        return document.get("gemini_chat", []) if document else []

    def _update_gemini_chat_in_db(self, gemini_chat):
        get_data_user = {"user_id": self.user_id}
        document = self.collection.find_one(get_data_user)
        if document:
            self.collection.update_one({"_id": document["_id"]}, {"$set": {"gemini_chat": gemini_chat}})
        else:
            self.collection.insert_one({"user_id": self.user_id, "gemini_chat": gemini_chat})
