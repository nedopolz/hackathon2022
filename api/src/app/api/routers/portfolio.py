from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.services.db.potrfolio import get_portfolio_db_service
from api.services.db.session import get_session

router = APIRouter(prefix="/portfolio", tags=["Portfolio"])


@router.get("/{user_id}", description="Получить портфель пользователя")
async def get_portfolio(
        user_id: int, portfolio_service=Depends(get_portfolio_db_service), session: AsyncSession = Depends(get_session)
):
    portfolios = await portfolio_service.get_portfolio(user_id, session)
    return portfolios


@router.post("/", description="Создать портфель пользователя")
async def create_portfolio():
    pass


@router.delete("/", description="Удалить портфель пользователя")
async def delete_portfolio():
    pass


@router.put("/", description="Изменить портфель пользователя")
async def put_portfolio():
    pass
