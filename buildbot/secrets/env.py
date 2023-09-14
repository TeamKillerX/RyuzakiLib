from dotenv import load_dotenv
from base64 import b64decode
from os import getenv

API_ID = int(getenv("API_ID", b64decode("").decode("utf-8")))
API_HASH = getenv("API_HASH", b64decode("").decode("utf-8"))
TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN", b64decode("").decode("utf-8"))
