import os
import requests
from utils import download_image



def get_space_images(launch_url, filename_path):
        response = requests.get(launch_url)
        response.raise_for_status()
        images = response.json().get('links', {}).get('flickr', {}).get('original', [])
        os.makedirs(filename_path, exist_ok=True)
        for url in images:
            if not url:
                continue
            download_image(url, filename_path)