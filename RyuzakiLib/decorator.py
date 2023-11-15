from pyrogram import Client, filters
from pyrogram.types import Message

class RyuzakiPowers:
    def __init__(self):
        pass

    def ryuzaki_ban(self, blacklist: list, func):
        def wrapper(client, message):
            user_id = message.from_user.id if message.from_user else None
            if user_id in blacklist:
                return f"User {user_id} is banned."
            else:
                return func(client, message)
        return wrapper

    def ryuzaki_owner(self, user: int = None, sudo: bool = None):
        def wrapper(client, message):
            if sudo:
                user_id = message.from_user.id if message.from_user else None
                if user_id != user:
                    return func(client, message)
                else:
                    return "Only Developed"
            else:
                return "Something error"
        return wrapper
