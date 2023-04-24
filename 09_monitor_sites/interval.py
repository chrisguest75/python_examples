import logging
import time
import threading
import random


class Interval:
    def __init__(self, name: str, intervalMs: int) -> None:
        self.logger = logging.getLogger(__name__)
        self.name = name
        self.interval = intervalMs / 1000.0
        self.stopped = False

    def stop(self):
        self.stopped = True

    def start(self):
        self.logger.info(
            {
                "message": "Operation started",
                "time": time.ctime(),
                "name": self.name,
            }
        )

        # sleep for a random amount of time between 0 and 1 second
        time.sleep(random.random() * 5)

        self.logger.info(
            {
                "message": "Operation ended",
                "time": time.ctime(),
                "name": self.name,
            }
        )

        if not self.stopped:
            threading.Timer(self.interval, self.start).start()
