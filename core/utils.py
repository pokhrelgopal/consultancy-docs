import requests
from django.conf import settings
import random
import string


STORAGE_ZONE_NAME = settings.BUNNY_STORAGE_ZONE_NAME
PULL_ZONE_URL = settings.BUNNY_PULL_ZONE_URL
API_KEY = settings.BUNNY_API_KEY
STORAGE_ZONE_REGION = settings.BUNNY_STORAGE_ZONE_REGION


def random_string(length=8):
    characters = string.ascii_letters + string.digits
    random_string = "".join(random.choices(characters, k=length))
    return random_string


def upload_to_bunnycdn(file):
    try:
        file_name = random_string() + file.name
        base_url = "storage.bunnycdn.com"
        if STORAGE_ZONE_REGION:
            base_url = f"{STORAGE_ZONE_REGION}.{base_url}"

        url = f"https://{base_url}/{STORAGE_ZONE_NAME}/media/{file_name}"

        headers = {
            "AccessKey": API_KEY,
            "Content-Type": "application/octet-stream",
            "accept": "application/json",
        }

        response = requests.put(url, headers=headers, data=file.read())

        if response.status_code != 201:
            raise Exception(
                f"Failed to upload: {response.status_code} {response.reason} - {response.text}"
            )

        cdn_url = f"https://{base_url}/{STORAGE_ZONE_NAME}/{file_name}"

        return cdn_url

    except Exception as e:
        raise Exception(f"Failed to upload to BunnyCDN: {str(e)}")
