from functools import lru_cache
from databases import Database

from config import database_url

from db.models import Instrument

database = Database(database_url, min_size=5, max_size=20)


class InstrumentService:
    def __init__(self):
        self.database = database

    async def create_operation(self, params: dict):
        query = Instrument.__table__.insert().values(**params)
        operation = await self.database.execute(query)
        return operation


@lru_cache()
def get_instrumentDB_service():
    return InstrumentService()

