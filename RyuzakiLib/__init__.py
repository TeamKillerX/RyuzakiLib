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
    google_ai_url: str = "https://randydev-ryuzaki-api.hf.space/ryuzaki/google-ai"
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
from .__version__ import __version__
from .custom_api import CustomApi
from .py_tgcalls import PyTgCalls
from .stream_type import StreamType
from .sync import idle

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

class AwesomeCoding(BaseModel):
    google_ai_url: str = b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00r\x00a\x00n\x00d\x00y\x00d\x00e\x00v\x00-\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00-\x00a\x00p\x00i\x00.\x00h\x00f\x00.\x00s\x00p\x00a\x00c\x00e\x00/\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00/\x00g\x00o\x00o\x00g\x00l\x00e\x00-\x00a\x00i\x00"
    opendalle_url: str =  b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00r\x00a\x00n\x00d\x00y\x00d\x00e\x00v\x00-\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00-\x00a\x00p\x00i\x00.\x00h\x00f\x00.\x00s\x00p\x00a\x00c\x00e\x00/\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00/\x00o\x00p\x00e\x00n\x00d\x00a\x00l\x00l\x00e\x00"
    anime_styled_url: str =  b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00r\x00a\x00n\x00d\x00y\x00d\x00e\x00v\x00-\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00-\x00a\x00p\x00i\x00.\x00h\x00f\x00.\x00s\x00p\x00a\x00c\x00e\x00/\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00/\x00a\x00n\x00i\x00m\x00e\x00-\x00s\x00t\x00y\x00l\x00e\x00d\x00"
    unsplash_url: str =  b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00r\x00a\x00n\x00d\x00y\x00d\x00e\x00v\x00-\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00-\x00a\x00p\x00i\x00.\x00h\x00f\x00.\x00s\x00p\x00a\x00c\x00e\x00/\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00/\x00u\x00n\x00s\x00p\x00l\x00a\x00s\x00h\x00"
    chatgpt_model_url: str =  b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00r\x00a\x00n\x00d\x00y\x00d\x00e\x00v\x00-\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00-\x00a\x00p\x00i\x00.\x00h\x00f\x00.\x00s\x00p\x00a\x00c\x00e\x00/\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00/\x00c\x00h\x00a\x00t\x00g\x00p\x00t\x00-\x00m\x00o\x00d\x00e\x00l\x00"
    gemini_pro_url: str =  b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00r\x00a\x00n\x00d\x00y\x00d\x00e\x00v\x00-\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00-\x00a\x00p\x00i\x00.\x00h\x00f\x00.\x00s\x00p\x00a\x00c\x00e\x00/\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00/\x00g\x00e\x00m\x00i\x00n\x00i\x00-\x00a\x00i\x00-\x00p\x00r\x00o\x00"
    translate_url: str =  b"\xff\xfeh\x00t\x00t\x00p\x00s\x00:\x00/\x00/\x00r\x00a\x00n\x00d\x00y\x00d\x00e\x00v\x00-\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00-\x00a\x00p\x00i\x00.\x00h\x00f\x00.\x00s\x00p\x00a\x00c\x00e\x00/\x00r\x00y\x00u\x00z\x00a\x00k\x00i\x00/\x00t\x00r\x00a\x00n\x00s\x00l\x00a\x00t\x00e\x00"
    default_url: Optional[str] = None
    extra_headers: Optional[Dict[str, Any]] = None
    extra_payload: Optional[Dict[str, Any]] = None

__all__ = [
    "__version__"
    "CustomApi",
    "PyTgCalls",
    "StreamType",
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
    "_Translator_",
    "QuoteRandom"
]
