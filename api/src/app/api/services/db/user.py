from functools import lru_cache

from src.app.api.models.models import User
from src.app.db import database


class UserService:
    def __init__(self):
        self.database = database

    async def get_user_by_tg_id(self, telegram_id: str):
        query = User.__table__.select().where(User.telegram_id == telegram_id)
        user = await self.database.fetch_one(query)
        return user

    async def create_user(self, data: dict):
        query = User.__table__.insert().values(**data)
        user = await self.database.execute(query)
        return user


@lru_cache()
def get_user_db_service():
    return UserService()
