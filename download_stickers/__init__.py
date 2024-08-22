import os
import pickle
from functools import lru_cache

from dotenv import load_dotenv

from download_stickers.sticker_repo import StickerRepository


load_dotenv()


@lru_cache(1)
def get_stickers_repo() -> StickerRepository:
    return _init_stickers_repo()


def _init_stickers_repo() -> StickerRepository:
    token = os.getenv('BOT_TOKEN')
    counter_name = int(os.getenv('COUNTER_NAME'))
    extension = os.getenv('EXTENSION')
    return StickerRepository(token=token, counter_name=counter_name, extension=extension)


def make_directory():
    if not os.path.exists('data'):
        os.mkdir('data')
