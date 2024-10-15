import requests
import os
from config import nasa_token
from utils import get_image_extension



def get_apod_photo(count=1):
    response = requests.get('https://api.nasa.gov/planetary/apod', params={'api_key': nasa_token, 'count': count})
    response.raise_for_status()
    images = response.json()

    for item in images:
        image_url = item.get('hdurl', item.get('url'))
        if image_url:
            image_extension = get_image_extension(image_url)
            print(f"URL = {image_url}, Расширение = {image_extension}")
            img_response = requests.get(image_url)
            img_response.raise_for_status()
            filename = os.path.join('images', os.path.basename(image_url))
            with open(filename, 'wb') as f:
                f.write(img_response.content)
