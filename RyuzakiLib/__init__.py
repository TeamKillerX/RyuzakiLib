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
    chatgpt_model_url: str = "https://randydev-ryuzaki-api.hf.space/ryuzaki/chatgpt-model"
    gemini_pro_url: str = "https://randydev-ryuzaki-api.hf.space/ryuzaki/gemini-ai-pro"
    translate_url: str = "https://randydev-ryuzaki-api.hf.space/ryuzaki/translate"
    default_url: Optional[str] = None
    extra_headers: Optional[Dict[str, Any]] = None
    extra_payload: Optional[Dict[str, Any]] = None

__version__ = "0.6.6"

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

from .hackertools.chatgpt import RendyDevChat
from .hackertools.github import GithubUsername
from .hackertools.openai_api import OpenAiToken
from .hackertools.prefixes import CustomPrefixes
from .hackertools.reverse import GoogleReverseImage
from .hackertools.rmbg import RemoveBg
from .hackertools.ocrapi import OcrApiUrl
from .hackertools.ipinfo import WhoisIpHacker

from .extreme.carbon import CarbonSuper
from .extreme.chatbot import ChatbotAi
from .extreme.quotestk import QouteSticker
from .extreme.rayso import CarbonRaySo
from .extreme.userinfo import TelegramUserInfo
from .extreme.webshot import WebShotUrl

from .spamwatch.clients import SibylBan
from .profile.user import ProfileClone
from .api.fullstack import FullStackDev
from .api.private import PrivateApiUrl
from .dl.tiktok import TiktokUrl, faster_tiktok_downloader

__all__ = [
    "RendyDevChat",
    "GithubUsername",
    "OpenAiToken",
    "CustomPrefixes",
    "GoogleReverseImage",
    "RemoveBg",
    "OcrApiUrl",
    "WhoisIpHacker",
    "CarbonSuper",
    "ChatbotAi",
    "QouteSticker",
    "CarbonRaySo",
    "TelegramUserInfo",
    "WebShotUrl",
    "SibylBan",
    "ProfileClone",
    "FullStackDev",
    "PrivateApiUrl",
    "TiktokUrl",
    "faster_tiktok_downloader",
    "BadWordsList",
    "Reminder",
    "Translator",
    "QuoteRandom"
]
