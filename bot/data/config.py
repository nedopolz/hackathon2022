import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
POSTGRES_USER = str(os.getenv("POSTGRES_USER"))
POSTGRES_PASSWORD = str(os.getenv("POSTGRES_PASSWORD"))
POSTGRES_DB = str(os.getenv("POSTGRES_DB"))
DBHOST = str(os.getenv("DBHOST"))

admins = [
    419519710
]

admin_chat_id = int(os.getenv("admin_chat_id"))

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

debug = False

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

POSTGRES_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DBHOST}/{POSTGRES_DB}"
