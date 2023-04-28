from dataclasses import dataclass


@dataclass
class Response:
    """Response object for the monitor_sites function"""

    """The name of the site being monitored"""
    name: str
    """The url of the site being monitored"""
    url: str
    """The HTTP verb used to monitor the site"""
    verb: str
    """The timestamp of the response"""
    timestamp: int
    """The HTTP status code of the response"""
    status: int
    """The elapsed time in milliseconds for the response"""
    elapsedMs: int
    """The expiry date of the certificate for the endpoint"""
    expiry_date: str
    """The regex used for the match"""
    regex_match: bool
    """The tags for this object"""
    tags: dict
