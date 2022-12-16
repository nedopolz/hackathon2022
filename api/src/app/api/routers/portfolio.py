from fastapi import APIRouter

router = APIRouter(prefix="/portfolio", tags=["Portfolio"])


@router.get("/", description="Получить портфель пользователя")
async def get_portfolio():
    pass


@router.post("/", description="Создать портфель пользователя")
async def create_portfolio():
    pass


@router.delete("/", description="Удалить портфель пользователя")
async def delete_portfolio():
    pass


@router.put("/", description="Изменить портфель пользователя")
async def put_portfolio():
    pass
