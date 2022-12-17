from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from data.config import debug
from data.text_config import RISK_PROFILE
from keyboards.inline.user_keyboards import generate_answers_keyboard, generate_portfolio_keyboard
from loader import dp, api
from states.portfolio_generation import PortfolioState


@dp.callback_query_handler(text_contains="generate_portfolio", state="*")
async def generate_portfolio(call: CallbackQuery, state: FSMContext):
    if debug:
        await call.message.answer("generate_portfolio")
    data_list = call.data.split(":")
    if not await state.get_state():
        await PortfolioState.init.set()
        questions = await api.get_questions()
        portfolio = await api.create_portfolio(call.from_user.id)
        await state.set_data(
            {"questions": questions, "answered_questions_number": 0, "answers": [], "portfolio_id": portfolio})
    print('1')
    if len(data_list) > 1:
        print('2')
        answer_id = data_list[1]
        question_id = data_list[2]
        answers = await state.get_data()
        answers = answers.get("answers")
        answers.append({"question_id": question_id, "answer_id": answer_id})
        await state.update_data(answers=answers)
        data = await state.get_data()
        answered_questions = data.get("answered_questions_number")
        await state.update_data(answered_questions_number=int(answered_questions) + 1)
    data = await state.get_data()
    questions = data.get("questions")
    answered_questions = data.get("answered_questions_number")
    print('3')
    if len(questions) == answered_questions:
        risk_profile = await api.get_risk_profile(call.from_user.id)
        await call.message.edit_text(text=RISK_PROFILE.format(risk_profile),
                                     reply_markup=generate_portfolio_keyboard)
        data = await state.get_data()
        answers = data.get("answers")
        await api.save_answers(answers, portfolio_id=data.get("portfolio_id"))
        await state.finish()
        return
    question = questions[answered_questions]
    keyboard = generate_answers_keyboard(question.get("answers"), question_id=question.get("question").get("id"))
    await call.message.edit_text(text=question.get("question").get("question"), reply_markup=keyboard)
