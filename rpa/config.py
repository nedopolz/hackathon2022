import os

from dotenv import load_dotenv

load_dotenv()
database_host = os.getenv("DATABASE_HOST")
database_port = os.getenv("DATABASE_PORT")
database_user = os.getenv("DATABASE_USER")
database_password = os.getenv("DATABASE_PASSWORD")
database_name = os.getenv("DATABASE_NAME")

database_url = f"postgresql+asyncpg://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"

tinkoff_api_key = os.getenv("TINKOFF_API_KEY")
