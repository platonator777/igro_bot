from aiogram import types
from loader import dp
from filters import IsPrivate
from utils.db_api.quick_comands import select_user
from keyboards.default import kb_menu
from utils.misc import rate_limit


@rate_limit(limit=2)
@dp.message_handler(IsPrivate(), text = ["Профиль", "/profile"])
async def registration_(message: types.Message):
    user_id = message.from_user.id
    user = await select_user(user_id)
    win_money = user.win_money
    lose_money = user.lose_money
    profit = win_money - lose_money
    wins = user.wins
    loses = user.loses
    draw = user.draws
    await message.answer(f"Имя: {message.from_user.first_name} \n"
                         f"Баланс: {user.balance}\n"
                         f"Ставка: {user.stake}\n"
                         f"Общий выигрыш: {win_money}\n"
                         f"Общий проигрыш: {lose_money}\n"
                         f"Заработок: {profit}\n"
                         f"Общее количество побед: {wins}\n"
                         f"Общее количество поражений: {loses}\n"
                         f"Общее количество ничей: {draw}", reply_markup=kb_menu)
