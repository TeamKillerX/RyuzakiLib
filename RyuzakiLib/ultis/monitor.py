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

import requests


class Monitors:
    def __init__(self, api_key: str = None):
        self.api_key = api_key

    def _make_request(self, method: str, url: str, params: dict = None, json_data: dict = None):
        headers = {"accept": "application/json", "api-key": self.api_key}
        try:
            response = requests.request(
                method, url, headers=headers, params=params, json=json_data
            )
            return response.json()
        except requests.RequestException:
            pass

    def add_checking_monitor(self, url: str = None, is_monitor: bool = False):
        if is_monitor:
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/new-monitor"
            params = {"url": url}
            return self._make_request("POST", url, params=params)
        else:
            raise ValueError("Error: is_monitor must be True")

    def get_monitors(self, is_show: bool = False):
        if is_show:
            url = "https://randydev-ryuzaki-api.hf.space/ryuzaki/get-monitors"
            return self._make_request("POST", url)
        else:
            raise ValueError("Error: is_show must be True")
