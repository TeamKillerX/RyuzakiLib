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


class PrivateApiUrl:
    def __init__(
        self,
        url: str = "randydev-ryuzaki-api.hf.space",
        method: str = None,
        punctuation: str = "?",
        parameter: str = None,
        allow_web: str = "https",
    ):
        self.url = url
        self.method = method
        self.punctuation = punctuation
        self.parameter = parameter
        self.allow_web = allow_web

    def checking(self):
        api_url = f"{self.allow_web}://{self.url}/{self.method}{self.punctuation}{self.parameter}"
        return api_url
