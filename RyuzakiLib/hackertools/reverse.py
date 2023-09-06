from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import json
from serpapi import GoogleSearch

class GoogleRevergeImage:
    def __init__(self, image_url, apikey):
        self.image_url = image_url
        self.apikey = apikey

    def get_reverse(self):
        params = {
            "api_key": self.apikey,
            "engine": "google_reverse_image",
            "image_url": self.image_url, 
            "hl": "en",
            "gl": "us"
        }
        search = GoogleSearch(params) # where data extraction happens on the SerpApi backend
        results = search.get_dict() # JSON -> Python dictionary
        return results

"""
example
apikey = "..."
image_url = "..."
check = GoogleRevergeImage(image_url, apikey)
results = check.get_reverse()
print(results)

parameter 
google_url = results["search_metadata"]["google_reverse_image"]
"""

    
