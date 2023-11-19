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

from base64 import b64decode
import requests
import base64
from io import BytesIO

from gpytranslate import SyncTranslator


class CarbonRaySo:
    def __init__(
        self,
        code=None,
        title="Ryuzaki Dev",
        theme=None,
        setlang="en",
        base="aHR0cHM6Ly9hcGkuc2Fmb25lLmRldi9yYXlzbw==",
    ):
        self.code = code
        self.title = title
        self.theme = theme
        self.setlang = setlang
        self.base = base

    def make_carbon_rayso(
        self,
        auto_translate: bool = None,
        check_sticker: bool = None,
        darkmode: bool = None,
        ryuzaki: bool = None,
    ):
        trans = SyncTranslator()
        api_url = b64decode(self.base).decode("utf-8")
        if check_sticker:
            filename = "rayso.webp"
        else:
            filename = "rayso.jpg"
        if auto_translate:
            source = trans.detect(self.code)
            translation = trans(self.code, sourcelang=source, targetlang=self.setlang)
            code = translation.text
        else:
            code = self.code
        if ryuzaki:
            x = requests.post(
                f"{api_url}",
                json={
                    "code": code,
                    "title": self.title,
                    "theme": self.theme,
                    "darkMode": darkmode,
                },
            )
            if x.status_code != 200:
                return "Error api Gay"
            data = x.json()
            try:
                image_data = base64.b64decode(data["image"])
                f = BytesIO(image_data)
                f.name = filename
                return f
            except Exception as e:
                return f"Error: {e}"
        else:
            x = requests.post(
                f"{api_url}",
                json={
                    "code": code,
                    "title": self.title,
                    "theme": "breeze",
                    "darkMode": darkmode,
                },
            )
            if x.status_code != 200:
                return "Error api Gay"
            data = x.json()
            try:
                image_data = base64.b64decode(data["image"])
                f = BytesIO(image_data)
                f.name = filename
                return f
            except Exception as e:
                return f"Error: {e}"
