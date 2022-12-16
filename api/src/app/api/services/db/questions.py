from functools import lru_cache

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.models.models import Question, Answer, QuestionsAnswer
from api.schemas.question import QuestionAndHisAnswer, QuestionSchema, AnswerSchema
from db import database


class QuestionsService:
    def __init__(self):
        self.database = database

    async def get_question(self, session: AsyncSession) -> list[QuestionAndHisAnswer]:
        questions_and_his_answer = await session.execute(
            select(Question, Answer).join(Answer)
        )

        questions_and_his_answer_dict = {}
        for questions, answer in questions_and_his_answer:
            questions_and_his_answer_dict.setdefault(questions, []).append(answer)

        return [
            QuestionAndHisAnswer(
                question=QuestionSchema(id=question.id, question=question.question),
                answers=[AnswerSchema(id=answer.id, answer=answer.answer) for answer in answers]
            )
            for question, answers in questions_and_his_answer_dict.items()
        ]


class AnswerService:
    def __init__(self):
        self.database = database

    # async def save_question_answer(self, answer_id, question_id, portfolio_id):
    #     query = QuestionsAnswer.__table__.insert().values(answer_id=answer_id, question_id=question_id, portfolio_id=portfolio_id)


@lru_cache()
def get_questions_service():
    return QuestionsService()


@lru_cache()
def get_answer_service():
    return AnswerService()
