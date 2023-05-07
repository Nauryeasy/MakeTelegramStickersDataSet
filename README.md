Итак, данный проект нужен для сбора датасета стикеров из телеграм.
Результатом будет являться папка data (которую кстати перед запуском всего этого дела нужно создать) в которой будут храниться папки с названиями 
стикерпаков, внтури которых будут лежать файлы стикеров в формате webp, а названиями будут принадлежащие этим стикерам эмодзи.
Чтобы измненить формат стикеров нужно зайди в файл Download_stickers и на 42 строчке изменить разширение. 
Файл metadata.pkl это словарь, где по ключам названий стикерпаков храняться списки с соответствующими стикерам эмодзи отсортированные по порядку загрузки. Для того,
чтобы этот файл имел смысл (Если охота брать эмодзи не из названия файла стикера, а из metadata) нужно в файле Download_stickers изменить названия 
сохраняемых стикеров на какой-нибудь счетчик, чтобы стикеры имели названия 1, 2, 3, ..., n, чтобы эмодзи в metadata соответствовали стикерам.

Итак, инструкция:
1. Создаем папочку data в директории проекта
2. В файлике config в переменную TOKEN добавляем токен нашего тг ботика.
3. Запускаем файл Bot.py предворительно скачав все либы из requirements.txt
4. Идем в нашего бота и отправляем ему по одному стикеру из каждого стикерпака, которые хотим скачать
5. Офаем бота и получаем все стикеры с эмодзи.

Приятного использования!
