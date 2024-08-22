import os

from aiogram import Dispatcher, Bot
from dotenv import load_dotenv


dp = Dispatcher()


def init_bot() -> Bot:
    load_dotenv()
    token = os.getenv("BOT_TOKEN")
    return Bot(token)


from bot.handlers import *
from bot.handlers import sticker_set_names
