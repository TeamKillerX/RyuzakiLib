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


import cv2
from pyrogram import Client, filters
from pyrogram.types import Message

class FaceDark:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def check_detect(self):
        try:
            img = cv2.imread(self.file_path)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            face_cascade = cv2.CascadeClassifier(
                f"{cv2.data.haarcascades}haarcascade_frontalface_default.xml"
            )
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        except Exception as e:
            return f"Error request {e}"

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        try:
            output_file_path = "output.jpg"
            cv2.imwrite(output_file_path, img)
            return output_file_path
        except Exception as e:
            return f"Error request {e}"
