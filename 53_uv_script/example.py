#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests<3",
#     "rich",
# ]
# ///

import requests
import time
from rich.pretty import pprint
from rich.progress import track

def main() -> None:
    print("Hello from example.py!")

    resp = requests.get("https://peps.python.org/api/peps.json")
    data = resp.json()
    pprint([(k, v["title"]) for k, v in data.items()][:10])

    for i in track(range(20), description="For example:"):
        time.sleep(0.05)    


if __name__ == "__main__":
    main()
