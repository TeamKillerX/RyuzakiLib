# Credits @xtdevs
# Code updated 2024

from datetime import datetime as dt

from huggingface_hub import InferenceClient
from pymongo import MongoClient


class BetaRag:
    def __init__(
        self,
        clients_name: str = b"\xff\xfeH\x00u\x00g\x00g\x00i\x00n\x00g\x00F\x00a\x00c\x00e\x00H\x004\x00/\x00z\x00e\x00p\x00h\x00y\x00r\x00-\x007\x00b\x00-\x00b\x00e\x00t\x00a\x00",
        token: str = None,
        user_id: str = None,
        mongo_url: str = None
    ):
        self.clients_name = clients_name
        self.token = token
        self.user_id = user_id
        self.mongo_url = mongo_url
        self.client = MongoClient(self.mongo_url)
        self.db = self.client.tiktokbot
        self.collection = self.db.users

    def _get_rag_chat_from_db(self):
        get_data_user = {"user_id": self.user_id}
        document = self.collection.find_one(get_data_user)
        return document.get("rag_chat", []) if document else []

    def _update_rag_chat_in_db(self, rag_chat):
        get_data_user = {"user_id": self.user_id}
        document = self.collection.find_one(get_data_user)
        if document:
            self.collection.update_one({"_id": document["_id"]}, {"$set": {"rag_chat": rag_chat}})
        else:
            self.collection.insert_one({"user_id": self.user_id, "rag_chat": rag_chat})

    def _clear_history_in_db(self):
        unset_clear = {"rag_chat": None}
        return self.collection.update_one({"user_id": self.user_id}, {"$unset": unset_clear})

    def rag_chat(self, args):
        try:
            rag_chat = self._get_rag_chat_from_db()
            rag_chat.append({"role": "user", "content": args})
            client_face = InferenceClient(
                self.clients_name.decode("utf-16"),
                token=self.token
            )
            answer = ""
            for message in client_face.chat_completion(
                messages=rag_chat,
                max_tokens=500,
                stream=True
            ):
                content = message.choices[0].delta.content
                answer += content
            rag_chat.append({"role": "assistant", "content": answer})
            self._update_rag_chat_in_db(rag_chat)
            return answer
        except Exception:
            errros_msg = f"Error responding: API long time (timeout 600)"
            return errros_msg
