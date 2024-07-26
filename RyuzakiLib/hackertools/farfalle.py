import json
import re
from typing import Dict, List, Optional

import requests
from pymongo import MongoClient


class FarFalle:
    """A class to interact with the FarFalle chat service.

    Attributes:
        session: A requests.Session object for making HTTP requests.
        url: The URL endpoint for the FarFalle chat service.
    """

    def __init__(
        self,
        mongo_url: Optional[str] = None,
        user_id: Optional[int] = None
    ):
        self.mongo_url = mongo_url
        self.user_id = user_id
        self.client = MongoClient(self.mongo_url)
        self.db = self.client.tiktokbot
        self.collection = self.db.users
        """Initializes the FarFalle class with a session and the service URL."""
        self.session: requests.Session = requests.Session()
        self.url: str = "https://farfalle.onrender.com/chat"

    def _close(self):
        self.client.close()

    def _get_falle_chat_from_db(self):
        user_data = self.collection.find_one({"user_id": self.user_id})
        return user_data.get("falle_chat", []) if user_data else []

    def _update_falle_chat_in_db(self, falle_chat):
        self.collection.update_one(
            {"user_id": self.user_id},
            {"$set": {"falle_chat": falle_chat}},
            upsert=True
        )

    def _clear_history_in_db(self):
        unset_clear = {"falle_chat": None}
        return self.collection.update_one({"user_id": self.user_id}, {"$unset": unset_clear})

    def clear_database(self):
        """Clear the history for the current user."""
        result = self._clear_history_in_db()
        if result.modified_count > 0:
            return "Chat history cleared successfully."
        else:
            return "No chat history found to clear."

    def generate(self, query, model: Optional[str] = 'llama-3-70b', stream: Optional[bool] = False):
        """Generates a response from the FarFalle chat service.

        Args:
            conversation_history: A list of dictionaries containing the conversation history.
            model: The model name to use for generating the response. Defaults to 'llama-3-70b'.
            stream: If True, prints the content as it arrives. Defaults to False.

        Available models: 'llama-3-70b', 'gpt-3.5-turbo', 'gpt-4o'.

        Returns:
            A tuple containing the generated response as a string and the sources as a dictionary.
        """
        conversation_history = self._get_falle_chat_from_db()
        # Prepare the payload with the extracted query and the updated conversation_history
        payload = {
            "query": query,
            "history": conversation_history,
            "model": model
        }

        content = ""
        sources = {}
        # Make the POST request and stream the response
        response = self.session.post(self.url, json=payload, stream=True)
        for line in response.iter_lines(decode_unicode=True, chunk_size=1):
            if line:
                modified_line = re.sub("data:", "", line)
                try:
                    json_data = json.loads(modified_line)
                    if not sources:
                        sources = json_data
                    content += json_data['data']['text']
                    if stream:
                        print(json_data['data']['text'], end="", flush=True)
                except: continue
        conversation_history.append({"role": "assistant", "content": content})
        self._update_falle_chat_in_db(conversation_history)
        return content, sources

    def process_sources(self, sources: dict) -> tuple[List[Dict[str, str]], List[str]]:
        """Processes the sources dictionary to extract relevant information.

        Args:
            sources: A dictionary containing the sources data.

        Returns:
            A tuple containing a list of dictionaries with title, url, and content for each result,
            and a list of image URLs.
        """
        results = []
        images = []

        for result in sources['data']['results']:
            results.append({
                'title': result['title'],
                'url': result['url'],
                'content': result['content']
            })

        images = sources['data']['images']

        return results, images
