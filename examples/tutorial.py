from pymongo import MongoClient
from pyrogram import Client, filters
from pyrogram.types import Message

from RyuzakiLib.hackertools import CustomPrefixes

client = MongoClient("mongodb://localhost:27017/")
db = client["your_database_name"]
collection = db["your_collection_name"]


def add_set_prefix(db_name, user_id, prefix, collection):
    set_handler = CustomPrefixes(db_name, user_id, prefix, collection, True)
    set_handler.add_prefixes()


def get_prefix(db_name, user_id, collection):
    set_handler = CustomPrefixes(db_name, user_id, None, collection, True)
    return set_handler.get_prefix()


@Client.on_message(filters.command("setprefix", prefixes=".") & filters.me)
async def set_prefix(client, message):
    user_id = message.from_user.id
    setprefix = message.command[1] if len(message.command) > 1 else None
    if not setprefix:
        return
    add_set_prefix("handler", user_id, setprefix, collection)
    await message.reply_text(f"Successfully changed to {setprefix}")


@Client.on_message(filters.text & filters.me)
async def get_current_prefix(client, message):
    user_id = message.from_user.id
    current_prefix = get_prefix("handler", user_id, collection)
    if message.text.lower() == f"{current_prefix}ping":
        await message.reply_text("Pong!!........")
        return
