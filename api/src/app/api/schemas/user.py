from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    tg_id: str