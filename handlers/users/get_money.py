from aiogram import types
from loader import dp
from asyncio import sleep
from filters import IsPrivate
from utils.db_api.quick_comands import update_balance, select_user
from utils.misc import rate_limit


@rate_limit(limit=2)
@dp.message_handler(IsPrivate(), text = "Получить Деньги")
async def check_message(message: types.Message):
    user_id = message.from_user.id
    user = await select_user(user_id)
    balance = user.balance
    if balance >= 100:
        await message.answer("Ты можешь получить деньги, если твой баланс ниже 100")
    else:
        await update_balance(user_id, 1000)
        await message.answer("+1000")
