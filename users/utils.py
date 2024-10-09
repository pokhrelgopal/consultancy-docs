import requests
from django.conf import settings

STORAGE_ZONE_NAME = settings.STORAGE_ZONE_NAME
PULL_ZONE_URL = settings.PULL_ZONE_URL
API_KEY = settings.BUNNYCDN_API_KEY
STORAGE_ZONE_REGION = settings.STORAGE_ZONE_REGION


def upload_to_bunnycdn(file):
    try:
        file_name = f"{file.name}"

        base_url = "storage.bunnycdn.com"
        if STORAGE_ZONE_REGION:
            base_url = f"{STORAGE_ZONE_REGION}.{base_url}"

        url = f"https://{base_url}/{STORAGE_ZONE_NAME}/{file_name}"

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
