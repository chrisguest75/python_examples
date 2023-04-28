import time
import logging
from kafkaconfig import KafkaConfig
from kafka import KafkaProducer
import json


class PublisherConfig(KafkaConfig):
    def __init__(self, admin: bool = False) -> None:
        super().__init__(admin=admin)


class Publisher:
    TOPIC_NAME = "default_topic"

    def __init__(self, config: PublisherConfig, topic: str = "default_topic") -> None:
        self.logger = logging.getLogger()
        self.TOPIC_NAME = topic

        self.logger.info(f"Create producer for topic {self.TOPIC_NAME}")

        self.producer = KafkaProducer(
            bootstrap_servers=config.bootstrap_servers,
            security_protocol=config.security_protocol,
            ssl_cafile=config.ssl_cafile,
            ssl_certfile=config.ssl_certfile,
            ssl_keyfile=config.ssl_keyfile,
        )

    def send_message(self, message: dict) -> None:
        message_json = json.dumps(message)
        self.producer.send(self.TOPIC_NAME, message_json.encode("utf-8"))
        self.logger.info(f"Message sent: {message}")

    def send(self, repeat=100) -> None:
        self.logger.info(f"Publish messages topic {self.TOPIC_NAME}")
        for i in range(repeat):
            message = {
                "message": f"Message {i}",
                "timestamp": int(time.time()),
            }
            self.send_message(message)
            time.sleep(1)

    def __del__(self) -> None:
        if self is not None and hasattr(self, "producer"):
            self.logger.info(f"Closing producer for topic {self.TOPIC_NAME}")
            self.producer.close()
