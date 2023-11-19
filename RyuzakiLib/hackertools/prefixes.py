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


class CustomPrefixes:
    def __init__(self, name, user_id, prefix, collection, value: bool):
        self.name = name
        self.prefix = prefix
        self.user_id = user_id
        self.collection = collection
        self.value = value

    def add_prefixes(self):
        add_handler = {f"{self.name}": self.prefix}
        return self.collection.update_one(
            {"user_id": self.user_id}, {"$set": add_handler}, upsert=self.value
        )

    def get_prefix(self):
        user_data = self.collection.find_one({"user_id": self.user_id})
        return user_data.get(f"{self.name}") if user_data else None
