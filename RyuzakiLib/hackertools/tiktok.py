import requests


class Tiktok:
    @staticmethod
    async def download(api_name, url):
        response = requests.get("{}/api/?url={}".format(api_name, url))
        if response.status_code != 200:
            return "Error Response limits"
        data_json = response.json()
        author_tiktok = data_json["data"]["author"].get("nickname") or "Unknown"
        play_tiktok = data_json["data"].get("play")
        music_tiktok = data_json["data"]["music_info"].get("play")
        return [
            play_tiktok,
            music_tiktok,
            author_tiktok
        ]
