from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_play = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Монетка"),
            KeyboardButton(text="Камень Ножницы Бумага")
        ],
        [
            KeyboardButton(text="Меню")
        ]
    ],
    resize_keyboard=True
)