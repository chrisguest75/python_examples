import logging
from kafkaconfig import KafkaConfig
from kafka import KafkaConsumer


class ConsumerConfig(KafkaConfig):
    def __init__(self) -> None:
        super().__init__()
        self.client_id = "CONSUMER_CLIENT_ID",
        self.group_id = "CONSUMER_GROUP_ID",


class Consumer:
    TOPIC_NAME = "default_topic"

    def __init__(self, config: ConsumerConfig ) -> None:
        self.logger = logging.getLogger()
        self.logger.info(f"Create consumer for topic {self.TOPIC_NAME}")
        
        self.logger.info(str(config))
        self.consumer = KafkaConsumer(
            bootstrap_servers=config.bootstrap_servers,
            security_protocol=config.security_protocol,
            ssl_cafile=config.ssl_cafile,
            ssl_certfile=config.ssl_certfile,
            ssl_keyfile=config.ssl_keyfile,
            client_id=config.client_id,
            group_id=config.group_id,
        )


    def receive(self) -> None:
        self.logger.info(f"Consume messages topic {self.TOPIC_NAME}")
        while True:
            for message in self.consumer.poll().values():
                logging.info("Got message using SSL: " + message[0].value.decode('utf-8'))


    def __del__(self) -> None:
        if self != None and self.consumer:
            self.logger.info(f"Closing consumer for topic {self.TOPIC_NAME}")
            self.consumer.close()





