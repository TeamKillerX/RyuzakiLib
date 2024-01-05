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

from datetime import datetime as dt
from datetime import timedelta

from pytz import timezone


class Reminder:
    def __init__(
        self,
        days: int = None,
        timezone_str: str = None,
    ):
        self.days = days
        self.timezone_str = timezone_str
        self.timezone = timezone(timezone_str)

    async def warning_alert(self, check_break: bool = None):
        if check_break:
            now = dt.now(self.timezone)
            time = now.strftime("%d-%m-%Y")
            expire_date = now + timedelta(days=self.days)
            return [expire_date, time]
        else:
            return None
