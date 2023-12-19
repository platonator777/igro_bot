from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states import Change_stake
from filters import IsPrivate
from aiogram.types import ReplyKeyboardRemove
from keyboards.default import kb_menu
from utils.db_api.quick_comands import select_user


@dp.message_handler(IsPrivate(), text=["Установить ставку", "/stake"])
async def stake_(message: types.Message):
    await message.answer("Введи ставку", reply_markup=ReplyKeyboardRemove())
    await Change_stake.stake.set()


# @dp.message_handler(state=Change_stake.stake)
# async def state1(message:types.message, state: FSMContext):
#     answer = message.text
#     await state.update_data(stake = answer)

@dp.message_handler(state=Change_stake.stake)
async def send_message(message:types.message,state: FSMContext):
    answer = message.text
    await state.update_data(stake = answer)
    data = await state.get_data()
    stake = data.get("stake")
    try:
        stake = int(stake)
    except Exception:
        pass
    if isinstance(stake, int) and stake >0:
        user_id = message.from_user.id
        user = await select_user(user_id)
        await user.update(stake=stake).apply()
        await message.answer("ставка установлена", reply_markup=kb_menu)
    else:
        await message.answer("неверный ввод", reply_markup=kb_menu)

    await state.finish()