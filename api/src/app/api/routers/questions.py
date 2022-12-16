from fastapi import APIRouter

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get("/", description="Получить список вопросов для пользователя")
async def get_questions():
    pass
