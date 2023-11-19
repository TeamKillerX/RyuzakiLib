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

from pyrogram import Client


class SettingPyrogram:
    def __init__(
        self,
        name: str = None,
        app_version: str = None,
        device_model: str = None,
        system_version: str = None,
        api_id: int = None,
        api_hash: str = None,
        bot_token: str = None,
        session_string: str = None,
    ):
        self.name = name
        self.app_version = app_version
        self.device_model = device_model
        self.system_version = system_version
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.session_string = session_string

    async def telegram_original(self, setting_telegram: bool = None):
        if setting_telegram:
            client = Client(
                self.name,
                app_version=self.app_version,
                device_model=self.device_model,
                system_version=self.system_version,
                api_id=self.api_id,
                api_hash=self.api_hash,
                session_string=self.session_string,
            )
        else:
            client = Client(
                self.name,
                api_id=self.api_id,
                api_hash=self.api_hash,
                bot_token=self.bot_token,
            )
        return client
