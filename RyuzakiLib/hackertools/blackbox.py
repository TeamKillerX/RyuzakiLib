import json
import urllib
from base64 import b64decode as m

import requests


class Blackbox:
    def __init__(self) -> None:
        """API Class for various purposes"""
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
            "Content-Type": m("YXBwbGljYXRpb24vanNvbg==").decode("utf-8"),
            "Cookie": m("c2Vzc2lvbklkPWY3N2E5MWUxLWNiZTEtNDdkMC1iMTM4LWMyZTIzZWViNWRjZjtpbnRlcmNvbS1pZC1qbG1xeGljYj00Y2YwN2RkOC03NDJlLTRlM2YtODFkZS0zODY2OTgxNmQzMDA7aW50ZXJjb20tZGV2aWNlLWlkLWpsbXF4aWNiPTFlYWZhYWNiLWYxOGQtNDAyYS04MjU1LWI3NjNjZjM5MGRmNjtpbnRlcmNvbS1zZXNzaW9uLWpsbXF4aWNiPQ==").decode("utf-8"),
            "Origin": m("aHR0cHM6Ly93d3cuYmxhY2tib3guYWk=").decode("utf-8"),
            "User-Agent": m("TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCBsaWtlIEdlY2tvKUNocm9tZS8xMjEuMC4wLjAgU2FmYXJpLzUzNy4zNg==").decode("utf-8"),
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            clean_text = response.text.replace("$@$v=undefined-rv1$@$", "")

            split_text = clean_text.split("\n\n", 2)

            if len(split_text) >= 3:
                content_after_second_newline = split_text[2]
            else:
                content_after_second_newline = ""

            return {"answer": content_after_second_newline, "success": True}

        except requests.exceptions.RequestException as e:
            return {"results": str(e), "success": False}

# EXAMPLE
# response = Blackbox.chat("What is today's date?")
# print(response.get("answer"))
