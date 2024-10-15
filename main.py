import requests
import argparse

from config import filename_path
from fetch_earth_photos import get_earth_photos
from fetch_space_apod_photo import get_apod_photo
from fetch_spacex_images import get_space_image



def main(action, launch_id=None, num_photos=None):
    if action == 'space':
        image_url = (
            f'https://api.spacexdata.com/v5/launches/{launch_id}' if launch_id
            else requests.get('https://api.spacexdata.com/v5/launches/latest').json()['links']['flickr']['original']
        )
        get_space_image(image_url, filename_path)

    elif action == 'earth':
        if num_photos:
            get_earth_photos(num_photos)
        else:
            print("Необходимо указать количество фотографий для получения.")

    elif action == 'apod':
        if num_photos:
            get_apod_photo(num_photos)
        else:
            print("Необходимо указать количество фотографий NASA для получения.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Получить изображения запусков SpaceX, фотографии Земли или NASA APOD.')
    parser.add_argument('--action', choices=['space', 'earth', 'apod'], required=True,
                        help='Выберите действие: "space" для изображений SpaceX, "earth" для фотографий Земли или "apod" для фотографий космоса NASA.')
    parser.add_argument('--launch_id', type=str, help='ID запуска SpaceX для получения изображений')
    parser.add_argument('--num_photos', type=int, help='Количество фотографий для получения.')

    args = parser.parse_args()
    main(args.action, args.launch_id, args.num_photos)