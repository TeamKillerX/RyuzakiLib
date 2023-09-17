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

from pyrogram import Client, filters
from pyrogram.types import Message
from base64 import b64decode
import requests
import base64
from io import BytesIO

from gpytranslate import SyncTranslator

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

class CarbonRaySo:
    def __init__(
        self,
        code=None,
        title="Ryuzaki Dev",
        theme=None,
        setlang="en",
        auto_translate: bool=None,
        check_sticker: bool=None,
        ryuzaki: bool=None,
        chrome_options=None
    ):
        self.code = code
        self.title = title
        self.theme = theme
        self.setlang = setlang
        self.auto_translate = auto_translate
        self.check_sticker = check_sticker
        self.ryuzaki = ryuzaki

    def start_driver(self):
        if Config.CHROME_BIN is None:
            return None, "Need to install Google Chrome or Chromium. Module Stopping."
        try:
            chrome_options = ChromeOptions()
            chrome_options.binary_location = Config.CHROME_BIN
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--test-type")
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--window-size=1920x1080")
            chrome_options.add_argument("--disable-gpu")
            prefs = {"download.default_directory": "./"}
            chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(options=chrome_options)
            return driver, None
        except Exception as err:
            return None, str(err)

    def make_carbon_rayso(self):
        trans = SyncTranslator()
        api_url = b64decode("aHR0cHM6Ly9hcGkuc2Fmb25lLm1lL3JheXNv").decode("utf-8")
        if self.check_sticker:
            filename = "rayso.webp"
        else:
            filename = "rayso.jpg"
        if self.auto_translate:
            source = trans.detect(self.code)
            translation = trans(self.code, sourcelang=source, targetlang=self.setlang)
            code = translation.text
        else:
            code = self.code
        if self.chrome_options:
            url = f'https://ray.so/#code={base64.b64encode(inputstr.encode()).decode().replace("+","-")}&title={self.title}&theme={self.theme}&padding=64&darkMode=True&language=python'
            driver, error = self.start_driver()
            if error:
                return None, error
            driver.set_window_size(2000, 20000)
            driver.get(url)
            element = driver.find_element(By.CLASS_NAME, "Controls_controls__kwzcE")
            driver.execute_script("arguments[0].style.display = 'none';", element)
            frame = driver.find_element(By.CLASS_NAME, "Frame_frame__Dmfe9")
            frame.screenshot(file_name)
            driver.quit()
            return file_name, None
        if self.ryuzaki:
            x = requests.post(
                f"{api_url}",
                json={
                    "code": code,
                    "title": self.title,
                    "theme": self.theme,
                    "darkMode": True
                }
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
                    "darkMode": True
                }
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
