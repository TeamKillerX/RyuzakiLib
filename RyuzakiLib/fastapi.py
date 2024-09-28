import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from functools import wraps
from typing import *

import requests
from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.sessions import SessionMiddleware


class FastAPISuper:
    def __init__(
        self,
        docs_url=None,
        redoc_url="/",
        config=None,
        mongo_url=None,
        bot_token=None,
    ):
        self.docs_url = docs_url
        self.redoc_url = redoc_url
        self.fastapi = FastAPI(docs_url=self.docs_url, redoc_url=self.redoc_url)
        self.auth = OAuth(config)
        self.async_mongodb = AsyncIOMotorClient(mongo_url)
        self.bot_token = bot_token
        self.api_endpoint = "https://api.telegram.org"

    def async_motor_client(self):
        return self.async_mongodb

    def logger(self):
        logging.basicConfig(level=logging.ERROR)
        logging.basicConfig(level=logging.INFO)
        LOGS = logging.getLogger("[fastapi]")
        return LOGS

    def send_verification_email(
        self,
        sender_email=None,
        password=None,
        receiver_email=None,
        custom_text=None,
    ):
        try:
            LOGS = self.logger()
            smtp_server = "smtp.gmail.com"
            port = 587
            msg = MIMEMultipart()
            msg["From"] = 'RyuzakiLib <no-reply@gmail.com>'
            msg["To"] = receiver_email
            msg["Subject"] = "Verify Email - RyuzakiLib API"
            html = f"""
            <html>
            <body>
               <p>Click the button below to verify your email address:</p>
               {custom_text}
            </body>
            </html>
            """
            msg.attach(MIMEText(html, 'html'))
            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            LOGS.info("Email sent successfully!")
        except Exception:
            raise HTTPException(status_code=404, detail="can't send email issue")

    def auth_register(
        self,
        auth0_client_id=None,
        auth0_client_secrect=None,
        auth0_domain=None,
        domain_url=None
    ):
        self.auth.register(
            name="auth0",
            client_id=auth0_client_id,
            client_secret=auth0_client_secrect,
            client_kwargs={
                "scope": "openid profile email",
                "redirect_url": f"{domain_url}/callback"
            },
            server_metadata_url=f"https://{auth0_domain}/.well-known/openid-configuration"
        )

    async def authorize_redirect(self, request=None, redirect_uri=None):
        return await self.auth.auth0.authorize_redirect(
            request,
            redirect_uri=redirect_uri,
            scope="openid profile email",
            response_type="code"
        )

    async def authorize_access_token(self, request=None):
        token = await self.auth.auth0.authorize_access_token(request)
        return token

    async def send_message(self, chat_id: int, text: str, parse_mode: str = "Markdown", disable_web_page_preview: bool = True) -> None:
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_web_page_preview": disable_web_page_preview
        }
        return requests.post(
            f"{self.api_endpoint}/bot{self.bot_token}/sendMessage",
            data=payload
        )

    def moderator(self):
        return self.fastapi

    def only_apikey(self, valid_api_keys=None):
        def decorator(func):
            @wraps(func)
            async def wrapper(*args, **kwargs):
                request: Request = kwargs.get("request") or args[0]
                api_key = request.headers.get("X-API-KEY")
                if api_key not in valid_api_keys:
                    raise HTTPException(status_code=403, detail="Invalid API Key")
                return await func(*args, **kwargs)
            return wrapper
        return decorator

    def add_session_middleware(self, secret_key=None):
        self.fastapi.add_middleware(
            SessionMiddleware,
            secret_key=secret_key
        )

    def add_cors_middleware(self):
        self.fastapi.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
