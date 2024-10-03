import asyncio
import os

import aiohttp
import httpx
import requests
import wget
from fastapi import HTTPException


class DictToObj:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObj(value))
            elif isinstance(value, list):
                setattr(self, key, [DictToObj(item) if isinstance(item, dict) else item for item in value])
            else:
                setattr(self, key, value)

    def __repr__(self):
        return f"{self.__dict__}"

class AkenoPlus:
    def __init__(
        self,
        key: str = None,
        api_endpoint: str = "https://private-akeno.randydev.my.id",
        issue: bool = False,
        ip_unban=None
    ):
        self.issue = issue
        self.api_endpoint = api_endpoint
        self.headers = {"x-akeno-key": key}

        if isinstance(ip_unban, str):
            self.ip_unban = [ip_unban]
        elif isinstance(ip_unban, list):
            self.ip_unban = ip_unban
        else:
            self.ip_unban = []

    async def all_blacklist(self):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{self.api_endpoint}/blacklist/list-ip/", headers=self.headers)
                response.raise_for_status()
                return response.json()["blacklisted_ips"]
            except httpx.HTTPStatusError:
                return []
            except Exception:
                return []

    async def call_next(self, request, call_next):
        banned_ips = await self.all_blacklist()
        client_ip = request.headers.get("X-Real-IP") or request.client.host
        if self.issue and client_ip in banned_ips and client_ip not in self.ip_unban:
            raise HTTPException(status_code=403, detail="Your IP is banned.")
        response = await call_next(request)
        return response

    async def download_now(self, data):
        return wget.download(data)

    async def clean(self, file_path: str):
        try:
            os.remove(file_path)
        except OSError as e:
            return f"Error removing file {file_path}: {e}"

    async def terabox(self, link=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/terabox-v1?link={link}", headers=self.headers) as response:
                return await response.json()

    async def terabox_v2(self, link=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/terabox-v2?link={link}", headers=self.headers) as response:
                return await response.json()

    async def chatgpt_old(self, query=None):
        payload = {"query": query}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/ryuzaki/chatgpt-old", json=payload) as response:
                return await response.json()

    async def chatgpt_mode_web(self, query=None, **params):
        combined_params = {"query": query}
        combined_params.update(params)
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/api/akeno-ai-web", params=combined_params) as response:
                return await response.json()

    async def paal_see(self, files_open=None, **params):
        async with aiohttp.ClientSession() as session:
            form_data = aiohttp.FormData()
            form_data.add_field(
                'file',
                open(files_open, 'rb'),
                filename=os.path.basename(files_open),
                content_type='application/octet-stream'
            )
            async with session.post(f"{self.api_endpoint}/akeno/paal-see", data=form_data, params=params) as response:
                if response.status != 200:
                    raise Exception(f"Error occurred: {response.status}")
                return await response.json()

    async def blackbox(self, query=None):
        params = {"query": query}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/ryuzaki/blackbox", params=params, headers=self.headers) as response:
                return await response.json()

    async def hentai(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/hentai", headers=self.headers) as response:
                return await response.json()

    async def fbdown(self, link=None):
        params = {"link": link}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/fbdown-v2", params=params, headers=self.headers) as response:
                return await response.json()

    async def fdownloader(self, link=None):
        params = {"link": link}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/fdownloader", params=params, headers=self.headers) as response:
                return await response.json()

    async def capcut(self, link=None):
        params = {"link": link}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.api_endpoint}/akeno/capcut-v1", params=params, headers=self.headers) as response:
                return await response.json()

    async def add_ipblock(self, ip=None):
        params = {"ip": ip}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/add_to_blacklist_ip/", params=params, headers=self.headers_blacklist) as response:
                return await response.json()

    async def unblock_ip(self, ip=None):
        params = {"ip": ip}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/remove_from_blacklist_ip", params=params, headers=self.headers_blacklist) as response:
                return await response.json()

    async def allowed_ip(self, ip=None):
        payload = {"ip": ip}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/update_allow_ip", json=payload, headers=self.headers_blacklist) as response:
                return await response.json()

    async def unallowed_ip(self, ip=None):
        params = {"ip": ip}
        async with aiohttp.ClientSession() as session:
            async with session.delete(f"{self.api_endpoint}/remove_allow_ip/", params=params, headers=self.headers_blacklist) as response:
                return await response.json()

    async def get_json(self, response=None):
        return DictToObj(response)
