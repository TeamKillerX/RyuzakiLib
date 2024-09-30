import requests

from RyuzakiLib.api.reqs import AsyicXSearcher


class FluxAi:
    @staticmethod
    async def schellwithflux(args: str):
        API_URL = "https://private-akeno.randydev.my.id/akeno/fluxai"
        payload = {
            "args": args
        }
        response = requests.post(API_URL, json=payload)
        return response.content
