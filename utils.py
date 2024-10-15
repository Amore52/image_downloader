import os

def get_image_extension(image_url): # Получение расширения фотографии
    _, ext = os.path.splitext(image_url)
    return ext