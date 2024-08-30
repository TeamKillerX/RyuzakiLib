from authlib.integrations.starlette_client import OAuth
from fastapi import FastAPI, Request, HTTPException
from functools import wraps
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

class FastAPISuper:
    def __init__(
        self,
        docs_url=None,
        redoc_url=None,
        config=None,
        mongo_url=None
    ):
        self.docs_url = docs_url
        self.redoc_url = redoc_url
        self.fastapi = FastAPI(docs_url=self.docs_url, redoc_url=self.redoc_url)
        self.auth = OAuth(config)
        self.mongodb = AsyncIOMotorClient(mongo_url)

    def client_db(self):
        return self.mongodb

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
