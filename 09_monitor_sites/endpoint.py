from dataclasses import dataclass


@dataclass
class Endpoint:
    """Endpoint object for the a site that will be monitored"""

    """ Name of the monitored endpoint """
    name: str
    """ Is the endpoint enabled? """
    enabled: bool
    """ The HTTP verb used to monitor the endpoint """
    verb: str
    """ The URL of the endpoint """
    url: str
    """ The timeout in milliseconds for the request """
    timeoutMs: int
    """ The regex used to match the response """
    regex: str
    """ The interval in milliseconds for the monitor """
    intervalMs: int
    """ Should redirects be followed? """
    follow_redirects: bool
    """ Should the certificate expiration be checked? """
    check_certificate_expiration: bool
    """ Should the SSL certificate be verified? """
    verify_ssl: bool
    """ The tags for this object """
    tags: dict
