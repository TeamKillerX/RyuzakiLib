# Credits @xtdevs
# Code updated 2024

from datetime import datetime as dt

from huggingface_hub import InferenceClient
from motor.motor_asyncio import AsyncIOMotorClient


class FaceAI:
    def __init__(
        self,
        clients_name: str = "microsoft/Phi-3-mini-4k-instruct",
        token: str = None,
        user_id: str = None,
        mongo_url: str = None
    ):
        self.clients_name = clients_name
        self.token = token
        self.user_id = user_id
        self.mongo_url = mongo_url
        self.client = AsyncIOMotorClient(self.mongo_url)
        self.db = self.client.tiktokbot
        self.collection = self.db.users

    async def _get_rag_chat_from_db(self):
        get_data_user = {"user_id": self.user_id}
        document = await self.collection.find_one(get_data_user)
        return document.get("rag_chat", []) if document else []

    async def _update_rag_chat_in_db(self, rag_chat):
        get_data_user = {"user_id": self.user_id}
        document = self.collection.find_one(get_data_user)
        if document:
            self.collection.update_one({"_id": document["_id"]}, {"$set": {"rag_chat": rag_chat}})
        else:
            self.collection.insert_one({"user_id": self.user_id, "rag_chat": rag_chat})

    async def _clear_history_in_db(self):
        unset_clear = {"rag_chat": None}
        return await self.collection.update_one({"user_id": self.user_id}, {"$unset": unset_clear})

    async def chat(self, args, no_db=False):
        try:
            client_face = InferenceClient(
                self.clients_name,
                token=self.token
            )
            if no_db:
                answer = ""
                for messages in client_face.chat_completion(
                    messages=[{"role": "user", "content": args}],
                    max_tokens=500,
                    stream=True
                ):
                    answer += messages.choices[0].delta.content
                return answer
            else:
                rag_chat = await self._get_rag_chat_from_db()
                rag_chat.append({"role": "user", "content": args})
                answer = ""
                for messages in client_face.chat_completion(
                    messages=rag_chat,
                    max_tokens=500,
                    stream=True
                ):
                    answer += messages.choices[0].delta.content
                rag_chat.append({"role": "assistant", "content": answer})
                await self._update_rag_chat_in_db(rag_chat)
                return answer
        except:
            pass
