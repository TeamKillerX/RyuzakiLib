from pyrogram import Client, filters
from pyrogram.types import Message

class custom_prefixes:
    def __init__(self, name, user_id, prefix, collection):
        self.name = name 
        self.prefix = prefix
        self.user_id = user_id
        self.collection = collection
        
    def add_prefixes(self):
        add_handler = {f"{self.name}": self.prefix}
        return self.collection.update_one(
            {"user_id": self.user_id},
            {"$set": add_handler},
            upsert=True
        )
        
def get_prefix(self):
    user_data = self.collection.find_one({"user_id": self.user_id})
    return user_data.get(f"{self.name}") if user_data else None

db_name = "custom_prefixes"
user_id = message.from_user.id
prefix = [".", "+", "-"]
set_handler = custom_prefixes(db_name, user_id, prefix, collection)
set_handler.add_prefixes()
now_show_prefix = set_handler.get_prefix()
print(now_show_prefix)
