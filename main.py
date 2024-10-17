import os
import argparse
from dotenv import load_dotenv
from fetch_earth_photos import get_earth_photos
from fetch_space_apod_photo import get_apod_photos
from fetch_spacex_images import get_space_images



def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    filename_path = './images/'

    parser = argparse.ArgumentParser(
        description='Получить изображения запусков SpaceX, фотографии Земли или NASA APOD.')
    parser.add_argument('--action', choices=['space', 'earth', 'apod'], required=True,
                        help='Выберите действие: "space" для изображений SpaceX, "earth" для фотографий Земли или "apod" для фотографий космоса NASA.')
    parser.add_argument('--launch_id', type=str, default='latest', help='ID запуска SpaceX для получения изображений')
    parser.add_argument('--num_photos', type=int, default=1, help='Количество фотографий для получения.')

    args = parser.parse_args()

    if args.action == 'space':
        launch_url = f'https://api.spacexdata.com/v5/launches/{args.launch_id}'
        get_space_images(launch_url, filename_path)

    elif args.action == 'earth':
            get_earth_photos(nasa_token, filename_path, args.num_photos)


    elif args.action == 'apod':
            get_apod_photos(nasa_token, filename_path, args.num_photos)


if __name__ == "__main__":
    main()
