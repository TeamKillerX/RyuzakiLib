from pyrogram import Client, filters
from pyrogram.types import Message

class set_prefixes:
    def __init__(self, user_id, prefix, collection):
        self.prefix = prefix
        self.user_id = user_id
        self.collection = collection
        
    def add_prefixes(self):
        add_handler = {"handler": self.prefix}
        return self.collection.update_one(
            {"user_id": self.user_id},
            {"$set": add_handler},
            upsert=True
        )
