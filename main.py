import requests
import argparse

from config import filename_path
from fetch_earth_photos import get_earth_photos
from fetch_space_apod_photo import get_apod_photos
from fetch_spacex_images import get_space_images



def main():

    parser = argparse.ArgumentParser(
        description='Получить изображения запусков SpaceX, фотографии Земли или NASA APOD.')
    parser.add_argument('--action', choices=['space', 'earth', 'apod'], required=True,
                        help='Выберите действие: "space" для изображений SpaceX, "earth" для фотографий Земли или "apod" для фотографий космоса NASA.')
    parser.add_argument('--launch_id', type=str, default='latest', help='ID запуска SpaceX для получения изображений')
    parser.add_argument('--num_photos', type=int, default=1, help='Количество фотографий для получения.')

    args = parser.parse_args()

    if args.action == 'space':
        if args.launch_id:
            launch_url = f'https://api.spacexdata.com/v5/launches/{args.launch_id}'
        else:
            launch_url = requests.get('https://api.spacexdata.com/v5/launches/latest').json()['links']['flickr'][
                'original']
        get_space_images(launch_url, filename_path)

    elif args.action == 'earth':
        if args.num_photos:
            get_earth_photos(args.num_photos)
        else:
            print("Необходимо указать количество фотографий для получения.")

    elif args.action == 'apod':
        if args.num_photos:
            get_apod_photos(args.num_photos)
        else:
            print("Необходимо указать количество фотографий NASA для получения.")


if __name__ == "__main__":
    main()