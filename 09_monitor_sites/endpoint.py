from dataclasses import dataclass


@dataclass
class Endpoint:
    name: str
    enabled: bool
    verb: str
    url: str
    timeoutMs: int
    regex: str
    intervalMs: int
    follow_redirects: bool
    check_certificate_expiration: bool
    verify_ssl: bool
    tags: dict
