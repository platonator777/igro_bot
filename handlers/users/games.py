from aiogram import types
from loader import dp
from asyncio import sleep
from filters import enough_money, IsPrivate
from keyboards.default import kb_play, kb_knb, kb_coin
from utils.db_api.quick_comands import update_balance, select_user
from utils.misc import rate_limit
from random import randint


@rate_limit(limit=2)
@dp.message_handler(IsPrivate(), text = ["Играть", "К играм"])
async def check_message(message: types.Message):
    await message.answer("Для игры в кости отпрвь эмодзи 🎲\n"
                         "Для игры в рулетку отправь эмодзи 🎰 \n"
                         "👇Для остальных игр нажми на кнопки👇", reply_markup=kb_play)


@rate_limit(limit=3)
@dp.message_handler(enough_money(), content_types="dice")
async def check_message(message: types.Message):
    user_id = message.from_user.id
    user = await select_user(user_id)
    if message.dice.emoji == "🎰":
        value = message.dice.value
        await sleep(2)
        if value == 1 or value == 22 or value == 43 or value == 64:
            await update_balance(user_id, int(user.stake) * 15)
            user = await select_user(user_id)
            await message.answer("Поздравляю ты выиграл x15 от ставки \n"
                                 f"+{int(user.stake)*15 }\n"
                                 f"баланс = {user.balance}")
            wins = user.wins + 1
            await user.update(wins=wins).apply()
            win_money = user.win_money + user.stake*15
            await user.update(win_money=int(win_money)).apply()
        else:
            await update_balance(user_id, -int(user.stake))
            user = await select_user(user_id)
            await message.answer("К сожалению ты проиграл \n"
                                 f"-{user.stake}\n"
                                 f"баланс = {user.balance}")
            loses = user.loses + 1
            await user.update(loses=loses).apply()
            lose_money = user.lose_money + user.stake
            await user.update(lose_money=lose_money).apply()
    elif message.dice.emoji == "🎲":
        player_1 = message.dice.value
        player = await message.answer_dice()
        player_2 = player.dice.value
        await sleep(3.5)
        if player_1 > player_2:
            await update_balance(user_id, int(user.stake))
            user = await select_user(user_id)
            await message.answer("Поздравляю, победа\n"
                                 f"+{user.stake}\n"
                                 f"баланс = {user.balance}")
            wins = user.wins + 1
            await user.update(wins=wins).apply()
            win_money = user.win_money + user.stake
            await user.update(win_money=win_money).apply()

        elif player_1 == player_2:
            await message.answer("Ничья, возврат ставки\n"
                                 f"баланс = {user.balance}")
            draw = user.draws + 1
            await user.update(draws=draw).apply()
        else:
            await update_balance(user_id, -int(user.stake))
            user = await select_user(user_id)
            await message.answer("К сожалению ты проиграл\n"
                                 f"-{user.stake}\n"
                                 f"баланс = {user.balance}")
            loses = user.loses + 1
            await user.update(loses=loses).apply()
            lose_money = user.lose_money + user.stake
            await user.update(lose_money=lose_money).apply()


@rate_limit(limit=1)
@dp.message_handler(enough_money(), text="Камень Ножницы Бумага")
async def check_message(message: types.Message):
    await message.answer("Выбрасывай", reply_markup=kb_knb)


@rate_limit(limit=1)
@dp.message_handler(enough_money(), text=["🪨", "✂️", "🧻"])
async def check_message(message: types.Message):
    user_id = message.from_user.id
    user = await select_user(user_id)
    result = randint(1,3)
    win_status = 0
    if result==1:
        await message.answer("🪨", reply_markup=kb_knb)
        if message.text == "✂️":
            win_status = 2
        elif message.text == "🧻":
            win_status = 1
        else:
            win_status = 3
    elif result==2:
        await message.answer("✂️", reply_markup=kb_knb)
        if message.text == "🧻":
            win_status = 2
        elif message.text == "🪨":
            win_status = 1
        else:
            win_status = 3
    else:
        await message.answer("🧻", reply_markup=kb_knb)
        if message.text == "🪨":
            win_status = 2
        elif message.text == "✂️":
            win_status = 1
        else:
            win_status = 3

    if win_status == 1:
        await update_balance(user_id, int(user.stake))
        user = await select_user(user_id)
        await message.answer("Поздравляю, победа\n"
                             f"+{user.stake}\n"
                             f"баланс = {user.balance}")
        wins = user.wins + 1
        await user.update(wins=wins).apply()
        win_money = user.win_money + user.stake
        await user.update(win_money=win_money).apply()

    elif win_status == 3:
        await message.answer("Ничья, возврат ставки\n"
                             f"баланс = {user.balance}")
        draw = user.draws + 1
        await user.update(draws=draw).apply()
    else:
        await update_balance(user_id, -int(user.stake))
        user = await select_user(user_id)
        await message.answer("К сожалению ты проиграл\n"
                             f"-{user.stake}\n"
                             f"баланс = {user.balance}")
        loses = user.loses + 1
        await user.update(loses=loses).apply()
        lose_money = user.lose_money + user.stake
        await user.update(lose_money=lose_money).apply()


@rate_limit(limit=1)
@dp.message_handler(enough_money(), text="Монетка")
async def check_message(message: types.Message):
    await message.answer("Выбирай", reply_markup=kb_coin)


@rate_limit(limit=1)
@dp.message_handler(enough_money(), text = ["Орел", "Решка"])
async def check_message(message: types.Message):
    user_id = message.from_user.id
    user = await select_user(user_id)
    result = randint(1, 2)
    win_status = 0
    if result == 1:
        await message.answer("Выпал Решка")
        if message.text=="Решка":
            win_status = 1
        else:
            win_status = 2
    else:
        await message.answer("Выпал Орел")
        if message.text == "Орел":
            win_status = 1
        else:
            win_status = 2
    if win_status == 1:
        await update_balance(user_id, int(user.stake))
        user = await select_user(user_id)
        await message.answer("Поздравляю, победа\n"
                             f"+{user.stake}\n"
                             f"баланс = {user.balance}")
        wins = user.wins + 1
        await user.update(wins=wins).apply()
        win_money = user.win_money + user.stake
        await user.update(win_money=win_money).apply()
    else:
        await update_balance(user_id, -int(user.stake))
        user = await select_user(user_id)
        await message.answer("К сожалению ты проиграл\n"
                             f"-{user.stake}\n"
                             f"баланс = {user.balance}")
        loses = user.loses + 1
        await user.update(loses=loses).apply()
        lose_money = user.lose_money + user.stake
        await user.update(lose_money=lose_money).apply()



