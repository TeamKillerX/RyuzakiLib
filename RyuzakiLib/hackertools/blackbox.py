import random
import urllib
from base64 import b64decode as m

import requests


class blackbox:

    def __init__(self) -> None:
        """API Class for various purpose"""
        pass

    @staticmethod
    def chat(args: str) -> dict:
        url = m("aHR0cHM6Ly93d3cuYmxhY2tib3guYWkvYXBpL2NoYXQ=").decode("utf-8")

        payload = {
            "agentMode": {},
            "codeModelMode": True,
            "id": "XM7KpOE",
            "isMicMode": False,
            "maxTokens": None,
            "messages": [
                {"id": "XM7KpOE", "content": urllib.parse.unquote(args), "role": "user"}
            ],
            "previewToken": None,
            "trendingAgentMode": {},
            "userId": "87cdaa48-cdad-4dda-bef5-6087d6fc72f6",
            "userSystemPrompt": None,
        }

        headers = {
            "Content-Type": "application/json",
            "Cookie": "sessionId=f77a91e1-cbe1-47d0-b138-c2e23eeb5dcf; intercom-id-jlmqxicb=4cf07dd8-742e-4e3f-81de-38669816d300; intercom-device-id-jlmqxicb=1eafaacb-f18d-402a-8255-b763cf390df6; intercom-session-jlmqxicb=",
            "Origin": m("aHR0cHM6Ly93d3cuYmxhY2tib3guYWk=").decode("utf-8"),
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        }
        try:
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                clean_text = response.text.replace("$@$v=undefined-rv1$@$", "")
                return {"results": clean_text, "success": True}
        except Exception as e:
            return {"results": str(e), "success": False}

#EXAMPLE
#response = blackbox.chat("Hello, how are you?")
#print(response)
