import asyncio
import logging
import os

from pyrogram import Client, filters
from pyrogram.types import Message

from buildbot.secrets.env import *

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO)

LOGS = logging.getLogger(__name__)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


if not TELEGRAM_TOKEN:
    print("Warning no bot token")

client = Client(
    "RyuzakiLib",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TELEGRAM_TOKEN,
    plugins=dict(root="buildbot.modules"),
    in_memory=True,
)
