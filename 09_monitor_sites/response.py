from dataclasses import dataclass


@dataclass
class Response:
    name: str
    url: str
    verb: str
    timestamp: int
    status: int
    elapsedMs: int
    expiry_date: str
    regex_match: bool
    tags: dict
