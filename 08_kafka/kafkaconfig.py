import os


class KafkaConfig:
    def __init__(self, admin: bool = False) -> None:
        self.bootstrap_servers = os.environ["SERVICE_URI"]
        self.security_protocol = os.environ["SECURITY_PROTOCOL"]
        self.ssl_cafile = os.environ["SSL_CAFILE"]

        if admin:
            self.ssl_certfile = os.environ["ADMIN_SSL_CERTFILE"]
            self.ssl_keyfile = os.environ["ADMIN_SSL_KEYFILE"]
        else:
            self.ssl_certfile = os.environ["USER_SSL_CERTFILE"]
            self.ssl_keyfile = os.environ["USER_SSL_KEYFILE"]
