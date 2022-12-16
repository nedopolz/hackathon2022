from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_button = InlineKeyboardButton(text="Назад", callback_data="back")
back_keyboard = InlineKeyboardMarkup().add(back_button)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Описание", callback_data='description'),
        ],
        [
            InlineKeyboardButton(text="Сгенерировать портфель", callback_data='generate_portfolio'),
        ],
        [
            InlineKeyboardButton(text="Изменить портфель", callback_data='change_portfolio'),
        ],
        [
            InlineKeyboardButton(text="Мой портфель", callback_data='my_portfolio'),
        ],

    ],
    resize_keyboard=True
)

generate_portfolio_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Посмотреть портфель", callback_data='my_portfolio'),
        ],
    ], resize_keyboard=True
)


def generate_answers_keyboard(answers, question_id):
    keyboard = InlineKeyboardMarkup()
    for answer in answers:
        keyboard.add(
            InlineKeyboardButton(text=answer.get("text"), callback_data=f"generate_portfolio:{answer.get('id')}:{question_id}"))
    keyboard.add(back_button)
    return keyboard
