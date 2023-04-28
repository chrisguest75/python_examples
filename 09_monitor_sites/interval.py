import ssl
import socket
import logging
import time
import threading
import re
from endpoint import Endpoint
from response import Response
from datetime import datetime
import requests
from urllib.parse import urlparse


class Interval:
    """Responsible for requesting the endpoint and recording the response"""

    def __init__(self, endpoint: Endpoint) -> None:
        self.logger = logging.getLogger(__name__)
        self.endpoint = endpoint
        self.intervalMs = endpoint.intervalMs / 1000.0
        self.stopped = False
        self.timer = None

    @staticmethod
    def extract_hostname(url):
        parsed_url = urlparse(url)
        return parsed_url.hostname

    @staticmethod
    def get_certificate_expiration_date(hostname, port=443):
        """"""
        context = ssl.create_default_context()
        conn = context.wrap_socket(
            socket.socket(socket.AF_INET), server_hostname=hostname
        )
        conn.settimeout(5.0)
        conn.connect((hostname, port))
        cert = conn.getpeercert()
        conn.close()

        expiry_date = datetime.strptime(cert["notAfter"], r"%b %d %H:%M:%S %Y %Z")
        return expiry_date

    def matcher(self, response: str, regex: str) -> bool:
        # Convert the pattern string to a raw string
        pattern = re.compile(regex)

        # Search for the pattern in the response text
        match = re.search(pattern, response)

        # Check if the pattern was found
        if match:
            self.logger.info({"message": "Pattern found", "match": match.group(0)})
            return True
        else:
            self.logger.warning(f"Pattern '{regex}' not found in the response")
            return False

    def stop(self):
        self.stopped = True
        if self.timer:
            self.timer.cancel()

    def start(self) -> Response:
        self.ping()
        # if not stopped, start the timer again
        if not self.stopped:
            self.timer = threading.Timer(self.intervalMs, self.start)
            self.timer.start()

    def ping(self) -> Response:
        self.logger.info(
            {
                "message": "Interval started",
                "name": self.endpoint.name,
            }
        )

        endpoint_response = Response(
            name=self.endpoint.name,
            url=self.endpoint.url,
            timestamp=int(time.time()),
            status=-1,
            elapsedMs=0,
            expiry_date="UNCHECKED",
            regex_match=None,
            tags=self.endpoint.tags,
            verb=self.endpoint.verb,
        )

        # check the certificate expiration
        if self.endpoint.check_certificate_expiration:
            try:
                hostname = self.extract_hostname(self.endpoint.url)
                expiry_date = self.get_certificate_expiration_date(hostname)
                endpoint_response.expiry_date = expiry_date.strftime("%Y-%m-%d")
            except Exception as e:
                self.logger.error(
                    f"An error occurred while checking the certificate: {e}", e
                )
                endpoint_response.expiry_date = "ERROR"

        try:
            timeout = max(int(self.endpoint.timeoutMs / 1000.0), 1)
            tic = time.perf_counter()
            response = requests.get(self.endpoint.url, timeout=timeout)
            toc = time.perf_counter()
            endpoint_response.elapsedMs = (toc - tic) * 1000.0

            response.raise_for_status()
            endpoint_response.status = response.status_code

            # check the regex
            endpoint_response.regex_match = self.matcher(
                response.text, self.endpoint.regex
            )

        except requests.exceptions.Timeout as e:
            self.logger.warning(f"Request timed out after {timeout} seconds", e)
            endpoint_response.status = 999
        except requests.exceptions.HTTPError as e:
            self.logger.error(f"An HTTP error occurred: {e}", e)
            endpoint_response.status = response.status_code
        except requests.exceptions.RequestException as e:
            self.logger.error(f"An error occurred while making the request: {e}", e)
            endpoint_response.status = 999

        self.logger.info(
            {
                "response": endpoint_response,
                "message": "Interval ended",
                "name": self.endpoint.name,
            }
        )

        return endpoint_response
