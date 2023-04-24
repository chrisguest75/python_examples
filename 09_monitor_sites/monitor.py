import logging
import time
import threading


class Monitor:
    def __init__(self, name: str, intervalMs: int) -> None:
        self.logger = logging.getLogger(__name__)
        self.name = name
        self.interval = intervalMs / 1000.0

    def start(self):
        self.logger.info(
            {
                "message": "timer...",
                "time": time.ctime(),
                "name": self.name,
            }
        )
        threading.Timer(self.interval, self.start).start()
