import os
import pickle
import requests
import json

from config import *

try:
    with open('data/metadata.pkl', 'rb') as file:
        emojis = pickle.load(file)
        print('emojis is load')
except:
    emojis = {}

print(emojis)

def download_sticker_pack(sticker_set_name):
    response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getStickerSet?name={sticker_set_name}")
    sticker_set = json.loads(response.text)["result"]

    emojis_list = []

    print(f'{sticker_set_name} start download')

    if sticker_set_name not in emojis:

        dir_path = f'data/{sticker_set_name}'
        os.mkdir(dir_path)

        for sticker in sticker_set["stickers"]:

            emoji = sticker['emoji']
            emojis_list.append(emoji)
            file_id = sticker["file_id"]
            response = requests.get(f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}")
            file_path = json.loads(response.text)["result"]["file_path"]

            file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"

            response = requests.get(file_url)

            file_name = f"{dir_path}/{sticker['emoji']}.webp"
            with open(file_name, "wb") as f:
                f.write(response.content)

        emojis[sticker_set_name] = emojis_list
    print(f'{sticker_set_name} is downloaded')
