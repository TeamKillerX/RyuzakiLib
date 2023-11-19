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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests


class FullStackDev:
    def __init__(
        self,
        domain_url: str = None,
        headers=None,
        params: str = None,
        json_data=None,
        type_mode: str = "wb",
        filename: str = None,
    ):
        self.headers = headers
        self.domain_url = domain_url
        self.params = params
        self.json_data = json_data
        self.type_mode = type_mode
        self.filename = filename

    def domain_urls(self):
        request_url = self.domain_url
        return request_url

    def ryuzaki_get(self, re_json: bool = None):
        request_url = self.domain_urls()
        if re_json:
            req = requests.get(
                request_url, headers=self.headers, params=self.params
            ).json()
            return req
        else:
            req = requests.get(request_url, headers=self.headers, params=self.params)
            return req

    def ryuzaki_post(self, re_json: bool = None):
        request_url = self.domain_urls()
        if re_json:
            req = requests.post(
                request_url, headers=self.headers, params=self.json_data
            ).json()
            return req
        else:
            req = requests.post(request_url, headers=self.headers, json=self.json_data)
            return req

    def faster_downloader(self):
        request_url = self.domain_urls()
        req = requests.get(request_url, allow_redirects=True)
        with open(self.filename, self.type_mode) as file:
            file.write(req.content)
        return self.filename

    def fastapi_get(self, re_json: bool = None):
        request_url = self.domain_urls()
        if re_json:
            req = requests.get(
                request_url, headers=self.headers, params=self.json_data
            ).json()
            if req.status_code != 200:
                return "Not Responding"
            try:
                return req
            except Exception as e:
                return {"status": "false", "message": f"error {e}"}
        else:
            req = requests.get(request_url, headers=self.headers, json=self.json_data)
            if req.status_code != 200:
                return "Not Responding"
            try:
                return req
            except Exception as e:
                return {"status": "false", "message": f"error {e}"}
