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

import asyncio
import os
from time import sleep

import telethon
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


def setting_telegram():
    API_ID = input("Enter your API ID: ")
    API_HASH = input("Enter your API HASH: ")
    return API_ID, API_HASH


async def starting_account():
    API_ID, API_HASH = setting_telegram()
    with TelegramClient(StringSession(), API_ID, API_HASH) as ubot:
        return ubot


async def export_session_all():
    os.system("clear")
    TELETHON = "Telethon Session Generate\n"
    try:
        from telethon.sync import TelegramClient
    except ImportError:
        print("Telethon library not found. Installing...")
        await asyncio.sleep(3)
        try:
            await asyncio.to_thread(lambda: os.system("pip3 install -U telethon"))
            print("Telethon library installed successfully.")
        except:
            print("Error installing Telethon library.")
            return
    ubot = await starting_account()
    try:
        s = ubot.session.save()
        await ubot.send_message("me", f"{TELETHON}\n\n{s}")
        print(f"SESSION TELETHON:\n\n{s}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await ubot.stop()


if __name__ == "__main__":
    asyncio.run(export_session_all())
