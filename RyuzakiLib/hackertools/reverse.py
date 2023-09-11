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


from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import json
from serpapi import GoogleSearch

class GoogleReverseImage:
    def __init__(self, image_url, apikey):
        self.image_url = image_url
        self.apikey = apikey

    def get_reverse(self):
        params = {
            "api_key": self.apikey,
            "engine": "google_reverse_image",
            "image_url": self.image_url,
            "hl": "en",
            "gl": "us"
        }
        search = GoogleSearch(params) # where data extraction happens on the SerpApi backend
        return search.get_dict()
