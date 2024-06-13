from os import getenv
from dotenv import load_dotenv
load_dotenv()

API_ID = (getenv("API_ID")
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
LOG_ID = ("-4220293329")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)
SUDO_USER = list(map(int, getenv("SUDO_USER", "").split()))
