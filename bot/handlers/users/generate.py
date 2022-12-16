from aiogram.types import CallbackQuery

from data.config import debug
from data.text_config import DESCRIPTION, RISK_PROFILE
from keyboards.inline.user_keyboards import generate_answers_keyboard, generate_portfolio_keyboard
from loader import dp, api


@dp.callback_query_handler(text_contains="generate_portfolio", state="*")
async def generate_portfolio(call: CallbackQuery):
    if debug:
        await call.message.answer("generate_portfolio")
    data_list = call.data.split(":")
    if len(data_list) > 1:
        answer_id = data_list[1]
        question_id = data_list[2]
        await api.save_answer(answer_id, question_id, call.from_user.id)
    question = await api.get_question(call.from_user.id)
    if not question:
        risk_profile = await api.get_risk_profile(call.from_user.id)
        await call.message.edit_text(text=RISK_PROFILE.format(risk_profile.get("name")),
                                     reply_markup=generate_portfolio_keyboard)
        return
    keyboard = generate_answers_keyboard(question.get("answers"), question_id=question.get("id"))
    await call.message.edit_text(text=question.get("name"), reply_markup=keyboard)
