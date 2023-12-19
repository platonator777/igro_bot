from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_users(user_id: int, first_name:str):
    try:
        user = User(user_id=user_id, first_name=first_name)
        await user.create()
    except UniqueViolationError:
        print("Пользователь не добавлен")

async def select_all_users():
    users = await User.query.gino.all()
    return users

async def update_balance(user_id, value):
    user = await select_user(user_id)
    balance = user.balance
    balance += value
    await user.update(balance=balance).apply()
async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def update_user_name(user_id, new_name):
    user = await select_user(user_id)
    await user.update(first_name=new_name).apply()

async def delte_user(user_id):
    info = await User.query.where(User.user_id == user_id).gino.first()
    await info.delete()

async def update_user_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()