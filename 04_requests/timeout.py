import requests
import logging

logger = logging.getLogger()


def timeout_get(url: str, timeout_seconds: int = 5) -> dict:
    try:
        response = requests.get(url, timeout=timeout_seconds)
        response.raise_for_status()  # Raise an exception if the response contains an HTTP error
        return response.json()
    except requests.exceptions.Timeout as e:
        logger.warning(f"Request timed out after {timeout_seconds} seconds", e)
    except requests.exceptions.HTTPError as e:
        logger.error(f"An HTTP error occurred: {e}", e)
    except requests.exceptions.RequestException as e:
        logger.error(f"An error occurred while making the request: {e}", e)
