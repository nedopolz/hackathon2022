import uvicorn
from fastapi import FastAPI

from api.routers.portfolio import router as portfolio_router
from api.routers.questions import router as question_router
from api.routers.user import router as user_router
from db import database

app = FastAPI()
app.include_router(question_router)
app.include_router(portfolio_router)
app.include_router(user_router)


@app.on_event("startup")
async def startup_event():
    await database.connect()
    app.state.db = database


@app.on_event("shutdown")
async def shutdown_event():
    if not app.state.db:
        await app.state.db.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)  # TODO заменить
