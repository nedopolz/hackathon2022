from aiogram.types import CallbackQuery

from data.config import debug
from data.text_config import DESCRIPTION
from keyboards.inline.user_keyboards import back_keyboard
from loader import dp


@dp.callback_query_handler(text="description", state="*")
async def description(call: CallbackQuery):
    if debug:
        await call.message.answer("description")
    await call.message.edit_text(DESCRIPTION, reply_markup=back_keyboard)
