from fastapi import APIRouter, Depends

from api.schemas.user import UserSchema
from api.services.db.user import get_user_db_service

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/{telegram_id}", description="Получить юзера по telegram id", response_model=UserSchema)
async def get_user_by_tg_id(telegram_id: str, user_service=Depends(get_user_db_service)):
    user = await user_service.get_user_by_tg_id(telegram_id)
    return UserSchema(id=user.id, telegram_id=user.telegram_id)
