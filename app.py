from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from aiogram import executor
from handlers import dp
import filters
from loader import db
from utils.db_api.db_gino import on_startup
import middlewares

async def startup(dp):
    filters.setup(dp)
    middlewares.setup(dp)
    print("Подключение к бд")
    await on_startup(dp)

    await db.gino.drop_all()
    print("создание бд")
    await db.gino.create_all()
    print("готово")
    print("уведомление")
    await on_startup_notify(dp)
    await set_default_commands(dp)

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=startup, skip_updates=True)