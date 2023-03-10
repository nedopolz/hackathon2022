from functools import lru_cache

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.models import Portfolio, InstrumentPortfolio, Instrument, QuestionsAnswer, Question, Answer
from api.schemas.portfolio import PortfolioSchema, InstrumentSchema
from calculations.instrument_calc import ic
from db import database
from calculations.portfilio_risk_calc import pr

from src.app.calculations.portfoli_calc import pg


class PortfolioService:
    def __init__(self):
        self.database = database

    async def get_portfolios(self, user_id: int, session: AsyncSession):
        portfolios = await session.execute(select(Portfolio).where(Portfolio.user_id == user_id))
        portfolios = [dict(portfolio) for portfolio in portfolios]
        for portfolio in portfolios:
            instruments = await session.execute(select(InstrumentPortfolio, Instrument).where(
                InstrumentPortfolio.portfolio_id == portfolio["Portfolio"].id).join(Instrument).where(
                InstrumentPortfolio.instrument_id == Instrument.id))
            instruments = [dict(instrument) for instrument in instruments]
            portfolio["Portfolio"].instruments = [InstrumentSchema(**instrument) for instrument in instruments]

        return [
            PortfolioSchema(
                id=portfolio["Portfolio"].id,
                name=portfolio["Portfolio"].name,
                portfolio_risk_degree=portfolio["Portfolio"].portfolio_risk_degree,
                acceptable_risk_degree=portfolio["Portfolio"].acceptable_risk_degree,
                assets=[
                    InstrumentSchema(
                        id=instrument["Instrument"].id,
                        name=instrument["Instrument"].name,
                        amount=instrument["Instrument"].amount,
                        price=instrument["Instrument"].price
                    )
                    for instrument in portfolio["Portfolio"].instruments]
            )
            for portfolio in portfolios
        ]

    async def get_portfolio(self, portfolio_id: int, session: AsyncSession):
        portfolios = await session.execute(select(Portfolio).where(Portfolio.id == portfolio_id))
        portfolios = [dict(portfolio) for portfolio in portfolios]
        return portfolios[0]["Portfolio"]

    async def create_portfolio(self, data: dict):
        query = Portfolio.__table__.insert().values(**data)
        portfolio = await self.database.execute(query)
        return portfolio

    async def del_portfolio(self, portfolio_id: int):
        query = Portfolio.__table__.delete().where(Portfolio.id == portfolio_id)
        portfolio = await self.database.execute(query)
        return portfolio

    async def set_acceptable_risk_degree(self, portfolio_id: int, session: AsyncSession):
        portfolio = await session.execute(
            select(Portfolio, QuestionsAnswer, Question, Answer)
            .join(QuestionsAnswer, QuestionsAnswer.portfolio_id == Portfolio.id)
            .join(Question, Question.id == QuestionsAnswer.question_id)
            .join(Answer, Answer.id == QuestionsAnswer.answer_id)
            .where(Portfolio.id == portfolio_id)
        )

        q_a = {question.question: answer.answer for _, _, question, answer in portfolio}
        acceptable_risk_degree = pr.calculate(q_a)
        query = Portfolio.__table__.update().values(acceptable_risk_degree=acceptable_risk_degree).where(
            Portfolio.id == portfolio_id)
        portfolio = await self.database.execute(query)
        return portfolio

    async def generate_portfolio(self, portfolio_id: int, session: AsyncSession):
        instruments = await session.execute(select(Instrument))
        instruments = [dict(instrument) for instrument in instruments]
        instruments = [instrument["Instrument"] for instrument in instruments]
        instruments = [{"instrument_degree": instrument.instrument_degree,
                        "price": instrument.price,
                        "id": instrument.id
                        } for instrument in instruments]
        personal_risk_index = await self.get_portfolio(portfolio_id, session)
        personal_risk_index = personal_risk_index.acceptable_risk_degree
        investment_amount = 100000
        data = pg.generate(personal_risk_index, instruments, investment_amount)
        return data


class InstrumentService:
    def __init__(self):
        self.database = database

    async def set_instrument_degree(self, session: AsyncSession):
        instruments = await session.execute(
            select(Instrument)
        )

        for instrument in instruments:
            data = instrument[0].data[0]
            instrument_degree = ic.instruments_risk_calculate(data)

            query = Instrument.__table__.update().values(instrument_degree=instrument_degree).where(
                Instrument.id == instrument[0].id)
            instrument = await self.database.execute(query)


@lru_cache()
def get_portfolio_db_service():
    return PortfolioService()


@lru_cache()
def get_instrument_db_service():
    return InstrumentService()
