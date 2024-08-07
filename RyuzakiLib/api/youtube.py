import json

async def cookies_loads(file_json=None):
    with open(file_json, "r") as f:
        cookies = json.load(f)
    return cookies

async def cookies_convert_to_txt(file_json=None, name_txt="youtube_cookies.txt"):
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
