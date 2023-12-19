from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from data.config import admins_id

class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        ok = False
        for id in admins_id:
            if message.from_user.id == id:
                ok = True
        return ok