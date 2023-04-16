import requests


def simple_get(url: str) -> dict:
    response = requests.get(url)

    return response.json()
