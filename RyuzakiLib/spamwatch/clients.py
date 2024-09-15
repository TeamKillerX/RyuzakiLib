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
    def _make_request(method: str, url: str, params: dict = None, json_data: dict = None):
        headers = {"accept": "application/json", "api-key": "6398769dabd9fe0e49bedce0354b40a9b1a69d9594dc9d48c1d8a2a071c51e89"}
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
    def ban(api_key: str = None, user_id: int = None, reason: str = None, is_working_dev=True) -> str:
        if is_working_dev:
            url = f"https://akeno.randydev.my.id/sibylban?api_key={api_key}"
        else:
            url = "https://randydev-ryuzaki-api.hf.space/sibylban"
        payload = {"user_id": user_id, "reason": reason}
        response = SibylBan._make_request("POST", url, json_data=payload)
        return response.get("randydev", {}).get(
            "message", response.get("message", "Unknown error")
        )

    @staticmethod
    def banlist(api_key: str = None, user_id: int = None, is_working_dev=True) -> Union[dict, str]:
        if is_working_dev:
            url = f"https://akeno.randydev.my.id/ryuzaki/sibyl?api_key={api_key}"
        else:
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/sibyl"
        payload = {"user_id": user_id}
        return SibylBan._make_request("GET", url, json_data=payload)

    @staticmethod
    def unban(api_key: str = None, user_id: int = None, is_working_dev=True) -> Union[dict, str]:
        if is_working_dev:
            url = f"https://akeno.randydev.my.id/ryuzaki/sibyldel?api_key={api_key}"
        else:
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/sibydel"
        payload = {"user_id": user_id}
        return SibylBan._make_request("DELETE", url, json_data=payload)

    @staticmethod
    def banlist_all(is_working_dev=True) -> Union[dict, str]:
        if is_working_dev:
            url = "https://akeno.randydev.my.id/ryuzaki/getbanlist"
        else:
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/getbanlist"
        return SibylBan._make_request("GET", url)
