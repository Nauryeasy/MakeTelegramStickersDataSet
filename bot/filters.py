from aiogram import types
from aiogram.filters import Filter


class StickerFilter(Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.sticker is not None
