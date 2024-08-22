Description
--
This project was created to create a data set from Telegram stickers. The data set is a data folder
in which folders will be located, where the folder name is the name of the sticker pack. The contents of the internal folders will be sticker files
in the webp extension, and the name of its emoji (Provided that the COUNTER_NAME parameter = 0, more details in the "Parameters" section. I advise you to read about this, since if there are stickers with the same emoji in the sticker pack, they will not be saved)

---
I hope this project will be useful to you!

---

Usage
--
First of all, you need to clone the repository
```
https://github.com/Nauryeasy/MakeTelegramStickersDataSet.git
```
Or
```
git@github.com:Nauryeasy/MakeTelegramStickersDataSet.git
```

Next, you need to set up a Python virtual environment, which I'm sure you can handle

After that, you need to install the project dependencies. While in the main project directory
```
pip install -r requirements.txt
```

Before launching, you need to specify the token of the bot you will use in the BOT_TOKEN parameter in the .env file
(Information for this can be found on the Internet), and also change other parameters if necessary (more details in
"Parameters")

Next, launch the project
```
python main.py
```
Or through your IDE

After that, you need to send the bot a sticker and it will download the entire sticker pack (For this, I asked my friends to send
stickers to the bot). After sending the bot one sticker from each necessary sticker pack, you need to turn it off, after which
the metadata.pkl file will appear (Needed for COUNTER_NAME=1). After that, you can use the stickers at your own discretion.
Errors when closing are normal, I just got too lazy to mess with them >.<

---

Parameters
--
__COUNTER_NAME__ - The parameter determines what the name of the sticker will be. If the parameter value is 0, then the names of the sticker files
will be the corresponding emoji, which can be bad if several stickers in the sticker pack have the same emoji.
If the parameter value is 1, then the name of the sticker file will be a number, which will be its number, as well as an index
in the list that will be stored in metadata.pkl by the key "sticker pack name". That is, when loading the metadata.pkl file, you
will get a dictionary, where the keys will be the names of sticker packs, and the values ​​are lists with emoji and the name of each saved sticker
will be the index of its emoji in this list.
(You can see an example of downloading metadata.pkl in /download_stickers/sticker_repo on line 74)

---
Enjoy using it! (It won't be)

---

Описание 
--
Данный проект создан для создания набора данных из стикеров Telegram. Набор данных представляет собой папку data в 
которой будут находиться папки, где имя папки - название стикерпака. Содержимым внутренних папок будут файлы стикеров 
в расширении webp, а именем его эмодзи (При условии, что параметр COUNTER_NAME=0, подробнее в пункте "Параметры". Об
этом советую прочитать, так как если в стикерпаке есть стикеры с одинаковым эмодзи, то они не сохраняться)

---
Я надеюсь этот проект будет вам полезен!

---

Использование
--
Первым делом необходимо клонировать репозиторий
```
https://github.com/Nauryeasy/MakeTelegramStickersDataSet.git
```
Или 
```
git@github.com:Nauryeasy/MakeTelegramStickersDataSet.git
```

Далее необходимо настроить виртуальное окружение Python, с чем я уверен вы справитесь

После этого необходимо установить зависимости проекта. Находясь в главной директории проекта
```
pip install -r requirements.txt
```

Перед запуском необходимо в файле .env в параметр BOT_TOKEN указать токен бота, которого вы будете использовать
(Информацию для этого можно найти в интернете), так же при необходимости изменить другие параметры (подробнее в 
"Параметры")

Далее запускаем проект
```
python main.py
```
Или же через вашу IDE

После этого нужно отправить боту стикер и он скачает весь стикерпак (Для этого я попросил своих друзей отправлять 
стикеры боту). Отправив боту по одному стикеру из каждого необходимого стикерпака нужно его выключить, после чего
появиться файлик metadata.pkl (Нужен при COUNTER_NAME=1). После этого можно использовать стикеры по своему усмотрению.
Ошибки при закрытии являются нормальными, просто мне стало лень с ними возиться >.<

---

Параметры
--
__COUNTER_NAME__ - Параметр определяет, что будет именем стикера. Если значение параметра 0, то именами файлов стикеров
будут соответствующие им эмодзи, что может быть плохо, если в стикерпаке несколько стикеров имеют один и тот же эмодзи.
Если значение параметра 1, то именем файла стикера будет число, которое будет являтся его номером, а так же индексом 
в списке, который будет храниться в metadata.pkl по ключу "имя стикерпака". То есть при загрузке файла metadata.pkl вы 
получите словарь, где ключами будут имена стикерпаков, а значениями списки с эмодзи и имя каждого сохраненного стикера
будет индексом его эмодзи в этом списке. 
(Пример загрузки metadata.pkl можно посомтреть в /download_stickers/sticker_repo на 74 строке)

---
Приятного использования! (Оно таковым не будет)