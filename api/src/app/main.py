import uvicorn
from fastapi import FastAPI

from api.routers.portfolio import router as portfolio_router
from api.routers.questions import router as question_router
from db import database

app = FastAPI()
app.include_router(question_router)
app.include_router(portfolio_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)  # TODO заменить
