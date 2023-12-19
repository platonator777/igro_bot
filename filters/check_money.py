from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from utils.db_api.quick_comands import select_user
from keyboards.default import kb_menu
class enough_money(BoundFilter):
    async def check(self, message: types.Message):
        ok = False
        user_id = message.from_user.id
        user = await select_user(user_id)
        balance = user.balance
        stake = user.stake
        if balance < stake:
            await message.answer("недостаточно денег", reply_markup=kb_menu)
        else:
            ok = True
        return ok
