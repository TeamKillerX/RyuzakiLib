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
from pyrogram import Client
from time import sleep

def setting_telegram():
    API_ID = input("Enter your API ID: ")
    API_HASH = input("Enter your API HASH: ")
    return API_ID, API_HASH

def starting_account():
    API_ID, API_HASH = setting_telegram()
    client = Client(":memory", API_ID, API_HASH)
    return client

async def export_session_all():
    os.system("clear")
    PYROGRAM = "Pyrogram Session Generate\n"
    client = starting_account()
    try:
        from pyrogram import Client
    except:
        os.system("pip3 install -U pyrogram")
    sleep(3)
    await client.start()
    try:
        s = await client.export_session_string()
        await client.send_message("me", f"{PYROGRAM}\n\n:{s}")
        print(f"SESSION PYROGRAM:\n\n{s}")
    except:
        print("Error not responding")

asyncio.run(export_session_all())
