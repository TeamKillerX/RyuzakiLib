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

# JANGAN COPAS INI LU KEK KONTOL
# TANYA KE SUPPORT @KillerXSupport

import requests

class RequestsUrl:
    def __init__(
        self,
        url=None,
        params=None,
        data=None,
        expected_status_code: int=None
    ):
        self.url = url
        self.params = params
        self.data = data
        self.expected_status_code = expected_status_code

    def geturl(self):
        x = requests.get(
            self.url,
            params=self.params
        )
        if x.status_code != self.expected_status_code:
            return f"Error request: Expected status code {self.expected_status_code}, got {x.status_code}"
        return x.json()

    def posturl(self):
        x = requests.post(
            self.url,
            json=self.data
        )
        if x.status_code != self.expected_status_code:
            return f"Error request: Expected status code {self.expected_status_code}, got {x.status_code}"
        return x.json()
