import os
import time

import requests


def get_image_extension(image_url): # Получение расширения фотографии
    _, ext = os.path.splitext(image_url)
    return ext


def download_image(image_url, filename_path):
    image_extension = get_image_extension(image_url)
    timestamp = int(time.time())
    file_path = os.path.join(filename_path, f'image_{timestamp}{image_extension}')

    response = requests.get(image_url)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)