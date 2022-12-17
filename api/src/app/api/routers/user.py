from api.schemas.user import UserSchema, UserCreateSchema
from api.services.db.potrfolio import get_portfolio_db_service
from api.services.db.session import get_session
from api.services.db.user import get_user_db_service
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/{telegram_id}", description="Получить юзера по telegram id", response_model=UserSchema)
async def get_user_by_tg_id(telegram_id: str, user_service=Depends(get_user_db_service),
                            portfolio_service=Depends(get_portfolio_db_service),
                            session: AsyncSession = Depends(get_session)):
    user = await user_service.get_user_by_tg_id(telegram_id)
    if not user:
        return JSONResponse(None, status_code=404)
    portfolio = await portfolio_service.get_portfolios(user.id, session=session)
    if not portfolio:
        portfolio = None
    else:
        portfolio = portfolio[0].portfolio_risk_degree
    return UserSchema(id=user.id, telegram_id=user.telegram_id, risk_profile=portfolio)


@router.post("/", description="Создать пользователя")
async def create_user(user: UserCreateSchema, user_service=Depends(get_user_db_service)):
    data = user.dict()
    new_user = await user_service.create_user(data)
    if new_user:
        return JSONResponse({"success": True, "id": new_user})

    return JSONResponse({"success": False})
