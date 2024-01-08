import asyncio
import importlib

from pyrogram import Client, idle

from buildbot import client


async def start_bot():
    try:
        await client.start()
        ur = await client.get_me()
        print(f"Started {ur.first_name}")
    except Exception as e:
        print(f"{e}")
    await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
