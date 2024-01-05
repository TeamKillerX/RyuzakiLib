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

from pyrogram import Client, filters
from pyrogram.types import Message


class TelegramUserInfo:
    def __init__(self, info_id):
        self.info_id = info_id

    async def who_is(self, client: Client):
        try:
            user = await client.get_users(self.info_id)
            username = f"@{user.username}" if user.username else "-"
            first_name = f"{user.first_name}" if user.first_name else "-"
            last_name = f"{user.last_name}" if user.last_name else "-"
            fullname = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
            user_details = (await client.get_chat(user.id)).bio
            bio = f"{user_details}" if user_details else "-"
            h = f"{user.status}"
            if h.startswith("UserStatus"):
                y = h.replace("UserStatus.", "")
                status = y.capitalize()
            else:
                status = "-"
            dc_id = f"{user.dc_id}" if user.dc_id else "-"
            common = await client.get_common_chats(user.id)
            out_str = f"""<b>USER INFORMATION:</b>
🆔 <b>User ID:</b> <code>{user.id}</code>
👤 <b>First Name:</b> {first_name}
🗣️ <b>Last Name:</b> {last_name}
🌐 <b>Username:</b> {username}
🏛️ <b>DC ID:</b> <code>{dc_id}</code>
🤖 <b>Is Bot:</b> <code>{user.is_bot}</code>
🚷 <b>Is Scam:</b> <code>{user.is_scam}</code>
🚫 <b>Restricted:</b> <code>{user.is_restricted}</code>
✅ <b>Verified:</b> <code>{user.is_verified}</code>
⭐ <b>Premium:</b> <code>{user.is_premium}</code>
📝 <b>User Bio:</b> {bio}

👀 <b>Same groups seen:</b> {len(common)}
👁️ <b>Last Seen:</b> <code>{status}</code>
🔗 <b>User permanent link:</b> <a href='tg://user?id={user.id}'>{fullname}</a>
"""
            photo_id = user.photo.big_file_id if user.photo else None
            if photo_id:
                photo = await client.download_media(photo_id)
                return [photo, out_str]
            else:
                return out_str
        except Exception as e:
            return f"INFO: {e}"
