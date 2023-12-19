from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_knb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🪨"),
            KeyboardButton(text="✂️"),
            KeyboardButton(text="🧻"),
        ],
        [
            KeyboardButton(text="К играм"),
            KeyboardButton(text="Меню")
        ]

    ],
    resize_keyboard=True
)