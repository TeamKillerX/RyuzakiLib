import asyncio
import json


class YoutubeJsonConvert:
    @staticmethod
    async def cookies_loads(file_json: str):
        with open(file_json, "r") as f:
            cookies = json.load(f)
        return cookies

    @staticmethod
    async def to_cookies(file_json: str, name_txt="cookies.txt"):
        with open(name_txt, 'w') as f:
            f.write("# Netscape HTTP Cookie File\n")
            f.write("# This is a generated file! Do not edit.\n\n")
            cookies = await YoutubeJsonConvert.cookies_loads(file_json)
            for cookie in cookies:
                f.write("\t".join([
                    cookie.get('domain', ''),
                    'TRUE' if cookie.get('hostOnly', False) else 'TRUE',
                    cookie.get('path', '/'),
                    'TRUE' if cookie.get('secure', False) else 'TRUE',
                    str(int(cookie.get('expirationDate', 0))),
                    cookie.get('name', ''),
                    cookie.get('value', ''),
                ]) + "\n")
        OUTPUT = "Successful output cookies.txt"
        return OUTPUT
