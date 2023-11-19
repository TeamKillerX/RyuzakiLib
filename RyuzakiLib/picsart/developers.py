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


class PicsArtAI:
    developers_url = "https://api.picsart.io/tools/1.0"

    def __init__(
        self,
        api_key: str = None,
        endpoint: str = None,
        file_image=None,
        image_url: str = None,
        image_id: str = None,
        downscale_to: int = 2048,
        output_type: str = "cutout",
        bg_image: str = None,
        bg_image_url: str = None,
        bg_image_id: str = None,
        bg_color: str = None,
        bg_blur: int = None,
        bg_width: int = None,
        bg_height: int = None,
        format: str = "PNG",
        scale: str = "fit",
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.file_image = file_image
        self.image_url = image_url
        self.image_id = image_id
        self.downscale_to = downscale_to
        self.output_type = output_type
        self.bg_image = bg_image
        self.bg_image_url = bg_image_url
        self.bg_image_id = bg_image_id
        self.bg_color = bg_color
        self.bg_blur = bg_blur
        self.bg_width = bg_width
        self.bg_height = bg_height
        self.format = format

    def vectorize_image(self, allow_image_id: bool = None):
        headers = {"accept": "application/json", "X-Picsart-API-Key": self.api_key}

        if allow_image_id:
            with open(self.file_image, "rb") as path:
                payload = {
                    "image": path,
                    "image_id": self.image_id,
                    "downscale_to": self.downscale_to,
                }
        else:
            payload = {"image_url": self.image_url, "downscale_to": self.downscale_to}
        try:
            response = requests.post(
                f"{self.developers_url}/{self.endpoint}", headers=headers, data=payload
            )
            response_data = response.json()
            return response_data
        except Exception as e:
            print(f"Error: {e}")
            return None

    def remove_background(self, allow_image_id: bool = None):
        headers = {"accept": "application/json", "X-Picsart-API-Key": self.api_key}

        if allow_image_id:
            with open(self.file_image, "rb") as path:
                payload = {
                    "image": path,
                    "image_id": self.image_id,
                    "output_type": self.output_type,
                    "bg_image": self.bg_image,
                    "bg_image_url": self.bg_image_url,
                    "bg_image_id": self.bg_image_id,
                    "bg_color": self.bg_color,
                    "bg_blur": self.bg_blur,
                    "bg_width": self.bg_width,
                    "bg_height": self.bg_height,
                    "scale": self.scale,
                    "format": self.format,
                }
        else:
            payload = {
                "image_url": self.image_url,
                "output_type": self.output_type,
                "scale": self.scale,
                "format": self.format,
            }

        try:
            response = requests.post(
                f"{self.developers_url}/{self.endpoint}", headers=headers, data=payload
            )
            response_data = response.json()
            return response_data
        except Exception as e:
            print(f"Error: {e}")
            return None
