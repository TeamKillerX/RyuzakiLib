import requests

class SibylBan:
    def __init__(self):
        pass

    async def add_ban(user_id: int=None, reason: str=None, is_banned: bool=False):
        if is_banned:
            url = f"https://private.randydev.my.id/ryuzaki/sibylban?user_id={user_id}&reason={reason}"
            try:
                response = requests.post(url).json()
                if response.status_code != 200:
                    return f"Error Request: {response.status_code}"
                message = response["randydev"]["message"] if response else response["message"]
                return message
            except Exception as e:
                return f"Error: {e}"
        else:
            return "Error required is_banned=True"

    async def get_ban(user_id: int=None, banlist: bool=False):
        if banlist:
            url = f"https://private.randydev.my.id/ryuzaki/sibyl?user_id={user_id}"
            try:
                response = requests.get(url).json()
                if response.status_code != 200:
                    return f"Error Request: {response.status_code}"
                return response
            except Exception as e:
                return f"Error: {e}"
        else:
            return "Error required banlist=True"
