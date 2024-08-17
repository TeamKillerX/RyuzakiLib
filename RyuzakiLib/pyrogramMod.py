from pyrogram import Client

class PyorgramMod:
    @staticmethod
    async def chat_photos(client: Client, user):
        if isinstance(client, Client):
            async for photo in client.get_chat_photos(user):
                return photo
