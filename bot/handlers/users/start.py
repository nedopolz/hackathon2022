from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Text
from aiogram.types import CallbackQuery

from data.config import debug
from keyboards.inline.user_keyboards import menu
from loader import dp

from data.text_config import HELLO_NEW_UESR, MAIN_MENU
from loader import api


@dp.callback_query_handler(text="back", state="*")
async def back_query(call: CallbackQuery, state: FSMContext):
    if debug:
        await call.message.answer("back_query")
    await call.message.edit_text(MAIN_MENU, reply_markup=menu)


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message, state: FSMContext):
    if debug:
        await message.answer("Приветствую, дорогой инвестор! Добро пожаловать в бота-помощника InvestHelper. "
                             "Для ознакомления с работой бота нажмите на кнопку 'Инструкция'."
                             "Желаем удачи!")
    user = await api.get_user_by_tg_id(message.from_user.id)
    if not user:
        full_name = message.from_user.full_name
        tg_id = message.from_user.id
        await api.create_user(full_name, tg_id)
        await message.answer(HELLO_NEW_UESR, reply_markup=menu)
        return
    await message.answer(text=MAIN_MENU, reply_markup=menu)

