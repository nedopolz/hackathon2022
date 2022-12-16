from pydantic import BaseModel


class QuestionSchema(BaseModel):
    id: int
    question: str


class AnswerSchema(BaseModel):
    id: int
    answer: str


class QuestionAndHisAnswer(BaseModel):
    question: QuestionSchema
    answers: list[AnswerSchema]


class QuestionAndAnswer(BaseModel):
    portfolio_id: int
    question_id: int
    answer_id: int
