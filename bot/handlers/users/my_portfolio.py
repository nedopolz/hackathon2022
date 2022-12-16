from aiogram.types import CallbackQuery

from data.config import debug
from data.text_config import DESCRIPTION, RISK_PROFILE
from keyboards.inline.user_keyboards import generate_answers_keyboard, generate_portfolio_keyboard, back_keyboard
from loader import dp, api


@dp.callback_query_handler(text_contains="my_portfolio", state="*")
async def my_portfolio(call: CallbackQuery):
    if debug:
        await call.message.answer("my_portfolio")
    portfolio = await api.get_portfolio(call.from_user.id)
    if not portfolio:
        await call.message.edit_text("Генерация в процессе погодь малех", reply_markup=generate_portfolio_keyboard)
        return
    assets = portfolio.get("assets")
    text = "Ваш портфель:\n"
    for asset in assets:
        text += f"{asset.get('name')} - {asset.get('amount')} - {asset.get('total_price')}\n"
    await call.message.edit_text(text=text, reply_markup=back_keyboard)
