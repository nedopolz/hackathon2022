from functools import lru_cache

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.models import Portfolio, InstrumentPortfolio, Instrument, QuestionsAnswer, Question, Answer
from api.schemas.portfolio import PortfolioSchema, InstrumentSchema
from db import database
from calculations.portfilio_risk_calc import pr


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

        query = Portfolio.__table__.update().values(acceptable_risk_degree=acceptable_risk_degree).where(Portfolio.id == portfolio_id)
        portfolio = await self.database.execute(query)
        return portfolio


@lru_cache()
def get_portfolio_db_service():
    return PortfolioService()
