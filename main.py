import requests
import os
import urllib
from datetime import datetime

filename_path = 'images/'
image_url = 'https://api.nasa.gov/planetary/apod'
params = {
          'api_key' : '9cAIMsmCSSeurXh4AXXj0YVNgSLje1BQOnURuLNU',
          'count' : 10
         }


def get_image_extension(image_url):
    _, extension = os.path.splitext(image_url)
    return extension


def get_some_photo (image_url, filename_path):
    response = requests.get(image_url, params=params)
    response.raise_for_status()
    data = response.json()
    for idx, item in enumerate(data):
        image_url = item.get('url')
        if image_url:
            image_extension = get_image_extension(image_url)
            print(f"URL = {image_url}, Расширение = {image_extension}")
            image_response = requests.get(image_url)
            image_response.raise_for_status()
            with open(os.path.join(filename_path, f'image_{idx + 1}{image_extension}'), 'wb') as file:
                file.write(image_response.content)



def get_earth_photos(num_photos=5):
    epic_api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': '9cAIMsmCSSeurXh4AXXj0YVNgSLje1BQOnURuLNU'  # Замените на свой API-ключ
    }
    response = requests.get(epic_api_url, params=params)
    response.raise_for_status()
    data = response.json()

    for photo in data[:num_photos]:
        date_str = photo['date']
        image_name = photo['image']
        date_time = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        formatted_date = date_time.strftime('%Y/%m/%d')
        image_url = f'https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/png/{image_name}.png'
        image_response = requests.get(image_url)
        image_response.raise_for_status()
        with open(f'image_{image_name}.png', 'wb') as file:
            file.write(image_response.content)
            print(f'Скачано: {image_url}')


get_earth_photos(1)

