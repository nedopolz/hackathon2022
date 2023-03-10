from api.schemas.portfolio import CreatePortfolio
from api.services.db.potrfolio import get_portfolio_db_service, get_instrument_db_service
from api.services.db.session import get_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from starlette.responses import JSONResponse

router = APIRouter(prefix="/portfolio", tags=["Portfolio"])


@router.get("/{user_id}", description="Получить портфель пользователя")
async def get_portfolio(
        user_id: int, portfolio_service=Depends(get_portfolio_db_service), session: AsyncSession = Depends(get_session)
):
    portfolios = await portfolio_service.get_portfolios(user_id, session)
    return portfolios


@router.post("/", description="Создать портфель пользователя")
async def create_portfolio(
        portfolio: CreatePortfolio, portfolio_service=Depends(get_portfolio_db_service)
):
    data = portfolio.dict()
    new_portfolio = await portfolio_service.create_portfolio(data)
    if new_portfolio:
        return JSONResponse({"success": True, "id": new_portfolio})

    return JSONResponse({"success": False})


@router.delete("/{portfolio_id}", description="Удалить портфель пользователя")
async def delete_portfolio(portfolio_id: int, portfolio_service=Depends(get_portfolio_db_service)):
    portfolio = await portfolio_service.del_portfolio(portfolio_id)
    if portfolio:
        return JSONResponse({"status": "ok"})
    return JSONResponse({"status": "not found"}, status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{portfolio_id}", description="Изменить портфель пользователя")
async def put_portfolio():
    pass


@router.post("/calc_instrument_degree")
async def calc_instrument_degree(i_s=Depends(get_instrument_db_service), session: AsyncSession = Depends(get_session)):
    await i_s.set_instrument_degree(session)


@router.post("/generate_portfolio/{portfolio_id}")
async def generate_portfolio(portfolio_id: int, session: AsyncSession = Depends(get_session),
                             portfolio_service=Depends(get_portfolio_db_service)):
    data = await portfolio_service.generate_portfolio(portfolio_id, session)
    return data
