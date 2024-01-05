from typing import Tuple, Union

from pyrogram import Client, filters
from pyrogram.types import Message


class ChannelCopy:
    def __init__(self, client: Client, chat_id: Union[str, int] = None):
        self.client = client
        self.chat_id = chat_id

    async def download(
        self, message_id: int = None, faster: bool = False, to_forward: bool = False
    ) -> Union[Tuple[str, str], Message, str]:
        try:
            if faster:
                processed = await self.client.get_messages(
                    chat_id=self.chat_id, message_ids=message_id
                )
                photo_or_video = await processed.download()
                return [photo_or_video, processed.caption]
            elif to_forward:
                processed = await self.client.get_messages(
                    chat_id=self.chat_id, message_ids=message_id
                )
                return await processed.forward(self.chat_id)
            else:
                return "Please use required to_forward: boolean"
        except Exception as e:
            return f"Error: {e}"
