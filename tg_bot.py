import os
import random
import telegram
import asyncio

from config import filename_path, tg_token, chat_id, delay



published_images = set()
bot = telegram.Bot(token=tg_token)

async def send_photos(image_to_send=None):
    published_images = set()

    while True:
        images = [img for img in os.listdir(filename_path) if img.endswith(('.jpg', '.png'))]

        if image_to_send:
            if image_to_send in images:
                images = [image_to_send]
            else:
                print(f"Изображение {image_to_send} не найдено.")
                return

        random.shuffle(images)

        for image in images:
            if image not in published_images:
                with open(os.path.join(filename_path, image), 'rb') as photo:
                    await bot.send_photo(chat_id, photo)
                published_images.add(image)
                print(f"Фото {image} успешно размещено.")
                await asyncio.sleep(delay)

        published_images.clear()


async def choice_selection_image():
    images = [img for img in os.listdir(filename_path) if img.endswith(('.jpg', '.png'))]
    if not images:
        print("Нет изображений для отправки.")
        return None

    print("Выберите изображение для отправки (или нажмите Enter для случайного):")
    for idx, img in enumerate(images):
        print(f"{idx + 1}. {img}")

    choice = input("Введите номер изображения: ")
    if choice.isdigit() and 1 <= int(choice) <= len(images):
        return images[int(choice) - 1]
    return None


if __name__ == "__main__":
    image_choice = asyncio.run(choice_selection_image())
    asyncio.run(send_photos(image_choice))