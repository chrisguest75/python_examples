import time
import logging
from kafkaconfig import KafkaConfig
from kafka import KafkaProducer


class PublisherConfig(KafkaConfig):
    def __init__(self) -> None:
        super().__init__()


class Publisher:
    TOPIC_NAME = "default_topic"

    def __init__(self, config: PublisherConfig, topic: str = "default_topic") -> None:
        self.logger = logging.getLogger()
        self.TOPIC_NAME = topic

        self.logger.info(f"Create producer for topic {self.TOPIC_NAME}")

        self.logger.info(str(config))
        self.producer = KafkaProducer(
            bootstrap_servers=config.bootstrap_servers,
            security_protocol=config.security_protocol,
            ssl_cafile=config.ssl_cafile,
            ssl_certfile=config.ssl_certfile,
            ssl_keyfile=config.ssl_keyfile,
        )

    def send(self) -> None:
        self.logger.info(f"Publish messages topic {self.TOPIC_NAME}")
        for i in range(100):
            message = f"Hello from Python using SSL {i + 1}!"
            self.producer.send(self.TOPIC_NAME, message.encode("utf-8"))
            self.logger.info(f"Message sent: {message}")
            time.sleep(1)

    def __del__(self) -> None:
        if self != None and self.producer:
            self.logger.info(f"Closing producer for topic {self.TOPIC_NAME}")
            self.producer.close()
