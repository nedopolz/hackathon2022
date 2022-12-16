from functools import lru_cache

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.models import Portfolio, InstrumentPortfolio, Instrument
from api.schemas.portfolio import PortfolioSchema, InstrumentSchema
from db import database


class PortfolioService:
    def __init__(self):
        self.database = database

    async def get_portfolios(self, user_id: int, session: AsyncSession):
        portfolios = await session.execute(
            select(Portfolio, InstrumentPortfolio, Instrument).join(InstrumentPortfolio).join(Instrument).where(
                Portfolio.user_id == user_id)
        )

        portfolios_dict = {}
        for portfolio, _, instrument in portfolios:
            portfolios_dict.setdefault(portfolio, []).append(instrument)

        return [
            PortfolioSchema(
                id=portfolio.id,
                name=portfolio.name,
                portfolio_risk_degree=portfolio.portfolio_risk_degree,
                assets=[
                    InstrumentSchema(
                        id=instrument.id,
                        name=instrument.name,
                        amount=instrument.amount,
                        price=instrument.price
                    )
                    for instrument in instruments
                ]
            )
            for portfolio, instruments in portfolios_dict.items()
        ]

    # async def create_user(self, data: dict):
    #     query = Portfolio.__table__.insert().values(**data)
    #     user = await self.database.execute(query)
    #     return user


@lru_cache()
def get_portfolio_db_service():
    return PortfolioService()
