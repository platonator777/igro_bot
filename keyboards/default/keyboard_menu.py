from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Играть")
        ],
        [
            KeyboardButton(text="Профиль"),
            KeyboardButton(text="Установить ставку")
        ],
        [
            KeyboardButton(text="Получить Деньги")
        ]
    ],
    resize_keyboard=True
)