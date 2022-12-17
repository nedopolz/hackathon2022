from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    telegram_id: str


class UserCreateSchema(BaseModel):
    telegram_id: str
