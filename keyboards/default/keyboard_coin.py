from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_coin = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Орел"),
            KeyboardButton(text="Решка"),

        ],
        [
            KeyboardButton(text="К играм"),
            KeyboardButton(text="Меню")
        ]
    ],
    resize_keyboard=True
)