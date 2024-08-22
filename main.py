import asyncio
from threading import Thread

from bot import dp, init_bot, sticker_set_names
from download_stickers import make_directory, get_stickers_repo


def download_sticker_packs_thread():
    sticker_repo = get_stickers_repo()
    try:
        while True:
            if sticker_set_names:
                sticker_set_name = sticker_set_names.pop(0)
                sticker_repo.download_sticker_pack(sticker_set_name)
    finally:
        pass


async def main():
    print("Made with love by NAURY for anyone who might need a sticker dataset")

    make_directory()

    th = Thread(target=download_sticker_packs_thread)
    th.start()

    await dp.start_polling(init_bot())


if __name__ == "__main__":
    stickers_repo = get_stickers_repo()
    try:
        asyncio.run(main())
    finally:
        stickers_repo.save_emojis()
