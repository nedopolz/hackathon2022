from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    telegram_id: str
    risl_profile: str | None = None


class UserCreateSchema(BaseModel):
    telegram_id: str
