import json
import asyncio

class Youtube:
    @staticmethod
    async def cookies_loads(file_json=None):
        with open(file_json, "r") as f:
            cookies = json.load(f)
        return cookies

    @staticmethod
    async def download(file_json=None, url: str, name_txt="youtube_cookies.txt"):
        with open('youtube_cookies.txt', 'w') as f:
            f.write("# Netscape HTTP Cookie File\n")
            f.write("# This is a generated file! Do not edit.\n\n")
            cookies = await cookies_loads(file_json)
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
        cmd = f"yt-dlp --cookies youtube_cookies.txt {url}"
        process = await asyncio.create_subprocess_shell(
        cmd, stdout = asyncio.subprocess.PIPE, stderr = asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        e = stderr.decode()
        if not e:
            e = "No errors"
        o = stdout.decode()
        if not o:
            o = "No output"
        OUTPUT = ""
        OUTPUT += f"<b>Output</b>: \n<code>{o}</code>\n"
        OUTPUT += f"<b>Errors</b>: \n<code>{e}</code>"
        return OUTPUT
