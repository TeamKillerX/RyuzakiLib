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

from typing import Union

import requests


class API:
    def __init__(self, bot_token: str = None):
        self.bot_token = bot_token

    def telegram(self, method):
        url = f"https://api.telegram.org/bot{self.bot_token}/{method}"
        return url

    def get_me(self, re_json: bool = False):
        urls = self.telegram("getMe")
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        }
        if re_json:
            response = requests.post(urls, headers=headers).json()
            return response
        else:
            response = requests.post(urls, headers=headers)
            return response

    def forward_message(
        self,
        chat_id: Union[str, int] = None,
        from_chat_id: Union[str, int] = None,
        disable_notification: bool = False,
        message_id: int = None,
        re_json: bool = False,
    ):
        urls = self.telegram("forwardMessage")
        payload = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id,
            "disable_notification": disable_notification,
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json",
        }
        if re_json:
            response = requests.post(urls, json=payload, headers=headers).json()
            return response
        else:
            response = requests.post(urls, json=payload, headers=headers)
            return response

    def send_photo(
        self,
        chat_id: Union[str, int] = None,
        photo: Union[str, None] = None,
        caption: str = None,
        disable_notification: bool = False,
        reply_to_message_id: int = None,
    ):
        urls = self.telegram("sendPhoto")
        payload = {
            "chat_id": chat_id,
            "photo": photo,
            "caption": caption,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id,
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json",
        }
        if re_json:
            response = requests.post(urls, json=payload, headers=headers).json()
            return response
        else:
            response = requests.post(urls, json=payload, headers=headers)
            return response

    def send_audio(
        self,
        chat_id: Union[str, int] = None,
        audio: Union[str, None] = None,
        duration: int = None,
        performer=None,
        track=None,
        disable_notification: bool = False,
        reply_to_message_id: int = None,
        re_json: bool = False,
    ):
        urls = self.telegram("sendAudio")
        payload = {
            "chat_id": chat_id,
            "audio": audio,
            "duration": duration,
            "performer": performer,
            "track": track,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id,
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json",
        }
        if re_json:
            response = requests.post(urls, json=payload, headers=headers)
            return response
        else:
            response = requests.post(urls, json=payload, headers=headers)
            return response

    def send_document(
        self,
        chat_id: Union[str, int] = None,
        document: Union[str, None] = None,
        caption: str = None,
        disable_notification: bool = False,
        reply_to_message_id: int = None,
        re_json: bool = False,
    ):
        urls = self.telegram("sendDocument")
        payload = {
            "chat_id": chat_id,
            "document": document,
            "caption": caption,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id,
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json",
        }
        if re_json:
            response = requests.post(urls, json=payload, headers=headers)
            return response
        else:
            response = requests.post(urls, json=payload, headers=headers)
            return response

    def send_sticker(
        self,
        chat_id: Union[str, int] = None,
        sticker: Union[str, None] = None,
        caption: str = None,
        disable_notification: bool = False,
        reply_to_message_id: int = None,
        re_json: bool = False,
    ):
        urls = self.telegram("sendSticker")
        payload = {
            "chat_id": chat_id,
            "sticker": sticker,
            "caption": caption,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id,
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json",
        }
        if re_json:
            response = requests.post(urls, json=payload, headers=headers)
            return response
        else:
            response = requests.post(urls, json=payload, headers=headers)
            return response

    def send_message(
        self,
        chat_id: Union[str, int] = None,
        text: str = None,
        disable_web_page_preview: bool = False,
        disable_notification: bool = False,
        reply_to_message_id: int = None,
        re_json: bool = False,
    ):
        urls = self.telegram("sendMessage")
        payload = {
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": disable_web_page_preview,
            "disable_notification": disable_notification,
            "reply_to_message_id": reply_to_message_id,
            "chat_id": chat_id,
        }
        headers = {
            "accept": "application/json",
            "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
            "content-type": "application/json",
        }
        if re_json:
            response = requests.post(urls, json=payload, headers=headers).json()
            return response
        else:
            response = requests.post(urls, json=payload, headers=headers)
            return response
