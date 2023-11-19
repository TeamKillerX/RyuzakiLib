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


class QuoteRandom:
    endpoint_url = "https://api.quotable.io"

    def __init__(self):
        pass

    def get_results(self, parameter: str = "/quotes/random", check_for: bool = None):
        api_url = self.endpoint_url
        response = requests.get(api_url + parameter)
        if response.status_code != 200:
            return f"Error status {response.status_code}"
        results = response.json()
        if check_for:
            for x in results:
                return x
        else:
            return results
