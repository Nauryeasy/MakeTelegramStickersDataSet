import json
import os
import pickle

import requests


class StickerRepository:

    stickers_url = "https://api.telegram.org/bot{token}/getStickerSet?name={sticker_set_name}"

    def __init__(self, token, counter_name: bool = False, extension: str = "webp"):
        self.token = token
        self.counter_name = counter_name
        self.extension = extension
        self.__load_emojis()
        print('emojis_dict:', self.emojis)

    def download_sticker_pack(self, sticker_set_name):
        sticker_set = self.__get_sticker_set(sticker_set_name)

        print(f'{sticker_set_name} start download')

        if sticker_set_name not in self.emojis:
            emojis_list = []

            dir_path = f'data/{sticker_set_name}'
            os.mkdir(dir_path)

            count = 0

            for sticker in sticker_set["stickers"]:
                emoji = sticker['emoji']
                emojis_list.append(emoji)
                sticker = self.__download_sticker(sticker)
                self.__save_sticker(sticker, dir_path, emoji, count)
                count += 1

            self.emojis[sticker_set_name] = emojis_list

        print(f'{sticker_set_name} is downloaded')

    def __get_sticker_set(self, sticker_set_name):
        response = requests.get(self.stickers_url.format(token=self.token, sticker_set_name=sticker_set_name))
        sticker_set = response.json()["result"]
        return sticker_set

    def __download_sticker(self, sticker: dict):
        file_id = sticker["file_id"]
        response = requests.get(f"https://api.telegram.org/bot{self.token}/getFile?file_id={file_id}")
        file_path = json.loads(response.text)["result"]["file_path"]

        file_url = f"https://api.telegram.org/file/bot{self.token}/{file_path}"

        response = requests.get(file_url)

        return response.content

    def __save_sticker(self, sticker, dir_path, emoji, count):
        if self.counter_name:
            file_name = f"{dir_path}/{count}.{self.extension}"
            with open(file_name, "wb") as f:
                f.write(sticker)
        else:
            file_name = f"{dir_path}/{emoji}.{self.extension}"
            with open(file_name, "wb") as f:
                f.write(sticker)

    def save_emojis(self):
        print('emojis_dict:', self.emojis)
        with open('data/metadata.pkl', 'wb') as file:
            pickle.dump(self.emojis, file)

    def __load_emojis(self):
        try:
            with open('data/metadata.pkl', 'rb') as file:
                self.emojis = pickle.load(file)
                print('emojis is load')
        except:
            self.emojis = {}
