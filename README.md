# Загрузчик изображений NASA и Телеграм-бот

Этот проект представляет собой приложение на Python, которое загружает изображения из API NASA и отправляет их в указанный чат Телеграм. Он включает функции для получения фотографий Земли, изображений запусков SpaceX и изображений космоса(APOD).

## Функции

- Получение фотографий Земли с использованием API EPIC NASA.
- Загрузка изображений запусков SpaceX с использованием API SpaceX.
- Загрузка астрономической картинки дня (APOD) от NASA.
- Отправка выбранных или случайных изображений в чат Телеграм.
- Удобный интерфейс командной строки для использования.

## Требования

- Python 3.7 или выше
- Библиотеки:
  - `requests`
  - `python-telegram-bot`
  - `envparse`

## Установка

1. Клонируйте этот репозиторий:
   ```
   git clone https://github.com/ваше_имя_пользователя/nasa-image-downloader.git
   cd nasa-image-downloader
   
2. Установите необходимые пакеты:
    ```
    pip install requests python-telegram-bot envparse
   
3. Создайте файл .env в корневом каталоге и добавьте свой ключ API NASA и токен бота Телеграм:
    ```
    NASA_TOKEN=ваш nasa_api_key
    TG_TOKEN=ваш telegram_bot_token
    CHAT_ID=ваш chat_id чата
    DELAY=задержка времени публикации в секундах. По умолчанию 1 фото в 4 часа

## Использование

1. Чтобы скачать изображения, выполните:
    ```
   python main.py --action <действие> [--launch_id <launch_id>] [--num_photos <количество_фото>] [--image <имя_изображения>]

Замените `<действие>` на одно из следующих:
* `space:` для получения изображений SpaceX.
* `earth:` для получения фотографий Земли.
* `apod:` для получения астрономической картинки дня NASA.
   
2. Опции:
* `--launch_id:`  Укажите ID запуска для изображений SpaceX.
* `--num_photos:`  Укажите количество фотографий Земли или APOD для получения.

## Структура кода
* `config.py:` Файл конфигурации для чтения ключей API и настроек из окружения.
* `fetch_earth_photos.py:` Модуль для получения фотографий Земли от NASA.
* `fetch_space_apod_photo.py:` Модуль для получения изображений APOD от NASA.
* `fetch_spacex_images.py:` Модуль для получения изображений из запусков SpaceX.
* `tg_bot.py:` Модуль для работы с функциональностью Телеграм-бота и отправки изображений.
* `utils.py:` Получение расширения изображения.
* `main.py:` Главная точка входа для приложения.
## Пример
Чтобы получить и отправить 5 фотографий Земли, выполните:

    python main.py --action earth --num_photos 5

Чтобы отправить конкретное изображение (например, image_1.png), выполните:
    

    python tg_bot.py

и введите номер изображения.