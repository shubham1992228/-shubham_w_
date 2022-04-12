import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "shubham 712")
ALIVE_NAME = getenv("ALIVE_NAME", "Shubham 712")
BOT_USERNAME = getenv("BOT_USERNAME", "shubham_w_712")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "shubham_712")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Old is Gold")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Old is Gold")
UPSTREAM_REPO = getenv("UPSTREAM_REPO","https://github.com/shubham1992228/NOBITA_JAAN?organization=shubham1992228&organization=shubham1992228")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/9ef29940fd5d6d7bc756c.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/9ef29940fd5d6d7bc756c.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/9ef29940fd5d6d7bc756c.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/9ef29940fd5d6d7bc756c.jpg")
