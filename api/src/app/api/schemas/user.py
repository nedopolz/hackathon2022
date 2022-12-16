from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    telegram_id: str
