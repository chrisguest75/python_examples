import requests
import logging

def simple_get(url: str) -> dict:
    response = requests.get(url)

    return response.json()
