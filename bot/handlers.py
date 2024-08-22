from aiogram import types
from aiogram.filters import CommandStart

from bot import dp
from bot.filters import StickerFilter

from download_stickers import get_stickers_repo


sticker_set_names = []


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет! Отправь мне стикер и я его скачаю.\nHello! Send me a sticker and I will download it.')


"""
Пошла ***** CallBackData, я так и не разобрался кого куда пихать и что от кого наследовать :(
"""


@dp.message(StickerFilter())
async def get_sticker(message: types.Message):
    stickers_set_name = message.sticker.set_name
    sticker_set_names.append(stickers_set_name)

    await message.answer("Загрузка стикерпака была запущена (Подробнее в консоли).\nThe sticker pack download has started (More details in the console).")
