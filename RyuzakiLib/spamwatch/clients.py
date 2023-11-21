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
# along with this program.  If not, see <https://www.gnu.org/licenses/>

import requests

class SibylBan:
    def __init__(self):
        pass

    async def add_ban(self, user_id: int=None, reason: str=None, is_banned: bool=False):
        if is_banned:
            url = f"https://private.randydev.my.id/ryuzaki/sibylban?user_id={user_id}&reason={reason}"
            try:
                response = requests.post(url).json()
                message = response["randydev"]["message"] if response else response["message"]
                return message
            except Exception as e:
                return f"Error: {e}"
        else:
            return "Error required is_banned=True"

    async def get_ban(self, user_id: int=None, banlist: bool=False):
        if banlist:
            url = f"https://private.randydev.my.id/ryuzaki/sibyl?user_id={user_id}"
            try:
                response = requests.get(url).json()
                return response
            except Exception as e:
                return f"Error: {e}"
        else:
            return "Error required banlist=True"

    async def get_all_banlist(self):
        try:
            url = "https://private.randydev.my.id/ryuzaki/getbanlist"
            response = requests.get(url).json()
            return response
        except Exception as e:
            return f"Error: {e}"
