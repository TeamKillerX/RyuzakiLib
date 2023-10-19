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

class ImageVectorizer:
    BASE_URL = "https://api.picsart.io/tools/1.0/vectorizer"

    def __init__(
        self,
        api_key: str=None,
        file_image=None,
        image_url: str=None,
        image_id: str=None,
        downscale_to: int=2048,
        allow_image_id: bool=None
    ):
        self.api_key = api_key
        self.file_image = file_image
        self.image_url = image_url
        self.image_id = image_id
        self.downscale_to = downscale_to
        self.allow_image_id = allow_image_id

    def vectorize_image(self):
        headers = {
            "accept": "application/json",
            "X-Picsart-API-Key": self.api_key
        }

        if self.allow_image_id:
            with open(self.file_image, "rb") as path:
                payload = {
                    "image": path,
                    "image_id": self.image_id,
                    "downscale_to": self.downscale_to
                }
        else:
            payload = {
                "image_url": self.image_url,
                "downscale_to": self.downscale_to
            }
        try:
            response = requests.post(self.BASE_URL, headers=headers, data=payload)
            response_data = response.json()
            return response_data
        except Exception as e:
            print(f"Error: {e}")
            return None
