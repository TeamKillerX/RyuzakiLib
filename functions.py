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

import os

import requests
from dotenv import load_dotenv

load_dotenv()
HUGGING_TOKEN = os.environ["HUGGING_TOKEN"]
SOURCE_ALPHA_URL = os.environ["SOURCE_ALPHA_URL"]


def ryuzaki_ai_text(text):
    API_URL = SOURCE_ALPHA_URL
    headers = {"Authorization": f"Bearer {HUGGING_TOKEN}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    return response.json()
