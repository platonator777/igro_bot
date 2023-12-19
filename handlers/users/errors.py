from aiogram import types
from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=3)
@dp.message_handler()
async def command_error(message: types.Message):
    if message.text != "Камень Ножницы Бумага" and message.text != "Монетка":
        await message.answer(f"такой команды нету")
