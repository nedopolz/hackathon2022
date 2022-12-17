from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

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


@router.post("/save", description="Сохранить ответы на вопросы")
async def save_answers(
    question_and_answer: list[QuestionAndAnswer], answer_service=Depends(get_answer_service)
):
    q_a = answer_service.save_question_answers(
        question_and_answer
    )

    if q_a:
        return JSONResponse({"success": True})

    return JSONResponse({"success": False})
