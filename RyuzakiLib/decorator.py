from typing import Union

from pyrogram import Client, filters
from pyrogram.types import Message


class RyuzakiPowers:
    def __init__(self):
        pass

    def ryuzaki_ban(self, blacklist: Union[int, list] = None, func=None):
        def wrapper(client: Client, message: Message):
            user_id = message.from_user.id if message.from_user else None
            if user_id in blacklist:
                return f"User {user_id} is banned."
            else:
                return func(client, message)

        return wrapper

    def ryuzaki_owner(self, user: Union[int, list] = None, sudo: bool = None, func=None):
        def wrapper(client: Client, message: Message):
            if sudo:
                user_id = message.from_user.id if message.from_user else None
                if user_id != user:
                    return func(client, message)
                else:
                    return "Only Developed"
            else:
                return "Something error"

        return wrapper
