import os
import random
import sys
import telegram
import asyncio
import argparse
from config import filename_path, tg_bot_token, tg_chat_id, delay

async def send_photos(bot, published_images, image_to_send=None):
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
                    await bot.send_photo(tg_chat_id, photo)
                published_images.add(image)
                print(f"Фото {image} успешно размещено.")
                await asyncio.sleep(delay)

        published_images.clear()

def choice_selection_image(images, choice):
    if choice.isdigit() and 1 <= int(choice) <= len(images):
        return images[int(choice) - 1]
    return None

def main():
    parser = argparse.ArgumentParser(description='Send images to Telegram.')
    parser.add_argument('--image', type=int, help='Number of the image to send.')
    args = parser.parse_args()

    published_images = set()
    bot = telegram.Bot(token=tg_bot_token)

    images = [img for img in os.listdir(filename_path) if img.endswith(('.jpg', '.png'))]

    if args.image is not None:
        image_choice = choice_selection_image(images, str(args.image))
    else:
        random.shuffle(images)
        image_choice = images[0]

    asyncio.run(send_photos(bot, published_images, image_choice))

if __name__ == "__main__":
    main()