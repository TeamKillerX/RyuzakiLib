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

import requests
import json
import base64
import re
import uvicorn
import os
import shutil
import random
import tempfile
import io
from io import BytesIO
from datetime import datetime as dt
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from typing import *
from typing_extensions import Annotated
from typing import Annotated, Union
from typing import Optional, List, Dict, Any


from pydantic import BaseModel
from base64 import b64decode as kc
from base64 import b64decode
from random import choice
from gpytranslate import SyncTranslator
from httpx import AsyncClient
from telegraph import Telegraph, upload_file
from pathlib import Path
from serpapi import GoogleSearch

from fastapi import FastAPI, UploadFile, File, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.openapi.utils import get_openapi
from fastapi.responses import StreamingResponse
from fastapi import HTTPException
from fastapi import FastAPI, Request, Header
from fastapi import Body, Query
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse

from pymongo import MongoClient

from RyuzakiLib.hackertools.chatgpt import RendyDevChat
from RyuzakiLib.hackertools.openai_api import OpenAiToken
from RyuzakiLib.mental import BadWordsList

from bardapi import Bard

import logging
import functions as code

logging.basicConfig(level=logging.ERROR)

# I DON'T KNOW LIKE THIS HACKER
load_dotenv()

# Database url
MONGO_URL = os.environ["MONGO_URL"]

# source url
SOURCE_UNSPLASH_URL = os.environ["SOURCE_UNSPLASH_URL"]
SOURCE_OCR_URL = os.environ["SOURCE_OCR_URL"]
SOURCE_ALPHA_URL = os.environ["SOURCE_ALPHA_URL"]
SOURCE_WAIFU_URL = os.environ["SOURCE_WAIFU_URL"]
SOURCE_TIKTOK_WTF_URL = os.environ["SOURCE_TIKTOK_WTF_URL"]
SOURCE_TIKTOK_TECH_URL = os.environ["SOURCE_TIKTOK_TECH_URL"]
SOURCE_CALLI_GRAPHY_URL = os.environ["SOURCE_CALLI_GRAPHY_URL"]
SOURCE_WHAT_GAY_URL = os.environ["SOURCE_WHAT_GAY_URL"]
SOURCE_ASSISTANT_GOOGLE_AI = os.environ["SOURCE_ASSISTANT_GOOGLE_AI"]
SOURCE_MONITOR_URL = os.environ["SOURCE_MONITOR_URL"]

# api keys
REVERSE_IMAGE_API = os.environ["REVERSE_IMAGE_API"]
OCR_API_KEY = os.environ["OCR_API_KEY"]
ONLY_DEVELOPER_API_KEYS = os.environ["ONLY_DEVELOPER_API_KEYS"]
HUGGING_TOKEN = os.environ["HUGGING_TOKEN"]
ASSISTANT_GOOGLE_API_KEYS = os.environ["ASSISTANT_GOOGLE_API_KEYS"]
COOKIE_BARD_TOKEN = os.environ["COOKIE_BARD_TOKEN"]
MONITOR_API_KEYS = os.environ["MONITOR_API_KEYS"]

client_mongo = MongoClient(MONGO_URL)
db = client_mongo["tiktokbot"]
collection = db["users"]

app = FastAPI(docs_url=None, redoc_url="/")

def get_all_api_keys():
    user = collection.find({})
    api_keys = []
    for x in user:
        api_key = x.get("ryuzaki_api_key")
        if api_key:
            api_keys.append(api_key)
    return api_keys

def validate_api_key(api_key: str = Header(...)):
    USERS_API_KEYS = get_all_api_keys()
    if api_key not in USERS_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")

def validate_api_key_only_devs(api_key: str = Header(...)):
    if api_key not in ONLY_DEVELOPER_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")

RAMDOM_STATUS = [
    "civilian",
    "wanted",
    "undercover",
    "rogue_agent",
    "innocent",
    "fugitive",
    "covert_operator"
]

def remove_sibyl_system_banned(user_id):
    update_doc = {
        "sibyl_ban": None,
        "reason_sibyl": None,
        "is_banned_sibly": None,
        "date_joined_sib": None,
        "sibyl_userid": None
    }
    return collection.update_one({"user_id": user_id}, {"$unset": update_doc}, upsert=True)

def new_sibyl_system_banned(user_id, name, reason, date_joined):
    update_doc = {
        "sibyl_ban": name,
        "reason_sibyl": reason,
        "is_banned_sibly": True,
        "date_joined_sib": date_joined,
        "sibyl_userid": user_id
    }
    return collection.update_one({"user_id": user_id}, {"$set": update_doc}, upsert=True)

def get_sibyl_system_banned(user_id):
    user = collection.find_one({"user_id": user_id})
    if user:
        sibyl_name = user.get("sibyl_ban")
        reason = user.get("reason_sibyl")
        is_banned = user.get("is_banned_sibly")
        date_joined = user.get("date_joined_sib")
        sibyl_user_id = user.get("sibyl_userid")
        return sibyl_name, reason, is_banned, date_joined, sibyl_user_id
    else:
        return None

def get_all_banned():
    banned_users = []

    users = collection.find({})

    for user_id in users:
        reason = user_id.get("reason_sibyl")
        user_id = user_id.get("sibyl_userid")
        banned_users.append({"user_id": user_id, "reason": reason})
    return banned_users

def new_profile_clone(
    user_id,
    first_name,
    last_name=None,
    profile_id=None,
    bio=None
):
    update_doc = {
        "first_name_2": first_name,
        "last_name_2": last_name,
        "profile_id_2": profile_id,
        "bio_2": bio
    }
    collection.update_one({"user_id": user_id}, {"$set": update_doc}, upsert=True)

def get_profile_clone(user_id):
    user = collection.find_one({"user_id": user_id})
    if user:
        first_name = user.get("first_name_2")
        last_name = user.get("last_name_2")
        profile_id = user.get("profile_id_2")
        bio = user.get("bio_2")
        return first_name, last_name, profile_id, bio
    else:
        return None

class CustomErrorResponseModel(BaseModel):
    detail: List[Dict[str, Any]]

class SuccessResponse(BaseModel):
    status: str
    randydev: Dict[str, Any]

class ErrorResponse(BaseModel):
    status: str
    detail: str

class ErrorStatus(BaseModel):
    status: str
    message: str

class ProfileClone(BaseModel):
    user_id: int
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    profile_id: Optional[str] = None
    bio: Optional[str] = None

class GetProfileClone(BaseModel):
    user_id: int

class SibylSystemDel(BaseModel):
    user_id: int

class SibylSystemBan(BaseModel):
    user_id: int
    reason: str

class RyuzakiAi(BaseModel):
    text: str

class SibylSystem(BaseModel):
    user_id: int

class GoogleReverse(BaseModel):
    engine: str="google_reverse_image"
    image_url: str
    language: str="en"
    google_lang: str="us"

class GetImageUnsplash(BaseModel):
    query: str
    size: str="500x500"

class OrcSpaceUrl(BaseModel):
    url: str
    overlay: bool=False
    language: str="eng"

class ChatgptModel(BaseModel):
    query: str
    model_id: Optional[int] = None
    is_models: bool=False

class ChatgptCustom(BaseModel):
    query: str

class GeminiPro(BaseModel):
    query: str
    bard_api_key: Optional[str] = None
    is_login: bool=False

class WaifuPics(BaseModel):
    types: str="sfw"
    category: str="neko"
    media_type: Optional[str] = None
    is_bytes: bool=False

class MakeRayso(BaseModel):
    code: str
    title: str="Ryuzaki Dev"
    theme: str
    setlang: str="en"
    auto_translate: Optional[bool] = None
    ryuzaki_dark: bool=True

class Webshot(BaseModel):
    url: str
    quality: str="1920x1080"
    type_mine: str="JPEG"
    pixels: str="1024"
    cast: str="Z100"

class GithubUsernames(BaseModel):
    username: str

class ChatBots(BaseModel):
    query: str
    user_id: Optional[int] = None
    bot_name: Optional[str] = None
    bot_username: Optional[str] = None

class NewMonitor(BaseModel):
    type: int=1
    url: str
    friendly_name: str

class TiktokBeta(BaseModel):
    tiktok_url: str
    only_video: Optional[bool] = None

class TiktokDownloader(BaseModel):
    tiktok_url: str

class GetMonitorLogs(BaseModel):
    logs: int

class DownloadLink(BaseModel):
    link: str

@app.post("/ryuzaki/profile-clone", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def profile_clone(
    item: ProfileClone,
    api_key: None = Depends(validate_api_key)
):
    if item.user_id == 1191668125:
        return {"status": "false", "message": "Only Developer"}

    try:
        new_profile_clone(
            user_id=item.user_id,
            first_name=item.first_name,
            last_name=item.last_name,
            profile_id=item.profile_id,
            bio=item.bio
        )
        return SuccessResponse(
            status="True",
            randydev={
                "user_id": item.user_id,
                "first_name": item.first_name,
                "last_name": item.last_name,
                "profile_id": item.profile_id,
                "bio": item.bio
            }
        )
    except Exception as e:
        return ErrorStatus(status="false", message=f"Internal server error: {str(e)}")

@app.get("/ryuzaki/get-profile-clone", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def get_profile_(
    item: GetProfileClone,
    api_key: None = Depends(validate_api_key)
):
    try:
        first_name, last_name, profile_id, bio = get_profile_clone(item.user_id)
        if last_name is None:
            last_name_str = ""
        else:
            last_name_str = last_name
        if bio is None:
            bio_str = ""
        else:
            bio_str = bio
        if first_name and profile_id:
            return SuccessResponse(
                status="True",
                randydev={
                    "user_id": item.user_id,
                    "first_name": first_name,
                    "last_name": last_name_str,
                    "profile_id": profile_id,
                    "bio": bio_str
                }
            )
        else:
            return ErrorStatus(status="false", message="Not found user")
    except Exception as e:
        return ErrorStatus(status="false", message=f"Internal server error: {str(e)}")

@app.get("/ryuzaki/getbanlist")
def sibyl_get_all_banlist():
    banned_users = get_all_banned()
    return {
        "status": "True",
        "randydev": {
            "results": banned_users
        }
    }

@app.get("/ryuzaki/blacklist-words")
def blacklist_words():
    try:
        BLACKLIST_WORDS = BadWordsList()
        results_all = BLACKLIST_WORDS.banned_by_google(file_txt="banned_by_google.txt", storage=True)
        return {"status": "true", "results": results_all}
    except Exception as e:
        return {"status": "false", "message": f"Internal server error: {str(e)}"}

@app.delete("/ryuzaki/sibyldel", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def sibyl_system_delete(
    item: SibylSystemDel,
    api_key: None = Depends(validate_api_key_only_devs)
):
    try:
        _, _, _, _, sibyl_user_id = get_sibyl_system_banned(item.user_id)

        if sibyl_user_id:
            remove_sibyl_system_banned(item.user_id)
            return SuccessResponse(
                status="True",
                randydev={
                    "message": f"Successfully removed {item.user_id} from the Sibyl ban list"
                }
            )
        else:
            return ErrorStatus(status="false", message="Not found user")
    except Exception as e:
        return ErrorStatus(status="false", message=f"Internal server error: {str(e)}")

@app.post("/ryuzaki/sibylban", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def sibyl_system_ban(
    item: SibylSystemBan,
    api_key: None = Depends(validate_api_key)
):
    if item.user_id == 1191668125:
        return {"status": "false", "message": "Only Developer"}

    try:
        date_joined = str(dt.now())
        sibyl_ban = random.choice(RAMDOM_STATUS)
        _, _, is_banned, _, sibyl_user_id = get_sibyl_system_banned(item.user_id)

        if sibyl_user_id and is_banned:
            return {"status": "false", "message": "User is already banned"}

        new_sibyl_system_banned(item.user_id, sibyl_ban, item.reason, date_joined)
        return SuccessResponse(
            status="True",
            randydev={
                "user_id": item.user_id,
                "sibyl_name": sibyl_ban,
                "reason": item.reason,
                "date_joined": date_joined,
                "message": f"Successfully banned {item.user_id} from the Sibyl ban list."
            }
        )
    except Exception as e:
        return ErrorStatus(status="false", message=f"Internal server error: {str(e)}")

@app.get("/ryuzaki/sibyl", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def sibyl_system(
    item: SibylSystem,
    api_key: None = Depends(validate_api_key)
):
    sibyl_name, reason, is_banned, date_joined, sibyl_user_id = get_sibyl_system_banned(item.user_id)
    if sibyl_name and reason and is_banned and date_joined and sibyl_user_id:
        return SuccessResponse(
            status="True",
            randydev={
                "sibyl_name": sibyl_name,
                "reason": reason,
                "is_banned": is_banned,
                "date_joined": date_joined,
                "sibyl_user_id": sibyl_user_id
            }
        )
    else:
        return ErrorStatus(status="false", message="Not found user")

@app.get("/ryuzaki/ai", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def ryuzaki_ai(
    item: RyuzakiAi,
    api_key: None = Depends(validate_api_key)
):
    try:
        response_data = code.ryuzaki_ai_text(item.text)

        if isinstance(response_data, list) and len(response_data) > 0:
            first_result = response_data[0]
            if "generated_text" in first_result:
                message = first_result["generated_text"]
                return SuccessResponse(
                    status="True",
                    randydev={
                        "ryuzaki_text": message
                    }
                )
        return {"status": "false", "message": "Invalid response format"}

    except Exception:
        return {"status": "false", "message": "Internal server error"}

@app.get("/ryuzaki/unsplash")
async def get_image_unsplash(item: GetImageUnsplash):
    url = SOURCE_UNSPLASH_URL
    image_url = f"{url}/?{item.query}/{item.size}"
    try:
        response = requests.get(image_url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=500,
            detail=CustomErrorResponseModel(detail=[{}])
        )
    try:
        encoded_string = base64.b64encode(response.content).decode("utf-8")
    except Exception:
        raise HTTPException(
            status_code=500,
            detail=CustomErrorResponseModel(detail=[{}])
        )
    headers = {"Content-Type": "image/jpeg"}
    return Response(
        content=encoded_string,
        media_type="image/jpeg",
        headers=headers
    )

@app.get("/ryuzaki/reverse", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def google_reverse(
    item: GoogleReverse,
    api_key: None = Depends(validate_api_key)
):
    params = {
        "api_key": REVERSE_IMAGE_API,
        "engine": item.engine,
        "image_url": item.image_url,
        "hl": item.language,
        "gl": item.google_lang
    }
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        link = results["search_metadata"]["google_reverse_image_url"]
        total_time_taken = results["search_metadata"]["total_time_taken"]
        create_at = results["search_metadata"]["created_at"]
        processed_at = results["search_metadata"]["processed_at"]
        return SuccessResponse(
            status="True",
            randydev={
                "link": link,
                "total_time_taken": total_time_taken,
                "create_at": create_at,
                "processed_at": processed_at
            }
        )
    except Exception:
        return {"status": "false", "message": "Internal server error"}

@app.get("/ryuzaki/ocr", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def ocr_space_url(
    item: OrcSpaceUrl,
    api_key: None = Depends(validate_api_key)
):
    payload = {
        "url": item.url,
        "isOverlayRequired": item.overlay,
        "apikey": OCR_API_KEY,
        "language": item.language
    }
    try:
        response = requests.post(SOURCE_OCR_URL, data=payload)
        response.raise_for_status()
        test_url = response.content.decode()
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
    try:
        parsed_response = json.loads(test_url)
        if "ParsedResults" in parsed_response and len(parsed_response["ParsedResults"]) > 0:
            return SuccessResponse(
                status="True",
                randydev={
                    "text": parsed_response["ParsedResults"][0]["ParsedText"]
                }
            )
        else:
            return {"status": "false", "message": "Error response."}
    except (json.JSONDecodeError, KeyError):
        return "Error parsing the OCR response."

@app.post("/ryuzaki/chatgpt-model", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def chatgpt_model(item: ChatgptModel):
    url = "https://lexica.qewertyy.me/models"
    if item.is_models:
        params = {"model_id": item.model_id, "prompt": item.query}
        response = requests.post(url, params=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"
        check_response = response.json()
        answer = check_response.get("content")
        return SuccessResponse(
            status="True",
            randydev={
                "message": answer
            }
        )
    else:
        params = {"model_id": 5, "prompt": item.query}
        response = requests.post(url, params=params)
        if response.status_code != 200:
            return f"Error status: {response.status_code}"
        check_response = response.json()
        answer = check_response.get("content")
        return SuccessResponse(
            status="True",
            randydev={
                "message": answer
            }
        )

@app.get("/ryuzaki/freechatgpt-beta", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def free_chatgpt4_beta(item: ChatgptCustom):
    try:
        response = RendyDevChat(item.query).get_response_beta(joke=True)
        return SuccessResponse(
            status="True",
            randydev={
                "message": response
            }
        )
    except:
        return {"status": "false", "message": "Error response."}

@app.get("/ryuzaki/freechatgpt-bing", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def free_chatgpt4_bing(item: ChatgptCustom):
    try:
        response = RendyDevChat(query).get_response_bing(bing=True)
        return SuccessResponse(
            status="True",
            randydev={
                "message": response
            }
        )
    except:
        return {"status": "false", "message": "Error response."}

@app.post("/ryuzaki/google-ai", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def v1beta3_google_ai(
    item: ChatgptCustom,
    api_key: None = Depends(validate_api_key)
):
    url = SOURCE_ASSISTANT_GOOGLE_AI
    token = ASSISTANT_GOOGLE_API_KEYS
    api_url = f"{SOURCE_ASSISTANT_GOOGLE_AI}/v1beta3/models/text-bison-001:generateText?key={ASSISTANT_GOOGLE_API_KEYS}"
    try:
        headers = {"Content-Type": "application/json"}
        data = {
            "prompt": {
                "text": item.query
            }
        }
        response = requests.post(api_url, headers=headers, json=data)
        response_str = response.json()
        answer = response_str["candidates"]
        for results in answer:
            message = results.get("output")
        return SuccessResponse(
            status="True",
            randydev={
                "message": message
            }
        )
    except:
        return {"status": "false", "message": "Error response."}

@app.post("/ryuzaki/gemini-ai-pro", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def gemini_pro(
    item: GeminiPro,
    api_key: None = Depends(validate_api_key)
):
    if item.is_login:
        token = item.bard_api_key
    else:
        token = COOKIE_BARD_TOKEN
    owner_base = f"""
    Your name is Randy Dev. A kind and friendly AI assistant that answers in
    a short and concise answer. Give short step-by-step reasoning if required.

    Today is {dt.now():%A %d %B %Y %H:%M}
    """
    try:
        session = requests.Session()
        session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/"
        }
        session.cookies.set("__Secure-1PSID", token)
        bard = Bard(token=token, session=session, timeout=30)
        bard.get_answer(owner_base)["content"]
        message = bard.get_answer(item.query)["content"]
        return SuccessResponse(
            status="True",
            randydev={
                "message": message
            }
        )
    except:
        return {"status": "false", "message": "Error response."}

@app.post("/ryuzaki/v1beta2-google-ai", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def v1beta2_google_ai(
    item: ChatgptCustom,
    api_key: None = Depends(validate_api_key)
):
    url = SOURCE_ASSISTANT_GOOGLE_AI
    token = ASSISTANT_GOOGLE_API_KEYS
    api_url = f"{SOURCE_ASSISTANT_GOOGLE_AI}/v1beta2/models/chat-bison-001:generateMessage?key={ASSISTANT_GOOGLE_API_KEYS}"
    try:
        headers = {"Content-Type": "application/json"}
        data = {
            "prompt": {
                "messages": [{"content": item.query}]}
        }
        response = requests.post(api_url, headers=headers, json=data)
        response_str = response.json()
        answer = response_str["candidates"]
        for results in answer:
            message = results.get("content")
        return SuccessResponse(
            status="True",
            randydev={
                "message": message
            }
        )
    except:
        return {"status": "false", "message": "Error response."}

@app.post("/ryuzaki/new-monitor", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def new_monitor(
    item: NewMonitor,
    api_key: None = Depends(validate_api_key)
):
    urls = SOURCE_MONITOR_URL
    token = MONITOR_API_KEYS
    api_url = f"{urls}/newMonitor"
    try:
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "cache-control": "no-cache"
        }
        payload = {
            "api_key": token,
            "format": "json",
            "type": item.type,
            "url": item.url,
            "friendly_name": item.friendly_name
        }
        response = requests.post(api_url, data=payload, headers=headers)
        response_str = response.json()
        status_ok = response_str["stat"]
        monitor_id = response_str["monitor"].get("id")
        monitor_status = response_str["monitor"].get("status")
        return {
            "status": "true",
            "randydev":{
                "status_ok": status_ok,
                "monitor_id": monitor_id,
                "monitor_status": monitor_status
            }
        }
    except:
        return {"status": "false", "message": "Error response."}

@app.post("/ryuzaki/get-monitors", response_model=SuccessResponse, responses={422: {"model": ErrorResponse}})
def getMonitors(
    item: GetMonitorLogs,
    api_key: None = Depends(validate_api_key)
):
    url = SOURCE_MONITOR_URL
    token = MONITOR_API_KEYS
    api_url = f"{url}/getMonitors"
    try:
        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "cache-control": "no-cache"
        }
        payload = {
            "api_key": token,
            "format": "json",
            "logs": item.logs
        }
        response = requests.post(api_url, data=payload, headers=headers)
        response_str = response.json()
        data = response_str["monitors"]
        url_list = []
        for x in data:
            url = x.get("url")
            if url:
                url_list.append(url)
        return {
            "status": "true",
            "randydev":{
                "url": url_list,
            }
        }
    except:
        return {"status": "false", "message": "Error response."}

async def get_data(username):
    base_msg = ""
    async with AsyncClient() as gpx:
        req = (await gpx.get(f"https://api.github.com/users/{username}")).json()
        try:
            avatar = req["avatar_url"]
            twitter = req['twitter_username']
            base_msg += "**❆ Gitub Information ❆** \n\n"
            base_msg += f"**Profile Url:** {req['html_url']} \n"
            base_msg += f"**Name:** `{req['name']}` \n"
            base_msg += f"**Username:** `{req['login']}` \n"
            base_msg += f"**User ID:** `{req['id']}` \n"
            base_msg += f"**Location:** `{req['location']}` \n"
            base_msg += f"**Company:** `{req['company']}` \n"
            base_msg += f"**Blog:** `{req['name']}` \n"
            base_msg += f"**Twitter:** `{f'https://twitter.com/{twitter}' if twitter else 'None'}` \n"
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

@app.get("/ryuzaki/github", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
async def github(item: GithubUsernames):
    try:
        details = await get_data(item.username)
        return {
            "status": "true",
            "randydev":{
                "avatar": details[1],
                "results": details[0]
            }
        }
    except:
        return {"status": "false", "message": "Error response."}

@app.get("/ryuzaki/webshot", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def webshot(item: Webshot):
    try:
        required_url = f"https://mini.s-shot.ru/{item.quality}/{item.type_mine}/{item.pixels}/{item.cast}/?{item.url}"
        return {
            "status": "true",
            "randydev":{
                "image_url": required_url
            }
        }
    except:
        return {"status": "false", "message": "Error response."}

@app.get("/ryuzaki/chatbot", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def chatbot(item: ChatBots):
    api_url = b64decode("aHR0cHM6Ly9hcGkuc2Fmb25lLmRldi9jaGF0Ym90").decode("utf-8")
    params = {
        "query": item.query,
        "user_id": item.user_id,
        "bot_name": item.bot_name,
        "bot_master": item.bot_username
    }
    x = requests.get(f"{api_url}", params=params)
    if x.status_code != 200:
        return "Error api request"
    try:
        y = x.json()
        response = y["response"]
        return {
            "status": "true",
            "randydev":{
                "message": response
            }
        }
    except:
        return {"status": "false", "message": "Error response."}

@app.get("/ryuzaki/llama", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def get_llama(item: ChatgptCustom):
    api_url = SOURCE_WHAT_GAY_URL
    params = {"query": item.query}
    x = requests.get(f"{api_url}/llama", params=params)
    if x.status_code != 200:
        return "Error api request"
    try:
        y = x.json()
        response = y["answer"]
        return {
            "status": "true",
            "randydev":{
                "message": response
            }
        }
    except:
        return {"status": "false", "message": "Error response."}

@app.get("/ryuzaki/waifu", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def waifu_pics(item: WaifuPics):
    waifu_api = f"{SOURCE_WAIFU_URL}/{item.types}"
    waifu_param = f"{waifu_api}/{item.category}"

    response = requests.get(waifu_param)

    if response.status_code != 200:
        return "Sorry, there was an error processing your request. Please try again later"
    data_waifu = response.json()
    try:
        waifu_image_url = data_waifu["url"]
    except Exception as e:
        return f"Error request {e}"
    if waifu_image_url:
        if item.is_bytes:
            try:
                response_two = requests.get(waifu_image_url)
                response_two.raise_for_status()
            except requests.exceptions.RequestException:
                raise HTTPException(status_code=500, detail="Internal server error")
            return StreamingResponse(BytesIO(response_two.content), media_type=item.media_type)
        else:
            return {
                "status": "true",
                "randydev":{
                    "image_url": waifu_image_url
                }
            }
    else:
        return {"status": "false", "message": "Error response."}

@app.get("/ryuzaki/rayso", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def make_rayso(item: MakeRayso):
    trans = SyncTranslator()
    api_url = b64decode("aHR0cHM6Ly9hcGkuc2Fmb25lLm1lL3JheXNv").decode("utf-8")
    if item.auto_translate:
        source = trans.detect(item.code)
        translation = trans(item.code, sourcelang=source, targetlang=item.setlang)
        code = translation.text
    else:
        code = item.code
    if item.ryuzaki_dark:
        x = requests.post(
            f"{api_url}",
            json={
                "code": code,
                "title": item.title,
                "theme": item.theme,
                "darkMode": True
            }
        )
        if x.status_code != 200:
            return "Error api Gay"
        data = x.json()
        try:
            image_data = base64.b64decode(data["image"])
            return {
                "status": "true",
                "data":{
                    "image": image_data
                }
            }
        except:
            return {"status": "false", "message": "Error response"}
    else:
        x = requests.post(
            f"{api_url}",
            json={
                "code": code,
                "title": item.title,
                "theme": item.theme,
                "darkMode": False
            }
        )
        if x.status_code != 200:
            return "Error api Gay"
        data = x.json()
        try:
            image_data = base64.b64decode(data["image"])
            return {
                "status": "true",
                "data":{
                    "image": image_data
                }
            }
        except:
            return {"status": "false", "message": "Error response"}

@app.get("/ryuzaki/ipcheck")
def whois_ip_address(ip_address: str=None):
    apikey = kc("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
    location_link = "https"
    location_api = "api.ip2location.io"
    location_key = f"key={apikey}"
    location_search = f"ip={ip_address}"
    location_param = (
        f"{location_link}://{location_api}/?{location_key}&{location_search}"
    )
    response = requests.get(location_param)
    if response.status_code != 200:
        return "Sorry, there was an error processing your request. Please try again later"
    data_location = response.json()
    try:
        location_ip = data_location["ip"]
        location_code = data_location["country_code"]
        location_name = data_location["country_name"]
        location_region = data_location["region_name"]
        location_city = data_location["city_name"]
        location_zip = data_location["zip_code"]
        location_zone = data_location["time_zone"]
        location_card = data_location["as"]
    except Exception as e:
        return f"error {e}"
    if (
        location_ip
        and location_code
        and location_name
        and location_region
        and location_city
        and location_zip
        and location_zone
        and location_card
    ):
        return {
            "ip_address": location_ip,
            "country_code": location_code,
            "region_name": location_region,
            "city_name": location_city,
            "zip_code": location_zip,
            "time_zone": location_zone,
            "as": location_card
        }
    else:
        return {"status": "false", "message": "Invalid ip address"}

@app.get("/ryuzaki/tiktok_douyin", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def tiktok_douyin(item: TiktokDownloader):
    response = requests.get(f"{SOURCE_TIKTOK_WTF_URL}={item.tiktok_url}")
    if response.status_code != 200:
        return "Internal server error"
    try:
        download_video = response.json()["aweme_list"][0]["video"]["play_addr"]["url_list"][0]
        download_audio = response.json()["aweme_list"][0]["music"]["play_url"]["url_list"][0]
        description = response.json()["aweme_list"][0]["desc"]
        author = response.json()["aweme_list"][0]["author"]["nickname"]
        request = response.json()["aweme_list"][0]["author"]["signature"]
        return {
            "status": "true",
            "randydev": {
                "video_url": download_video,
                "music_url": download_audio,
                "description": description,
                "author": author,
                "request": request
            }
        }
    except:
        return {"status": "false", "message": "Error request"}

@app.get("/ryuzaki/tiktok", response_model=SuccessResponse, responses={422: {"model": ErrorStatus}})
def tiktok_downloader(item: TiktokBeta):
    api_devs = SOURCE_TIKTOK_TECH_URL
    parameter = f"tiktok?url={item.tiktok_url}"
    api_url = f"{api_devs}/{parameter}"
    response = requests.get(api_url)

    if response.status_code != 200:
        return "Error: Unable to fetch data from the TikTok API"
    try:
        results = response.json()
        caption = results.get("result", {}).get("desc", "")
        if item.only_video:
            video_url = results.get("result", {}).get("withoutWaterMarkVideo", "")
            if video_url:
                return {
                    "download_url": video_url,
                    "caption": caption
                }
        else:
            music_mp3 = results.get("result", {}).get("music", "")
            if music_mp3:
                return {
                    "music_url": music_mp3,
                    "caption": caption
                }
        return "Error: TikTok data not found or unsupported format"
    except:
        return {"status": "false", "message": "Invalid Link"}

@app.get("/ryuzaki/mediafire")
def mediafire(item: DownloadLink):
    try:
        down_link = str(item.link)
        mid = down_link.split('/', 5)
        if mid[3] == "view":
            mid[3] = "file"
            down_link = '/'.join(mid)
        r = requests.get(down_link)
        soup = BeautifulSoup(r.content, "html.parser")
        a_href = soup.find("a", {"class": "input popsok"}).get("href")
        a = str(a_href)
        id = link.split('/', 5)[4]
        a_byte = soup.find("a", {"class": "input popsok"}).get_text()
        a_name = soup.find("div", {"class": "dl-btn-label"}).get_text()
        details = soup.find("ul", {"class": "details"})
        li_items = details.find_all('li')[1]
        some = li_items.find_all("span")[0].get_text().split()
        dat = list(some)
        down = a_byte.replace(" ", "").strip()
        time = dat[1]
        date = dat[0]
        byte = down.split("(", 1)[1].split(")", 1)[0]
        name = a_name.replace(" ", "").strip()
        return SuccessResponse(
            status="True",
            randydev={
                "directDownload": a,
                "original": item.link,
                "id": id,
                "name": name,
                "readable": byte,
                "time": byte,
                "date": date
            }
        )
    except:
        return {'status': 'false', 'message': 'Invalid Link'}

@app.get("/ryuzaki/gdrive")
def gdrive(item: DownloadLink):
    try:
        down = link.split('/', 6)
        url = f'https://drive.google.com/uc?export=download&id={down[5]}'
        session = requests.Session()
        response = session.get(url, stream=True)
        headers = response.headers
        content_disp = headers.get('content-disposition')
        filename = None
        if content_disp:
            match = re.search(r'filename="(.+)"', content_disp)
            if match:
                filename = match.group(1)
        content_length = headers.get('content-length')
        last_modified = headers.get('last-modified')
        content_type = headers.get('content-type')
        return SuccessResponse(
            status="True",
            randydev={
                "directDownload": url,
                "original": item.link,
                "id": down[5],
                "name": filename if filename else "No filename provided by the server.",
                "readable": f"{round(int(content_length) / (1024 * 1024), 2)} MB" if content_length else "No content length provided by the server.",
                "type": content_type if content_type else "No content type provided by the server.",
                "DateAndTime": last_modified if last_modified else "No last modified date provided by the server."
            }
        )
    except:
        return {'status': 'false', 'message': 'Invalid Link'}

@app.get("/ryuzaki/anonfiles")
def anonfiles(item: DownloadLink):
    try:
        r = requests.get(item.link)
        soup = BeautifulSoup(r.content, "html.parser")
        a_href = soup.find("a", {"id": "download-url"}).get("href")
        a = str(a_href)
        id = link.split('/', 4)[3]
        jsondata = requests.get(f'https://api.anonfiles.com/v2/file/{id}/info').json()
        jsondata['data']['file']['url']['directDownload'] = a
        del jsondata['data']['file']['url']['full']
        return jsondata
    except:
        return "{'status': 'false', 'message': 'Invalid Link'}"

@app.get("/ryuzaki/filechan")
def filechan(item: DownloadLink):
    try:
        r = requests.get(item.link)
        soup = BeautifulSoup(r.content, "html.parser")
        a_href = soup.find("a", {"id": "download-url"}).get("href")
        a = str(a_href)
        id = link.split('/', 4)[3]
        jsondata = requests.get(f'https://api.filechan.org/v2/file/{id}/info').json()
        jsondata['data']['file']['url']['directDownload'] = a
        del jsondata['data']['file']['url']['full']
        return jsondata
    except:
        return {'status': 'false', 'message': 'Invalid Link'}

@app.get("/ryuzaki/letsupload")
def letsupload(item: DownloadLink):
    try:
        r = requests.get(item.link)
        soup = BeautifulSoup(r.content, "html.parser")
        a_href = soup.find("a", {"id": "download-url"}).get("href")
        a = str(a_href)
        id = link.split('/', 4)[3]
        jsondata = requests.get(f'https://api.letsupload.cc/v2/file/{id}/info').json()
        jsondata['data']['file']['url']['directDownload'] = a
        del jsondata['data']['file']['url']['full']
        return jsondata
    except:
        return {'status': 'false', 'message': 'Invalid Link'}

@app.get("/ryuzaki/megaupload")
def megaupload(item: DownloadLink):
    try:
        r = requests.get(item.link)
        soup = BeautifulSoup(r.content, "html.parser")
        a_href = soup.find("a", {"id": "download-url"}).get("href")
        a = str(a_href)
        id = link.split('/', 4)[3]
        jsondata = requests.get(f'https://api.megaupload.nz/v2/file/{id}/info').json()
        jsondata['data']['file']['url']['directDownload'] = a
        del jsondata['data']['file']['url']['full']
        return jsondata
    except:
        return {'status': 'false', 'message': 'Invalid Link'}

@app.get("/ryuzaki/myfile")
def myfile(item: DownloadLink):
    try:
        r = requests.get(item.link)
        soup = BeautifulSoup(r.content, "html.parser")
        a_href = soup.find("a", {"id": "download-url"}).get("href")
        a = str(a_href)
        id = link.split('/', 4)[3]
        jsondata = requests.get(f'https://api.myfile.is/v2/file/{id}/info').json()
        jsondata['data']['file']['url']['directDownload'] = a
        del jsondata['data']['file']['url']['full']
        return jsondata
    except:
        return {'status': 'false', 'message': 'Invalid Link'}

description = """
- Ryuzaki Library: [Library Here](https://github.com/TeamKillerX/RyuzakiLib)

•Developed by [@xtdevs](https://t.me/xtdevs)
"""
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="RyuzakiLib API",
        version="2.2.1",
        summary="Use It Only For Personal Project Else I Need To Delete The Api",
        description=description,
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://github-production-user-asset-6210df.s3.amazonaws.com/90479255/289277800-f26513f7-cdf4-44ee-9a08-f6b27e6b99f7.jpg"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
