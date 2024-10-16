import requests
from datetime import datetime
from config import nasa_token, filename_path
from utils import download_image



def get_earth_photos(num_photos):
    response = requests.get(
        'https://api.nasa.gov/EPIC/api/natural/images',
        params={'api_key': nasa_token}
    )
    response.raise_for_status()

    for photo in response.json()[:num_photos]:
        date_time = datetime.strptime(photo['date'], '%Y-%m-%d %H:%M:%S')
        formatted_date = date_time.strftime('%Y/%m/%d')
        image_url = f'https://epic.gsfc.nasa.gov/archive/natural/{formatted_date}/png/{photo["image"]}.png'
        download_image(image_url, filename_path)