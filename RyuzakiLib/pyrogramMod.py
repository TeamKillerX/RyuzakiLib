from pyrogram import Client, enums


class PyrogramMod:
    @staticmethod
    async def chat_photos(client: Client, user, set_limit=None, is_limit: bool = False):
        if not isinstance(client, Client):
            raise ValueError("Invalid client instance provided")

        if is_limit and set_limit:
            async for photo in client.get_chat_photos(chat_id=user, limit=set_limit):
                yield photo
        else:
            async for photo in client.get_chat_photos(chat_id=user):
                yield photo

    @staticmethod
    async def chat_members(
        client: Client,
        chat=None,
        query=None,
        filter: enums.ChatMembersFilter = None,
        is_query: bool = False,
        is_filter: bool = False,
    ):
        if not isinstance(client, Client):
            raise ValueError("Invalid client instance provided")

        if is_query and query:
            async for member in client.get_chat_members(chat_id=chat, query=query):
                yield member
        elif is_filter and filter:
            async for member in client.get_chat_members(chat_id=chat, filter=filter):
                yield member
        else:
            async for member in client.get_chat_members(chat_id=chat):
                yield member
