import os


# class MissingConfigException(Exception):
#    pass


class KafkaConfig:
    """
    Used to get configuration for Kafka.

    This abstraction can be replaced with a different configuration source at a later date.
    """

    def __init__(self, admin: bool = False) -> None:
        # Url to the server including port
        self.bootstrap_servers = os.environ["SERVICE_URI"]
        # Protocol to use
        self.security_protocol = os.environ["SECURITY_PROTOCOL"]
        # SSL CA file
        self.ssl_cafile = os.environ["SSL_CAFILE"]

        # Admin and user creds are different
        if admin:
            self.ssl_certfile = os.environ["ADMIN_SSL_CERTFILE"]
            self.ssl_keyfile = os.environ["ADMIN_SSL_KEYFILE"]
        else:
            self.ssl_certfile = os.environ["USER_SSL_CERTFILE"]
            self.ssl_keyfile = os.environ["USER_SSL_KEYFILE"]
