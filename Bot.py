from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType
from aiogram.utils import executor
from Download_stickers import *
from threading import Thread
import pickle


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('<сообщение>')


@dp.message_handler(content_types=ContentType.STICKER)
async def get_sticker(message: types.Message):
    sticker_pack_name = message.sticker.set_name
    th = Thread(target=download_sticker_pack, kwargs={'sticker_set_name': sticker_pack_name})
    th.start()
    await message.answer('<сообщение>')


if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    finally:
        with open('data/metadata.pkl', 'wb') as file:
            pickle.dump(emojis, file)
        print(emojis)
