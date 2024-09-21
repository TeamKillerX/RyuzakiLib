import asyncio
import os

import aiohttp
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
    def __init__(self, key: str, issue: bool = False, ip_unban=None):
        self.issue = issue
        self.api_endpoint = "https://akeno.randydev.my.id"
        self.headers = {"x-akeno-key": key}
        self.headers_blacklist = {"x-blacklist-key": key}

        if isinstance(ip_unban, str):
            self.ip_unban = [ip_unban]
        elif isinstance(ip_unban, list):
            self.ip_unban = ip_unban
        else:
            self.ip_unban = []

    def all_blacklist(self):
        response = requests.get("https://akeno.randydev.my.id/blacklist/list-ip/").json()
        return response["blacklisted_ips"]

    async def call_next(self, request, call_next):
        banned_ips = self.all_blacklist()
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
        payload={"query": query}
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.api_endpoint}/ryuzaki/chatgpt-old", json=payload, headers=self.headers) as response:
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
