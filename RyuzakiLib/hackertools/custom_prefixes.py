from pyrogram import Client, filters
from pyrogram.types import Message

class custom_prefixes:
    def __init__(self, name, user_id, prefix, collection, value: bool):
        self.name = name 
        self.prefix = prefix
        self.user_id = user_id
        self.collection = collection
        self.value = value
        
    def add_prefixes(self):
        add_handler = {f"{self.name}": self.prefix}
        return self.collection.update_one(
            {"user_id": self.user_id},
            {"$set": add_handler},
            upsert=self.value
        )
    def get_prefix(self):
        user_data = self.collection.find_one({"user_id": self.user_id})
        return user_data.get(f"{self.name}") if user_data else None
