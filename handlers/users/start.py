from aiogram import types
from loader import dp
from filters import IsPrivate
from utils.db_api import quick_comands as com
from keyboards.default import kb_menu
from utils.misc import rate_limit

@rate_limit(limit=2)
@dp.message_handler(IsPrivate(), text = ["/start", "Меню"])
async def command_help(message: types.Message):
    try:
        user = await com.select_user(message.from_user.id)
        await message.answer(f"Привет {user.first_name}", reply_markup=kb_menu)
    except Exception:
        await com.add_users(user_id=message.from_user.id, first_name=message.from_user.first_name)
        await message.answer(f"Привет {message.from_user.first_name}, ты зарегестрирован", reply_markup=kb_menu)