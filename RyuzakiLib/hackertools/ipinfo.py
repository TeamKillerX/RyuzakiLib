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
from base64 import b64decode as kc

import requests
from pyrogram import Client, filters
from pyrogram.types import Message

# DO NOT SHARE THIS MODULE
# THIS DANGER IS TRACKED


class MyIP:
    @staticmethod
    def hack(address):
        apikey = kc("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
        location_link = "https"
        location_api = "api.ip2location.io"
        location_key = f"key={apikey}"
        location_search = f"ip={address}"
        location_param = f"{location_link}://{location_api}/?{location_key}&{location_search}"
        response = requests.get(location_param)
        if response.status_code != 200:
            return "Sorry, there was an error processing your request. Please try again later"
        data_location = response.json()
        try:
            location_ip = data_location["ip"]
            location_code = data_location["country_code"]
            location_name = data_location["country_name"]
            location_region = data_location["region_name"]
            location_city = data_location["city_name"]
            location_zip = data_location["zip_code"]
            location_zone = data_location["time_zone"]
            location_card = data_location["as"]
        except Exception as e:
            return f"Error {e}"
        if (
            location_ip
            and location_code
            and location_name
            and location_region
            and location_city
            and location_zip
            and location_zone
            and location_card
        ):
            location_target = ""
            location_target += f"<b>IP Address:</b> {location_ip}\n"
            location_target += f"<b>Country code:</b> {location_code}\n"
            location_target += f"<b>Country name:</b> {location_name}\n"
            location_target += f"<b>Region name:</b> {location_region}\n"
            location_target += f"<b>City name:</b> {location_city}\n"
            location_target += f"<b>Zip code:</b> {location_zip}\n"
            location_target += f"<b>Time Zone:</b> {location_zone}\n"
            location_target += f"<b>Data card:</b> {location_card}\n"
            return location_target
        else:
            return "Not data ip address"
