import random

import requests
from tqdm import tqdm

BASE_URL = 'https://this-person-does-not-exist.com'
IMAGE_LOCATION = 'StyleGAN_generated'
ITERATION_COUNT = 90


def fetch_image_metadata(random_id: int):
    url = f'{BASE_URL}/en'
    params = {'new': random_id}
    response = requests.get(url, params).json()
    if response.get('generated') == 'true':
        return response.get('src'), response.get('name')
    else:
        return None, None


def fetch_image(url):
    url = f'{BASE_URL}/{url}'
    response = requests.get(url)
    if response.ok:
        return response.content
    else:
        print(f'image download failed for{url}')


def save_image(img_data, name):
    file_path = f'{IMAGE_LOCATION}/{name}'
    with open(file_path, 'wb') as handle:
        handle.write(img_data)


if __name__ == '__main__':
    for i in tqdm(range(ITERATION_COUNT)):
        rand_id = random.getrandbits(42)
        url, name = fetch_image_metadata(rand_id)
        image_data = fetch_image(url)
        save_image(image_data, name)

