from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from api.schemas.question import QuestionAndHisAnswer, QuestionAndAnswer
from api.services.db.potrfolio import get_portfolio_db_service
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
        question_and_answer: list[QuestionAndAnswer], answer_service=Depends(get_answer_service),
        portfolio_service=Depends(get_portfolio_db_service), session: AsyncSession = Depends(get_session)
):

    try:
        qu_a = await answer_service.save_question_answers(
            question_and_answer
        )
    except:
        return JSONResponse({"success": False})

    await portfolio_service.set_acceptable_risk_degree(question_and_answer[0].portfolio_id, session)
    return JSONResponse({"success": True})
