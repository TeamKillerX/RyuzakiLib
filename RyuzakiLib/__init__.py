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

from typing import Optional, Dict, Any
from pydantic import BaseModel

class AwesomeCoding(BaseModel):
    opendalle_url: str = "https://randydev-ryuzaki-api.hf.space/ryuzaki/opendalle"
    anime_styled_url: str = "https://randydev-ryuzaki-api.hf.space/ryuzaki/anime-styled"
    unsplash_url: str = "https://randydev-ryuzaki-api.hf.space/ryuzaki/unsplash"
    extra_headers: Optional[Dict[str, Any]] = None

__version__ = "0.6.5"

from . import *
from .pushdb import *
from .reminder import *
from .story import *
from .quote import *
from .tr import *
from .channels import *
from .bot import *
from .decorator import *
from .mental import *
