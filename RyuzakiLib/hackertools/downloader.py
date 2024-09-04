import httpx

class Downloader:
    def __init__(self):
        pass

    def _ok(self, use_name, link):
        if use_name == "fb":
            return {"link": link}
        return {}

    async def optimized_plugins(
        self,
        use_name=None,
        json=None,
        params=None,
        with_open_files=None,
        is_get=True
    ):
        OPTIONS = {
            "fb": "https://randydev-ryuzaki-api.hf.space/akeno/fbdown",
        }
        if is_get:
            if use_name in OPTIONS:
                url = OPTIONS[use_name]
                try:
                    async with httpx.AsyncClient() as client:
                        response = await client.get(url, json=json, params=params)
                        if response.status_code == 200:
                            return response.json()
                        else:
                            return {"error": f"Failed with status code {response.status_code}"}
                except Exception as e:
                    return {"error": str(e)}
            return {"error": "Unsupported platform"}
        else:
            if use_name in OPTIONS:
                url = OPTIONS[use_name]
                try:
                    async with httpx.AsyncClient() as client:
                        response = await client.post(url, json=json, params=params)
                        if response.status_code == 200:
                            return response.json()
                        else:
                            return {"error": f"Failed with status code {response.status_code}"}
                except Exception as e:
                    return {"error": str(e)}
            return {"error": "Unsupported platform"}
