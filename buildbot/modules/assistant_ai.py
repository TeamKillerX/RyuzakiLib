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

from pyrogram import *
from pyrogram import Client, filters
from pyrogram.types import *
from pyrogram.types import Message

from RyuzakiLib.extreme.chatbot import ChatbotAi


@Client.on_message(filters.text & filters.private)
async def chatbot_assistant(client: Client, message: Message):
    if message.text:
        text = message.text
        chat_id = message.chat.id
        user_id = message.from_user.id
        try:
            code = ChatbotAi(query=text, user_id=user_id)
            response = code.get_response_ai()
            await client.send_message(chat_id, text=response, reply_to_message_id=message.id)
        except Exception as e:
            await message.reply_text(str(e))
            return
