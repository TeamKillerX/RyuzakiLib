import os

import httpx
import requests


class Downloader:
    def __init__(self):
        pass

    def _ok(self, use_name=None, link=None):
        if use_name == "fb":
            return {"link": link}
        return {}

    async def with_download(self, open_files=None, response_url=None):
        try:
            response = requests.get(response_url).content
            with open(open_files, "wb") as f:
                f.write(response)
        except Exception as e:
            return f"Error: {e}"
        finally:
            os.remove(open_files)

    def with_(self, open_files=None):
        with open(open_files, "rb") as file:
            files = {"file": file}
            return files

    async def optimized_plugins(
        self,
        use_name=None,
        json=None,
        params=None,
        files=None,
        is_get=True
    ):
        OPTIONS = {
            "fb": "https://randydev-ryuzaki-api.hf.space/akeno/fbdown",
            "graph": "https://akeno.randydev.my.id/uploadfile/"
        }
        if is_get:
            if use_name in OPTIONS:
                url = OPTIONS[use_name]
                try:
                    async with httpx.AsyncClient() as client:
                        request_args = {}
                        if json is not None:
                            request_args["json"] = json
                        if params is not None:
                            request_args["params"] = params
                        if files is not None:
                            request_args["files"] = files
                        response = await client.get(url, **request_args)
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
                        request_args = {}
                        if json is not None:
                            request_args["json"] = json
                        if params is not None:
                            request_args["params"] = params
                        if files is not None:
                            request_args["files"] = files
                        response = await client.post(url, **request_args)
                        if response.status_code == 200:
                            return response.json()
                        else:
                            return {"error": f"Failed with status code {response.status_code}"}
                except Exception as e:
                    return {"error": str(e)}
            return {"error": "Unsupported platform"}
