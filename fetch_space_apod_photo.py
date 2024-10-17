import requests
from utils import download_image



def get_apod_photos(nasa_token, filename_path, count=1):
    response = requests.get('https://api.nasa.gov/planetary/apod', params={'api_key': nasa_token, 'count': count})
    response.raise_for_status()
    images_info = response.json()

    for photo in images_info:
        image_url = photo.get('hdurl', photo.get('url'))
        if not image_url:
            continue
        download_image(image_url, filename_path)
