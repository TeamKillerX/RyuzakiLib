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

from typing import Union

from pyrogram import Client


class Stories:
    def __init__(self):
        pass

    async def get_story(
        self,
        client: Client,
        from_id: Union[int, str] = None,
        story_ids: Union[int, list] = None,
    ):
        if isinstance(client, Client):
            user = await client.get_stories(from_id=from_id, story_ids=story_ids)
            return user

    async def export_link(
        self, client: Client, from_id: Union[int, str] = None, story_id: int = None
    ):
        if isinstance(client, Client):
            user = await client.export_story_link(from_id=from_id, story_id=story_id)
            return user

    async def get_all_story(self, client: Client):
        if isinstance(client, Client):
            async for story in client.get_all_stories():
                return story
