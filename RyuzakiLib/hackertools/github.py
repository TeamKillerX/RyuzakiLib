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

from httpx import AsyncClient
from pyrogram import Client, filters
from pyrogram.types import Message


class Github:
    @staticmethod
    async def username(args):
        base_msg = ""
        async with AsyncClient() as gpx:
            req = (await gpx.get(f"https://api.github.com/users/{args}")).json()
            try:
                avatar = req["avatar_url"]
                twitter = req["twitter_username"]
                base_msg += "**❆ Gitub Information ❆** \n\n"
                base_msg += f"**Profile Url:** {req['html_url']} \n"
                base_msg += f"**Name:** `{req['name']}` \n"
                base_msg += f"**Username:** `{req['login']}` \n"
                base_msg += f"**User ID:** `{req['id']}` \n"
                base_msg += f"**Location:** `{req['location']}` \n"
                base_msg += f"**Company:** `{req['company']}` \n"
                base_msg += f"**Blog:** `{req['name']}` \n"
                base_msg += (
                    f"**Twitter:** `{f'https://twitter.com/{twitter}' if twitter else 'None'}` \n"
                )
                base_msg += f"**Bio:** `{req['bio']}` \n"
                base_msg += f"**Public Repos:** `{req['public_repos']}` \n"
                base_msg += f"**Public Gists:** `{req['public_gists']}` \n"
                base_msg += f"**Followers:** `{req['followers']}` \n"
                base_msg += f"**Following:** `{req['following']}` \n"
                base_msg += f"**Created At:** `{req['created_at']}` \n"
                base_msg += f"**Update At:** `{req['updated_at']}` \n"
                return [base_msg, avatar]
            except Exception as e:
                base_msg += f"**An error occured while parsing the data!** \n\n**Traceback:** \n `{e}` \n\n`Make sure that you've sent the command with the correct username!`"
                return [base_msg, "https://telegra.ph//file/32f69c18190666ea96553.jpg"]
