from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas.question import QuestionAndHisAnswer
from api.services.db.questions import get_questions_service
from api.services.db.session import get_session

router = APIRouter(prefix="/questions", tags=["Questions"])


@router.get("/", description="Получить список вопросов для пользователя", response_model=list[QuestionAndHisAnswer])
async def get_questions(
    question_service=Depends(get_questions_service), session: AsyncSession = Depends(get_session)
):
    questions = await question_service.get_question(session)
    return questions
