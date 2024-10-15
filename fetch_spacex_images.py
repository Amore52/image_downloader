import os
import requests
from utils import get_image_extension



def get_space_image(image_url, filename_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        images = response.json().get('links', {}).get('flickr', {}).get('original', [])
        os.makedirs(filename_path, exist_ok=True)
        for idx, url in enumerate(images):
            if url:
                image_extension = get_image_extension(url)
                print(f"URL = {url}, Расширение = {image_extension}")
                image_response = requests.get(url)
                image_response.raise_for_status()
                file_path = os.path.join(filename_path, f'image_{idx + 1}{image_extension}')
                with open(file_path, 'wb') as file:
                    file.write(image_response.content)
    except requests.RequestException:
        print('Фотографий во время запуска не сделано.')