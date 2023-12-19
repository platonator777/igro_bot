from aiogram import Dispatcher
from .private_chat import IsPrivate
from .check_admin import IsAdmin
from .check_money import enough_money

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(enough_money)