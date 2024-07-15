#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>

from typing import List, Optional, Union

import requests

class SibylBan:
    @staticmethod
    def connect():
        return "c0e7a3275bebac9a833ecc55e6eeb6dbe51d67578e3d60728ac371f98924c2e3"
        
    @staticmethod
    def _make_request(method: str, url: str, params: dict = None, json_data: dict = None):
        new_api_key = SibylBan.connect()
        headers = {"accept": "application/json", "api-key": new_api_key}
        try:
            response = requests.request(
                method, url, headers=headers, params=params, json=json_data
            )
            response.raise_for_status()  # Raise an error for bad status codes
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    @staticmethod
    def ban(user_id: int = None, reason: str = None) -> str:
        url = "https://randydev-ryuzaki-api.hf.space/sibylban"
        payload = {"user_id": user_id, "reason": reason}
        response = SibylBan._make_request("POST", url, json_data=payload)
        return response.get("randydev", {}).get(
            "message", response.get("message", "Unknown error")
        )

    @staticmethod
    def banlist(user_id: int = None) -> Union[dict, str]:
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/sibyl"
        payload = {"user_id": user_id}
        return SibylBan._make_request("GET", url, json_data=payload)

    @staticmethod
    def unban(user_id: int = None) -> Union[dict, str]:
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/sibyldel"
        payload = {"user_id": user_id}
        return SibylBan._make_request("DELETE", url, json_data=payload)

    @staticmethod
    def banlist_all() -> Union[dict, str]:
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/getbanlist"
        return SibylBan._make_request("GET", url)
