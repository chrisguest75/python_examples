import time
import logging
from kafka import KafkaProducer

class KafkaConfig:
    def __init__(self) -> None:
        self.bootstrap_servers=f"kafka-26102821-guestchris75-1a5d.aivencloud.com:27944"
        self.security_protocol="SSL"
        self.ssl_cafile="./secrets/ca.pem"
        self.ssl_certfile="./secrets/service.cert"
        self.ssl_keyfile="./secrets/service.key"

