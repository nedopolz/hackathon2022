from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.question import QuestionAndHisAnswer, QuestionAndAnswer
from api.services.db.questions import get_questions_service, get_answer_service
from api.services.db.session import get_session

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get("/", description="Получить список вопросов для пользователя", response_model=list[QuestionAndHisAnswer])
async def get_questions(
    question_service=Depends(get_questions_service), session: AsyncSession = Depends(get_session)
):
    questions = await question_service.get_question(session)
    return questions


@router.get("/save", description="Сохранить ответы на вопросы")
async def save_answers(
    answer_service=Depends(get_answer_service)
):
    await answer_service.save_question_answer(1, 2, 1)
