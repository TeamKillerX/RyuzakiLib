from pyrogram import Client

class PyorgramMod:
    @staticmethod
    async def chat_photos(client: Client, user, is_limit: bool = False, set_limit=None):
        if isinstance(client, Client):
            if is_limit:
                async for photo in client.get_chat_photos(chat_id=user):
                    return photo
            else:
                async for photo in client.get_chat_photos(chat_id=user, limit=set_limit):
                    return photo
