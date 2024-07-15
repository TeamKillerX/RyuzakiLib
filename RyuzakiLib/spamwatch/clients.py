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
    def __init__(self: str) -> None:
        pass

    def _make_request(method: str, url: str, params: dict = None, json_data: dict = None):
        headers = {"accept": "application/json", "api-key": ""}
        try:
            response = requests.request(
                method, url, headers=headers, params=params, json=json_data
            )
            return response.json()
        except requests.RequestException:
            pass

    def ban(user_id: int = None, reason: str = None) -> str:
        url = "https://randydev-ryuzaki-api.hf.space/sibylban"
        payload = {"user_id": user_id, "reason": reason}
        response = _make_request("POST", url, json_data=payload)
        return response.get("randydev", {}).get(
            "message", response.get("message", "Unknown error")
        )

    def banlist(user_id: int = None) -> Union[dict, str]:
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/sibyl"
        payload = {"user_id": user_id}
        return _make_request("GET", url, json_data=payload)
    
    def unban(user_id: int = None) -> Union[dict, str]:
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/sibyldel"
            payload = {"user_id": user_id}
            return _make_request("DELETE", url, json_data=payload)

    def banlist_all() -> Union[dict, str]:
        url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/getbanlist"
        return _make_request("GET", url)
