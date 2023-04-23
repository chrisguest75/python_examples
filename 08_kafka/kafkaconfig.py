import os


class KafkaConfig:
    def __init__(self) -> None:
        self.bootstrap_servers = os.environ["SERVICE_URI"]
        self.security_protocol = os.environ["SECURITY_PROTOCOL"]
        self.ssl_cafile = os.environ["SSL_CAFILE"]
        self.ssl_certfile = os.environ["SSL_CERTFILE"]
        self.ssl_keyfile = os.environ["SSL_KEYFILE"]
