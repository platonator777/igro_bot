from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import CommandHelp
from filters import IsPrivate
from keyboards.default import kb_menu
from utils.misc import rate_limit


@rate_limit(limit=2)
@dp.message_handler(IsPrivate(), CommandHelp())
async def command_help(message: types.Message):
    await message.answer("Это игровой бот, здесь можешь поиграть в игры на у.е. ", reply_markup=kb_menu)