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


@Client.on_message(filters.command("start"))
async def startwb(client: Client, message: Message):
    text = "Welcome to Ryuzaki Library"
    keyboard = [[InlineKeyboardButton(text="Ryuzaki Library", url="https://docs.randydev.my.id")]]
    bttn = InlineKeyboardMarkup(keyboard)
    try:
        await client.send_message(
            message.chat.id,
            text=text,
            reply_markup=bttn,
            reply_to_message_id=message.id,
        )
    except Exception as e:
        await message.reply_text(str(e))
        return
