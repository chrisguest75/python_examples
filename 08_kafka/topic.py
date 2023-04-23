import logging
from kafkaconfig import KafkaConfig
from kafka import KafkaAdminClient
from kafka.admin import NewTopic


class TopicConfig(KafkaConfig):
    def __init__(self, admin: bool = False) -> None:
        super().__init__(admin=admin)


class Topic:
    def __init__(
        self,
        config: TopicConfig,
    ) -> None:
        self.logger = logging.getLogger()
        self.config = config

    def create(self, topic: str = "default_topic") -> None:
        self.logger.info(f"Create topic {topic}")

        # Create 'my-topic' Kafka topic
        try:
            admin = KafkaAdminClient(
                bootstrap_servers=self.config.bootstrap_servers,
                security_protocol=self.config.security_protocol,
                ssl_cafile=self.config.ssl_cafile,
                ssl_certfile=self.config.ssl_certfile,
                ssl_keyfile=self.config.ssl_keyfile,
            )
            topic = NewTopic(name=topic, num_partitions=1, replication_factor=1)
            admin.create_topics([topic])
        except Exception:
            self.logger.exception("Failed to create topic", exc_info=True)
